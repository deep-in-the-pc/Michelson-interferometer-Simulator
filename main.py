from func import desfazamento, colourization, circunferencia, desenho
import numpy

i=1
print("hello world")
section = numpy.tile([1, 0], 3) #3*2 = 6
print(desfazamento(7,3.589,1,680))

print(colourization(700))

print(circunferencia(700))

print(desenho(circunferencia(700),1,1,680,section,i))

desenho(circunferencia(700),1,1,680,section,i)