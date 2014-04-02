# -*- coding: utf-8 -*-
from board import Board
from userinput import userinput
from ai import ai
import random
# ToDo:
# Hreinsa upp (og helst endurskrifa) start() fallið.
# Gera difficulty að constant
# Lagfæra samskipti milli userinput og game klasana (sjá userinput) Virkar fínt núna
# en er frekar unintuitive.


# Game klasinn heldur utan um spilid sjalft
# hann smidar bord med board klasanum, tekur vid
# skipunum fra spilara i gegnum input klasann
class Game:
    # Gogn
    # player1 og player2 eru fastar, gildin (1 og -1) eru sett i gameBoard thegar
    # ad samsvarandi leikmadur gerir sina umferd. Einnig eru gildin notud til
    # ad skipta milli umferda
    # currentPlayer er sa spilari sem a umferd hverju sinni
    # winner er 0 ef enginn hefur unnid, -1 ef player2 hefur unnid og 1 ef player1 hefur unnid
    # action tekur vid inntaki fra spilara
    # gameBoard er spilabordid sem leikid er á

    player1 = 1
    player2 = -1
    currentPlayer = player1
    winner = 0 
    action = userinput()
    gameBoard = Board(7,6)

    def __init__(self):
        self.currentPlayer = self.player1
        self.winner = 0

    # Notkun: board.start()
    #   Byrjar leik
    # Eftir: Buid er ad spila heilan leik.
    def start(self):
        print "Welcome! Do you want to go first? [y/n]"
        if raw_input() == "n":
            isValid = True # Hack!
            self.currentPlayer = self.player2

        # aiOn segir til um hvort spilari spilar mot mennskun spilara eda tolvu
        aiOn = True
        if aiOn:
            comPlayer = ai()
            difficulty = 2 # 2 tölva fljót að hugsa, gæti gert klaufavillur, 3 tölva lengi að hugsa.
        # Medan enginn hefur unnid
        while self.winner == 0:
            # Teikna bord
            self.gameBoard.draw()
            if aiOn:
                if self.currentPlayer > 0:
                    isValid = self.action.makemove(self.gameBoard, self.currentPlayer)
                    print "== Human plays =="
                elif self.currentPlayer < 0:
                    print "== Computer plays =="
                    self.gameBoard.insert(self.currentPlayer,comPlayer.getComputerMove(self.gameBoard,self.currentPlayer,difficulty))
            elif not aiOn:
                # 2 mennskir spilarar
                isValid = self.action.makemove(self.gameBoard, self.currentPlayer)
            # Ath hvort spilari hafi unnid
            self.winner = self.gameBoard.isWinner(self.currentPlayer)
            
            # Skiptum!
            if isValid == True:
                self.currentPlayer *= -1
        
        self.gameBoard.draw()
        print "And the winner is:"
        print self.winner

# Hefjum leikinn!!
iLoveThisGame = True
while iLoveThisGame == True:
    G = Game()
    G.start()
    print "Want to play again? [y/n] "
    if raw_input() == "n":
        iLoveThisGame = False
    G.gameBoard.clear()
        
