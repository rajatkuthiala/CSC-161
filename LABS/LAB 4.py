#
# CSC161 Fall 2014
#
# Rajat Kuthiala
#
# Chapter 4, Exercise 11
#
# Lab Section MW 6:15-7:30PM
#


from graphics import *
 
def main():
    win = GraphWin('house',500,350)
    win.setCoords(0, 0, 20, 14)
    
#### Click#1     
    
    houseBL = win.getMouse()
    houseBL.draw(win)
     
#### Click#2
    
    houseTR = win.getMouse()
    houseTR.draw(win)
     
    
    HOUSEREC = Rectangle(houseBL,houseTR)
    HOUSEREC.draw(win)
     
#### Click#3
    
    
    doorClick = win.getMouse()
     
    
    doorWidth = houseTR.getX() - houseBL.getX()
    doorWidth= abs(doorWidth)/5
     
    
    doorXl = doorClick.getX()-doorWidth/2
    doorXr = doorClick.getX()+doorWidth/2
     
    
    doorYt = doorClick.getY()
    doorYb = houseBL.getY()
     
    
    DOORREC = Rectangle(Point(doorXl,doorYt),Point(doorXr,doorYb))
    DOORREC.draw(win)
     
#### Click#4
 
    windowClick = win.getMouse()
     
    
    windowWidth = doorWidth/2
     
    
    windowXl = windowClick.getX()-windowWidth/2
    windowXr = windowClick.getX()+windowWidth/2
 
    windowYt = windowClick.getY()+windowWidth/2
    windowYb = windowClick.getY()-windowWidth/2
     
    
    WINDOWREC = Rectangle(Point(windowXl,windowYt),Point(windowXr,windowYb))
    WINDOWREC.draw(win)
 
#### Click#5 
    
    roofClick = win.getMouse()
     
    
    houseLength = houseTR.getY() - houseBL.getY()
    houseLength = abs(houseLength)
     
    houseTL = Point(houseBL.getX(),houseBL.getY()+houseLength)
     
    
    roofleft = Line(roofClick,houseTL)
    roofleft.draw(win)
     
    roofRight = Line(roofClick,houseTR)
    roofRight.draw(win)
     

         
    win.getMouse()
    win.close()   
 
main()
