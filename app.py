from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sys
janela = Tk()
janela.title("Hand avaluator")
janela.geometry("312x110")



#gerador de mao
cartas = ['A', '2', '3', '4', '5', '6', '7','8', '9' , '10', "J", "Q", "K"]

#Para esse codigo é irrelevante os naipes individuais de cada carta, basta saber se as duas possuem o mesmo naipe
naipe =['S', 'N']
naipado = False

#Posicao em que esta sentado na mesa
positions = ["Dealer", 'Small Blind', 'Big Blind', 'Meio', "Fim"]

#recebe a mao do jogador
labelc1 = Label(janela, text='Selecione sua primeira carta ')
labelc1.grid(column=2, row=0)

comboc1 = ttk.Combobox(janela, values=cartas)
comboc1.grid(column=3, row=0)
def selecionar_c1():
    c1=comboc1.get()
    return c1
        

labelc2 = Label(janela, text='Selecione sua segunda carta ')
labelc2.grid(column=2, row=1)

comboc2 = ttk.Combobox(janela, values=cartas)
comboc2.grid(column=3, row=1)

combon=ttk.Combobox(janela, values=naipe )
combon.grid(column=3, row=2)
labeln= Label(janela, text='Suas cartas estao naipadas? ')
labeln.grid(column=2, row=2)


def naipar():
    global naipado
    n = combon.get()
    if n == "S":
        naipado = True
    else:
        naipado = False
    return naipado  


def selecionar_c2():
    c2=comboc2.get()
    return c2





#recebe a posicao
combop=ttk.Combobox(janela, values=positions )
labelp= Label(janela, text='Qual sua posicao? ')
labelp.grid(column=2, row=3)
combop.grid(column=3, row=3)
def selecionar_p():
    p=combop.get()
    return p

#avalia a mao
fold=True

##posicao de meio
def avaliar():
    global fold
    naipar()
    c1 = selecionar_c1()
    c2 = selecionar_c2()
    p = selecionar_p()
    hand=c1+c2
    cartas_meio = ["AA", 'QQ', "JJ", 'KK', '1010', '99', 'AK', 'AQ', 'AJ', 'KQ','KA', 'QA', 'JA',"QK"]

    if (p=='Meio') and hand  in cartas_meio:
        fold=False
    elif  (p=='Meio') and hand not in cartas_meio:
        fold=True


    ##posicao FIM e Dealer
    cartas_fim= ["AA", 'QQ', "JJ", 'KK', '1010', '99', 'AK', 'AQ', 'AJ', 'KQ','KA', 'QA', 'JA',"QK", 'A10','A9','9A','10A','KJ','JK', 'K10','10K', 'QJ','JQ', 'Q10', '10Q', 'J10', '10J','109','910','98','89']
    if p=='Fim' or p=="Dealer":
        if hand in cartas_fim:
            fold=False
        
        elif c1==c2:
                fold=False
        elif (c1 == 'A' or c2 == 'A') and naipado == True:
                
                    fold=False
        elif (c1 == 'A' or c2 == 'A') and naipado == False:
                    
                    
                        fold=True
        elif hand not in cartas_meio:
             fold=True

                    
        elif (hand== "K9" or hand=="9K") and naipado==True:
            fold=False
        elif (hand== "K9" or hand=="9K") and naipado==False:
            fold=True
        elif(hand=='Q9' or hand== '9Q') and naipado==True:
            fold=False
        elif (hand== "Q9" or hand=="9Q") and naipado==False:
                fold=True
        elif (hand=='J9' or hand== '9J') and naipado==True:
            fold=False
        elif (hand== "J9" or hand=="9J") and naipado==False:
            fold=True
        elif (hand=='108' or hand== '810') and naipado==True:
            fold=False
        elif (hand=='108' or hand=='810') and naipado==False:
            fold=True
        elif (hand=='97' or hand== '79') and naipado==True:
            fold=False
        elif (hand=='97' or hand=='79') and naipado==False:
                fold=True
        elif (hand=='87' or hand== '78') and naipado==True:
            fold=False
        elif (hand=='87' or hand=='78') and naipado==False:
            fold=True
        
    ##posicao Small Blind
    cartas_SB=["AA", 'QQ', "JJ", 'KK', '1010', '99', 'AK', 'AQ', 'AJ', 'KQ','KA', 'QA', 'JA',"QK", '88', 'Q10', '10Q', 'JQ', 'QJ', 'K10', '10K', 'A10', "10A", 'J10', '10J']
    
    if(p=='Small Blind') and hand in cartas_SB:
        fold=False
    elif (p=='Small Blind') and hand not in cartas_SB:
         fold=True

    ##posicao Big Blind
    if p=='Big Blind':

                if hand in cartas_SB:
                    fold=False
                elif hand not in cartas_SB:
                    fold=True
                    messagebox.showinfo('Se ninguem tiver aumentado, check, senao')
                
    if fold==False:
        messagebox.showinfo('Jogue', 'Sua mao tem boas chances de conseguir algo forte no flop')
    elif fold==True:
        messagebox.showerror('Corra', 'Sua mao nao e forte o suficiente para jogar nessa posicao')
    print(hand,naipado, fold)

avaliarb = Button(janela, text='Avaliar',command=avaliar)
avaliarb.grid(column=3, row=4)


        

janela.mainloop()
    

    

        
        


