lista = ['hamburguer', 'molho', 'agua', 'coxinha']
print(lista)
#['hamburguer', 'molho', 'agua', 'coxinha']

lista[3] = 'sorvete' #substitui o item 
print(lista)
#['hamburguer', 'molho', 'agua', 'sorvete']

lista.append('enroladinho') #adiciona um item na lista
print(lista)
#['hamburguer', 'molho', 'agua', 'sorvete', 'enroladinho']

lista.insert(0,'bacon') #adiciona um item na posicao que eu coloco antes do item. nesse exemplo a posicao foi 0, o item 0 vira item 1, 1 vira o 1 e assim sucessivamente.
print(lista)
#['bacon', 'hamburguer', 'molho', 'agua', 'sorvete', 'enroladinho']

del lista [3]#remove o item no indice que colocar
lista.pop(3) #normalmente é usando para deletar o ultimo item, porem, pode passaro indice do item para exclui-lo tambem.
lista.remove('agua') #aqui exclui o item pelo valor, ou seja, pelo nome.
##['bacon', 'hamburguer', 'molho', 'sorvete', 'enroladinho']

if 'agua' in lista:
    lista.remove('agua')#se tiver o item, ele remova, se nao, segue o jogo.
#['bacon', 'hamburguer', 'molho', 'sorvete', 'enroladinho']

valores = list(range(3, 11))#com o range a lista criad vai se acordo com os valores que eu declarar. posso ate colocar o step. (3,11,2) ai ele vai de 3 a 10 pulando de 2 em 2.
#['3', '4', '5', '6','7', '8','9', '10']

valores = ['3', '6', '9', '4', '5', '10'] #criei uma lista
valores.sort() #aqui eu organizo em ordem a lista
#['3', '4', '5', '6', '9', '10']
valores.sort(reverse=True) #aqui organizo em ordem reversa.
#['10', '9', '6', '5', '4', '3']

len(valores) #aqui eu sei o tamanho da lista
#6

valores = []
valores.append(5)
valores.append(2)
valores.append(7)

for chave, v in enumerate(valores): #o enumerate pega a chave do item.
    print(f"na posicao {chave} encontrei {v}")
#na posicao 0 encontrei 5
#na posicao 1 encontrei 2
#na posicao 2 encontrei 7

valores = lista #aqui eu crio uma ligacao entre elas, ou seja, se eu excluir um item da lista (lista), esse item tambem sera excluido na lista valores. o python cria uma ligacao entre elas.
valores = lista[:] # aqui o python faz uma copia, ou seja, nao tem ligacao entre as listas. se eu mudar um item na lista (lista), ele nao sera modificado na lista (valores)