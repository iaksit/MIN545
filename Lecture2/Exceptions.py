def get_user_age():
    return int(input('Enter your age in years: '))


age = -1 # an initially invalid choice 
while age <= 0:
  try:
    age = get_user_age()
    if age <= 0:
      print('Your age must be positive')
  except (ValueError, EOFError):
    print('Invalid response')
