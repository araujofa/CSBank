# IMPORTA BIBLIOTECA DATETIME
from datetime import datetime

# CRIA A CLASSE USER 
class User:
    # VARIAVEL DA CLASSE PARA PEGAR O ANO ATUAL
    get_year = datetime.today().year

    # CONSTRUTOR PADRÃO DA CLASSE CONTENDO PARÂMETROS PARA CRIAR UM OBJETO
    def __init__(self, nome='',email='', cpf='', ano_nascimento='', senha='', saldo='0'):
        self.nome = nome
        self.email = email
        self.ano_nascimento = ano_nascimento
        self.senha = senha
        self.saldo = saldo
        self.cpf = cpf

    # MÉTODO PARA CADASTRO DE UM USUARIO
    def Cadastro(self):
        ano_nascimento_tem_letras = True

        # VERIFICA SE AS VARIAVEIS NÃO POSSUEM CONTEUDO, CASO NÃO POSSUAM, ATRIBUI O VALOR QUE ESTIVER NELA MESMA
        if not self.nome and not self.cpf and not self.ano_nascimento and not self.email and not self.senha:
            self.nome = self.nome
            self.email = self.email
            self.ano_nascimento = self.ano_nascimento
            self.senha = self.senha
            self.cpf = self.cpf

        self.nome = input('Digite seu nome completo: ').split()
        self.email = input('Digite seu e-mail: ')

        while True:
            self.cpf = input('Digite seu CPF (Somente números): ')
            if self.cpf.isdigit():
                cpf_len = len(self.cpf)
                numbers_cpf = [int(digit) for digit in self.cpf]

                # FAZ A VERIFICAÇÃO SE O CPF CONTEM A QUANTIDADE DE DIGITOS CORRETOS
                if cpf_len == 11:

                    # FAZ A CONTA PARA SABER SE O PRIMEIRO DIGITO VERIFICADOR CORRESPONDE AO CPF DIGITADO
                    conta_digito_um = (numbers_cpf[0] * 10 + numbers_cpf[1] * 9 + numbers_cpf[2] * 8 + numbers_cpf[3] * 7 + numbers_cpf[4] * 6 + numbers_cpf[5] * 5 + numbers_cpf[6] * 4 + numbers_cpf[7] * 3 + numbers_cpf[8] * 2) * 10

                    # FAZ A CONTA PARA SABER SE O SEGUNDO DIGITO VERIFICADOR CORRESPONDE AO CPF DIGITADO
                    conta_digito_dois = (numbers_cpf[0] * 11 + numbers_cpf[1] * 10 + numbers_cpf[2] * 9 + numbers_cpf[3] * 8 + numbers_cpf[4] * 7 + numbers_cpf[5] * 6 + numbers_cpf[6] * 5 + numbers_cpf[7] * 4 + numbers_cpf[8] * 3 + numbers_cpf[9] * 2) * 10

                    # FAZ A VALIDAÇÃO INICIAL PARA SABER SE TODOS DIGITOS SÃO IGUAIS PARA INVALIDÁ-LO
                    if numbers_cpf[0] == numbers_cpf[1] and numbers_cpf[1] == numbers_cpf[2] and numbers_cpf[2] == numbers_cpf[3] and numbers_cpf[3] == numbers_cpf[4] and numbers_cpf[4] == numbers_cpf[5] and numbers_cpf[5] == numbers_cpf[6] and numbers_cpf[6] == numbers_cpf[7] and numbers_cpf[7] == numbers_cpf[8] and numbers_cpf[8] == numbers_cpf[9] and numbers_cpf[9] == numbers_cpf[10]:

                        print('CPF INVÁLIDO!')

                    else:

                        # CASO OS DIGITOS NÃO SEJAM TODOS IGUAIS, FAZ A VALIDAÇÃO SE O CPF É VALIDO OU NÃO
                        if conta_digito_um % 11 == numbers_cpf[9] and conta_digito_dois % 11 == numbers_cpf[10]:
                            pass
                            break
                        else:
                            print('CPF INVÁLIDO!')
                else:
                    print('CPF digitado contem a quantidade errada de digitos!')

            else:
                print('DIGITE SOMENTE NÚMEROS')

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
                self.saldo = float(self.saldo)
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
    
    # MÉTODO PARA QUE UM USUARIO POSSA LOGAR SUA CONTA
    def Logar(self):
        input_email_vazio = True
        input_senha_vazio = True
        input_nome_vazio = True

        # VERIFICA SE AS VARIAVEIS NÃO POSSUEM CONTEUDO, CASO NÃO POSSUAM, ATRIBUI O VALOR QUE ESTIVER NELA MESMA
        if not self.nome and not self.email and not self.senha:
            self.nome = self.nome
            self.email = self.email
            self.senha = self.senha

        # LOOP WHILE PARA VERIFICAÇÃO DE INPUT VAZIO
        while(input_nome_vazio):
            self.nome = input('Digite seu nome completo:')
            if self.nome == '':
                print('O CAMPO NÃO PODE FICAR VAZIO!')
            else:
                # ENCERRA WHILE LOOP CASO INPUT NÃO ESTEJA VAZIO
                input_nome_vazio = False

        # LOOP WHILE PARA VERIFICAÇÃO DE INPUT VAZIO
        while(input_email_vazio):
            self.email = input('Digite seu email: ')
            if self.email == '':
                print('O CAMPO NÃO PODE FICAR VAZIO!')
            else:
                # ENCERRA WHILE LOOP CASO INPUT NÃO ESTEJA VAZIO
                input_email_vazio = False

        # LOOP WHILE PARA VERIFICAÇÃO DE INPUT VAZIO
        while(input_senha_vazio):
            self.senha = input('Digite sua senha: ')
            if self.senha == '':
                print('O CAMPO NÃO PODE FICAR VAZIO!')
            else:
                # ENCERRA WHILE LOOP CASO INPUT NÃO ESTEJA VAZIO
                input_senha_vazio = False
            
        return
    
        