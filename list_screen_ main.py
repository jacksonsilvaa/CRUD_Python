#-------------------------------------------------------------------------------
# Name:        crud_python.py
# Purpose:
#
# Author:      Jackson Silva (jsilvacco@gmail.com)
#

import tkinter as tk
from create_screen import CreateScreen # Import the create class
from edit_screen import EditScreen  # Imports the edit screen class
from PIL import Image, ImageTk
from database import read_select_table

#Colors

co0 = "#000000"  # Black
co1 = "#59656F"  # bluish gray
co2 = "#feffff"  # White
co3 = "#0074eb"  # Blue
co4 = "#f04141"  # Red
co5 = "#59b356"  # Green
co6 = "#cdd1cd"  # Gray


class ListScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.grid()

        self.title("List of Item")

        #The method below is used to close the window properly
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.protocol("WM_DELETE_WINDOW", self.close)
        
        # Sets the window size
        self.maxsize(500, 500)
        self.minsize(500, 500)
        self.geometry("500x500")
        
        #upload images
        try:

            #image create
            self.image_create = Image.open("icons/create.png")
            self.image_create = self.image_create.resize((30,30))
            self.photo_create = ImageTk.PhotoImage(self.image_create)
            #image edit
            self.image_edit = Image.open("icons/edit.png")
            self.image_edit = self.image_edit.resize((30,30))
            self.photo_edit = ImageTk.PhotoImage(self.image_edit)
            #image read
            self.image_read = Image.open("icons/read.png")
            self.image_read = self.image_read.resize((30,30))
            self.photo_read = ImageTk.PhotoImage(self.image_read)
            #image delete
            self.image_delete = Image.open("icons/delete.png")
            self.image_delete = self.image_delete.resize((30,30))
            self.photo_delete = ImageTk.PhotoImage(self.image_delete)
            #image clear
            self.image_clear = Image.open("icons/clear.png")
            self.image_clear = self.image_clear.resize((30,30))
            self.photo_clear = ImageTk.PhotoImage(self.image_clear)
            #image quit
            self.image_quit = Image.open("icons/quit.png")
            self.image_quit = self.image_quit.resize((30,30))
            self.photo_quit =  ImageTk.PhotoImage(self.image_quit)

        except Exception as e:
            print("error loading images:", e)

        #Create button
        self.create_label = tk.Label(self, text="Create")
        self.create_label.grid(column=0, row=0)

        self.create_button = tk.Button(self, text="Create", image=self.photo_create, fg=co2,
        command=self.open_create_screen)
        self.create_button.grid(column=0, row=1, sticky='w', padx=5, pady=5)

        #Read Button
        self.read_label = tk.Label(self, text="Read")
        self.read_label.grid(column=1, row=0)

        self.read_button = tk.Button(self, text="Read", image=self.photo_read, fg=co2,
        command=self.button_read_table)
        self.read_button.grid(column=1, row=1, sticky='w', padx=5, pady=5)

        #Edit button

        self.edit_label = tk.Label(self, text="Update")
        self.edit_label.grid(column=2, row=0)

        self.edit_button = tk.Button(self, text="Edit", image=self.photo_edit, fg=co2,
        command=self.open_edit_screen)
        self.edit_button.grid(column=2, row=1, sticky='w', padx=5, pady=5)

        #Delete Button
        self.delete_label = tk.Label(self, text="Delete")
        self.delete_label.grid(column=3, row=0)

        self.delete_button = tk.Button(self, text="Delete", image=self.photo_delete, fg=co2)
        self.delete_button.grid(column=3, row=1, sticky="w", padx=5, pady=5)

        #clear screen Button

        self.clear_label = tk.Label(self, text="Clear")
        self.clear_label.grid(column=4, row=0)

        self.clear_button = tk.Button(self, text="Clear",image=self.photo_clear,fg=co2, 
        command=self.clear_text_main_screen)
        self.clear_button.grid(column=4, row=1, sticky="w", padx=5, pady=5)

        #exit button
        self.back_label = tk.Label(self, text="Exit")
        self.back_label.grid(column=5, row=0)

        self.back_button = tk.Button(self, text="Quit Program", image=self.photo_quit, fg="White",
        command=self.on_close)

        self.back_button.grid(column=5, row=1, sticky='w', padx=5, pady=5)

        #displaying message if you click on the x to exit

        self.message_click_x = tk.Text(self, height=10, width=40)
        self.message_click_x.grid(column=0, row=2, columnspan=5, rowspan=5, sticky='nsew', padx=5, pady=5)
        #self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)


        #New implementation to open the screens inside the main screen
        self.container = tk.Frame(self)
        self.container.grid()

        self.current_screen = None

    #function

    ''' 
    the functions below are not used:
       #add empty column and row
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(6, weight=1)
    
    def open_edit_screen(self):
        #self.withdraw()  # Esconde a tela atual
        self.iconify() # minimizar a janela principal
        edit_screen = EditScreen(self)  # Cria a tela de edição
        edit_screen.mainloop()  # Inicia o loop da tela de edição quando voltar do loop, exibe a tela atual novamente
        self.deiconify()  # Torna a tela atual visível novamente

    def open_create_screen(self):
        #self.withdraw()  # Hide the current screee
        self.iconify() # minimizar a janela principal
        create_screen = CreateScreen(self)  # Cria a tela de edição
        create_screen.mainloop()  # Inicia o loop da tela de edição quando voltar do loop, exibe a tela atual novamente
        self.deiconify()  # Torna a tela atual visível novamente'''
    
    
    
    #new functions to open other screens without necessarily closing the main one
    
    def open_edit_screen(self):
        self.clear_container()
        self.current_screen = EditScreen(self.container)
        self.current_screen.grid()

    def open_create_screen(self):
        self.clear_container()
        self.current_screen = CreateScreen(self.container)
        self.current_screen.grid()

    def button_read_table(self):
        message = f"{read_select_table('users.tb_users_his')}"
        self.message_click_x.insert(tk.END, message)
        self.message_click_x.config(fg=co5)


    #clear text main screen

    def clear_text_main_screen(self):
        message = ''
        self.message_click_x.insert(tk.END, message)
        self.message_click_x.delete('1.0', tk.END)

    #clear container

    def clear_container(self):
        if self.current_screen:
            self.current_screen.destroy()

    # Close the main window
    def on_close(self):
        self.destroy()

    # Leave it empty to avoid errors when closing using the "x" and inform the user the message
    def close(self):
        pass
        message = "To close the application click Quit Program"
        self.message_click_x.insert(tk.END, message + "\n")
        self.message_click_x.config(fg=co4)
        

if __name__ == "__main__":
    list_screen = ListScreen()
    list_screen.mainloop()