import tkinter as tk
import tkinter.messagebox as mb
from tkinter import *
from tkinter.filedialog import askopenfilename
from Compress import *


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")
        self.resizable(False, False)
        self.title("Huffman arhciver")
        self.background_image = PhotoImage(file=("bg.png"))
        Label(self, image=self.background_image).pack()
        self.btn = Button(self, text="Choose a file to archivate / dearchivate:",
                          command=self.code_message, bg="white", fg="black", font="Arial 16", bd=4).place(relx=0.5, rely=0.25, anchor=CENTER)

    def code_message(self):
        file_path = askopenfilename()
        if file_path:
            path = file_path.split("/")[0:-1]
            correct_path = ""
            for p in path:
                correct_path += p + "/"
            file = file_path.split("/")[-1]
            name = file.split(".")[0]
            extension = file.split(".")[1]
            if extension == "txt":
                c = Compress(name=file_path,
                             output=correct_path + name + ".bin")
                c.write_message()
            elif extension == "bin":
                c = Compress(name=correct_path + name + ".txt",
                             output=correct_path + name + ".bin")
                c.write_decoded_result()
            self.show_info()
        else:
            self.show_warning()

    def show_info(self):
        msg = "Готово!"
        mb.showinfo("Информация", msg)

    def show_warning(self):
        msg = "Неккоректный ввод"
        mb.showwarning("Предупреждение", msg)
