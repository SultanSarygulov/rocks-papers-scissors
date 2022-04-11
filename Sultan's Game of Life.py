from tkinter import *
from time import sleep
from random import choice

class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        self.c = c
        self.mat = []
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.walls = walls
        self.count = 0
        self.moves = 0

        for j in range(self.m):
            self.mat.append([])
            for i in range(self.n):
                self.mat[j].append(choice([0,0,0,0,1,2,3]))
                
        
        self.draw()
       
    def step(self):
        for j in range(1,self.m-1):
            for i in range(1,self.n-1):
                if self.mat[i][j] == 1:
                    if self.mat[i-1][j-1] == 2 or self.mat[i][j-1] == 2 or self.mat[i+1][j-1] == 2 or self.mat[i-1][j] == 2 or self.mat[i+1][j] == 2 or self.mat[i-1][j+1] == 2 or self.mat[i][j+1] == 2 or self.mat[i+1][j+1] == 2: 
                        self.mat[i][j] = 2
                    else:
                        self.mat[i][j] = 0

                elif self.mat[i][j] == 2:
                    if self.mat[i-1][j-1] == 3 or self.mat[i][j-1] == 3 or self.mat[i+1][j-1] == 3 or self.mat[i-1][j] == 3 or self.mat[i+1][j] == 3 or self.mat[i-1][j+1] == 3 or self.mat[i][j+1] == 3 or self.mat[i+1][j+1] == 3: 
                        self.mat[i][j] = 3
                    else:
                        self.mat[i][j] = 0

                elif self.mat[i][j] == 3:
                    if self.mat[i-1][j-1] == 1 or self.mat[i][j-1] == 1 or self.mat[i+1][j-1] == 1 or self.mat[i-1][j] == 1 or self.mat[i+1][j] == 1 or self.mat[i-1][j+1] == 1 or self.mat[i][j+1] == 1 or self.mat[i+1][j+1] == 1: 
                        self.mat[i][j] = 1
                    else:
                        self.mat[i][j] = 0

    def draw(self):
        '''
        we draw/color our field
        '''

        color = "WHITE" 
        for j in range(1,self.m-1):
            for i in range(1,self.n-1):
                if self.mat[i][j] == 1:
                    color = "RED"
                elif self.mat[i][j] == 2:
                    color = "GRAY"
                elif self.mat[i][j] == 3:
                    color = "YELLOW"
                else:
                    color = "WHITE"
                    

                self.body = self.c.create_rectangle((i)*self.width, 
                (j)*self.height, 
                (i+1)*self.width, 
                (j+1)*self.height,
                fill = color)

                #mylabel = c.create_text(((i+1)*self.width - self.width / 2,(j+1)*self.height - self.height / 2), 
                #text=self.mat[i][j])
        
        self.step()
        self.c.after(600,self.draw)


root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

f = Field(c, 40, 40, 20, 20)

root.mainloop()

