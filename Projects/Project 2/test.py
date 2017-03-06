import time # for sleep
import random
random.seed(1) # TODO: look up what this line means on Google

"""
First thing, we are settung up CArd class which will define the value of our card. This class assign value to our card.

"""
class Card():
    
    rank=["","","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suit=["Clubs","Diamonds","Hearts","Spades"]
    
    def __init__(self, rank, suit): #initializes the class.
        # checks the rank is in range
        assert(2 <= rank <= 14), "Improper card rank " + str(rank)
        
        #checks suit is in range
        assert(0 <= suit <= 3), "Improper card suit" + str(suit)
        
        self.rank = rank # 2-14
        self.suit = suit # 0-3
        
    def __str__(self): #return the name of card
        
        cardNameString = Card.rank[self.rank] +' Of '+ Card.suit[self.suit]
        return cardNameString
    
    def value(self):
        # return the value of card in term of black hawk values
        
        cardValue = 0
        rank=[0,0,2,3,4,5,6,7,8,9,7,7,7,7,7]
        cardValue+=rank[self.rank]
        return cardValue

def testCard():
    """ Runs several tests to ensure that the Card class is working. """
    # we use the assert function to check if the value is equal to what is expected without sending a true or false. If the program has some error
    #then the asser function gives an error.
    
    c1 = Card(2,3) # 2, spades
    c1name = str(c1)
    assert(c1name == "2 Of Spades")

    c2 = Card(10,0) # 10, clubs
    c2name = str(c2)
    assert(c2name == "10 Of Clubs")

    c3 = Card(13,2) # K, hearts
    c3name = str(c3)
    assert(c3name == "King Of Hearts")

    c4 = Card(10,2) # 10, hearts
    c4name = str(c4)
    assert(c4name == "10 Of Hearts")

    c5 = Card(14,3) # Ace, Spades
    c5name = str(c5)
    assert(c5name == "Ace Of Spades")

    c6 = Card(12,1) # K, hearts
    c6name = str(c6)
    assert(c6name == "Queen Of Diamonds")
    

 
    
class CardStack():
    """ Class to simulate a stack of cards. For example, a deck, a 
    player's hand, or dealer's hand.
    
    Attributes:
        cardList - a list of Cards representing what is in a player's hand.    
    """
    cardList=[]
    
    def __init__(self, cardList):
        """ initializes cardList. Constructor must have a cardList. An empty
        cardList can be specified by CardStack([]). """
        self.cardList = cardList
        
    def count(self):
        """ This function will return an integer representing the CardStack's 
        count in blackjack. 
        """
        l=[]
        for i in self.cardList:
            a=Card.value(i)
            l.append(a)
        
        return sum(l)
    
    def addCard(self, newCard):
        """ adds newCard to the list of cards in PlayersHand """
        self.cardList.append(newCard)
        
        
    def removeCard(self, leavingCard):
        """ Removes the card specified from the CardStack. """
        self.cardList.remove(leavingCard)

    def popCard(self):
        """ Removes and returns the bottom most card from the CardStack. """
        return self.cardList.pop()

    def Shuffle(self):
        """ Shuffles the order of the cards in the CardStack """
        random.shuffle(self.cardList)
        
    def __str__(self):
        """ the returned string for the CardStack is merely a 
        string formed by concatenating the __str__ output from each Card in the 
        cardList and appending a newline '\n' inbetween each Card 
        
        example: 
            ph = CardStack([Card(2,3), Card(10,0), Card(14, 1)])
            print(ph)
        
        should produce:
             2 of SPADES
            10 of CLUBS
             A of DIAMONDS     
        """
        l = ["  " + str(c) + "\n" for c in self.cardList]
        return ''.join(l)


def testCardStack_addCard():
    """ Runs several tests to ensure the CardStack.addCard(...) method is
    working correcly. """

    pass
    # OPTIONAL TODO: INSERT TEST CODE HERE

testCardStack_addCard()
  
def testCardStack_count():
    """ Runs several tests to ensure that the CardStack.count() method 
    is working. """
    h1 = CardStack([Card(2,3), Card(10,0), Card(10,1)])
    assert(h1.count() == 16)
    h2 = CardStack([Card(7,3), Card(10,0), Card(14,1)])
    assert(h2.count() == 21)
    h3 = CardStack([Card(14,0), Card(14,2), Card(9,1)])
    assert(h3.count() == 23)
    



class Game:
    """ TODO: Put comment here """
    def __init__(self):
        self.cardList=[]

    def addCard(self):
        self.cardList.append(Card(random.randrange(2,15),random.randrange(0,4)))
        
    def __str__(self):
        l = ["  " + str(c) + "\n" for c in self.cardList]
        return ''.join(l)
    
    def count(self):
        return CardStack.count(self)
        
            
