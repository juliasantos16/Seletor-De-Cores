from tkinter import *
import tkinter.messagebox

co0 = '#000000'
co1 = '#ffffff'
co2 = '#004338'
co3 = '#a6a39a'

# --- janela ---

janela= Tk()
janela.geometry('530x250')
janela.configure(bg=co1)
janela.title('Color Picker')
janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.resizable(width=False, height= False)

#--- configurando a janela ---

tela = Label(janela, bg=co0, width= 40, height=10, bd=1)
tela.grid(row=0, column=0, pady=10, padx=10)

# --PADY & PADX, usados na linha debaixo (ex: tela.grid)

frame_direito = Frame(janela, bg=co1)
frame_direito.grid(row=0, column=1)

frame_baixo = Frame(janela, bg=co1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=25)

# --- função ---

def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()
    
    
    
    rgb = f'{r}, {g}, {b}'
    
    
    hexadecimal = '#%02x%02x%02x'% (r, g, b)
    
# --- alterando coe de fundo ---
    tela['bg']=hexadecimal
    
# --- alterando entry ---
    e_cor.delete(0, END)
    e_cor.insert(0, hexadecimal)
    
# --- função de clicar ---

def onClick ():
    
    #mensagem
    tkinter.messagebox.showinfo('Cor', 'A cor foi copiada')
    
    
    clip = Tk ()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()


# --- config. frame direito ---

l_red = Label(frame_direito,  text='Red', width=7, bg=co1, fg='Red', anchor='nw', font=('Poppins', 12 ))
l_red.grid(row=0, column=0, pady=10, padx=5)

s_red=Scale(frame_direito, command=escala, from_=0, to=255, length=100, bg=co1, fg='Red', orient=HORIZONTAL)
s_red.grid(row=0, column=1)

#------------ green
l_green = Label(frame_direito, text='green', width=7, bg=co1, fg='green', anchor='nw', font=('Poppins', 12 ))
l_green.grid(row=1, column=0, pady=10, padx=5)

s_green=Scale(frame_direito, command=escala, from_=0, to=255, length=100, bg=co1, fg='green', orient=HORIZONTAL)
s_green.grid(row=1, column=1)

#------------ blue
l_blue = Label(frame_direito, text='blue', width=7, bg=co1, fg='blue', anchor='nw', font=('Poppins', 12 ))
l_blue.grid(row=2, column=0, pady=10, padx=5)

s_blue=Scale(frame_direito, command=escala, from_=0, to=255, length=100, bg=co1, fg='blue', orient=HORIZONTAL)
s_blue.grid(row=2, column=1)


# -------------config. frame baixo-------------

l_rgb = Label(frame_baixo, text='Código HEX: ', bg=co1, font=('Poppins', 10 ))
l_rgb.grid(row=0, column=0, pady=10, padx=5)

# --- ENTRY
e_cor = Entry(frame_baixo, width=12,font=('Poppins', 10 ), justify=CENTER)
e_cor.grid(row=0, column=1, padx=5)

# botão copiar
b_copiar = Button(frame_baixo, command=onClick, text='Copiar a cor', bg=co1, font=('Poppins', 8 ), relief=GROOVE, overrelief=RIDGE)
b_copiar.grid(row=0, column=2, pady=10, padx=5)







janela.mainloop()