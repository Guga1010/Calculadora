from tkinter import *

def resultado():
    try:
        sep_conta = str(val_conta.get()).split(" ")
        if(sep_conta[1] == '+'):
            res = int(sep_conta[0]) + int(sep_conta[2])
        elif(sep_conta[1] == '-'):
            res = int(sep_conta[0]) - int(sep_conta[2])
        elif(sep_conta[1] == '*'):
            res = int(sep_conta[0]) * int(sep_conta[2])
        elif(sep_conta[1] == '/'):
            res = int(sep_conta[0]) / int(sep_conta[2])
        val_conta.set(res)
    except:
        return
    
itfc = Tk()
itfc.title("Calculadora")
itfc.geometry("235x195")

#Conta principal

val_conta = StringVar()
conta = Entry(itfc,textvariable=val_conta)
conta.pack_configure(fill=X)

#Números - Botões

frame_btns = Frame(itfc)
frame_btns.pack_configure(fill=X,pady=5)

Button(frame_btns,text="0",command=lambda:val_conta.set(val_conta.get()+"0"),width=3,height=2).grid(column=0,row=0)
Button(frame_btns,text="1",command=lambda:val_conta.set(val_conta.get()+"1"),width=3,height=2).grid(column=1,row=0)
Button(frame_btns,text="2",command=lambda:val_conta.set(val_conta.get()+"2"),width=3,height=2).grid(column=2,row=0)
Button(frame_btns,text="3",command=lambda:val_conta.set(val_conta.get()+"3"),width=3,height=2).grid(column=3,row=0)
Button(frame_btns,text="4",command=lambda:val_conta.set(val_conta.get()+"4"),width=3,height=2).grid(column=4,row=0)
Button(frame_btns,text="5",command=lambda:val_conta.set(val_conta.get()+"5"),width=3,height=2).grid(column=0,row=1)
Button(frame_btns,text="6",command=lambda:val_conta.set(val_conta.get()+"6"),width=3,height=2).grid(column=1,row=1)
Button(frame_btns,text="7",command=lambda:val_conta.set(val_conta.get()+"7"),width=3,height=2).grid(column=2,row=1)
Button(frame_btns,text="8",command=lambda:val_conta.set(val_conta.get()+"8"),width=3,height=2).grid(column=3,row=1)
Button(frame_btns,text="9",command=lambda:val_conta.set(val_conta.get()+"9"),width=3,height=2).grid(column=4,row=1)


#Operações - Botões
Button(frame_btns,text="+",command=lambda:val_conta.set(val_conta.get()+" + "),width=3,height=2).grid_configure(column=5,row=0,padx=7)
Button(frame_btns,text="-",command=lambda:val_conta.set(val_conta.get()+" - "),width=3,height=2).grid_configure(column=5,row=1)
Button(frame_btns,text="*",command=lambda:val_conta.set(val_conta.get()+" * "),width=3,height=2).grid_configure(column=5,row=2)
Button(frame_btns,text="/",command=lambda:val_conta.set(val_conta.get()+" / "),width=3,height=2).grid_configure(column=5,row=3)

btn_res = Button(frame_btns,text="=",command=resultado,width=3,height=2)
btn_res.grid_configure(column=6,row=0)

Button(frame_btns,text="C",command=lambda:val_conta.set(""),width=3,height=2).grid_configure(column=6,row=1)

itfc.mainloop()
