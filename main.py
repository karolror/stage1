import tkinter as tk
import pymongo


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        '#Background'
        self.bg = tk.PhotoImage(file="img/board.png")
        self.label1 = tk.Label(image=self.bg)
        self.label1.place(x=0, y=0, relheight=1, relwidth=1)
        '#Listboxes'
        self.listbox1 = tk.Listbox()
        self.listbox1.place(x=25, y=30)
        self.listbox1.insert('end', "Ford")
        self.listbox1.insert('end', "Renault")
        self.listbox2 = tk.Listbox(width=100)
        self.listbox2.place(x=170, y=30)
        self.scrollbar = tk.Scrollbar()
        self.scrollbar.place(x=775, y=30)
        self.listbox2.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox2.yview)
        '#Buttons'
        self.search_button = tk.Button(text="Search Models", command=lambda: self.get_model(self.get_value_listbox()))
        self.search_button.place(x=26, y=220)
        self.generate_button = tk.Button(text="Click to generate Stage1!", height="2", width="105",
                                         activebackground="#72A56A", activeforeground="#ff3333")
        self.generate_button.place(x=30, y=450)
        '#DB'
        self.client = pymongo.MongoClient(
            "mongodb+srv://db_user1:useruser123@cluster0.qqmqr.mongodb.net/sample_training?retryWrites=true&w=majority")

    def get_value_listbox(self):
        keykey = self.listbox1.get(tk.ACTIVE)
        return keykey

    def get_model(self, brand):
        self.listbox2.delete(0, tk.END)
        db = self.client["drivers"]
        collection = db["sizes"]
        desc = collection.find({"brand": brand})
        goto = []
        for i in desc:
            for x in i:
                ins_text = str(x) + " : " + str(i[x]) + " | "
                goto.append(ins_text)
            concentrate = " ".join(goto)
            self.listbox2.insert(tk.END, concentrate)
            del goto[:]


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.maxsize(800, 500)
    root.minsize(800, 500)
    root.title("Stage1 Generator")
    MainApplication(root)
    root.mainloop()
