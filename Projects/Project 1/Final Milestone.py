"""
-------------------------------
NAME: Rajat Kuthiala
PROJECT: Project1, Final Milestone
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


from graphics import *
import random

def main():
    win = GraphWin('Slot Machine', 400, 300)
    balance=100
    #Shapes for box 1
    shape1= Entry(Point(145,165),7)
    shape1.setText('Triangle')
    shape1.draw(win)
    #Shape For Box 2
    shape2= Entry(Point(225,165),7)
    shape2.setText('Triangle')
    shape2.draw(win)

    #Shape for Box 3
    shape3= Entry(Point(310,165),7)
    shape3.setText('Triangle')
    shape3.draw(win)

    #Bet Entry
    Text(Point(25,35), 'Bet:').draw(win)
    betbox= Entry(Point(80,35),5)
    betbox.draw(win)

    #spinbutton
    spin= Circle(Point(41,170), 30)
    spin.setFill(color_rgb(255,0,0))
    spin.draw(win)
    spintext= Text(Point(41,170), 'SPIN')
    spintext.draw(win)

    #window1
    window1= Rectangle(Point(110,107), Point(190,220))
    window1.draw(win)

    #window2
    window2= Rectangle(Point(190,107), Point(270,220))
    window2.draw(win)

    #window3
    window3= Rectangle(Point(270,107), Point(350,220))
    window3.draw(win)

    #Display Balance
    balancebox = Text(Point(60,10),'Balance: $'+ str(balance))
    balancebox.setSize(12)
    balancebox.draw(win)

    #Balance Condition 
    while balance>0:
        
    #Detecting user to click on "SPIN" Button
        click=win.getMouse()
        clickx=click.getX()
        clicky=click.getY()
    
        if clickx in range(11,71) and clicky in range(140,200):

            #Program Initialization
            bet=int(betbox.getText())
            shapes=['Square', 'Triangle', 'Diamond']
            shape1.setText(str(random.sample(shapes, 1)))
            shape2.setText(str(random.sample(shapes, 1)))
            shape3.setText(str(random.sample(shapes, 1)))

            a=str(shape1.getText())
            b=str(shape2.getText())
            c=str(shape3.getText())

            #Win Condition
            if a==b==c:
                balannce=balance+bet
            if a==b!=c or a!=b==c or a==c!=b:
                balance=balance+(bet/2)
            if a!=b!=c:
                balance=balance-bet
            
        balancebox.setText('Balance: $'+ str(balance))

    #If balance is less than or equal to zero
    while balance<=0:
        lostmessage = 'You Loose!!'
        Text(Point(win.getWidth()/2, 250), lostmessage).draw(win)
        
        
    win.getMouse()
    win.close()
    
main()
