########################################################################
#                                                                      #
# Programa para controle de 4 servo motores ( servo a, b, c, d)        #
# www.fisicarduino.com                                                 #
# Autor: Marcelo Rocha                                                 #
# Data: 18-04-2014                                                     #
# Se comunica com o arduino atrav�s da porta serial                    #
# Protocolo simples de comunica��o: ( byte_servo + valor do slider )   #
# Exemplo a100 ( Envia o valor 100 para servo a)                       #
#                                                                      #
########################################################################

from Tkinter import *
import serial
import time

# Configura��o da porta serial

ser = serial.Serial("COM3",9600); # Define porta e velocidade de comunica��o
print ser.portstr; # Imprime a porta em uso
print ('aguarde, incializando a porta...');
time.sleep(3); # Aguarda 3 segundos

def servo_A(valor): # Func�o que envia o valor do slide A para a porta serial
   ser.write('a')
   ser.write(chr(int(valor))) # Converte a vari�vel valor de str para int e de int para char ( byte )

def servo_B(valor): # Func�o que envia o valor do slide B para a porta serial
   ser.write('b')
   ser.write(chr(int(valor))) # Converte a vari�vel valor de str para int e de int para char ( byte )

def servo_C(valor): # Func�o que envia o valor do slide C para a porta serial
   ser.write('c')
   ser.write(chr(int(valor))) # Converte a vari�vel valor de str para int e de int para char ( byte )

def servo_D(valor): # Func�o que envia o valor do slide D para a porta serial
   ser.write('d')
   ser.write(chr(int(valor))) # Converte a vari�vel valor de str para int e de int para char ( byte )
   
def sair(): # Fun��o que destr�i a Janela principal, antes fecha a porta serial
   ser.close() # Fecha a porta serial
   print('Fechando a porta serial...')
   time.sleep(1)
   print('Fechando a janela..')
   time.sleep(1)
   root.destroy() # Destr�i a janela

# processo de cria��o da UI com TKinter

root = Tk() # Cria a janela
root.title('FisicArduino - 4SM Controller') # Define o t�tula da janela
root.geometry('310x280') # Define o tamanho

# Cria um objeto Scale que pode varia de 0 a 179, e associa-o � fun��o y_axis

scale = Scale( root, from_=0, to=179, command = servo_A, width=15, length=179 )
scale.place(x=30,y=10)
scale = Scale( root, from_=0, to=179, command = servo_B, width=15, length=179 )
scale.place(x=90,y=10)
scale = Scale( root, from_=0, to=179, command = servo_C, width=15, length=179 )
scale.place(x=150,y=10)
scale = Scale( root, from_=0, to=179, command = servo_D, width=15, length=179 )
scale.place(x=210,y=10)

label1 = Label(root, text='Servo A')
label1.place(x=40, y=195)
label1 = Label(root, text='Servo B')
label1.place(x=100, y=195)
label1 = Label(root, text='Servo C')
label1.place(x=160, y=195)
label1 = Label(root, text='Servo D')
label1.place(x=220, y=195)
# Cria um objeto bot�o
b = Button(root, text ='Exit', command = sair)
b.place(x=140, y=240)
#b.pack() # Coloca o bot�o na janela

root.mainloop() # Coloca o programa em execu��o
