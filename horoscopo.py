# Criar um sistema de informação que receba o dia e o mês de nascimento de uma pessoa e informe o signo
dia = int (input ('Digite o dia: '))
mes = int (input ('Digite o mes: '))
if (dia>=21 and mes==3) or (dia<=20 and mes==4):
    print ('Aries')
if (dia>=24 and mes==9) or (dia<=23 and mes==10):
    print ('Libra')
if (dia>=21 and mes==4) or (dia<=21 and mes==5):
    print ('Touro')
if (dia>=24 and mes==10) or (dia<=22 and mes==11):
    print ('Escorpiao')
if (dia>=22 and mes==5) or (dia<=21 and mes==6):
    print ('Gemeos')
if (dia>=23 and mes==11) or (dia<=21 and mes==12):
    print ('Sagitario')
if (dia>=21 and mes==6) or (dia<=23 and mes==7):
    print ('Cancer')
if (dia>=22 and mes==12) or (dia<=20 and mes==1):
    print ('Capricornio')
if (dia>=24 and mes==7) or (dia<=23 and mes==8):
    print ('Leao')
if (dia>=21 and mes==1) or (dia<=19 and mes==2):
    print ('Aquario')
if (dia>=24 and mes==8) or (dia<=23 and mes==9):
    print ('Virgem')
if (dia>=20 and mes==2) or (dia<=20 and mes==3):
    print ('Peixes')

