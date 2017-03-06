
class Board:
    """ This class holds the state information for a game of TicTacToe 
    as well as provides methods to add a move and determine a winner. Each
    of the squares on the Tic-Tac-Tow board are labeled with a number 1-9.
    The figure below shows the board labeling used. 

        1|2|3
        -----
        4|5|6
        -----
        7|8|9

    Attributes:
      movesList - a growing list of squares picked by the players on their
                   turn in the order they were picked. Thus, the first list
                   element is always the square where X first went, the second
                   list element is always where O went after X, etc. In other 
                   words, the even indexed elements are X's moves, the
                   odd indexed elements are O's moves. When the list has
                   9 elements, the game board must be full.
    """
    def __init__(self):
        self.movesList = []  # board is empty at beginning
        
    def TryMove(self,squareNum):
        """ Checks if squareNum is a valid move and if so adds it to 
        movesList.
        Returns 0 if valid move, 1 otherwise. """
        assert(1 <= squareNum <= 9)
        # if the picked square has not previously been picked
        if (not squareNum in self.movesList): 
            self.movesList.append(squareNum)
            return 0 # signify valid move
        else:
            return 1 # signify illegal move, list not updated
        
    def Reset(self):
        """ Reset's the board for a new game.""" 
        self.movesList = []
        
    def MoveCount(self):
        """ Returns the number of squares which have been played on. """
        return len(self.movesList)
        
    def IsWin(self):
        """ Returns 0 if no winner, 1 if X wins, 2 if O wins, 3 if Cat's game"""
        # winning combos are: 123, 456, 789, 147, 258, 369, 159, 357
        winningSets = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9}, \
                       {1,5,9},{3,5,7})
        xSquares = set(self.movesList[::2])  #even indexed squares
        oSquares = set(self.movesList[1::2]) #odd indexed squares
        for winningSet in winningSets:
            if winningSet.issubset(xSquares): #does X have this winning combo?
                return 1
            elif winningSet.issubset(oSquares): #does O have this winning combo?
                return 2
        
        if (self.MoveCount() == 9):
            return 3
        else:
            return 0

    def GetRemainingSquares(self):
        """ Returns list of squares which have not been played on. """
        return list(set(range(1,10)) - set(self.movesList))
    
    
def test_board():
    """ Performs some simple testing of the Board class """
    b = Board()
    assert( not b.TryMove(1) )
    assert( b.TryMove(1) )
    assert( not b.IsWin() )
    assert( not b.TryMove(4) )
    assert( not b.IsWin() )
    assert( not b.TryMove(2) )
    assert( not b.IsWin() )
    assert( not b.TryMove(5) )
    assert( not b.IsWin() )
    assert( not b.TryMove(3) )
    assert( b.IsWin() == 1 )
    print("test_board() passed successfully")

        
    



