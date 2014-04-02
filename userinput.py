# -*- coding: utf-8 -*-
from board import Board

class userinput:
    # ToDo:
    # Endurforrita fallið:
    #
    # í staðinn fyrir að láta makemove taka inn board hlut
    # er best að láta því skila int sem er column number.
    # Svo ætti að kalla á það í game.start() með board.insert(action.makemove())

    
    # Notkun: makemove(board,player)
    # Fyrir:  board er leikborð, player er annaðhvort 1 eða -1
    # eftir: búið er að setja inn disk á board fyrir player
    def makemove(self, theBoard, currentPlayer):
        try:
            validMove = False
            while not validMove:
                player = "[O] Player One: "
                if currentPlayer < 0:
                    player = "[X] Player Two: "
                print(player+'Pick a column')
                column = input()
                if column > 0 and column < 8 :
                    theBoard.insert(currentPlayer, column)
                    validMove = True
                    return True
                else:
                    print "You can only select columns from 1-7"
                    
        except NameError:
            print "Only numbers are allowed."
        except SyntaxError:
            print(player+'Pick a column')
            
        # except IndexError:
            # print "You can only select columns from 1-7"
                
