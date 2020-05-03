#Sudoku Solver 
#Author:Evgeni Pogoster
#This program solve any correct uncompleted sudoku.

#Instructions:Fill in the sudoku which you want to solve. If there is a void cell, enter "0".

#Intialize the Sudoku board

#You can to choose either to load sudoku as a file named sudoku.txt with unsolved sudoku or type it by key.
class Sudoku:
  def __init__(self, file =1):
#Open a file
    if file:
      self.sudoku = [[],[],[],[],[],[],[],[],[]]
      t=0;
      with open('sudoku.txt', 'r') as f:
        contents = f.readlines()
        for line in contents:
          raws=line.split()
          for num in raws:
            self.sudoku[t].append(int(num))
          t=t+1
#If there is no file available, type by hand    
    else:
      self.sudoku = [[],[],[],[],[],[],[],[],[]]
      self.EnterNumbers()
#A method to enter the sudoku by hand

  def EnterNumbers(self):
    for i in range(9):
      for j in range(9):
        self.sudoku[i].append(int(input("Enter a value for row"+ ' %d'%(i+1)+" and column"+' %d'%(j+1)+': ')));

#Prints the sudoku to the console.
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

  #Checks if the number is in a row
  def isInRow(self,row,number):
    for i in range(9):
      if (self.sudoku[row][i]==number):
        return True;
    return False;
  
  #Checks if the number is in a col
  def isInCol(self,col,number):
    for i in range(9):
      if(self.sudoku[i][col]==number):
        return True;
    return False;
  
  #Checks if the number is in a box
  def isInBox(self,row,col,number):
    r=row-row%3;
    c=col-col%3;
 
    for i in range(r,r+3):
      for j in range(c,c+3):
        if(self.sudoku[i][j]==number):
          return True;
    return False;

#Checks if the number is allowed in a specific place
  def isAllowed(self,row,col,number):
    return not (self.isInRow(row,number) or self.isInCol(col,number) or self.isInBox
    (row,col,number));

#Solves the sudoku
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

#Writes the solution into a file
  def Solution(self):
    f=open("solution.txt", "a")
    f.write("The Solution of the Sudoku is:\n\n")
    for i in range(9):
      if(i%3==0 and i!=0):
        f.write("---------------------------------\n");
      for j in range(9):
        if ((j+1)%3==0 and j!=0 and j!=8):
          f.write(str(self.sudoku[i][j])+' | ')
        else:
          f.write(str(self.sudoku[i][j])+'   ')
      f.write('\n')
    f.write("\n\n Hope you enjoyed the solver!")

  
sodu = Sudoku();  
sodu.PrintBoard();
sodu.Solver();
print("This is the Solved Sudoku:\n");
sodu.PrintBoard();
sodu.Solution();

