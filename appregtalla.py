import sqlite3
from tkinter import Label, Button,Entry,LabelFrame,Tk,StringVar,CENTER
from tkinter import ttk

class RegistroTallGirl:
    def __init__(self,root):
        self.root=root
        self.root.title("Resitro de Altura")
        self.root.config(bg="#7C3E48")
        
        Nombre=StringVar()
        Altura=StringVar()
        Peso=StringVar()
        
        #ENCABEZADO DEL PROGRAMA
        encabezado=Label(root,text="Registro de Altura"
                         ,width=50,font=('arial',16,'bold'),bg='#477038')
        encabezado.grid(row=0,column=0,columnspan=2)
        
        #FRAME
        frame=LabelFrame(self.root,text='Ingreso de Datos',bg="#7C3E48",padx=20,pady=20)
        frame.grid(row=1,column=0,columnspan=3,pady=20)
        
        frame1=LabelFrame(self.root,text='Botones',bg="#7C3E48",padx=20,pady=20)
        frame1.grid(row=1,column=1,columnspan=2,pady=20,padx=10)
        
        frame3=LabelFrame(self.root,text='Lista de datos',bg='#7C3E48')
        frame3.grid(row=2,column=0,columnspan=2,pady=20,padx=10)
        
        #LABELS
        label_nom=Label(frame,text='Nombre:',
                        font=('arial',12,'bold'),
                        bg="#7C3E48")
        label_alt=Label(frame,text='Altura:',
                        font=('arial',12,'bold'),
                        bg="#7C3E48")
        label_pes=Label(frame,text='Peso:',font=('arial',12,'bold'),
                        bg="#7C3E48")
        
        #GRID LABEL
        label_nom.grid(row=0,column=0)
        label_alt.grid(row=1,column=0)
        label_pes.grid(row=2,column=0)
        
        #ENTRY
        e_nom=Entry(frame,width=50)
        e_alt=Entry(frame,width=50)
        e_pes=Entry(frame,width=50)
        
        #ENTRY GRID
        e_nom.grid(row=0,column=1)
        e_alt.grid(row=1,column=1)
        e_pes.grid(row=2,column=1)
        
        #BOTONES DE LA APLICACIONES
        
        btn_guardar=Button(frame1,text='Guardar',
                           padx=5,pady=5,
                           bg='#836F41')
        btn_mostrar=Button(frame1,text='Mostrar Base',
                           padx=5,pady=5,
                           bg='#836F41')
        btn_limpiar=Button(frame1,text='Limpiar',
                           padx=5,pady=5,
                           bg='#836F41')
        btn_borrar=Button(frame1,text='Borrar dato',
                          padx=5,pady=5,
                          bg='#836F41')
        btn_cerrar=Button(frame1,text='Cerrar Aplicacion',
                          padx=5,pady=5,
                          bg='#836F41')
        
        #GRID DE BOTONES
        btn_guardar.grid(row=0,column=0)
        btn_mostrar.grid(row=0,column=2)
        btn_limpiar.grid(row=1,column=0)
        btn_borrar.grid(row=1,column=2)
        btn_cerrar.grid(row=3,column=0,columnspan=2)
        
        
        
        tree=ttk.Treeview(frame3,height=10,column=('#0','#1'))
        tree.grid(row=4,column=0)
        tree.heading('#0',text="Nombre",anchor=CENTER)
        tree.heading('#1',text="Altura",anchor=CENTER)
        tree.heading('#2',text="Peso",anchor=CENTER)
  
    
    
    
    
    
    
    
    
    
    def CrearBBDD(self):
        con=sqlite3.connect("libbooks.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, Nom text, Alt real, Pes int")
        con.commit()
        con.close()
    
    

if __name__=='__main__':
    root=Tk()
    applicacion=RegistroTallGirl(root)
    root.mainloop()