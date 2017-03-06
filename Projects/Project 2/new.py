import random
def game():
    a=[]
    b=[]
    for i in range(2):
        a.append(random.randrange(2,15))
    b.append(random.randrange(2,15))

    print(a)
    print(b)
    
    while sum(a)<=21:
        x=input('Do you want another card')
        if x=='yes':
            print('hoho')
            a.append(random.randrange(2,15))
        else:
            while sum(b)<=21:
                b.append(random.randrange(2,15))
            else:
                return "Dealer Lost"
    else:
        print('Your Total ', sum(a))
        print("Dealer's Total", sum(b))
        print("You Lost")
game()
        
        
                
             
                 
             
             
        
