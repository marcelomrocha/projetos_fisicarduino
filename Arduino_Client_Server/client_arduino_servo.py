#!/usr/bin/python
# -*- coding: cp1252 -*-

############################################################################
#
# Este programa se conecta com um servidor que roda na mesma rede.
# Entao envia para o servidor os comandos segundo o protocolo especificado.
# Autor: Marcelo Rocha
# www.fisicarduino.com
#
############################################################################

from socket import *
from Tkinter import * # Importa a biblioteca grafica
import time # Importa a biblioteca para trabalhar com temporizacao


# Obs. A vari�vel valor � enviada pelo Scale implicitamente e cont�m o valor atual da posi��o do Scale
def ledr():
	s.send('L1')

def ledv():
	s.send('L2')

def sound():
	s.send('S');
   
def servo_A(valorA): # Func�o que envia o valor do Slide_A para o Servo_A, atrav�s da porta serial   
   dataA = 'a'+chr(int(valorA))   
   s.send(dataA)

def servo_B(valorB): # Func�o que envia o valor do slide B para o Servo_B, atrav�s da porta serial
   dataB = 'b'+chr(int(valorB))
   s.send(dataB)
   
def clica_Move( event ):
   if (event.x >= 0 and event.x <=179): # Verifica se o mouse esta dentro dos limites do Canvas
      scale1.set(179 - event.x) # Envia os valores da posicao do mouse para o scale, e consequentemente chama a funcao servo_A 
      
   if (event.y >= 0 and event.x <=179): # Verifica se o mouse esta dentro dos limites do Canvas
      scale2.set(179 - event.y) # Envia os valores da posicao do mouse para o scale, e consequentemente chama a funcao servo_B
     
def sair(): # Fun��o que destr�i a Janela principal, antes fecha a porta serial
   s.send('00')
   print s.recv(100)
   s.close()
   root.destroy() # Destr�i a janela
  
# processo de cria��o da UI com TKinter

root = Tk() # Cria a janela
root.title('Servo - Client - Wireless - Controller') # Define o t�tula da janela
root.geometry('410x290') # Define o tamanho da janela principal
Meu_Canvas = Canvas(root, width=180, height=180) # Cria um objeto tipo canvas e define o tamanho do Canvas
Meu_Canvas.place(x=30,y=30) # Posiciona o Canvas na janela pricipal


# Desenha o retangulo preto mais o grid ( Azul ) no Canvas

Meu_Canvas.create_rectangle(0, 0, 180, 180, fill="black")
coords = 1 # S�o 10 linhas horizontais e 10 verticais
while (coords <= 10): # conta de 1 at� 10
   Meu_Canvas.create_line(0, 18*coords, 179, 18*coords, fill="blue") # linha horizontal
   Meu_Canvas.create_line(18*coords, 0, 18*coords, 179, fill="blue") # linha vertical
   coords = coords+1 # Mais uma linha, mais uma coluna

Meu_Canvas.bind("<B1-Motion>", clica_Move) # Anexa ao Meu_Canvas, a fun��o que trata o clicar e arrastar do mouse sobre o Canvas

# Cria dois objetos Scale que pode variar de 0 a 179, e associa-o � fun��o servo_A e servo_B respectivamente

# Pega os valores do scale1 e 
scale1 = Scale( root, from_=0, to=179, command = servo_A, width=15, length=179 )
scale1.place(x=250,y=30)
scale2 = Scale( root, from_=0, to=179, command = servo_B, width=15, length=179 )
scale2.place(x=310,y=30)

# Cria os Labels na tela.
label = Label(root, text='www.FisicArduino.com')
label.place(x=40, y=5) # Posiciona o label
label = Label(root, text='Y_Spin')
label.place(x=260, y=210) # Posiciona o label
label = Label(root, text='X_Spin')
label.place(x=320, y=210) # Posiciona o label

# Cria um objeto bot�o

b = Button(root, text ='  Exit  ', command = sair) # Anexa a funcao Sair a evento de clique do botao
b.place(x=30, y=240) # Posiciona o botao

bleda = Button(root, text ='Led Vermelho', command = ledr) # Anexa a funcao Sair a evento de clique do botao
bleda.place(x=100, y=240)

bledb = Button(root, text ='Led Verde', command = ledv) # Anexa a funcao Sair a evento de clique do botao
bledb.place(x=217, y=240)

btone = Button(root, text ='Sound', command = sound) # Anexa a funcao Sair a evento de clique do botao
btone.place(x=312, y=240)

s = socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.1.102', 2124))
print s.recv(100)


root.mainloop() # Coloca o programa em execu��o
