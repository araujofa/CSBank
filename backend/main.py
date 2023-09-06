from users import User
import os

os.system('cls')
print('--------------------------------------------')
print('        SEJA BEM-VINDO(A) AO CS BANK\n')
print('        1. CRIAR UMA CONTA')
print('        2. FAZER LOGIN')
print('--------------------------------------------\n')
option = int(input('>>>> '))

# INSTANCIANDO A CLASSE 'USER' COMO UM OBJETO 'USUARIO'
usuario = User()

if option == 1:
    os.system('cls')
    print('--------------------------------------------')
    print('                CADASTRE-SE!')
    print('--------------------------------------------\n')
    usuario.Cadastro()
    
    usuario_nao_saiu = True
    while(usuario_nao_saiu):
        os.system('cls')
        print('--------------------------------------------')
        print(f'          SEJA BEM-VINDO(A) {usuario.nome.upper()}')
        print('--------------------------------------------')
        print('          O QUE DESEJA FAZER HOJE?\n')
        print('          1. FAZER DEPOSITO')
        print('          2. FAZER SAQUE')
        print('          3. VER SALDO NA CONTA')
        print('          4. SAIR')
        print('--------------------------------------------\n')
        opt = int(input('>>>> '))

        if opt == 1:
            os.system('cls')
            print('--------------------------------------------')
            print('               FAZER DEPOSITO!')
            print('--------------------------------------------\n')
            usuario.Depositar()
        elif opt == 2:
            os.system('cls')
            print('--------------------------------------------')
            print('               FAZER SAQUE!')
            print('--------------------------------------------\n')
            usuario.Sacar()
        elif opt == 3:
            os.system('cls')
            print('--------------------------------------------')
            print('            SALDO EM CONTA: ')
            print('--------------------------------------------\n')
            print(f'Olá {usuario.nome.upper()}, seu saldo atual é de R${usuario.saldo}\n')

            input('PRESSIONE QUALQUER TECLA PARA VOLTAR')
        else:
            usuario_nao_saiu = False