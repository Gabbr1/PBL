import random

player1 = ''
player2 = ''

player_1_pontuation = 0
player_2_pontuation = 0

text = []
option = -1
termlist = []
round_size = -1

tentative = 1
atual_rounds = 1
rounds_totality = 0

player_atuality = ''

atual_points = []

COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_RESET = '\033[0m'
COLOR_CIAN = '\033[36m'

def start():
    global option
    while option != '1' and option != '2':
        TelaGame()
        option = str(input('INSIRA SUA OPÇÃO: '))
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
       
        if option != '1' and option != '2':
            print(f'\n{COLOR_RED}OPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. {COLOR_RESET}')
            
    if option == '1':
        TelaGame1()
    elif option == '2':
        finish()

def TelaGame():
    print('----------------------------------------')
    print('| GAME: TERMO                          |')
    print('| DESENVOLVIDO POR: Felipe Gabriel     |')
    print('|                                      |')
    print('| Selecione:                           |')
    print('|                                      |')
    print(f'|{COLOR_GREEN} 1 - NOVO JOGO                        {COLOR_RESET}|')
    print(f'|{COLOR_RED} 2 - SAIR                             {COLOR_RESET}|')
    print('----------------------------------------\n')

def GameEspecification():
    print('----------------------------------------')
    print(f'|{COLOR_CIAN} TERMO:                   NOVO JOGO:{COLOR_RESET}  | ')
    print('----------------------------------------\n')

def TelaGame1():
    GameEspecification()
    global atual_rounds
    global player_atuality
    global player1
    global player2
    global text
   
    
    print(f'{COLOR_RED}O NOME DO JOGADOR 1 NÃO PODE SER IGUAL AO DO JOGADOR 2, ASSIM COMO AO INVERSO!\n{COLOR_RESET}')
    
    player1 = str(input('ADICIONE O NOME DO JOGADOR 1: '))
    print('')
    player2 = str(input('ADICIONE O NOME DO JOGADOR 2: '))
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    
    while player1 == '' or player2 == '' or player1 == player2:
      print(f'\n\n\n\n\n{COLOR_RED}OPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. {COLOR_RESET}')
      player1 = str(input('ADICIONE O NOME DO JOGADOR 1: '))
      print('')
      player2 = str(input('ADICIONE O NOME DO JOGADOR 2: '))    
      print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')   
      if player1 != '' or player2 != '' or player1 != player2:
          break
       
    if atual_rounds % 2 != 0:
        player_atuality = player1 
    else:
        player_atuality = player2
    GameEspecification()
    text = str(input('DIGITE ALGUM TEXTO ALEATÓRIO PARA O DICIONÁRIO: ')).upper()
    while text == '' or len(text)< 5:
        print(f'{COLOR_RED}OPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. {COLOR_RESET}')
        text = str(input('DIGITE ALGUM TEXTO ALEATÓRIO AO DICIONÁRIO: ')).upper()
        if text != '' and len(text) > 5:
          break
    filter(text)

    while True:
        print(f'\nValor Máximo: {len(termlist)}')
        rounds_totality = int(input("Defina a quantidade de rodadas: "))
        if rounds_totality > len(termlist):
            print(f'{COLOR_RED}OPS! A QUANTIDADE DE ROUNDS ULTRAPASSA A QUANTIDADE DE PALAVRAS NA LISTA DE PALAVRAS DO TERMO... POR FAVOR DIGITE UM VALOR MENOR!{COLOR_RESET}')
        elif rounds_totality == 0:
            print(f'{COLOR_RED}VOCÊ PROVAVELMENTE NÃO ADICIONOU NENHUM ITEM AO DICIONÁRIO OU SEU DICIONÁRIO NÃO TEM NENHUMA PALAVRA COM 5 LETRAS... REPITA O PROCESSO{COLOR_RESET}')
        elif rounds_totality <= len(termlist):
            break
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    TelaGame3()


def TelaGame3():
    global termlist
    global atual_rounds
    global tentative

    print('----------------------------------------------------------------------------------------------------------------------------')
    print('GAME: TERMO                                      ')
    print('')
    print(f'Rodada: {atual_rounds}         Rodadas Totais: {rounds_totality}         Tentativa: {tentative}         jogador: {player_atuality}')
    print('')
    print('')
    print('[] [] [] [] []')
    print('')
    termlist = str(input('INSIRA UMA PALAVRA: '))
    termlist = [letra.strip().upper for palavra in termlist for letra in palavra]
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def filter(text):
  wordslist = text.split(' ')
  for words in wordslist:
      words = words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', '')
      if len(words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', '')) == 5:
          global termlist
          if words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', '') not in termlist:
              termlist.append(words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', ''))
          print(text)
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def rounds():
    global tentative
    global atual_rounds

    if tentative == 6:
        atual_rounds+=1

def tentatives():
    global tentative

    while True:
        tentative+= 1
        break
    if tentative > 6:  
        tentative == 0

def finish():
    print('\033[32mMUITO OBRIGADO POR JOGAR!!! \n\n\n\n\n\n\n\033[0;0m')
    StopIteration

def reload():
    start()
