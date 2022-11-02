import datetime
import imp
import random
#import pygame
#import nunpy as np

Nombre = input ("Introduce tu nombre: ")
Start = input ("Presiona Y + Enter para iniciar el sistema")
print ("")
if Start == ("Y"):
  print ("Bienvenido, " , (Nombre) )
  print ("")
  Eligeaplicacion = input ("""Aplicaciones:
   1. Fecha y hora 
   2. Calculadora
   3. Dado
   4. Snake
   Para abrir una aplicación escribe el numero de dicha aplicación.
      """)

  if Eligeaplicacion == ("1"):
    ahora = datetime.datetime.now()
    # print(ahora)
    print ("Fecha y hora:")
    print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
  
    
   
  if Eligeaplicacion == ("2"):
    while (True):
      print ("Introduzca el tipo de operación que desea realizar: \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir ")
      opcion = input()
      if opcion == "1":
        n1 = float(input("Numero 1: "))
        n2 = float(input("Numero 2: "))
        print ("La suma de los numeros es: ", n1+n2)
        print ()
        
      elif opcion == "2":
        n1r = float(input("Numero 1: "))
        n2r = float(input("Numero 2: "))
        print ("La resta de los numeros es: ", n1r-n2r)
        print
      
      elif opcion == "3":
        n1r = float(input("Numero 1: "))
        n2r = float(input("Numero 2: "))
        print ("La multiplicación de los numeros es: ", n1r*n2r)
        print ()

      elif opcion == "4":
        n1r = float(input("Numero 1: "))
        n2r = float(input("Numero 2: "))
        print ("La división de los numeros es: ", n1r/n2r)
        print ()
  
  
  
  if Eligeaplicacion == ("3"):
      resultado = random.randint(1,6)
      print("Resultado: ", resultado)
 
  
  
  # if Eligeaplicacion == ("4"):
    # class Game(object):
      # def init (self, ancho juego, alto juego):
        #pygame.diaplay.set_caption('Snake')
        #self.ancho_juego = ancho_juego
        #self.alto_juego = alto_juego
        #self.display_juego = pygame.display.set_mode((ancho_juego, alto_juego+100))
        #self.fondo = pygame.image.load('img/fondo.png')
        #self.colision = False
        #self.score = 0
        #self.font = pygame.font.SysFont('Ubuntu', 20)

      #def display_ui(self, record):
        #self.display_juego.fill((255, 255, 255))
        #score_txt = self.font.render('RESULTADO: ', True, (0, 0, 0))
        #score_num = self.font.render(str(self.score), True, (0, 0, 0))
        #record_txt = self.font.render('Mejor: ', True, (0, 0, 0))
        #record_num = self.font.render(str(record), True, (0, 0, 0))

        #pygame.draw.rect(self.display_juego, (200, 200, 200), (0, self.alto_juego, self.alto_juego, 0)) 

        #self.display_juego.blit(score_txt, (45, 480))
        #self.display_juego.blit(score_num, (45, 480))
        #self.display_juego.blit(record_txt, (45, 480))
        #self.display_juego.blit(record_num, (45, 480))
        #self.display_juego.blit(self.fondo, (0, 0))
      #def obtener_record(self, score, record):
        #return score if score >= record else record


#def run():
  #pygame.init()
  #record = 0
  


        
