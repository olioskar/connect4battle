# -*- coding: utf-8 -*-
#...þangað til annað kemur í ljós... 
#Klasi fyrir gervigreind
#Inniheldur minimax reiknirit
#Leikur næstaleik

# OOE...
# ToDo:
# gera ai-inn þannig að hann ráði við dýnamíska stærð af board
# Alltaf hægt að bæta gervigreindina
import copy
import random
class ai:
    
#   def __init__(self):

    
    #Notkun: CheckLegalMoves(board)
    #Fyrir: borð er n*m connect four borð
    #Eftir: moves[xi..xn] er fylki sem inniheldur löglega leiki td.[1,2,3,4,5,6,7]
    def CheckLegalMoves(self, board):
        v = []
        for i in range(0, board.columns):
            v.append(not board.ColumnIsFull(i+1))
        return v


    #Notkun: Svo að við séum alltaf með rétt tilvik af borði
    #skilar afriti af borðinu til að prófa næstaleik
    #tók þetta út úr computerplayer fallinu svo við séum ekki að bæta nýju og nýju staki inn á borðið í hverju tékki
    def boardCopy(self, board):
        boardNext = copy.deepcopy(board)
        return boardNext
    
    #notkun: x = assBoardState(b,p)
    #fyrir: b er board, p er player (-1 eða 1)
    #eftir: x er einhver tala > 0, því hærri því betri staða fyrir p
    def assBoardState(self, board,player):
        # til að byrja með notum við bara modified version af isWinner() fallinu
        # og teljum þrjá í röð fyrir tiltekinn spilara
            # lodrett:
        fylki = board.get()
        mod = 0
        for i in range(len(fylki)):
            for     j in range(len(fylki[i])-3):
                if fylki[i][j] == player and fylki[i][j+1] == player and fylki[i][j+2] == player:
                    #print "lodrett"
                    mod = mod + 1
        # larett
        for i in range(len(fylki)-3):
            for j in range(len(fylki[i])):
                if fylki[i][j] == player and fylki[i+1][j] == player and fylki[i+2][j] == player:
                    #print "larett"
                    mod = mod + 1
        # a ska til haegri   
        for i in range(len(fylki)-3):
            for j in range(len(fylki)-4):   
                if fylki[i][j] == player and fylki[i+1][j+1] == player and fylki[i+2][j+2] == player:
                    #print "a ska til haegri"
                    mod = mod + 1
        # a ska til vinstri
        for i in range(len(fylki)-1,2,-1):
            for j in range(len(fylki[j])-3):    
                if fylki[i][j] == player and fylki[i-1][j+1] == player and fylki[i-2][j+2] == player:
                    #print "a ska til vinstri"
                    mod = mod + 1
        return mod

    # Notkun x = getComputerMove(b, p, d)
    # Fyrir b er instance af board, p er annaðhvort 1 eða -1, d er dypt (helst <= 2)
    # eftir x er "vænlegasti leikurinn
    def getComputerMove(self, board, comPlayer,depth):
        # Bý fyrst til random move
        # Sjáum til hvor við notum þetta...
        # optMove = random.randint(1,board.columns)
        
        # availMoves er listi af mögulegum moves
        availMoves = self.getMoves(board, comPlayer,depth)
        
        #moveScore = max af availMoves[i] .. fáum þannig gildi bestu mögulegu færslunar
        moveScore = max(availMoves)
        
        # optMoves.Append <<-- rennum svo í gegnum for lúppu sem bætir við optMoves öllum moves sem eru == moveScore
        legalMoves = self.CheckLegalMoves(board)
        
        #villutjékk!
        #print legalMoves
        #print availMoves
        #print moveScore
        
        optMoves = []
        for i in range(len(legalMoves)):
            if legalMoves[i] and moveScore == availMoves[i]:
                #print "besta múvið: "
                #print i+1
                optMoves.append(i)
        if len(optMoves) <= 1:
            optMove = optMoves[0]+1
        else:
            optMove = optMoves[random.randint(0,len(optMoves)-1)]+1     
        return optMove

    def getMoves(self,board,player,depth):
        #MinMax algorithminn
        # ToDo:
        # gera move dínamískt þannig að stærðin ráðist af column.board
        # gera fall í board klasanum sem athugar hvort borð sé fullt til að spara ítranir hér.
        
        # samansöfnud stig fyrir hvert move
        # upphaflega er það 0 í hverju
        moves = [0,0,0,0,0,0,0]
        # athugum hvort buid er að ítra allt... 
        if depth <= 0:
            return [0,0,0,0,0,0,0] # Geri ráð fyrir fyrst að borð sé með 7 á breidd
        # AThuga hvort borð sé fullt! ... if board.isFull return [0,0,0,0,0,0,0]
        if board.isFull():
            return [0,0,0,0,0,0,0]
        enemy = player*-1 # mótspilari
        mod = 0 # modifier
        # Leikum fyrir player
        for i in range(board.columns):
            nextBoard = self.boardCopy(board) #Dupliceita borðið
            if not nextBoard.ColumnIsFull(i): # Athugum hvort leyfilegt sé að spila
                nextBoard.insert(player,i) # leikum löglegan leik
                mod = self.assBoardState(nextBoard,player)
                moves[i-1] = moves[i-1] + mod
                # Villutjékk
                #nextBoard.draw()
            if nextBoard.isWinner(player) == player: # leikum winningsleik
                moves[i-1] = 10 # nógu há tala svo tölva velji alltaf að vinna
                return moves
                #break # return moves <-- var ekki að virka rétt því við viljum tjékka hina möguleikana líka
            # Leikum fyrir enemy
            for j in range(board.columns):
                if not nextBoard.ColumnIsFull(j):
                    nextBoard.insert(enemy,j)
                    mod = self.assBoardState(nextBoard,enemy)
                    moves[i-1] = moves[i-1] - mod
                    #Villutjékk
                    #nextBoard.draw()
                if nextBoard.isWinner(enemy) == enemy: #Stoppum enemy
                    moves[i-1] = -9 # slæmt að leika í dálk i
                    moves[j-1] = 9  # betra að leika í dálk j
                    break # vitum að enemy vinnur ef við förum þessa leið...
                #skellum okkur í næstu ítrun
                moves[i] += self.getMoves(nextBoard,player,depth-1)[i]
        return moves


