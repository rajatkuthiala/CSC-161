"""
-------------------------------
NAME: Rajat Kuthiala
PROJECT: Project1, milestone1
-------------------------------
This program is a slot machine game. In this user starts with a balance of $100.
He enter the amount in bet section for the bet he wants to do. Then he clicks on the spin
button. The program is inatilized when the user clicks the spin button. There are three windows
which initially show same shape, but as soon as user clicks spin button, the objects change to one of
the random objects(square, triangle, diamond). If all the shapes are same after spin, user balance increase
by the amount he betted. If two of the shapes are same, then his balance increase by half the amount he betted,
and if none of the shapes are same, then his balance reduces by the amount he betted.
If the balance of user reaches zero(0), then a message saying "YOU LOOSE" pops up.
Follow the following steps to use the program:

   1. Enter the amount you want to bet, in betting bos.
   2. Click the spin button
   3. Observe
"""


def balance(bet):
    """ Stores the initial balance which is $100 and after every spin it makes changes
        to its value depending upon the outcome of spin."""
    pass
    
def shapes(n):
    """ It contains the list of shapes which our program will use to get the outcome of the spin.
        """
    pass

def main():
    """ It contains the basic framework of the program. All the graphical objects
        and it calls the other functions.
    """
    pass
    
def spinbutton():
    """ It is a button which when clicked on inatialize a function. I have used the range operation
        for this function. If my mouse click is in in the range of the button, then the program will inatialize,
        else it wont do anything.
    """
    pass

from graphics import *
def button():
    
    win=GraphWin()

    spin= Circle(Point(50,50), 30)
    spin.setFill(color_rgb(255,0,0))
    spin.draw(win)
    spintext= Text(Point(50,50), 'SPIN')
    spintext.draw(win)

    click=win.getMouse()
    clickx=click.getX()
    clicky=click.getY()
    if clickx and clicky in range(20,80): 
        message = 'Clicked On Button'
        Text(Point(win.getWidth()/2, 100), message).draw(win)
    else:
        message = 'Clicked Outside Of Button'
        Text(Point(win.getWidth()/2, 100), message).draw(win)

    win.getMouse()
    win.close()

        
