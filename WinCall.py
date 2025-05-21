import tkinter as tk

def fnAdicao():
    x = float(entry.get())
    y = float(entry1.get())
    result = x + y
    resultado.config(text=f'A soma é {result}')

def fnSubtracao():
    x = float(entry.get())
    y = float(entry1.get())
    result = x - y
    resultado.config(text=f'A subtração é {result}')

def fnMultiplicacao():
    x =  float(entry.get())
    y = float(entry1.get())
    result = x * y
    resultado.config(text=f'A multiplicação é {result}')

def fnDivisao():
    x =  float(entry.get())
    y = float(entry1.get())
    result = x / y
    resultado.config(text=f'A multiplicação é {result}')



#Codigo da janela
ja = tk.Tk()
ja.title('Advanced calculator')
ja.geometry('1580x1024')

#titulo do aplicativo
titulo = tk.Label(ja,
                  text='Calculadora',
                  font=('elephant', 32),
                  bg='white',
                  width='800')
titulo.pack(padx=5,pady=5)

#opção para numero1
num1 = tk.Label(ja,
                text='Digite um numero:',
                 font=('arial', 15) )
num1.pack(padx=5,pady=5)

entry = tk.Entry(ja, width=50,
                 font=('arial', 50))
entry.pack(padx=5, pady=5)


 #opção para numero2
num2 = tk.Label(ja,
                text='Digite outro numero:',
                 font=('arial', 15) )
num2.pack(padx=5,pady=5)

entry1 = tk.Entry(ja, width=50,
                 font=('arial', 50))
entry1.pack(padx=5, pady=5)


ctnBotoes = tk.PanedWindow(ja)
ctnBotoes.pack(padx=5,pady=5)

#-------------------------------------------------------------#

    #Botão de Adição
btnad = tk.Button(ctnBotoes, width=15,
                text='ADIÇÃO',
                font=('callibri',15),
                command=fnAdicao)

btnad.grid(column=1,row=1,padx=5, pady=5)

#-------------------------------------------------------------#

    #Botão de Subtração
btnsub = tk.Button(ctnBotoes, width=15,
                text='SUBTRAÇÃO',
                font=('callibri',15),
                command=fnSubtracao)
btnsub.grid(column=2,row=1,padx=5, pady=5)

#-------------------------------------------------------------#

    #Botão de Multiplicação
btnmult = tk.Button(ctnBotoes, width=15,
                text='MULTIPLICAÇÃO',
                font=('callibri',15),
                command=fnMultiplicacao)
btnmult.grid(column=1,row=2,padx=5, pady=5)

#-------------------------------------------------------------#

    #Botão de Divisão
btndiv = tk.Button(ctnBotoes, width=15,
                text='DIVISÃO',
                font=('callibri',15),
                command=fnDivisao)
btndiv.grid(column=2,row=2,padx=5, pady=5)

resultado = tk.Label(ja,
                     text='0.00',
                     font=('callibri',32),
                     bg='white')
resultado.pack(padx=5, pady=5)











ja.mainloop()