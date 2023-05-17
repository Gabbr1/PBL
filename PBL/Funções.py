from random import randint

player1 = ''
player2 = ''
opcao = -1
termList = []
rodada = 0
rodada += 1
tentativa = 0
tentativa += 1


def TelaGame():
    global rodada
    global tentativa
    print('---------------------------------------------------------------')
    print(' GAME: TERMO                                      ')
    print('')
    #print(f' Rodada:  '{rodada}'      Tentativa:  '{}'      jogador:  '{}'      ')
    print('')
    print('')
    print('[] [] [] [] []')
    print('')
    str(input('INSIRA UMA LETRA: '))
    print('\n\n\n\n\n\n\n\n\n\n')

def game():
    TelaGame()
    


def start():
    global opcao
    while opcao != '1' and opcao != '2':
        TelaGame1()
        opcao = str(input('INSIRA SUA OPÇÃO: '))
        print('\n\n\n\n\n\n\n\n')

       
        if opcao != '1' and opcao != '2':
            print('\n\033[31mOPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. \033[97m')
            
    if opcao == '1':
        TelaGame2()

def TelaGame1():
    print('----------------------------------------')
    print('| \033[30;47mGAME: TERMO \033[97;0m                         |')
    print('| \033[30;47mDESENVOLVIDO POR: Felipe Gabriel \033[97;0m    |')
    print('|                                      |')
    print('| Selecione:                           |')
    print('|                                      |')
    print('|\033[32m 1 - NOVO JOGO                        \033[97m|')
    print('|\033[31m 2 - SAIR                             \033[97m|')
    print('----------------------------------------\n')

def GameEspecification():
    print('----------------------------------------')
    print('|\033[36m TERMO:\033[37m                   \033[36m NOVO JOGO:\033[37m | ')
    print('----------------------------------------\n')

def TelaGame2():
    GameEspecification()
    global player1
    player1 = str(input('ADICIONE O NOME DO JOGADOR 1: '))
    print('')
    global player2
    player2 = str(input('ADICIONE O NOME DO JOGADOR 2: '))
    print('\n\n\n\n\n\n')
    GameEspecification()
    text = str(input('DIGITE ALGUM TEXTO ALEATÓRIO PARA O DICIONÁRIO: ')).upper()
    filter(text)
    tela()

def filter(text):
    wordslist = text.split(' ')
    for words in wordslist:
        words = words.replace(',', '').replace('.', '')
        if len(words.replace(',', '').replace('.', '')) == 5:
            global termList
            if words.replace(',', '').replace('.', '') not in termList:
                termList.append(words.replace(',', '').replace('.', ''))
                palavras = print(words)
    print('\n\n\n\n\n\n\n\n\n')
    #game(words)



def main():
    start()
    
if __name__ == "__main__":
    main()
