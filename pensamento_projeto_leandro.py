'''
Um Bloco de Comentarios.

projeto hamburgeria:


PO: (como dono do negocio: quero um sistema de vendas para a minha hamburgeria,
para que eu possa controlar as vendas e produtos.)

QA: (como cliente: quero um sistema de vendas para a minha hamburgeria para 
que eu possa comprar meus produtos favoritos de forma facil e rapido.)

Tech: (como programador: quero um sistema de vendas para a minha hamburgeria,
para que eu possa desenvolver um software eficiente e funcional para o negocio.)

Dev: (como programador quero um sistema de vendas para a minha hambuergeria
 para que eu possa implementar as funcionalidades necessarias para atender as 
 necessidades do negocio e dos clientes.)

UX: (como designer de experiencia do usuario: quero um sistema de vendas
 para a minha hambuergeria para que eu possa criar uma interface intuitiva e 
 agradavel para os usuarios, garantindo uma experiencia de compra satisfatoria.)

IA: (como analista de dados: quero um sistema de vendas para a minha hamburgeria,
para que eu possa coletar e analisar os dados de vendas, ajudando a identificar
padrões de consumo e otimizar as estrategias de marketing e estoque.)



'''

# print("Olá, Mundo!")


print("\n== Hamburgeria ===")

print("1. Cardapio ")
print("2. Bebidas ")
print("3. Sobremesas ")
print("4. Combos ")
print("5. Pedidos ")
print("6. Fazer Pedidos ")
print("7. Combo Infantil ")
print("8. Forma de Pagamento ")
print("9. Combo do Dia ")
print("0. Sair")
print('-' * 50 + "\n")

while True:
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print("Cardapio: ")
        print("- Hamburguer de carne")
        print("- Hamburguer de frango")
        print("- Hamburguer vegetariano")
        print("- Hamburguer vegano")
        print("- Batata frita")
        print("- Onion rings")
        print("- Salada")

    elif opcao == "2":
        print("Bebidas: ")
        print("- Refrigerante")
        print("- Suco natural")
        print("- Agua mineral")
        print("- Cerveja")

    elif opcao == "3":
        print("Sobremesas: ")
        print("- Milkshake")
        print("- Sorvete")
        print("- Brownie")
        print("- Pudim")

    elif opcao == "4":
        print("Combos: ")
        print("- Combo 1: Hamburguer + Batata frita + Refrigerante")
        print("- Combo 2: Hamburguer + Onion rings + Suco natural")
        print("- Combo 3: Hamburguer + Salada + Agua mineral")

    elif opcao == "5":
        print("Pedidos: ")
        print("- Pedido 1: Hamburguer de carne + Batata frita + Refrigerante")
        print("- Pedido 2: Hamburguer vegetariano + Salada + Agua mineral")
        print("- Pedido 3: Hamburguer vegano + Onion rings + Suco natural")
        pedidos = input ("Digite o numero do pedido desejado: ")
        print("\nPedido realizado com sucesso!")
      

    elif opcao == "6":
        print("Fazer pedidos: ")
        print("Digite o numero do combo desejado: ")
        combo = input()
        
        print("Digite a forma de pagamento: ")
        pagamento = input()

        print("\nPedido realizado com sucesso!")
        print("Combo escolhido:", combo)
        print("Forma de pagamento:", pagamento)
        
    
    elif opcao == "7":
        print("Combo infantil: ")
        print("- Combo infantil 1: Hamburguer de carne + Batata frita + Refrigerante")
        print("- Combo infantil 2: Hamburguer de frango + Onion rings + Suco natural")
        print("- Combo infantil 3: Hamburguer vegetariano + Salada + Agua mineral")
        combo = input("- Digite o numero do combo infantil desejado: ")
        print("\n Pedido realizado com sucesso!")

    elif opcao == "8":
        print("Forma de pagamento: ")
        print("- Dinheiro")
        print("- Cartao de credito")
        print("- Cartao de debito")
        print("- Pix")
        pagamento = input("Digite a forma de pagamento que você deseja: ")
        print("\nPagamento realizado com sucesso!")

    elif opcao == "9":
        print("Combo do Dia: ")
        print("- Combo do Dia 1: Hamburguer de carne + Batata frita + Refrigerante")
        print("- Combo do Dia 2: Hamburguer de frango + Onion rings + Suco natural")
        print("- Combo do Dia 3: Hamburguer vegetariano + Salada + Agua mineral")
        combo_dia = input("digite o combo que você quer: ")
        

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opcao invalida. Escolha uma opcao valida.")

