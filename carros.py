import os

carros = []

class Carro:

    nome = ''
    potencia = 0
    velociade = 0
    ligado = False

    def __init__(self,nome,pot):

        self.nome = nome
        self.potencia = pot
        self.velociade = int(pot * 2)

    def Ligar(self):
        self.ligado= True

    def Deligar(self):
        self.ligado = False

    def Info(self):
        print('Nome: ' + self.nome)
        print('potencia: ' + str(self.potencia))
        print('Velocidade: ' + str(self.velociade))
        print('Ligado: ' + ('sim' if self.ligado else 'não'))

def Menu():
    os.system('cls') or None
    print('1 - Novo carro')
    print('2 - Info carro')
    print('3 - Excluir carro')
    print('4 - ligar carro')
    print('5 - desligar carro')
    print('6 - listar carro')
    print('7 - sair')
    print('Quantidade de carros: '+ str(len(carros)))
    opc = input('Digite uma opção: ')
    return opc

def Novocar():
    os.system('cls') or None
    n = input('Digite o nome do carro: ')
    p = input('Digite s potencia do carro: ')
    car = Carro(n,p)
    carros.append(car)
    print('Novo carro criado')
    os.system('pause')

def Informacoes():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja ver as irfomações: ')
    try:
        carros[int(n)].Info()
    except:
        print('Carro não existe na lista')
    os.system('pause')

def Excluircar():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja excluir: ')
    try:
       del  carros[int(n)]
    except:
        print('Carro não existe na lista')
    os.system('pause')


def Ligarcar():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja ligar: ')
    try:
         carros[int(n)].Ligar()
         print('Carro ligado')
    except:
        print('Carro não existe na lista')
    os.system('pause')

def Deligarcar():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja desligar: ')
    try:
         carros[int(n)].Desligar()
         print('Carro desligado')
    except:
        print('Carro não existe na lista')
    os.system('pause')

def listarCar():
    os.system('cls') or None
    p = 0
    for c in carros:
         print(str(p) + '-' + c.nome)

ret = Menu()
while ret < '7':
    if ret == '1':
        Novocar()
    elif ret == '2':
        Informacoes()
    elif ret == '3':
        Excluircar()
    elif ret == '4':
        Ligarcar()
    elif ret == '5':
        Deligarcar()
    elif ret == '6':
        listarCar()
    ret = Menu()

os.system('cls') or None
print('Programa finalizado')