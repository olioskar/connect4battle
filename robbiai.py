# -*- coding: utf-8 -*-
# ATH!
# Þetta script er AÐEINS til gamans! 
# Þetta er upphaflegi tölvuspilarinn okkar, en við lentum í blindgötu með hann.
# Eftir að hafa lent í miklu basli með robbiai.py, og sáum að sú nálgun var ekki að virka 
# ákváðum við að byrja alveg uppá nýtt og ai.py er afraksturinn af því.

#...þangað til annað kemur í ljós... 
#Klasi fyrir gervigreind
#Inniheldur minimax reiknirit
#Leikur næstaleik
import copy
import random
class robbiai:
    
    def __init__(self):
        a = 0
    
    #Notkun: CheckLegalMoves(board)
    #Fyrir: borð er n*m connect four borð
    #Eftir: moves[xi..xn] er fylki sem inniheldur True ef sæti fylkis er löglegur dálkur
    def CheckLegalMoves(self, board):
        v = [0,0,0,0,0,0,0] #Þarf alltaf að vera jafn langur og borðið sjálft
        for i in range(0, board.columns):
            if not board.ColumnIsFull(i+1):
                v[i]=True
            else:
                v[i]=False
        return v


    #Notkun: Svo að við séum alltaf með rétt tilvik af borði
    #skilar afriti af borðinu til að prófa næstaleik
    def boardcopy(self, board):
        boardNext = copy.deepcopy(board)
        return boardNext


    #Notkun: minimax(board,player, depth)
    #Fyrir: board er staða leiksins og v er vektor sem inniheldur löglega leiki
    #Eftir: ValueVector min/max gildum
    def computerPlayer(self, board, player,depth):
        ValueVector = [0,0,0,0,0,0,0]
        enemy = player * -1
        LegalMoves = self.CheckLegalMoves(board)
        for i in range(0, len(LegalMoves)):
            if LegalMoves[i]:
                if self.specialcase(board, enemy) == enemy:
                    return i+3
        for i in range(0, len(LegalMoves)):
            if LegalMoves[i]:
                ValueVector[i]=0
                ValueVector[i]=(self.minimaxValue(board,player,2,0,i+1))
        
        #for i in range(0, len(ValueVector)):
        #   print ValueVector[i]

        return(self.checkscore(ValueVector, LegalMoves))

    def checkscore(self, ValueVector, LegalMoves):
        #Ef ekkert sniðug gerist... enginn að vinna sérstaklega og enginn að tapa... þá random
        if min(ValueVector)==0 and max(ValueVector) ==0:
        #   print"random"           
            bil = len(LegalMoves)
            legalmove = False
            i=0
            while legalmove == False:
                i = random.randint(0,bil-1)             
                legalmove = LegalMoves[i]
            return i+1
        
        
        for i in range(0, len(ValueVector)):
            if ValueVector[i] == 666 and min(ValueVector) > -4:
                return i+1
        
        else:
            for i in range(0, len(ValueVector)):
                if ValueVector[i] == min(ValueVector):
                    return i+1      
                    
    #Notkun: minimaxValue(boardNext)
    #Fyrir: ekkert
    #Eftir: score er 
    def minimaxValue(self, board, player, depth, stig, column):
        enemy = player*(-1)
        boardNext = self.boardcopy(board)
        boardNext.insert(player,column)
        
        if boardNext.isWinner(player)==player:
            return  stig + (player * 4)
                                                        
        boardEnemy = self.boardcopy(board)
        boardEnemy.insert(enemy, column)
        if boardEnemy.isWinner(enemy)==enemy:
            return  666
        
#       if depth == 0:
#           return stig 
#       stig = self.stig(boardNext, player, stig, column)
#       if depth > 0:   
#           LegalMoves =  self.CheckLegalMoves(boardNext)
#           for i in range(0, len(LegalMoves)):
#               if LegalMoves[i]:
#                   stig = stig + self.stig(boardNext, (player)*-1, stig, i+1)
        else:
            if self.tveir(boardNext, column, player) == player:
                return stig + (player * 2)
            
            return 0
            
    def tveir(self, board, c, player):
        fylki = board.get()
#       print "c"
#       print c
        for i in range(len(fylki)-3):
            if fylki[c-1][i] == player and fylki[c-1][i+1] == player and fylki[c-1][i+2] == 0:
                return player
#       for i in range(len(fylki)-1):
#           if fylki[c-1][i] == player and fylki[c-1][i] == player and fylki[c-1][i] == 0:
#               return player
            
    def specialcase(self, board, player):
            
        fylki = board.get()
        
        
        for i in range(0,len(fylki)-3):
            for j in range(0,len(fylki[i])-1):
                if fylki[i][j] == 0 and fylki[i+1][j] == player and fylki[i+2][j] == player and fylki[i+3][j] == 0:
                    return player

        
#       
#       return 0
        

