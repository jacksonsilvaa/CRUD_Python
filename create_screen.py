import tkinter as tk
from maskedentry import MaskedWidget
from database import insert_data_table

class CreateScreen(tk.Toplevel):  # Use Toplevel to create a secondary window
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Create Item")

        #The method below is used to close the window properly
        self.protocol("WM_DELETE_WINDOW", self.close)

        # Sets the window size
        self.maxsize(500, 500)
        self.minsize(500, 500)
        self.geometry("500x500")


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


        # back button   
        self.back_button = tk.Button(self, text="Back", width=8, command=self.close)
        self.back_button.grid(column=1, row=11, sticky='e', padx=(0, 10))

        self.create_button = tk.Button(self, text="Create", width=8, command=self.create)
        self.create_button.grid(column=3, row=11, sticky='e', padx=(0, 10))


    def create(self):
        #getting property values
        
        name_value = self.name_entry.get()
        phone_value = self.phone_entry.get()
        email_value = self.email_entry.get()


        data = [phone_value, name_value, email_value]
        if name_value:
            insert_data_table("users.tb_users_his", data)
            self.clear_entry()
    

    #cleanning the data
    def clear_entry(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)




    def close(self):
        if self.winfo_exists():  # Checks if the window still exists
            self.clear_entry()
            self.destroy()  # Close the creation window

if __name__ == "__main__":
    create_screen = CreateScreen(None)  #Test the edit screen in isolation
    create_screen.mainloop()  