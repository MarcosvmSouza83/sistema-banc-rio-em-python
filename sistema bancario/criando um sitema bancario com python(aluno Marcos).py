
menu = """
================ *** Banco Santander *** ================

Olá Sr(a) Marcos Vinicius ,Digite a opção desejada...

[1] Depositar  
[2] sacar
[3] Extrato
[4] Saldo disponivel
[5] Pix
[0] Sair

=>"""

saldo = 5000
limite = 1500
pix = 5000
extrato = ""
numero_saques = 0
numero_pix = 0
LIMITES_SAQUES = 3
LIMITES_PIX = 3

input(menu)

while True:

    opção = input(menu)

    if opção == "1":
        valor = float(input("Informe o valor do depósito: "))


        
        if valor > 0:
            saldo += valor
            extrato +=  f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("operação falhou! o valor informado é invalido. ")
            

    elif opção == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES



        if excedeu_saldo:
          print("Operação falhou! Você não tem saldo suficiente.")


        elif excedeu_limite:
           print("Operação falhou! O valor do saque excede o limite disponivel.")    

        elif excedeu_saques: 
          print("Operação falhou! Numero Máximo de saques excedido.")

  
        elif valor > 0:
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n" 
            numero_saques += 1 

                
        else:
         print("Operação falhou!  O valor informado é inválido.") 


    elif opção == "3":  
      print("\n\n\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\n\nSaldo disponivel: R$ {saldo:.2f}")
      print("\n==============================================")
      

    elif opção == "4":
       print("\n================ SALDO ================")
       print("Sujeito alterações até o final do expediente.")
       print(f"\n\n\n\nSaldo disponivel: R$ {saldo:.2f}")
       print("\n=========================================")


    elif opção == "5":
         valor = float(input("Informe o valor do Pix: "))

         excedeu_saldo = valor > saldo

         excedeu_limite = valor > limite

         excedeu_pix = numero_pix >= LIMITES_PIX


         if excedeu_saldo:
          print("Operação falhou! Você não tem saldo suficiente.")


         elif excedeu_limite:
           print("Operação falhou! O valor do pix excede o limite disponivel.")    

         elif excedeu_pix: 
          print("Operação falhou! Numero Máximo de pix excedido.")

  
         elif valor > 0:
            saldo -= valor
            extrato +=  f"Pix: R$ {valor:.2f}\n" 
            numero_pix += 1
         elif opção == "0":
           valor = float(input)("================= Santander agradece a sua preferência! Obrigado.=====================")