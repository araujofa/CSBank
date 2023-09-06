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

        # VERIFICA SE AS VARIAVEIS NÃO POSSUEM CONTEUDO, CASO NÃO POSSUAM, ATRIBUI O VALOR QUE ESTIVER NELA MESMA
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
                        raise ValueError('SOMENTE MAIORES DE 18 ANOS PODEM ABRIR UMA CONTA')
                    # ENCERRA WHILE LOOP CASO USUARIO SEJA MAIOR DE 18 ANOS   
                    ano_nascimento_tem_letras = False  
                else:
                    print('O ANO DE NASCIMENTO DEVE CONTER QUATRO(4) NUMEROS')
            else:
                print('ANO DE NASCIMENTO PODE CONTER SOMENTE NÚMEROS!')
        
        self.senha = input('Digite uma senha: ')

        return
    
    # MÉTODO PARA QUE UM USUARIO POSSA FAZER UM DEPOSITO EM SUA CONTA
    def Depositar(self):
        saldo_tem_letras = True

        # VERIFICA SE AS VARIAVEIS NÃO POSSUEM CONTEUDO, CASO NÃO POSSUAM, ATRIBUI O VALOR QUE ESTIVER NELA MESMA
        if not self.saldo:
            self.saldo = self.saldo
        
        # LOOP WHILE FEITO PARA VERIFICAR SE O SALDO DO USUARIO CONTEM CARACTERES DIFERENTES DE NUMEROS
        while(saldo_tem_letras):
            deposit = input('Digite o valor a ser depositado: R$')
            # VERIFICA SE O QUE O USUARIO DIGITOU SÃO NUMEROS
            if deposit.isdigit():
                deposit = float(deposit)
                # VERIFICA SE O DEPOSITO DESEJADO PELO USUARIO É MAIOR QUE 0
                if deposit <= 0:
                    print('O VALOR A SER DEPOSITADO DEVE SER MAIOR QUE 0!')
                else:
                    print('DEPOSITO REALIZADO COM SUCESSO!')
                    # SOMA O DEPOSITO REALIZADO PELO USUARIO AO SEU SALDO ATUAL
                    self.saldo = deposit + float(self.saldo)
                    # ENCERRA WHILE LOOP CASO O DEPOSITO SEJA REALIZADO COM SUCESSO
                    saldo_tem_letras = False
            else:
                print('VALOR INVÁLIDO (DIGITE SOMENTE NUMEROS)') 

        return
    
    # MÉTODO PARA QUE UM USUARIO POSSA FAZER UM SAQUE DE SUA CONTA
    def Sacar(self):
        saque_tem_letra = True    
    
        # VERIFICA SE AS VARIAVEIS NÃO POSSUEM CONTEUDO, CASO NÃO POSSUAM, ATRIBUI O VALOR QUE ESTIVER NELA MESMA
        if not self.saldo:
            self.saldo = self.saldo
        
        # LOOP WHILE FEITO PARA VERIFICAR SE O SALDO DO USUARIO CONTEM CARACTERES DIFERENTES DE NUMEROS
        while(saque_tem_letra):
            saque = input('Digite o valor a ser sacado: R$')
            # VERIFICA SE O QUE O USUARIO DIGITOU SÃO NUMEROS
            if saque.isdigit():
                saque = float(saque)
                # VERIFICA SE O VALOR DESEJADO PARA SAQUE É MAIOR QUE O SALDO EM CONTA
                if saque > self.saldo:
                    print('SALDO INSUFICIENTE PARA SAQUE!')
                    # VERIFICA SE O SALDO EM CONTA DO USUARIO É IGUAL A 0
                    if self.saldo == 0:
                        print('Você não possui saldo em sua conta! volte e faça um deposito...\n')
                        input('PRESSIONE QUALQUER TECLA PARA VOLTAR')
                        # ENCERRA WHILE LOOP CASO O USUARIO NÃO POSSUA SALDO EM CONTA
                        saque_tem_letra = False
                # VERIFICA SE O VALOR DESEJADO PARA SAQUE É IGUAL A 0
                elif saque == 0:
                    print('VOCÊ NÃO PODE SACAR ESSE VALOR!')
                else:
                    # SUBTRAI O VALOR DESEJADO PARA SAQUE PELO USUARIO DO SEU SALDO ATUAL
                    self.saldo = self.saldo - saque
                    # ENCERRA WHILE LOOP CASO O SAQUE SEJA REALIZADO COM SUCESSO
                    saque_tem_letra = False
            else:
                print('VALOR INVÁLIDO (DIGITE SOMENTE NUMEROS)')
        
        return