import tkinter as tk
from tkinter import ttk
from create_screen import CreateScreen
from edit_screen import EditScreen

class ListScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Defina suas cores e outros elementos aqui

        self.title("List of Item")
        self.geometry("800x600")

        # Crie um Notebook para adicionar guias
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crie as guias
        self.create_tab = ttk.Frame(self.notebook)
        self.edit_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.create_tab, text="Create")
        self.notebook.add(self.edit_tab, text="Edit")

        # Configure os botões de voltar e fechar (você pode personalizá-los como desejar)
        self.back_button = tk.Button(self, text="Quit Program", fg="White", bg="Red", command=self.on_close)
        self.back_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.message_click_x = tk.Text(self, height=10, width=40)
        self.message_click_x.pack(side=tk.BOTTOM)

        # Associe o evento <<NotebookTabChanged>> para criar as telas de criação ou edição quando a guia for selecionada
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

    def on_close(self):
        self.destroy()

    def on_tab_changed(self, event):
        current_tab = self.notebook.select()
        if current_tab == self.create_tab:
            self.create_screen = CreateScreen(self.create_tab)
        elif current_tab == self.edit_tab:
            self.edit_screen = EditScreen(self.edit_tab)

if __name__ == "__main__":
    list_screen = ListScreen()
    list_screen.mainloop()