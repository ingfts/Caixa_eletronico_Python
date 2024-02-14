from datetime import date
data = date.today()
dt = data.strftime("%d/%m/%Y")


class conta: 
    
    
    def __init__(self, prop, tipo_conta, saldo = 1000): 
        self.prop = prop 
        self.tipo_conta = tipo_conta 
        self.saldo = saldo
    #
    #
    #
    
    def get_tipo_conta(self): 
        return self.tipo_conta 
    #
    #
    #
    
    def set_tipo_conta(self, tipo):
        if tipo == 1: 
            self.tipo_conta = 'CORRENTE'
            
            
        elif tipo == 2: 
            self.tipo_conta = "POUPANCA"
        
        else: 
            print("Opção inválida!")
            return exit()
            
    #
    #
    #
            
    def get_saldo(self): 
        return self.saldo
    #
    #
    #
    
    def sacar (self, valor): 

        if valor > self.saldo: 
            print("\n Você não possui este valor em conta!")
            
        else: 
            self.saldo -= valor
            return self.saldo
    
    #
    #
    #
    
    def depositar (self, valor): 
        self.saldo += valor
    
    
    #
    #
    #
    
    def menu (self): 
         op = int(input("\nOPÇÕES:\n 1-SAQUE  2-DEPOSITO  3-EXTRATO  4-SAIR  \n"))
         if op == 1: 
             saque = input("Digite o valor para saque: \n")
             self.sacar(int(saque))
             self.menu()
         elif op == 2: 
             deposito = input("Digite o valor para deposito: \n")
             c1.depositar(int(deposito))
             self.menu()
         elif op == 3: 
            self.extrato()
         elif op == 4: 
             print("\n Finalizando...")
             exit()
            
    #
    #
    #
    
    def extrato (self): 
        
        print("           ******************************")
        print("           ******************************")
        print("           EXTRATO DE CONTA -",self.tipo_conta,"*")
        print("           CLIENTE: ",self.prop)
        print("           ********   ")
        print("           DATA: ",  "            TIPO CONTA:")
        print("           ********           ***********")
        print("          "      ,dt, "       ", self.tipo_conta,"*")
        print("           **********   ")
        print("           ****** SALDO:"       , self.saldo,'R$',"******")
        print("           ******************************")
        print("           ******************************")
        print("           ******************************")
        print("           ******************************")
        


        
    
        self.menu()
    
    #
    #
    #

nome = input("\n> Digite seu nome: ")
tipo = int(input("\n> Insira o tipo de conta: \n  1-CORRENTE  2-POUPANCA \n"))
#
#
c1 = conta(nome, tipo) 
c1.set_tipo_conta(tipo)
c1.menu()






