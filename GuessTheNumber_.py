# Criar um jogo de numeros que utilize classes.
# Aplicação sistêmica
from random import randint
from time import sleep

# Definir o método __init__ como aceptor de qualquer comando
''' Variável de classe responsável por armazenar o valor da pontuação por sessão
                      À partir do momento em que o usuário digitar o valor inicial, tornam-se possíveis três POSSIBILIDADES: 
                       - Possibilidade de início de jogo
                       - Possibilidade de login, com a inserção do nome de usuário e 'criação de um perfil'
                                - Classe tem de ser iniciada novamente, fazendo com que o usuário insira seu nome no campo
                                
                       '''


class GameCore:

    total_score = 0

    def __init__(self, name=None):  # Definições básicas -- Atributos necessários para execução
        self.name = name
        print('Este é o GuessTheNumber!')

        if self.name is not None:        # Verificações relacionadas ao nome de usuário do jogador (passado na criação da classe):
            sleep(0.5)
            print('{}\nBem vindo(a), {}!\n{}'.format('-' * 20, name, '-' * 20))
            sleep(0.5)
        else:
            print('Running on anonymous mode;\ntype: /login {} to register\n{}'.format('"username"', '-' * 20))
# region CORE

    def show_menuActions(self,):
        print('- Alterar nome de usuário: /login "username"\n'
              '- Alterar dificuldade: /difficulty "easy", "medium", "hard"\n'
              '- Voltar: /resume\n')
        self.command = str(input('{}@command> '.format(str(self.name).lower())))

    def choice(self, difficulty=3):  # Armazena o número jogado pelo usuário
        self.user = input('Digite o número que pretende jogar: ')
        self.max = difficulty# Variável que armazena a dificuldade (definida pela quantidade de algarismos que podem ser sorteados pela cpu) de jogo
        try:
            self.user = int(self.user)
            if self.user in range(1, self.max + 1):
                pass
            else:
                self.choice()
        except:
            if self.user not in ['/login', '/menu']:
                self.choice()
            else:
                self.show_menuActions()

    def analyse(self):
        print(' SORTEANDO '.center(21, '-'))
        self.cpu = randint(1, self.max)
        sleep(0.5)
        for x in range(1, self.max + 1):
            sleep(0.2)
            if x is self.cpu:
                print('{}{}{}'.format('\033[1;31m', x, '\033[m'), end='')
            elif x is not self.cpu:
                print(x, end='')
        print('')
        if self.user == self.cpu:
            print('{}Certa resposta!{}'.format('\033[1;34m', '\033[m'))

            def score():

                return 1

            self.tot = score()
        else:
            print('{}Resposta Errada!{}'.format("\033[1;31m", "\033[m"))

            def score():
                return 0
            self.tot = score()

        GameCore.total_score += self.tot

    def terminate(self):
        print(f'Pontuação total nesta sessão: {GameCore.total_score} \n{" ^^^ ".center(21, "-")}')
# endregion
    def start(self, mode=None):
        print('Starting!')
        print('type /menu to access the options')
        self.mode = mode
        if self.mode is not None:
            self.verify_param = str(self.mode).split('=')
            if self.verify_param[1].capitalize() == 'True':
                while True:
                    print('Endless: ON')
                    self.choice(), self.analyse(), self.terminate()
        else:
            print('Endless: OFF')
            self.choice(), self.analyse(), self.terminate()


# Aplicação da classe ---
GameInstanceOne = GameCore('PintoJosé')
GameInstanceOne.start('semFim=True')
