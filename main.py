from tkinter import *
import tkinter as tk

Amostra = Tk()
Amostra.title("Saudação Amostra Gaming")

class Application:

#Código adaptado da minha primeira criação
#Aqui apliquei meu aprendizado sobre funções, argumentos, 
    def codigo(self):
      nome = self.nome.get().strip()
      nome_M = nome.capitalize()

      if not nome:
            self.mensagem["text"] = "Primeiro digite algo inteligível"
      
      elif nome.isdigit():                 
            self.mensagem ["text"] = ("Idiota digite seu nome, ou criador e não {}!".format(nome))
      else:
            texto = ("É um prazer te conhecer, {}!.".format(nome_M) + " {}".format(nome_M) + " é especial para o Amostra Gaming.\nNão é comum este tipo de coisa mas acontece sempre principalmente com o outro {}.".format(nome_M))
            if nome_M == "Gay":
                  self.mensagem["text"] = "tu que é"
            elif nome_M == "Criador":
                  self.mensagem["text"] = "Jandin"
            else:
                  self.mensagem["text"] = texto



    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.pc = Frame(master)
        self.pc["pady"] = 20
        self.pc.pack()
        

        self.sc = Frame(master)
        self.sc["padx"] = 20
        self.sc.pack()

        self.tc = Frame(master)
        self.tc["padx"] = 20
        self.tc.pack()

        self.qc = Frame(master)
        self.qc["pady"] = 20
        self.qc.pack()

        self.titulo = Label(self.pc, text="Insira seu nome para uma saudação ou 'criador' para revelar o criador do código.")
        self.titulo["font"] = ("Arial", "10", "bold", )
        self.titulo.pack()

        self.nomeLabel = Label(self.sc,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.sc)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        self.verificar = Button(self.qc)
        self.verificar["text"] = "Enviar"
        self.verificar["font"] = ("Calibri", "8")
        self.verificar["width"] = 12
        self.verificar["command"] = self.codigo
        self.verificar.pack()

        self.mensagem = Label(self.qc, text="", font=self.fontePadrao)
        self.mensagem.pack()

#Fiquei umas 5 horas tentando resolver essa merda de .bind que não fucionava. No fim, descobri que precisava ser anônimo usando a função lambda.

        master.bind("<Return>", lambda event=None: self.codigo())

Application(Amostra)
Amostra.mainloop()