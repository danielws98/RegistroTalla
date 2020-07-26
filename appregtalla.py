import sqlite3
from tkinter import Label, Button, Entry, LabelFrame, CENTER
from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import ttk


class RegistroTallGirl:
    def __init__(self, root):
        self.root = root
        self.root.title("Resitro de Altura")
        self.root.config(bg="#7C3E48")

        self.Nombre = StringVar()
        self.Altura = StringVar()
        self.Peso = StringVar()

        # ENCABEZADO DEL PROGRAMA
        encabezado = Label(root, text="Registro de Altura"
                           , width=50, font=('arial', 16, 'bold'), bg='#477038')
        encabezado.grid(row=0, column=0, columnspan=2)

        # FRAME
        frame = LabelFrame(self.root, text='Ingreso de Datos', bg="#7C3E48", padx=20, pady=20, )
        frame.grid(row=1, column=0, columnspan=3, pady=20, sticky='W')

        frame1 = LabelFrame(self.root, text='Controles', bg="#7C3E48", padx=20, pady=20)
        frame1.grid(row=1, column=1, columnspan=2, pady=20, padx=10, sticky='E')

        frame3 = LabelFrame(self.root, text='Lista de datos', bg='#7C3E48')
        frame3.grid(row=2, column=0, columnspan=2, pady=20, padx=10)

        # LABELS
        label_nom = Label(frame, text='Nombre:',
                          font=('arial', 12, 'bold'),
                          bg="#7C3E48")
        label_alt = Label(frame, text='Altura:',
                          font=('arial', 12, 'bold'),
                          bg="#7C3E48")
        label_pes = Label(frame, text='Peso:', font=('arial', 12, 'bold'),
                          bg="#7C3E48")

        # GRID LABEL
        label_nom.grid(row=0, column=0, sticky='W')
        label_alt.grid(row=1, column=0, sticky='W')
        label_pes.grid(row=2, column=0, sticky='W')

        # ENTRY
        e_nom = Entry(frame, width=40, textvariable=self.Nombre)
        e_alt = Entry(frame, width=40, textvariable=self.Altura)
        e_pes = Entry(frame, width=40, textvariable=self.Peso)

        # ENTRY GRID
        e_nom.grid(row=0, column=1)
        e_alt.grid(row=1, column=1)
        e_pes.grid(row=2, column=1)

        # BOTONES DE LA APLICACIONES

        btn_guardar = Button(frame1, text='Guardar',
                             padx=5, pady=5,
                             bg='#836F41',
                             command=self.AgregarDatos)
        btn_mostrar = Button(frame1, text='Mostrar Base',
                             padx=5, pady=5,
                             bg='#836F41',
                             command=self.obtener_productos)
        btn_limpiar = Button(frame1, text='Limpiar',
                             padx=5, pady=5,
                             bg='#836F41')
        btn_borrar = Button(frame1, text='Borrar dato',
                            padx=5, pady=5,
                            bg='#836F41',
                            command=self.borrar_dato)
        btn_cerrar = Button(frame1, text='Cerrar Aplicacion',
                            padx=5, pady=5,
                            bg='#836F41',
                            width=15,
                            command=self.root.destroy)

        # GRID DE BOTONES
        btn_guardar.grid(row=0, column=0)
        btn_mostrar.grid(row=0, column=1)
        btn_limpiar.grid(row=1, column=0)
        btn_borrar.grid(row=1, column=1)
        btn_cerrar.grid(row=3, column=0, columnspan=2)

        # LISTA DE LA BASE DE DATOS
        self.tree = ttk.Treeview(frame3, height=10, column=('#0', '#1'))
        self.tree.grid(row=4, column=0)
        self.tree.heading('#0', text="Nombre", anchor=CENTER)
        self.tree.heading('#1', text="Altura", anchor=CENTER)
        self.tree.heading('#2', text="Peso", anchor=CENTER)

        # Lista de ejecuciones
        self.CrearBBDD()
        self.obtener_productos()

    def CrearBBDD(self):
        con = sqlite3.connect("regaltura.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS talles (id INTEGER PRIMARY KEY,Nom TEXT, Alt TEXT, Pes TEXT)")
        con.commit()
        con.close()

    def validacion(self):
        return len(self.Nombre.get()) != 0 and len(self.Altura.get()) != 0 and len(self.Peso.get())

    def AgregarDatos(self):
        if self.validacion():
            con = sqlite3.connect("regaltura.db")
            cur = con.cursor()
            cur.execute("INSERT INTO talles VALUES (NULL,?,?,?)",
                        (self.Nombre.get(), self.Altura.get(), self.Peso.get()))
            con.commit()
            con.close()
            self.obtener_productos()

    def obtener_productos(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)

        con = sqlite3.connect("regaltura.db")
        cur = con.cursor()
        db_filas = cur.execute('SELECT * FROM talles ORDER BY Nom DESC')

        for row in db_filas:
            self.tree.insert('', 0, text=row[1], values=(row[2],row[3]))
        con.commit()
        con.close()

    def borrar_dato(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            pass
            return
        con = sqlite3.connect("regaltura.db")
        cur = con.cursor()
        Nom= self.tree.item(self.tree.selection())['text']
        cur.execute ('DELETE FROM talles WHERE Nom=?',[Nom])
        con.commit()
        con.close()

        self.obtener_productos()


if __name__ == '__main__':
    root = Tk()
    applicacion = RegistroTallGirl(root)
    root.mainloop()
