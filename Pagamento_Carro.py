
while (True):

    nome_carro = input('Digite o nome do carro: ')
    preco_carro = int(input('Digite o valor do carro: '))
    modalid_pagamento = int(input("Digite a modalidade do pagamento \n 1.A vista \n 2.Parcelado \n 3.Troca com Veículo usado\n"))

    if(modalid_pagamento == 1):
        desconto = int(preco_carro) * 0.05
    
    
    elif(modalid_pagamento == 2) :
        desconto = 0
        parcelas = int(input("Quantas parcelas: "))
        if (parcelas >= 48):
            desconto = (preco_carro * 0.1) * -1
    

    
    elif(modalid_pagamento == 3) :
        desconto = 0.3
    

    else:
        print("Opção inválida")
        break
    
    imposto = preco_carro * 0.3
    perc_vendedor = preco_carro * 0.1
    lucro_loja = preco_carro * 0.15

    preco_final = preco_carro + imposto + perc_vendedor + lucro_loja - desconto
    diferença_preco = preco_final - preco_carro 

    print(f"Nome: {nome_carro}" )
    print(f"Preço: {preco_carro}")  
    print(f"Modalid_Pagamento: {modalid_pagamento}" )
    print(f"Preço final:  {preco_final}")
    print(f"Diferença: {diferença_preco}")


    


