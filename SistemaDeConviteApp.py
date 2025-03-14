import tkinter as tk
lista_nomes=[];
lista_idades=[];
lista_emails=[];

def ad():
    valor1=entrada1.get()
    lista_nomes.append(valor1)
    valor2=entrada2.get()
    lista_idades.append(valor2)
    valor3=entrada3.get()
    lista_emails.append(valor3)
    
    alert=tk.Toplevel(root)
    label9=tk.Label(alert,text="Conviadados da lista")
    label9.pack()
    def ok():
        alert.destroy()
    b_ok=tk.Button(alert,text="OK",command=ok)
    b_ok.pack()
    entrada1.delete(0,"end")
    entrada2.delete(0,"end")
    entrada3.delete(0,"end")
    
def exi():
    lista1.delete(0,tk.END)
    lista2.delete(0,tk.END)
    lista3.delete(0,tk.END)
    for item1 in lista_nomes:
        lista1.insert(tk.END,item1)
    for item2 in lista_idades:
        lista2.insert(tk.END,item2) 
    for item3 in lista_nomes:
        lista3.insert(tk.END,item3)

def limp():
    lista_nomes.clear()
    lista_idades.clear()
    lista_emails.clear()
    
root = tk.Tk()
root.title("Convite")
root.geometry("600x350")

#Exibindo convidados na caixa de entrada
label1=tk.Label(root,text="Convidados",font=("Arial",15))
label1.grid(row=0,column=0)

#Exibindo nome na caixa de entrada
label2=tk.Label(root,text="Nome",font=("Arial",15))
label2.grid(row=1,column=0)

#Adicionando nome 
entrada1=tk.Entry(root,font=("Arial",15))
entrada1.grid(row=1,column=1)

#Exibindo idade na caixa de entrada
label3=tk.Label(root,text="Idade",font=("Arial",15))
label3.grid(row=2,column=0)

#Adicionando idade
entrada2=tk.Entry(root,font=("Arial",15))
entrada2.grid(row=2,column=1)

#Exibindo emails na caixa de entrada
label4=tk.Label(root,text="Emails",font=("Arial",15))
label4.grid(row=3,column=0)

#Adicionando emails
entrada3=tk.Entry(root,font=("Arial",15))
entrada3.grid(row=3,column=1)

#Adicionando botão de adicionar e exibir na tela
b_ad=tk.Button(root,text="Adicionar",font=("Arial",15),command=ad)
b_ad.grid(row=4,column=0)
b_exibir=tk.Button(root,text="Exibir",font=("Arial",15),command=exi)
b_exibir.grid(row=4,column=1)

lista1=tk.Listbox(root,font=("Arial",15))
lista1.grid(row=6,column=0)
lista2=tk.Listbox(root,font=("Arial",15))
lista2.grid(row=6,column=1)
lista3=tk.Listbox(root,font=("Arial",15))
lista3.grid(row=6,column=2)


root.mainloop()