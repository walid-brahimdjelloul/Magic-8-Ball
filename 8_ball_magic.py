### import random
import random

## the name of the person who will be asking the Magic 8-Ball
name = 'someone'

## a “Yes” or “No” question you’d like to ask the Magic 8-Ball
question = "will i win lottery"

## We want to store the answer of the Magic 8-Ball in another variable
answer = ''

##we’ll create a variable to store the randomly generated value
random_number = random.randint(1,9)
print(random_number)

##Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program
if random_number == 1:
  answer += 'Yes - definitely'
elif random_number == 2:
  answer += 'It is decidedly so' 
elif random_number == 3:
  answer += "Without a doubt"
elif random_number == 4:
  answer += 'Reply hazy, try again'
elif random_number == 5:
  answer += "Ask again later"
elif random_number == 6:
  answer += 'Better not tell you now'
elif random_number == 7:
  answer += "My sources say no"
elif random_number == 8:
  answer += 'Outlook not so good'
elif random_number == 9:
  answer += "Very doubtful"
else:
  answer += 'Error'

##Write a statement to output the asker’s name and their question
if name == '':
  print('Question: '+question)
  print('Magic 8-Ball\'s answer: '+ answer)
else:
  print(name+' '+'asks '+question)
  print('Magic 8-Ball\'s answer: '+ answer)
