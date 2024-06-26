preco = float(input("Qual o valor da compra?"))
print("""
     ======LOJA DARLAN======
     [ 1 ] A VISTA DINHEIRO
     [ 2 ] A VISTA CARTAO
     [ 3 ] 2x NO CARTAO
     [ 4 ] 3x NO CARTAO
      """)
opcao = int(input("Escolha a opcao de pagamento."))
if opcao == 1:
    desconto = preco * 0.9 
    print(f"o valor fica {desconto:.0f}R$ com o desconto de 10% aplicado.")
elif opcao == 2:
    desconto = preco * 0.95
    print(f"o valor fica {desconto:.0f}R$ com o desconto de 5% aplicado.")
elif opcao == 3:
    parcela = preco / 2
    print(f"Sua compra foi parcelada em 2x. O valor total ficou 2 parcelas de R${parcela:.0f}")
elif opcao == 4:
    num_parcela = int(input("Em quantas parcelas deseja? 3x ou mais: "))
    juros = preco + (preco * 0.2)
    final_parcelado = juros / num_parcela
    print(f"Sua compra sera parcelada em {num_parcela:.0f}x de R${final_parcelado:.0f} com juros.")
    print(f"sua compra de valor R${preco:.0f} vai custar R${juros:.0f} no final.")
else:
    print("opcao invalida")