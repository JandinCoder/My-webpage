"""
Olá Senhores do Amostra Gaming!
Este é o meu primeiro projeto baseado no conhecimento que adiquiri até o presente momento!
Tudo foi acriado a partir usando conhecimento gratuito (em inglês) diponivel na internet e SoloLearn.
Para aqueles manjam e puderem aprimorar o meu saber com dicas e otmizações sou todo ouvidos.
"""


from tkinter import *

def Amostra():
    nome = input('Digite seu nome: ')
    nome_M = nome.capitalize()
    texto = ("É um prazer te conhecer, {}!.".format(nome_M) + " {}".format(nome_M) + " é especial para o Amostra Gaming. Não é comum este tipo de coisa mas acontece sempre principalmente com o outro {}.".format(nome_M))
    if nome.isdigit():  
        print ("Idiota digite seu nome, ou criador e não {}!".format(nome))  
    else:
     
        if nome == "gay":
            print("tu que é")
        elif nome == "criador":
            print("Jandin")
        else:
            print(texto)
Amostra()


janela = Tk()
janela.tittle("Amostra seu Nome")

janela.mainloop()