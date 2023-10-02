# Break And Continue Statement In python:----------------------

i = 0
while(i<45):
    i+=1
    print(i,end=" ") # use the end the code output came in one line. 

# Break Statement In Python :----------

i = 0
while(True):
    print(i+1,end=" ")
    if (i==44):
      break  #stop the loop using of break 
    i+=1

#Continue and break Statement :-----------

i=0
while(True):
    if i+1<5:
        i = i+1
        continue
    print(i+1,end=" ")
    if(i==44):
        break
    i = i+1

# Quiz Question with Solution:---------------------

while(True):
    num = int(input("Enter the number"))
    if num>=100:
        print("Congrats🎉🎉 You Have Entered the number")
        break
    else:
        print("Try again")
        continue




    
    


    







