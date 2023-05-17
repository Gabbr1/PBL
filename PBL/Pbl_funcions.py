import random
#itl

score = 0

player1 = ''
player2 = ''

termList = []
    
def startGame():
    showGameMainScreenMessage()
    opcao = str(input('Insira a sua opção: '))
    
    if opcao == '1':
        showNewGameScreen()
    else:
        print('\033[31mÁdios hermano!\033[97m ')
  
    
    
def showGameMainScreenMessage():#mostra a tela inicial do jogo
    print('----------------------------------------')
    print('|\033[36m TERMO:\033[97m                               |')
    print('|                                      |')
    print('|\033[36m Desenvolvido por: Felipe Gabriel\033[97m     |')
    print('| Selecione:                           |')
    print('| 1 - Novo Jogo:                       |')
    print('| 2 - Sair:                            |')
    print('----------------------------------------\n')

def showNewGameScreenMessage():#mostra a proxima tela 
    print('----------------------------------------')
    print('|\033[36m TERMO:\033[30m                   \033[36m NOVO JOGO:\033[97m | ')
    print('----------------------------------------\n')

def showNewGameScreen(): 
    showNewGameScreenMessage();
    global player1
    player1 = str(input('Adicione o nome do jogador 1: '))
    global player2
    player2 = str(input('Adicione o nome do jogador 2: '))
    print('')
    showNewGameScreenMessage();
    text = str(input('Por favor, adicione um texto: '))
    createTermList(text) # create termlist vai obter o texto que foi digitado pelo usuário e vai passar para dentro dele, para ser processado
                         # como assim? Bom, o que irá acontecer é, depois que o funcionário obter o texto do escritor, vai mandar para o corretor
                         # que vai verificar quais palavras se encaixam no que foi pedido para ele que é separar todas as palavras que tem 5 letras no máximo
                         # e guardar em uma lista separada.
    

def createTermList(text):
    wordsList = text.split(' ')
    for words in wordsList:
        words = words.replace(',', '').replace('.','')
        if len(words.replace(',', '').replace('.','')) == 5:
            global termList
            if words.replace(',', '').replace('.','') not in termList:
                termList.append(words.replace(',', '').replace('.',''))
                print(words)
    print(termList)
    
    
def main():
    startGame()
    
if __name__ == "__main__":
    main()