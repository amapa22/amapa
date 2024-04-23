import random
x = random.randint(1,100)
cont=0
acertou=0
tentativas=int (100)




while  cont<100 and acertou==0 :
    cont+=1
    tentativas=int(input('Digite o número: '))
    if tentativas==x:
        acertou==1
     
        print(' \tPARABÉNS VOCẼ ACERTOU!!') 
    else:
        res= x- tentativas
        if(res >=15):
           print('frio')

        elif(res >5 and res <=15):
           print('morno')

        elif(res <=5):
           print('quente')


        print('\n\tERROU, TENTE NOVAMENTE ')
if acertou!=x:
 print('\n\tAcabou as suas chances ')            
elif acertou==x:
 print('\tO NÚMERO CORRETO ERA: ',x)


'''
Res= x - tentativa
________________________________
(dentro do else do erro)






'''