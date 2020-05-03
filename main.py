#Sudoku Solver 
#Author:Evgeni Pogoster
#This program solve any correct uncompleted sudoku.

#Instructions:Fill in the sudoku which you want to solve. If there is a void cell, enter "0".

#Intialize the Sudoku board

class Sudoku:
  def __init__(self, file = 0):
    if file:
      self.x=0
##      with open file as fw:
##        blabla
    else:
      self.sudoku = [[],[],[],[],[],[],[],[],[]]
      self.EnterNumbers()

  def EnterNumbers(self):
    for i in range(9):
      for j in range(9):
        self.sudoku[i].append(int(input("Enter a value for row"+ ' %d'%(i+1)+" and column"+' %d'%(j+1)+': ')));
  
  def PrintBoard(self):
    print('\n\n');
    for i in range(9):
      if(i%3==0 and i!=0):
        print("---------------------------");
      for j in range(9):
        if ((j+1)%3==0 and j!=0 and j!=8):
          print('%d'%(self.sudoku[i][j])+' | ', end="");
        else:
          print('%d'%(self.sudoku[i][j])+'  ', end="");
      print('\n');
  
  def isInRow(self,row,number):
    for i in range(9):
      if (self.sudoku[row][i]==number):
        return True;
    return False;
  
  def isInCol(self,col,number):
    for i in range(9):
      if(self.sudoku[i][col]==number):
        return True;
    return False;
  
  def isInBox(self,row,col,number):
    r=row-row%3;
    c=col-col%3;
 
    for i in range(r,r+3):
      for j in range(c,c+3):
        if(self.sudoku[i][j]==number):
          return True;
    return False;

  def isAllowed(self,row,col,number):
    return not (self.isInRow(row,number) or Sudoku.isInCol(col,number) or Sudoku.isInBox
    (row,col,number));

  def Solver(self):
    for row in range(9):
      for col in range(9):
        if (self.sudoku[row][col]==0):
          for num in range(1,10):
            if (self.isAllowed(row,col,num)):
              self.sudoku[row][col]=num;
              if(self.Solver()):
                return True;
              else:
                self.sudoku[row][col]=0;
          return False;
    return True;
  
sodu = Sudoku();  
sodu.PrintBoard();
sodu.Solver();
print("This is the Solved Sudoku:\n");
sodu.PrintBoard();
