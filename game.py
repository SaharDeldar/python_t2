from pickle import TRUE
import random
a=0
computer_number=random.randint(10,20)

while TRUE:
    user_number=int(input())
    a=a+1
    if user_number==computer_number:
       
        print("you win❤")
        break
    elif  user_number<computer_number:  
        print("go up⬆")
    elif  user_number>computer_number:  
        print("go down⬇")    
        print("tedad entekhab shode adad  = ",a)
print("end of game coming soon")        

