print('Welcome to Elite 101 Chatbot! Great to see you!')
name = input('Please enter your name:')
age = int(input(f'Nice to meet you {name}! How old are you? '))

if age < 30:
  print(f'Hello and welcome, {name}, your age is {age}, congrats! Anyways, How may I help you today?')
elif age > 30:
  print(f'Hello and welcome, {name}, your age is {age}, congrats! Anyways, How may I help you today?') 

x = True

while x == True:
  print('Please choose from the following options:')
  print('1. Whoah, you seem fun. Lets be friends, my name is Adam!')
  print('2. Pleasure meeting you!')
  print('3. Nice to meet you!')
  print('4. Exit the conversation')
  choice = int(input('Enter the number of your choice: '))
  if choice == 4:
    print(f'Goodbye, {name}! Have a great day!')
    x = False