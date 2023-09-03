# IMPORTA BIBLIOTECA DATETIME
from datetime import datetime

# CRIA A CLASSE USER 
class User:
    # VARIAVEL DA CLASSE PARA PEGAR O ANO ATUAL
    get_year = datetime.today().year

    # CONSTRUTOR PADRÃO DA CLASSE CONTENDO PARÂMETROS PARA CRIAR UM OBJETO
    def __init__(self, nome='',email='', ano_nascimento='', senha='', saldo='0'):
        self.nome = nome
        self.email = email
        self.ano_nascimento = ano_nascimento
        self.senha = senha
        self.saldo = saldo

    # MÉTODO PARA CADASTRO DE UM USUARIO
    def Cadastro(self):
        ano_nascimento_tem_letras = True

        # VERIFICA SE AS VARIAVEIS NÃO POSSUEM CONTEUDO, CASO NÃO POSSUAM, ADICIONA O VALOR QUE ESTIVER NELA MESMA
        if not self.nome and not self.ano_nascimento and not self.email and not self.senha:
            self.nome = self.nome
            self.email = self.email
            self.ano_nascimento = self.ano_nascimento
            self.senha = self.senha

        self.nome = input('Digite seu nome completo: ')
        self.email = input('Digite seu e-mail: ')

        # LOOP WHILE FEITO PARA VERIFICAR SE O ANO DE NASCIMENTO DO USUARIO CONTEM CARACTERES DIFERENTES DE NUMEROS
        while(ano_nascimento_tem_letras):
            self.ano_nascimento = input('Digite seu ano de nascimento: ')
            # VERIFICA SE O QUE O USUARIO DIGITOU SÃO NUMEROS
            if self.ano_nascimento.isdigit():
                # VERIFICA SE O ANO QUE O USUARIO DIGITOU TEM A QUANTIDADE CORRETA DE NUMEROS
                if len(str(self.ano_nascimento)) == 4:
                    self.ano_nascimento = int(self.ano_nascimento)
                    # VERIFICA SE O USUARIO TEM IDADE SUPERIOR A 18 ANOS
                    if self.get_year - self.ano_nascimento < 18:
                        print('SOMENTE MAIORES DE 18 ANOS PODEM ABRIR CONTA!')
                        return
                    # ENCERRA WHILE LOOP      
                    ano_nascimento_tem_letras = False  
                else:
                    print('O ANO DE NASCIMENTO DEVE CONTER QUATRO(4) NUMEROS')
            else:
                print('ANO DE NASCIMENTO PODE CONTER SOMENTE NÚMEROS!')
        
        self.senha = input('Digite uma senha: ')

        return
    
    def Depositar(self):
        saldo_tem_letras = True

        if not self.saldo:
            self.saldo = self.saldo
        
        while(saldo_tem_letras):
            deposit = input('Digite o valor a ser depositado: R$')
            if deposit.isdigit():
                deposit = float(deposit)
                if deposit <= 0:
                    print('O VALOR A SER DEPOSITADO DEVE SER MAIOR QUE 0!')
                else:
                    print('DEPOSITO REALIZADO COM SUCESSO!')
                    self.saldo = deposit + float(self.saldo)
                    saldo_tem_letras = False
            else:
                print('VALOR INVÁLIDO (DIGITE SOMENTE NUMEROS)') 

        return