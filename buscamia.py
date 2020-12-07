import sys
import pygame
from pygame.locals import *
import random
import time
##from minas20 import minas20
##from minas10 import minas_10
## reticula
pygame.init()
azul=(150,50,100)
arriba=K_UP
abajo=K_DOWN
izquierda=K_LEFT
derecha=K_RIGHT
noroeste=K_k
noreste=K_l
suroeste=K_n
sureste=K_m
movimientos=0
f=0
c=0
hora_actual=[0,0,0]
## reloj
def sumar_segundo():
	if hora_actual[2]<=58:
		hora_actual[2]+=1
	elif hora_actual[1]<=58:
		hora_actual[2]=0
		hora_actual[1]+=1
	else:
		hora_actual[2]=0
		hora_actual[1]=0
		hora_actual[0]+=1
	if hora_actual[0]<10:
		tiempo_j="0"+str(hora_actual[0])+":"
	else:
		tiempo_j=str(hora_actual[0])+":"
	if hora_actual[1]<10:
		tiempo_j=tiempo_j+"0"+str(hora_actual[1])+":"
	else:
		tiempo_j=tiempo_j+str(hora_actual[1])+":"
	if hora_actual[2]<10:
		tiempo_j=tiempo_j+"0"+str(hora_actual[2])
	else:
		tiempo_j=tiempo_j+str(hora_actual[2])
	return tiempo_j
## juego de 32 minas 
def reticula():
	filas=8
	colunas=16
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(16)] for f in range(8)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((370,250))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0
	while i < 33:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=6 and rc >=1 and rc <=14) or (rc==15 and rf<7 ) or (rf==7 and rc <15):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(150,230))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(150,210))
	ventanar.blit(pos,(3,210))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(150,230,150,20))
			ventanar.blit(contador,(150,230))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>348:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>164:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>348 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>348 or posy>164:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >164:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("HAS TERMINADO FELICITACIONES!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(150,210))
					ventanar.blit(pos,(3,210))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(150,230,150,20))
					ventanar.blit(contador,(150,230))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
## pantalla principal
def principal():
	ventana=pygame.display.set_mode((370,300))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	ventana.fill(azul)
	mi_imagen=pygame.image.load("uno.png")
	mi_imagen2=pygame.image.load("dos.png")
	ventana.blit(mi_imagen,(0,0))
	ventana.blit(mi_imagen2,(95,150))
	while True:
		for evento in pygame.event.get():
			if evento.type==QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type==pygame.KEYUP:
				secundaria()
		pygame.display.update()
## sengunda pantalla
def secundaria():
	ventana2=pygame.display.set_mode((370,300))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	ventana2.fill(azul)
	mi_imagen3=pygame.image.load("tres.png")
	mi_imagen4=pygame.image.load("cuatro.png")
	ventana2.blit(mi_imagen3,(95,70))
	ventana2.blit(mi_imagen4,(95,160))
	while True:
		for evento in pygame.event.get():
			if evento.type==QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					principal()
				elif evento.key==K_RIGHT:
					reticula()
				elif evento.key==K_LEFT:
					personalizar()
		pygame.display.update()
