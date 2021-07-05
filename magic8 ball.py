import random
name="Ibrahim "
question="Will I be rich?"
answer=" "
random_number=random.randint(1,11)
#print(random_number)
if random_number==1:
  answer="Yes -definetely"
elif random_number==2:
   answer="It is decidedly so"
elif random_number==3:
   answer="Without a doubt."
elif random_number==4:
   answer="Reply hazy, try again."
elif random_number==5:
   answer="Ask again later."
elif random_number==6:
   answer="Better not tell you now."
elif random_number==7:
   answer="My sources say no."
elif random_number==8:
   answer="Outlook not so good."
elif random_number==9:
   answer="Very doubtful."
elif random_number==10:
   answer="consult a different magic ball" 
elif random_number==11:
   answer="I do not know anything about it" 
else:
  answer="Error" 
print( name,"asks: ",question)
print("Magic 8-Ball's answer:",answer)



