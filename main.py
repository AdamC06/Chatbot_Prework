print('Welcome to Elite 101 Chatbot!')
name = input('Please enter your name:')
age = int(input(f'Nice to meet you {name}! How old are you? '))
if age < 30:
  print(f'Welcome {name}! Oh, to be {age} again! How can I help you today?') #Change thiis
elif age > 30:
  print(f'Welcome {name}! {age} is such a wise age! How can I help you today?') #Change This

x = True

while x == True:
  print('Please choose from the following options:')
  print('1. Placeholder Option 1')
  print('2. Placeholder Option 2')
  print('3. Placeholder Option 3')
  print('4. Exit the conversation')
  choice = int(input('Enter the number of your choice: '))
  if choice == 4:
    print(f'Goodbye, {name}! Have a great day!')
    x = False