from graphics import *
import random
def Game():
    gameplay='true'
    while gameplay== 'true':
        win = GraphWin('Tic-Tac Toe', 400, 350)

        #Splash Box Text
        splashText1=Text(Point(200,40),'CSC 161')
        splashText1.setSize(16)
        splashText1.draw(win)

        splashText2=Text(Point(80,100),'Name: Rajat Kuthiala')
        splashText2.setSize(12)
        splashText2.draw(win)

        splashText3=Text(Point(48,120),'Instructions:')
        splashText3.setSize(12)
        splashText3.draw(win)

        instruction1=Text(Point(115,140),'1) Click Ok to proceed to Game')
        instruction1.setSize(12)
        instruction1.draw(win)

        instruction2=Text(Point(145,160),'2) Click on the boxes to make your move')
        instruction2.setSize(12)
        instruction2.draw(win)

        instruction3=Text(Point(165,180),'3) Once you are Done click on rematch to play ' )
        instruction3.setSize(12)
        instruction3.draw(win)

        instruction4=Text(Point(143,200),'again or close the program to exit.')
        instruction4.setSize(12)
        instruction4.draw(win)
        

        

        #OK Box
        okBox = Rectangle(Point(160,250),Point(240,290))
        okBox.setFill(color_rgb(255,0,30))
        okBox.draw(win)

        #OK Box Text
        okText=Text(Point(200,270),'OK')
        okText.setSize(12)
        okText.draw(win)

        #game begins from here:

        
        okClick = win.getMouse()
        okclickx=okClick.getX()
        okclicky=okClick.getY()

        
        #If the user clicks on the OK box
        if okclickx in range(160,240) and okclicky in range(250,290):
            #removes all splash screen objects
            splashText1.undraw()
            splashText2.undraw()
            splashText3.undraw()
            okBox.undraw()
            okText.undraw()
            instruction1.undraw()
            instruction2.undraw()
            instruction3.undraw()
            instruction4.undraw()

            #Draws the game board
            game=Board()
            line1=Line(Point(160,50),Point(160,250))
            line2=Line(Point(220,50),Point(220,250))
            line3=Line(Point(100,120),Point(300,120))
            line4=Line(Point(100,200),Point(300,200))
            line1.draw(win)
            line2.draw(win)
            line3.draw(win)
            line4.draw(win)
            
            #Possible moves
            moves=[1,2,3,4,5,6,7,8,9]

            #Player and computer symbol
            player='X'
            computer='O'
           

                        
            while len(moves)>0 : #Only ask for moves if there are any moves left
                click=win.getMouse()
                clickx=click.getX()
                clicky=click.getY()
                #Draw the player's symbol when clicked on the box
                if clickx in range(100,160) and clicky in range(50,120):
                    x=1
                    Text(Point(130,85),player).draw(win)
                if clickx in range(160,220) and clicky in range(50,120):
                    
                    x=2
                    Text(Point(190,85),player).draw(win)
                if clickx in range(220,300) and clicky in range(50,120):
                    
                    x=3
                    Text(Point(260,85),player).draw(win)
                if clickx in range(100,160) and clicky in range(120,200):
                    
                    x=4
                    Text(Point(130,160),player).draw(win)
                if clickx in range(160,220) and clicky in range(120,200):
                    
                    x=5
                    Text(Point(190,160),player).draw(win)
                if clickx in range(220,300) and clicky in range(120,200):
                    
                    x=6
                    Text(Point(260,160),player).draw(win)
                if clickx in range(100,160) and clicky in range(200,250):
                    
                    x=7
                    Text(Point(130,225),player).draw(win)
                if clickx in range(160,220) and clicky in range(200,250):
                    
                    x=8
                    Text(Point(190,225),player).draw(win)
                if clickx in range(220,300) and clicky in range(200,250):
                    
                    x=9
                    Text(Point(260,225),player).draw(win)
                
                #Remove the move from moves list
                moves.remove(x)
                #There is a bug that user can click on the box where computer has made its move
                    #the 'if x in moves' command should be used first and after that symbils should be drawn
                    
                    
                #Computer choose from the available moves that are left after the player had made its move
                if len(moves)>0:
                    y=random.randrange(0,len(moves))
                    if moves[y]==1:
                        Text(Point(130,85),computer).draw(win)
                    if moves[y]==2:
                        Text(Point(190,85),computer).draw(win)
                    if moves[y]==3:
                        Text(Point(260,85),computer).draw(win)
                    if moves[y]==4:
                        Text(Point(130,160),computer).draw(win)
                    if moves[y]==5:
                        Text(Point(190,160),computer).draw(win)
                    if moves[y]==6:
                        Text(Point(260,160),computer).draw(win)
                    if moves[y]==7:
                        Text(Point(130,225),computer).draw(win)
                    if moves[y]==8:
                        Text(Point(190,225),computer).draw(win)
                    if moves[y]==9:
                        Text(Point(260,225),computer).draw(win)
                    moves.remove(moves[y])


                #If no moves are left then game over message displays. even if you win as I wasnt able to complete the winning part.
                    
            else:
                
                Text(Point(200,275),"Game Over!!").draw(win)
                Rectangle(Point(150,290), Point(250,320)).draw(win)
                Text(Point(200,305), 'Rematch').draw(win)

                rematch=win.getMouse()
                rematchx=rematch.getX()
                rematchy=rematch.getY()

                if rematchx in range(150,250) and rematchy in range(290,320):
                    gameplay='true'
                    win.close()
                    
                else:
                    break
                    
        else:
            break
    win.getMouse()
    win.close()        

Game()

