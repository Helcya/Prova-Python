#Um novo funcionário de supermercado quer saber em qual corredor se encontra um produto. 
#No sistema existem os seguintes produtos: 
#Arroz - corredor 1, Feijão - corredor 1, Óleo de soja - corredor 2, 
#Sal - corredor 3, Açúcar - corredor 3, Café- corredor 4, Molho de tomate -corredor 5, Macarrão- corredor 6.
#O funcionário precisa encontrar em qual corredor está o produto para ajudar o cliente em sua compra. 
#Use tupla para criar esse programa.

corredor_1 = ('Arroz','Feijão')
corredor_2 = ('Óleo de soja')
corredor_3 = ('Sal','Açúcar')
corredor_4 = ('Café')
corredor_5 = ('Molho de tomate')
corredor_6 = ('Macarrão')
produto = input('Insira o nome do produto que você deseja procurar:').capitalize()
if produto in corredor_1:
    print(f'O {produto} está no Corredor 1')
elif produto in corredor_2:
    print(f'O {produto} está no Corredor 2')
elif produto in corredor_3:
    print(f'O {produto} está no Corredor 3')
elif produto in corredor_4:
    print(f'O {produto} está no Corredor 4')
elif produto in corredor_5:
    print(f'O {produto} está no Corredor 5')
else:
    print(f'O {produto} está no Corredor 6')




