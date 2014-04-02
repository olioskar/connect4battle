# -*- coding: utf-8 -*-
# Nytt eintak af Board stendur fyrir spilabord 
# og stodu thess hverju sinni. Spilabordid samanstendur
# af x dalkum og y linum og z fjolda af "diskum" fra
# spilara 1 og 2. (x,y akvardast vid smid bordsins, 
# z er i upphafi 0 en breytist medan a spili stendur)
#
# ToDo
# laga til ýmis föll þannig að þau miði við columns og rows, en ekki 1 til 7 osfrv
# sjá t.d draw() fallið
class Board:
    # Gogn:
    # columns er breyddin a bordinu og rows er dyptin
    # matrix heldur utanum bordid sjalft og stodu thess
    # hverju sinni.
    # matrix[0] er dalkur 1, matrix[1] er dalkur 2 osfrv
    # matrix[0][0] er nedsta holf i dalki 1, 
    # matrix[0][1] er thad naesta i dalki 1, osfrv
    # ef x = matrix[n][m] tha:
    #   er n a bilinu [0..columns-1]
    #   er m a bilinu [0..rows-1] og
    #   x er annadhvort 0, -1, 1 thar sem
    #       0 er tomt holf,
    #       1 er diskur spilara 1 og
    #       -1 er diskur spilara 2.
    columns = 0
    rows = 0
    matrix = [] 
    
    # Notkun: b = Board(x,y)
    # Fyrir: x og y eru heiltolur
    # Eftir: b er nytt tomt leikbord med x dalkum og y linum
    def __init__(self, c, r):
        self.columns = c
        self.rows = r
        self.clear()
    
    #def copy(self):
    #   return self
    
    # Notkun: b.clear()
    # Fyrir: ekkert
    # eftir: b er tomt leikbord 
    def clear(self):
        self.matrix = []
        for x in range(self.columns):
            self.matrix.append([0]*self.rows)
    
    # Notkun: x = b.get()
    # Fyrir: ekkert
    # Eftir: x er tvivitt fylki sem sem inniheldur stodu leikbords
    #        x[n] er eru dalkar leikbords, x[n][m] eru holf.
    def get(self):
        return self.matrix
    
    # Notkun: b.insert(p,c)
    # Fyrir: p er annadhvort 1 eda -1
    #   fgffgf   c er heiltala > 0 og < en fjoldi dalka i b
    # Eftir: talan 1 eda -1 (fyrir p2) er i fyrsta lausa plassinu
    #        i dalki c i leikbordinu
    def insert(self, player, column):
        c = column - 1
        for i in range(0,self.rows):
            if self.matrix[c][i] == 0:
                self.matrix[c][i] = player
                return

    # Notkun: b.draw()
    # Fyrir: Ekkert
    # Eftir: leikbordid hefur verid prentad ut a skipanalinu.
    def draw(self):
        # Rada strengjum i stack og poppa tha svo ut
        # til ad fa i rettri rod.
        stack = []
        stack.append("1 2 3 4 5 6 7") # gera thetta dynamsikt seinna
        nextline = ""
        for r in range(0,self.rows):
            # Smida linur i streng
            for c in range (0,self.columns):
                if self.get()[c][r] == -1:
                    nextline += "X "
                if self.get()[c][r] == 1:
                    nextline += "O "
                if self.get()[c][r] == 0:
                    nextline += ". "
            stack.append(nextline)
            nextline = ""
        for x in range(len(stack)):
            print stack.pop()

    #Notkun: b.ColumnIsFull(1,2,...,7)
    #Fyrir: b er n*m connect four borð
    #Eftir: returns true ef dálkur n er með 6 stökum
    def ColumnIsFull(self, c):  
        if self.matrix[c-1][self.rows-1] == 0:
            return False
        return True
    
    # Notkun: x = b.boardIsFull()
    # fyrir: ekkert
    # eftir: x er true ef leikborðið er fullt.
    def isFull(self):
        for c in range(1, self.columns):
            if not self.ColumnIsFull(c):
                return False
        return True
      
    # Notkun: x = isWinner(p)
    # fyrir: p er annadhvort 1 eda -1 (player1 / player2)
    # eftir: ef engin hefur unnid tha x = 0, annars x = p
    def isWinner(self,player):
        # lodrett:
        fylki = self.get()
        for i in range(len(fylki)):
            for     j in range(len(fylki[i])-3):
                if fylki[i][j] == player and fylki[i][j+1] == player and fylki[i][j+2] == player and fylki[i][j+3] == player:
                    #print "lodrett"
                    return player 
        # larett
        for i in range(len(fylki)-3):
            for j in range(len(fylki[i])):
                if fylki[i][j] == player and fylki[i+1][j] == player and fylki[i+2][j] == player and fylki[i+3][j] == player:
                    #print "larett"
                    return player
        # a ska til haegri   
        for i in range(len(fylki)-3):
            for j in range(len(fylki)-4):   
                if fylki[i][j] == player and fylki[i+1][j+1] == player and fylki[i+2][j+2] == player and fylki[i+3][j+3] == player:
                    #print "a ska til haegri"
                    return player
        # a ska til vinstri
        for i in range(len(fylki)-1,2,-1):
            for j in range(len(fylki[j])-3):    
                if fylki[i][j] == player and fylki[i-1][j+1] == player and fylki[i-2][j+2] == player and fylki[i-3][j+3] == player:
                    #print "a ska til vinstri"
                    return player
        return 0

