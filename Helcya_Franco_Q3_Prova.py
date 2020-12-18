#Josemar trabalha numa revendedora de carros usados a cada carro vendido ele ganha 1,5 % de comissão. 
#Utilizando lista composta guarde o nome e preço dos carros. 
#Para vender o carro mostre uma tabela com os carros e os preços. 
#Quando o carro for vendido deve modificar a lista de carros para vendido. 

#A venda acaba quando os carros acabarem ou quando a pessoa não quiser continuar. 
#No final mostre: quantidade de carros vendidos e quanto Josemar lucrou no final em reais. 
#Para essa questão use pelo menos duas funções. 
loop = True
carros = [['Camaro', 20.000], ['Ferrari', 50.000],['Lamborghini', 70.000],['Celta', 5.000]]
carros_vendidos = []
comissao_josemar = 0

def venda_carros():
    print('=====================')
    print('CARROS\tPREÇO') 
    print('=====================')         
    for i in carros:
        print(f'{i[0]}......{i[1]},\n')
        print('======================')

def menu_compras():
    print('''
          ====================
          COMPRA DE AUTOMÓVEIS 
          ====================
          (1) Comprar um carro  
          --------------------
          (2) Sair
          ====================
          ''')
    
while loop:
    menu_compras()
    escolha_1 = int(input('Digite a opção de sua escolha:'))
    if escolha_1 == '1':
        venda_carros()
        escolha_2 = input('Digite o nome do carro de sua escolha:').capitalize()
        if escolha_2 == 'Camaro':
            carros_vendidos.append(carros[0:])
            carros[0][1] = 'Vendido'   
            comissao_josemar += carros[0][1] * 0.015  
        elif escolha_2 == 'Ferrari':
            carros_vendidos.append(carros[1:])
            carros[1][1] = 'Vendido'   
            comissao_josemar += carros[1][1] * 0.015  
        elif escolha_2 == 'Lamborghini':
            carros_vendidos.append(carros[2:])
            carros[2][1] = 'Vendido' 
            comissao_josemar += carros[2][1] * 0.015         
        elif escolha_2 == 'Celta':
            carros_vendidos.append(carros[3:])
            carros[3][1] = 'Vendido'
            comissao_josemar += carros[3][1] * 0.015  
        if len(carros_vendidos) == 4:
            loop = False
    print(f'Foram vendidos {len(carros_vendidos)} carros')
    print(f'Josemar obteve R${comissao_josemar} de comissão')

            
        
        

            
        
    
        
        
          
          