## personalizar minas
def personalizar():
	ventana3=pygame.display.set_mode((370,300))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	ventana3.fill(azul)
	mifuente=pygame.font.Font(None,40)
	mifuente2=pygame.font.Font(None,25)
	mitexto=mifuente.render("PERSONALIZAR MINAS",0,(30,255,0))
	mitexto2=mifuente2.render("presione 1 = 10 minas",0,(255,255,255))
	mitexto3=mifuente2.render("presione 2 = 20 minas",0,(255,255,255))
	mitexto4=mifuente2.render("presione 3 = 30 minas",0,(255,255,255))
	mitexto5=mifuente2.render("presione 4 = 40 minas",0,(255,255,255))
	mitexto6=mifuente2.render("presione 5 = 50 minas",0,(255,255,255))
	mitexto7=mifuente2.render("presione 6 = 60 minas",0,(255,255,255))
	ventana3.blit(mitexto,(10,10))
	ventana3.blit(mitexto2,(10,40))
	ventana3.blit(mitexto3,(10,70))
	ventana3.blit(mitexto4,(10,100))
	ventana3.blit(mitexto5,(10,130))
	ventana3.blit(mitexto6,(10,160))
	ventana3.blit(mitexto7,(10,190))
	while True:
		for evento in pygame.event.get():
			if evento.type==QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				if evento.key==K_1:
					minas_10()
				elif evento.key==K_2:
					minas_20()
				elif evento.key==K_3:
					minas_30()
				elif evento.key==K_4:
					minas_40()
				elif evento.key==K_5:
					minas_50()	
				elif evento.key==K_6:
					minas_60()
		pygame.display.update()
def minas_10():
	filas=5
	colunas=8
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(8)] for f in range(5)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((390,200))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0
	while i < 11:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=6 and rc >=1 and rc <=14) or (rc==15 and rf<7 ) or (rf==7 and rc <15):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(240,60))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(240,10))
	ventanar.blit(pos,(240,30))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(240,60,150,20))
			ventanar.blit(contador,(240,60))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>164:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>95:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>164 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>164 or posy>95:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >95:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("ERES UN BACAN GANASETE!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(240,10))
					ventanar.blit(pos,(240,30))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(240,60,150,20))
					ventanar.blit(contador,(240,60))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
def minas_20():
	filas=8
	colunas=10
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(10)] for f in range(8)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((375,250))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0
	while i < 21:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=6 and rc >=1 and rc <=14) or (rc==15 and rf<7 ) or (rf==7 and rc <15):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(235,80))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(235,10))
	ventanar.blit(pos,(235,50))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(235,80,150,20))
			ventanar.blit(contador,(235,80))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>210:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>164:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>210 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>210 or posy>164:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >164:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("EREES UN BACAN GANASETE!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(235,10))
					ventanar.blit(pos,(235,50))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(235,80,150,20))
					ventanar.blit(contador,(235,80))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
def minas_30():
	filas=8
	colunas=16
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(16)] for f in range(8)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((370,250))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0
	while i < 3:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=6 and rc >=1 and rc <=14) or (rc==15 and rf<7 ) or (rf==7 and rc <15):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(150,230))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(150,210))
	ventanar.blit(pos,(3,210))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(150,230,150,20))
			ventanar.blit(contador,(150,230))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>348:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>164:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>348 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>348 or posy>164:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >164:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("EREES UN BACAN GANASETE!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(150,210))
					ventanar.blit(pos,(3,210))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(150,230,150,20))
					ventanar.blit(contador,(150,230))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
def minas_40():
	filas=8
	colunas=16
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(16)] for f in range(8)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((370,250))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0


	while i < 41:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=6 and rc >=1 and rc <=14) or (rc==15 and rf<7 ) or (rf==7 and rc <15):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(150,230))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(150,210))
	ventanar.blit(pos,(3,210))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(150,230,150,20))
			ventanar.blit(contador,(150,230))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>348:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>164:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>348 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>348 or posy>164:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >164:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("EREES UN BACAN GANASETE!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(150,210))
					ventanar.blit(pos,(3,210))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(150,230,150,20))
					ventanar.blit(contador,(150,230))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
def minas_50():
	filas=10
	colunas=20
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(20)] for f in range(10)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((465,280))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0
	while i < 51:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=8 and rc >=1 and rc <=18) or (rc==19 and rf<9 ) or (rf==9 and rc <19):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(150,260))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(150,240))
	ventanar.blit(pos,(3,240))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(150,260,150,20))
			ventanar.blit(contador,(150,260))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>440:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>210:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>440 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>340 or posy>210:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >210:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("EREES UN BACAN GANASETE!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(150,240))
					ventanar.blit(pos,(3,240))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(150,260,150,20))
					ventanar.blit(contador,(150,260))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
