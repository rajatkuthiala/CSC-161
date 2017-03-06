#
# CSC161 Fall 2014
#
# Rajat Kuthiala
#
# Chapter 7, Exercise 12
#
# Lab Section MW 6:15-7:30PM
#



def date():
    date=input("Please enter the date(MM/DD/YYY): ")

    try:
        #(Searched how to do it on Google from here
        month,day,year = date.split('/')   #till here) 
         
        month = int(month)
        day = int(day)
        year = int(year)
        

        list1 = [1,3,5,7,8,10,12]
        list2 = [2]
        list3 = [4,6,9,11]

        for i in list1:
            if i==month:
                if day>=1 and day<=31:
                    print(date, "is valid.")
                else:
                    print(date, "is unvalid.")

        for i in list2:
            if i==month:
                if day>=1 and day<=28:
                    print(date, "is valid.")
                else:
                    print(date, "is unvalid.")


        for i in list3:
            if i==month:
                if day>=1 and day<=30:
                    print(date, "is valid.")
                else:
                    print(date, "is unvalid.")

        if month < 1:
            print("Wrong Month")
        if month > 12:
            print("Wrong Month")

    except ValueError:
        print("Invalid Format")

        
date()



                

        
                    
    
