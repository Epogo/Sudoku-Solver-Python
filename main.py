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
        sudoku[i].append(input("Enter a value for row"+ ' %d'%(i+1)+" and column"+' %d'%(j+1)+': '));
  
  def PrintBoard():
    print('\n\n');
    for i in range(9):
      if(i%3==0 and i!=0):
        print("---------------------------");
      for j in range(9):
        if ((j+1)%3==0 and j!=0 and j!=8):
          print(sudoku[i][j]+' | ', end="");
        else:
          print(sudoku[i][j]+'  ', end="");
      print('\n');
  
  def isInRow(number):
    




Sudoku.EnterNumbers();  
Sudoku.PrintBoard();
    
