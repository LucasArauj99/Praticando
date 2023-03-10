import os

class calculadora:
    def __init__(self, n1, n2, teste):
        self.n1 = n1
        self.n2 = n2
        self.teste = teste
    @staticmethod
    def imagem():
        print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")

    def soma(self, teste):
        if teste == '+':
            return self.n1 + self.n2
        elif teste == '-':
            return self.n1 - self.n2
        elif teste == '*':
            return self.n1 * self.n2
        elif teste == '/':
            return self.n1 / self.n2
        

def op():
    calculadora.imagem()       
    n1 = int (input("digite o primeiro numero:"))
    end_calculadora = False
    while not end_calculadora:
        teste = input('"+", "-", "/" ou "*": ')
        n2 = int(input('Digite outro numero:'))
        calculo = calculadora(n1, n2, teste)
        result = calculo.soma(teste)
        print(f'{n1} {teste} {n2} = {result}')
        #n1 = result
        cont = input("deseja continuar?[S] ou [N]:").upper() [0]
        if cont == 'S':
            n1 = result
        else:
            os.system("cls")
            op()
        
op()