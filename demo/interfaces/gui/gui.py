import tkinter
from tkinter import messagebox

from demo.db_manager import DBManager
from demo.models import Person


class PersonGui(tkinter.Frame):
    def __init__(self, parent=None):
        super(PersonGui, self).__init__(parent)
        self.db_manager = DBManager()
        self.fieldnames = ('name', 'age', 'job', 'pay')
        self.fields = {}
        form = tkinter.Frame(self)
        for i, fieldname in enumerate(('key',) + self.fieldnames):
            label = tkinter.Label(form, text=fieldname)
            entry = tkinter.Entry(form)
            label.grid(row=i, column=0)
            entry.grid(row=i, column=1)
            self.fields[fieldname] = entry
        form.pack(side=tkinter.TOP)
        fetch_button = tkinter.Button(self, text='Fetch', command=self.fetch)
        fetch_button.pack(side=tkinter.LEFT)
        update_button = tkinter.Button(self, text='Update',
                                       command=self.update)
        update_button.pack(side=tkinter.LEFT)

    def clear_field(self, fieldname):
        self.fields[fieldname].delete(0, tkinter.END)

    def clear_all(self):
        for fieldname in self.fieldnames:
            self.clear_field(fieldname)

    def set_value(self, fieldname, value):
        self.clear_field(fieldname)
        self.fields[fieldname].insert(0, value)

    def fetch(self):
        person = self.db_manager.get(self.fields['key'].get())
        if person is not None:
            for fieldname in self.fieldnames:
                self.set_value(fieldname, repr(getattr(person, fieldname)))
        else:
            self.clear_all()
            messagebox.showerror(title='Error', message="No such key")

    def update(self):
        person_dict = {}
        for fieldname in self.fieldnames:
            person_dict[fieldname] = eval(self.fields[fieldname].get())
        new_person = Person.from_dict(person_dict)
        self.db_manager.set(self.fields['key'].get(), new_person)
        messagebox.showinfo(title='Success', message="Person updated")


def set_icon(win, filename):
    icon = tkinter.Image('photo', file=filename)
    win.tk.call('wm', 'iconphoto', win._w, icon)


if __name__ == '__main__':
    mainwin = tkinter.Tk()
    mainwin.title('Echo')
    set_icon(mainwin, 'py_icon.png')
    PersonGui(mainwin).pack()
    mainwin.mainloop()
