# -*- coding: utf-8 -*-
# ATH!
# Þetta script er AÐEINS til gamans! 
# Hér etjum við saman upphaflega tölvuspilaranum 
# okkar (robbiai.py) við endurskrifaða tölvuspilarann (ai.py)
#
# Eftir að hafa lent í miklu basli með robbiai.py, og sáum að sú nálgun var ekki að virka 
# ákváðum við að byrja alveg uppá nýtt og ai.py er afraksturinn af því.
from board import Board
from userinput import userinput
from ai import ai
from robbiai import robbiai
import random
# hugmyndir...
# ...
# Game klasinn heldur utan um spilid sjalft
# hann smidar bord med board klasanum, tekur vid
# skipunum fra spilara i gegnum input klasann
class Game:
    # Gogn
    # player1 og player2 eru fastar, gildin (1 og -1) eru sett i gameBoard thegar
    # ad samsvarandi leikmadur gerir sina umferd. Einnig eru gildin notud til
    # ad skipta milli umferda
    #
    # currentPlayer er sa spilari sem a umferd hverju sinni
    #
    # winner er 0 ef enginn hefur unnid, -1 ef player2 hefur unnid og 1 ef player1 hefur unnid
    #
    # action tekur vid inntaki fra spilara
    #
    # gameBoard er spilabordid sem leikid er a
    player1 = 1
    player2 = -1
    currentPlayer = player1
    winner = 0 
    action = userinput()
    gameBoard = Board(7,6)

    def __init__(self):
        self.currentPlayer = self.player1
        self.winner = 0

    def start(self):
        comPlayer1 = ai()
        comPlayer2 = robbiai()
        difficulty = 2 # 2 tölva fljót að hugsa, gæti gert klaufavillur, 3 tölva lengi að hugsa.
        print "Welcome! Do you want Cthulhu to go first? [y/n]"
        if raw_input() == "n":
            self.currentPlayer = self.player2

        # Medan enginn hefur unnid
        while self.winner == 0:
            # Teikna bord
            self.gameBoard.draw()
            if self.currentPlayer > 0: #player 1
                self.gameBoard.insert(self.currentPlayer,comPlayer1.getComputerMove(self.gameBoard,self.currentPlayer,difficulty))
                print "==================="
                print "      Cthulhu      "
                print "==================="
            elif self.currentPlayer < 0 : #player 2
                self.gameBoard.insert(self.currentPlayer,comPlayer2.computerPlayer(self.gameBoard,self.currentPlayer,difficulty))   
                print "==================="
                print " Spaghetti Monster "
                print "==================="
            self.winner = self.gameBoard.isWinner(self.currentPlayer)
            # Skiptum!
            self.currentPlayer *= -1
    
        self.gameBoard.draw()
        print "AND THE WINNER IS!!!"
        if self.winner > 0:
            print "==================="
            print "      Cthulhu      "
            print "==================="
        elif self.winner < 0:
            print "==================="
            print " Spaghetti Monster "
            print "==================="
        
        print "WooooHoooo - The crowd goes Wild"

# Hefjum leikinn!!
iLoveThisGame = True
while iLoveThisGame == True:
    G = Game()
    G.start()
    print "Want to play again? [y/n] "
    if raw_input() == "n":
        iLoveThisGame = False
    G.gameBoard.clear()
        
