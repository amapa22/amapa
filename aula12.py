from colorama import Fore, Style


#DECLARAÇÃO DE UMA LISTA VAZIA 
lita1=[]

#DECLARAÇÃO DE UMA LISTA COM VALORES ESPECÍFICOS
lista2=[10,20,30]
print("lista inicial")

#DECLARAÇÃO DE LISTA COM VALORES VARIADOS PREENCHIDOS
lista3=[857, 15.2, "teste"]

print('imprimindo a lista original', lista3)

#PARA INCLUIR VALORES A UMA LISTA
lista2.append(50)#APPEND INCLUI QUALQUER ELEMENTO AO FINAL DA LISTA]
lista2.append(80)
lista2.append(90)


print('conteúdo lista',lista2[5])

#ATUALIZAR A 2 POSIÇÃO
lista2[2]=75


#ENTRADA DE DADOS
novovalor=(int(input('\n\tDIGITE UM VALOR: ')))
lista2.append(novovalor)

print(f"\n{Fore.GREEN}CONTEÚDO DA LISTA COM SEU NÚMERO NO FIM\n\n\t", lista2)

tamanho=len (lista2)
numeroBusca=int(input('\nDIGITE UM VALOR PARA DESCOBRIR SUA POSIÇÃO: '))
posicao=-1
for i in range (tamanho):
        if lista2[i]==numeroBusca:
            posicao=i

if(posicao!=-1):
      print('\n\tA POSIÇÃO É: ',posicao+1)                
       
 
 
else:
    print('VALOR NÃO ENCONTRADO.')