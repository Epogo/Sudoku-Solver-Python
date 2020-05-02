#Sudoku Solver 
#Autor:Evgeni Pogoster
#This program solve any correct uncompleted sudoku.

#Instructions:Fill in the sudoku which you want to solve. If there is a void cell, enter "0".

#Intialize the Sudoku board
sudoku=[[],[],[],[],[],[],[],[],[]];

class Sudoku:

  def EnterNumbers():
    for i in range(9):
      for j in range(9):
        sudoku[i].append(int(input("Enter a value for row"+ ' %d'%(i+1)+" and column"+' %d'%(j+1)+': ')));
  
  def PrintBoard():
    print('\n\n');
    for i in range(9):
      if(i%3==0 and i!=0):
        print("---------------------------");
      for j in range(9):
        if ((j+1)%3==0 and j!=0 and j!=8):
          print('%d'%(sudoku[i][j])+' | ', end="");
        else:
          print('%d'%(sudoku[i][j])+'  ', end="");
      print('\n');
  
  def isInRow(row,number):
    for i in range(9):
      if(sudoku[row][i]==number):
        return True;
    return False;
  
  def isInCol(col,number):
    for i in range(9):
      if(sudoku[i][col]==number):
        return True;
    return False;
  
  def isInBox(row,col,number):
    r=row-row%3;
    c=col-col%3;
 
    for i in range(r,r+3):
      for j in range(c,c+3):
        if(sudoku[i][j]==number):
          return True;
    return False;

  def isAllowed(row,col,number):
    return not (Sudoku.isInRow(row,number) or Sudoku.isInCol(col,number) or Sudoku.isInBox
    (row,col,number));

  def Solver():
    for row in range(9):
      for col in range(9):
        if (sudoku[row][col]==0):
          for num in range(1,10):
            if (Sudoku.isAllowed(row,col,num)):
              sudoku[row][col]=num;
              if(Sudoku.Solver()):
                return True;
              else:
                sudoku[row][col]=0;
          return False;
    return True;
  
Sudoku.EnterNumbers();  
Sudoku.PrintBoard();
Sudoku.Solver();
print("This is the Solved Sudoku:\n");
Sudoku.PrintBoard();
    
