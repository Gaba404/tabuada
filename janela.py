import tkinter
#janela branca
root = tkinter.Tk()
root.title('hello world')
root.geometry('1024x768')

#texto de boas-vindas
label = tkinter.Label(root,
                      text="Olá developer",
                      font=('magneto', 32),
                      fg= 'white',
                      bg= 'darkgray')
label.pack(padx=10,pady=10)

#campo de digitar nome
label = tkinter.Label(root,
                      font=('Comic Sans MS', 15),
                      fg= 'white',
                      bg= 'darkgray',
                      text='Digite seu nome:')

label.pack(padx=10,pady=10)

imput = tkinter.Entry(root, width=50)
imput.pack(padx=5, pady=5)

#botão
button = tkinter.Button(root,width=10,
                        font=('magneto', 30),
                        text='Gravar',
                        commando=None)
button.pack(padx=10 ,pady=10)
root.mainloop()
