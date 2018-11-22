from func import desfazamento, colourization, circunferencia, desenho, franj
import numpy

cont=0 #variavel para rotacao de cores
comprimento=680 # em 10^-6  laser da experiencia esta em 632.8*10^-6
distancia=10200 #em 10^-7  precisao do parafuso micro = 0.1*10^-6


print(desfazamento(0.2,.1,1,comprimento))

print(colourization(comprimento)) #RGB

tppcomp=circunferencia(comprimento)#defenir circunf do comp de onda
#print(tppcomp)

section=numpy.tile([1,0],3) #criar vetor alternado de 1 e 0's
#print(section)

# calculo da franja

franja=franj(1,distancia,comprimento) #determinar n da freanja
print(numpy.floor(franja))

#teste do desenho
print(section)
franja,vectortrue,cont,section = desenho(tppcomp,section,cont, franja, comprimento)

print(franja,vectortrue,section,cont)

print(desenho(tppcomp,section,cont, franja,comprimento))