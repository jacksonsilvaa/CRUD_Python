import tkinter as tk
from maskedentry import MaskedWidget

class EditScreen(tk.Toplevel):  # Use Toplevel to create a secondary window
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Edit Item")
        #The method below is used to close the window properly
        self.protocol("WM_DELETE_WINDOW", self.close)

        # Sets the window size
        self.maxsize(500, 500)
        self.minsize(500, 500)
        self.geometry("500x500") 


        #personal dates

        self.name_label = tk.Label(self, text="Name: ")
        self.name_label.grid(column=0, row=1)

        self.name_entry = tk.Entry(self)
        self.name_entry.insert(0, 'Yudi Tamashiro')
        self.name_entry.grid(column=1, row=1)

        self.phone_label = tk.Label(self, text="Phone: ")
        self.phone_label.grid(column=0, row=2)

        self.phone_entry = tk.Entry(self)
        self.phone_entry = MaskedWidget(self,'fixed', mask='(99) 9999-9999')
        self.phone_entry.insert(0, '1140028922')
        self.phone_entry.grid(column=1, row=2)

        self.email_label = tk.Label(self, text="E-mail: ")
        self.email_label.grid(column=0, row=3)

        self.email_entry = tk.Entry(self)
        self.email_entry.insert(0, 'yudi.bomdia@sbt.com')
        self.email_entry.grid(column=1, row=3)

        self.dateBirth_label = tk.Label(self, text = "Date of Birth")
        self.dateBirth_label.grid(column=0, row=4)

        self.dateBirth_entry = tk.Entry (self)
        self.dateBirth_entry = MaskedWidget(self,'fixed', mask='9999/99/99')
        self.dateBirth_entry.insert(0, '00000000')
        self.dateBirth_entry.grid(column=1, row=4)

        self.profession_label = tk.Label(self, text="Profession" )
        self.profession_label.grid(column=0, row=5)

        self.profession_entry = tk.Entry(self)
        self.profession_entry.grid(column=1, row=5)

        self.cpf_label = tk.Label(self, text="CPF")
        self.cpf_label.grid(column=0, row=6)

        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.grid(column=1, row=6)

        #Address

        self.address_label = tk.Label(self, text="Address")
        self.address_label.grid(column=0, row=7)

        self.address_entry = tk.Entry(self)
        self.address_entry.grid(column=1, row=7)

        self.cep_label = tk.Label(self, text="CEP")
        self.cep_label.grid(column=0, row=8)

        self.cep_entry = tk.Entry(self)
        self.cep_entry.grid(column=1, row=8)

        self.number_label = tk.Label(self, text="Number")
        self.number_label.grid(column=0, row=9)

        self.number_entry = tk.Entry(self)
        self.number_entry.grid(column=1, row=9)

        self.compl_label = tk.Label(self, text="COMPL")
        self.compl_label.grid(column=0, row=10)

        self.compl_entry = tk.Entry(self)
        self.compl_entry.grid(column=1, row=10)


        self.back_button = tk.Button(self, text="Back", width=8, command=self.close)
        self.back_button.grid(column=1, row=11, sticky='e', padx=(0, 10))

        self.read_button = tk.Button(self, text="Read", width=8)
        self.read_button.grid(column=2, row=11, sticky='e', padx=(0, 10))

        self.edit_button = tk.Button(self, text="Edit", width=8,)
        self.edit_button.grid(column=3, row=11, sticky='e', padx=(0, 10))

        

     #clearing the data
    def clear_entry(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
    
    def close(self):
        if self.winfo_exists():  #Checks if the window still exists
            self.clear_entry()
            self.destroy()  # Close the creation window


if __name__ == "__main__":
    edit_screen = EditScreen(None)  # Test the edit screen in isolation
    edit_screen.mainloop()