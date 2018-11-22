from func import desfazamento, colourization, circunferencia, desenho, franj
import numpy

cont=0 #variavel para rotacao de cores
comprimento=680 # em 10^-9  laser da experiencia esta em 632.8*10^-6
distancia=11000 #em 10^-7  precisao do parafuso micro = 0.1*10^-6
print("hello world")

section=numpy.tile([1,0],3)
print(section)

print(desfazamento(7,3.589,1,comprimento))

print(colourization(comprimento)) #RGB

print(circunferencia(comprimento)) #defenir circunf do comp de onda

franja=franj(1,distancia,comprimento) # determinar n da freanja
print(numpy.floor(franja))
# for m in range(int(numpy.floor(franja))):
#     print("ok")

#teste do desenho
print(section)
franja,vectortrue,cont,section = desenho(circunferencia(comprimento),section,cont, franja, comprimento)

print(franja,vectortrue,section,cont)

print(desenho(circunferencia(comprimento),section,cont, franja,comprimento))