#Criar um sistema de informação que receba o dia e o mês de nascimento de uma pessoa e informe o signo
dia = int (input ('Digite o DIA do seu aniversário: '))
mes = int (input ('Digite o MES do seu aniversário: '))
if (dia>=21 and mes==3) or (dia<=19 and mes==4):
   print ('Seu Signo é Aries')
if (dia>=23 and mes==9) or (dia<=22 and mes==10):
   print ('Seu Signo é Libra')
if (dia>=20 and mes==4) or (dia<=20 and mes==5):
   print ('Seu Signo é Touro')
if (dia>=23 and mes==10) or (dia<=21 and mes==11):
   print ('Seu Signo é Escorpiao')
if (dia>=21 and mes==5) or (dia<=20 and mes==6):
   print ('Seu Signo é Gemeos')
if (dia>=22 and mes==11) or (dia<=21 and mes==12):
   print ('Seu Signo é Sagitario')
if (dia>=22 and mes==6) or (dia<=22 and mes==7):
   print ('Seu Signo é Cancer')
if (dia>=22 and mes==12) or (dia<=19 and mes==1):
   print ('Seu Signo é Capricornio')
if (dia>=23 and mes==7) or (dia<=22 and mes==8):
   print ('Seu Signo é Leao')
if (dia>=20 and mes==1) or (dia<=18 and mes==2):
   print ('Seu Signo é Aquario')
if (dia>=23 and mes==8) or (dia<=22 and mes==9):
   print ('Seu Signo é Virgem')
if (dia>=19 and mes==2) or (dia<=20 and mes==3):
   print ('Seu Signo é Peixes')