def minas_60():
	filas=10
	colunas=20
	m=0
	f=0
	c=0
	matriz= [[0 for c in range(20)] for f in range(10)]
	tiempo_juego="00:00:00"
	posx=3
	posy=3
	ventanar=pygame.display.set_mode((465,280))
	pygame.display.set_caption("CAZADOR DE MINAS UTM")
	pau=1
	movimientos=0
	i=0
	p=0
	k=0
	while i < 61:
		rc=random.randint(0,colunas-1)
		rf=random.randint(0,filas-1)
		##print("col=",rc,"fil=",rf)
		if (rc ==0 and rf >0) or (rf==0 and rc >0) or(rf>=1 and rf<=8 and rc >=1 and rc <=18) or (rc==19 and rf<9 ) or (rf==9 and rc <19):
			if matriz[rf][rc]==0:

				matriz[rf][rc]=1
				i+=1
	perdido=0
	ventanar.fill(azul)
	fuentetiempo=pygame.font.Font(None,25)
	tiempoanterior=int(pygame.time.get_ticks()/1000)
	
	salir=False
	for fila in range(0,filas):
		for colu in range(0,colunas):
			pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
			
	contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
	ventanar.blit(contador,(150,260))
	pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
	
	m=0
	if f>0 and c>0:##and
		m=m+matriz[f-1][c-1]
	if c>0 :
		m=m+matriz[f][c-1]
	if c>0 and f<(filas-1):
		m=m+matriz[f+1][c-1]
	if f>0:
		m=m+matriz[f-1][c]#
	if f<(filas-1):
		m=m+matriz[f+1][c]
	if f>0 and c<(colunas-1):
		m=m+matriz[f-1][c+1]
	if c<(colunas-1):
		m=m+matriz[f][c+1]
	if f<(filas-1) and c<(colunas-1):
		m=m+matriz[f+1][c+1]
	pasos=fuentetiempo.render("PASOS: 0",0,(250,255,12))
	pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
	ventanar.blit(pasos,(150,240))
	ventanar.blit(pos,(3,240))
	pygame.display.update()
	while True:
		tiempoactual=int(pygame.time.get_ticks()/1000)
		if tiempoanterior!=tiempoactual and perdido==0:
			tiempoanterior=tiempoactual
			tiempo_juego=sumar_segundo()
			contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
			pygame.draw.rect(ventanar,(azul),(150,260,150,20))
			ventanar.blit(contador,(150,260))
			pygame.display.update()
		##ventanar.blit(fc,(10,210))
		for evento in pygame.event.get():
			movimiento_valido=False
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			elif evento.type==pygame.KEYUP:
				if evento.key==K_ESCAPE:
					secundaria()
				## identificar movimiento valido
				elif evento.key==derecha and perdido==0:
					movimientos+=1
					c+=1
					posx=posx+23
					movimiento_valido=True
					if posx>440:
						c-=1
						posx=posx-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==izquierda and perdido==0:
					movimientos+=1
					c-=1
					posx=posx-23 
					movimiento_valido=True
					if posx <3:
						c+=1
						posx=posx+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==abajo  and perdido==0:
					movimientos+=1
					f+=1
					posy=posy+23
					movimiento_valido=True
					if posy>210:
						f-=1
						posy=posy-23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==arriba and perdido==0:
					movimientos+=1
					f-=1
					posy=posy-23
					movimiento_valido=True
					if posy<3:
						f+=1
						posy=posy+23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noreste and perdido==0:
					movimientos+=1
					c+=1
					f-=1
					posx=posx+23
					posy=posy-23
					movimiento_valido=True
					if posx>440 or posy <3:
						c-=1
						f+=1
						posx-=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==noroeste and perdido==0:
					movimientos+=1
					c-=1
					f-=1
					posx=posx-23
					posy=posy-23
					movimiento_valido=True
					if posx<3 or posy<3:
						c+=1
						f+=1
						posx+=23
						posy+=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==sureste and perdido==0:
					movimientos+=1
					c+=1
					f+=1
					posx=posx+23
					posy=posy+23
					movimiento_valido=True
					if posx>340 or posy>210:
						c-=1
						f-=1
						posx-=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				elif evento.key==suroeste and perdido==0:
					movimientos+=1
					c-=1
					f+=1
					posx=posx-23
					posy=posy+23
					movimiento_valido=True
					if posx <3 or posy >210:
						c+=1
						f-=1
						posx+=23
						posy-=23
						movimientos-=1
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
				if perdido==1:
					salir=True
				if movimiento_valido==True	:
					## calcular minas cercanas 
					ventanar.fill(azul)
					m=0
					if f>0 and c>0:##and
						m=m+matriz[f-1][c-1]
					if c>0 :
						m=m+matriz[f][c-1]
					if c>0 and f<(filas-1):
						m=m+matriz[f+1][c-1]
					if f>0:
						m=m+matriz[f-1][c]#
					if f<(filas-1):
						m=m+matriz[f+1][c]
					if f>0 and c<(colunas-1):
						m=m+matriz[f-1][c+1]
					if c<(colunas-1):
						m=m+matriz[f][c+1]
					if f<(filas-1) and c<(colunas-1):
						m=m+matriz[f+1][c+1]		
					## llegada	
					if posx==348 and posy==164:
						venatanaf=pygame.display.set_mode((520,200))
						pygame.display.set_caption("CAZADOR DE MINAS UTM")
						while True:
							venatanaf.fill(azul)
							for evento in pygame.event.get():
								if evento.type==QUIT:
									pygame.quit()
									sys.exit()
							mifuentefin1=pygame.font.Font(None,40)
							mifuentefin=pygame.font.Font(None,25)
							feli=mifuentefin1.render("EREES UN BACAN GANASETE!!",0,(255,255,255))
							textotime=mifuentefin.render("TIEMPO: "+str(tiempo),0,(255,250,12))
							textopasos=mifuentefin.render("PASOS: "+str(movimientos-1),0,(250,255,12))
							venatanaf.blit(feli,(10,10))
							venatanaf.blit(textopasos,(10,40))
							venatanaf.blit(textotime,(10,60))
							pygame.display.update()
							time.sleep(5)
							secundaria()
					for fila in range(0,filas):
						for colu in range(0,colunas):
							
							pygame.draw.rect(ventanar,(255,255,255),(23*colu+3,23*fila+3,20,20))
							mifuentefin=pygame.font.Font(None,50)
							
							
							if matriz[f][c]==1:
							##if matriz[fila][colu]==0:
							    #ventanar.blit(cero,(23*colu+3,23*fila+3,20,20))
								if matriz[fila][colu]==1:
									
									##uno=pygame.image.load("imagenes/aterrisco.png")
									uno=mifuentefin.render("*",0,(0,0,0))
									mifuenteperdio=pygame.font.Font(None,100)
									perdio=mifuentefin.render("PERDIO",0,(255,0,0))
									pygame.draw.rect(ventanar,(250,250,250),(posx,posy,20,20))
									ventanar.blit(uno,(23*colu+5,23*fila+10))
									ventanar.blit(perdio,(120,80))
									pygame.display.update()
									perdido=1
						

					
					pasos=fuentetiempo.render("PASOS: "+str(movimientos),0,(250,255,12))
					pos=fuentetiempo.render("MINAS CERCA: "+str(m),0,(250,255,12))
					ventanar.blit(pasos,(150,240))
					ventanar.blit(pos,(3,240))
					contador=fuentetiempo.render("TIME: "+str(tiempo_juego),0,(250,255,12))
					pygame.draw.rect(ventanar,(azul),(150,260,150,20))
					ventanar.blit(contador,(150,260))
					pygame.draw.rect(ventanar,(255,211,0),(posx,posy,20,20))
					pygame.display.update()
					
		if salir==1:
			secundaria()
principal()				