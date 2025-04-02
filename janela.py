import tkinter

root = tkinter.Tk()
root.title('hello world')
root.geometry('1024x768')
label = tkinter.Label(root,
                      text="Olá",
                      font=('magneto', 32),
                      fg= 'purple',
                      bg= 'black')
label.pack(padx=10,pady=10)

label = tkinter.Label(root,
                      text='Digite seu nome:')
label.pack(padx=10,pady=10)

imput = tkinter.Entry(root)
imput.pack(padx=5, pady=5)
root.mainloop()