import numpy


def desfazamento(l1, l2, n, lambluz):
    x = float(2 * numpy.pi * (l1 - l2) * n / (lambluz * 10 ** -9))
    return x

def colourization(Wavelength):

    if Wavelength >= 380 and Wavelength < 440:
        Red = -(Wavelength - 440) / (440 - 380)
        Green = 0.0
        Blue = 1.0
    elif Wavelength >= 440 and Wavelength < 490:
        Red = 0.0
        Green = (Wavelength - 440) / (490 - 440)
        Blue = 1.0
    elif Wavelength >= 490 and Wavelength < 510:
        Red = 0.0
        Green = 1.0
        Blue = -(Wavelength - 510) / (510 - 490)
    elif Wavelength >= 510 and Wavelength < 580:
        Red = (Wavelength - 510) / (580 - 510)
        Green = 1.0
        Blue = 0.0
    elif Wavelength >= 580 and Wavelength < 645:
        Red = 1.0
        Green = -(Wavelength - 645) / (645 - 580)
        Blue = 0.0
    elif Wavelength >= 645 and Wavelength < 781:
        Red = 1.0
        Green = 0.0
        Blue = 0.0
    else:
        Red = 0.0
        Green = 0.0
        Blue = 0.0

#factor é intensidade das cores
    if Wavelength >= 380 and Wavelength < 420:
        factor = 0.3 + 0.7 * (Wavelength - 380) / (420 - 380)
    elif Wavelength >= 420 and Wavelength < 701:
        factor = 1.0
    elif Wavelength >= 701 and Wavelength < 781:
        factor = 0.3 + 0.7 * (780 - Wavelength) / (780 - 700)
    else:
        factor = 0.0

    return Red, Green, Blue, factor

def circunferencia(wavelength): #cria vector com as circunferencias a delimitar
    k=numpy.zeros(6)
    for x in range(6):
        k[x]+=wavelength*(x+1)

    return tuple(k)


def franj(n,d,lambluz):
    franjas = n * 2 * (d * 10 ** -7) / (lambluz * 10 ** -6)  # formula do enunciado para nº de franjas

    return franjas

def desenho(vector, section, i, franjas,lambluz):
    #section = numpy.tile([1, 0], 12) # vetor para identificar cor

    #movimento do valor de franjas (neste caso de o d desce ou sobe)
    if numpy.floor(franjas)>i : # verifica se o numero de franjas aumentou
        section=numpy.roll(section,int(numpy.floor(franjas)-i))         #caso sim ele da switch de cor branco pa preto
        i=numpy.floor(franjas)

    if numpy.floor(franjas)<i : # verifica se o numero de franjas diminuiu
        section=numpy.roll(section,-1)
        i=numpy.floor(franjas)



    sender=numpy.zeros(6)#vetor para enviar pq o vector[x] agr é um tupple

    for x in range(6):  # diminui progressivamente a imagem para representar o movimento
        sender[x]= vector[x]-(lambluz*(franjas-numpy.floor(franjas))) #o vector[x]tem que ser tupple para

    return franjas, sender, i ,section