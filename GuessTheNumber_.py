# Criar um jogo de numeros que utilize classes.
# Aplicação sistêmica
from random import randint
from time import sleep


class GameCore:

    a = 0

    def __init__(self, name=None):  # Definições básicas -- Atributos necessários para execução
        self.total_score = 0
        self.name = name
        print('Este é o GuessTheNumber!')

        if self.name is not None:        # Verificações relacionadas ao nome de usuário do jogador (passado na criação da classe):
            sleep(0.5)
            print('{}\nBem vindo(a), {}!\n{}'.format('-' * 20, name, '-' * 20))
            sleep(0.5)
        else:
            print('Running on anonymous mode;\ntype: /menu to acess the options\n{}'.format('-' * 20))
# region CORE

    def show_menuActions(self):
        print(' MAIN MENU '.center(40, '-'),
              '\n- Alterar nome de usuário: /login "username"\n'
              '- Alterar dificuldade: /difficulty "easy", "medium", "hard"\n'
              '- Voltar: /resume \n'
              '- Exit: /quit')
        self.command = str(input('{}@command_central> '.format(str(self.name).lower())))

        self.dfclt = {'easy': 3,
                      'medium': 5,
                       'hard': 7}

        if self.command == '/quit':
            exit()
        elif self.command == '/resume':
            return None
        elif str(self.command).strip()[0:6] == '/login' and self.command[7:] != '':
            self.name = self.command[7:].replace(' ', '')

            sleep(0.5)
            print('{}\nBem vindo(a), {}!\n{}'.format('-' * 20, self.name, '-' * 20))
            sleep(0.5)

            return self.show_menuActions()
        elif self.command[:11] == '/difficulty' and self.command[11:].replace(' ', '') is not '':

            def acessesto():
                GameCore.a += 1
            acessesto()

            print('Valor alterado com sucesso! Mudanças serão aplicadas na próxima partida.')
            return None


        else:
            return None

    def choice(self, difficulty=3):  # Armazena o número jogado pelo usuário
        if GameCore.a > 0:
            self.max = self.dfclt[self.command[11:].replace(' ', '')]
        else:
            self.max = difficulty
        self.user = None # Variável que armazena a dificuldade (definida pela quantidade de algarismos que podem ser sorteados pela cpu) de jogo

        def check():

            def verify():
                while True:
                    self.user = input(f'Digite o número que pretende jogar [1-{self.max}]: ')
                    if str(self.user).isnumeric() is True and int(self.user) in range(1, self.max + 1):
                        self.user = int(self.user)
                        break

                    elif str(self.user).lower() in ['/menu'] and str(self.user) is not '' and self.user is not None:
                        self.show_menuActions()

                    else:
                        print('Digite um valor válido!')

            if str(self.user).isnumeric() is True:
                if int(self.user) in range(1, self.max + 1):
                    pass
                else:
                    verify()
            elif str(self.user).lower() in ['/login', '/menu']:
                self.show_menuActions()
                if self.show_menuActions() is None:
                    verify()

            else:
                verify()
        check()

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
        if int(self.user) == self.cpu:  # Verificação de respostas
            print('{}Certa resposta!{}'.format('\033[1;34m', '\033[m'))

            def score():

                return 1

            self.tot = score()
        else:
            print('{}Resposta Errada!{}'.format("\033[1;31m", "\033[m"))

            def score():

                return 0

            self.tot = score()

        self.total_score += self.tot

    def terminate(self):
        print(f'Pontuação total nesta sessão: {self.total_score} \n{" ^^^ ".center(21, "-")}')
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
GameInstanceOne = GameCore('DaviR')
GameInstanceOne.start()


