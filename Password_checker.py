# PASSWORD CHECKER

# Take inputs for the password
password = input('Enter your password: ')
length = len(password)
ast = '*' * length
  
def checker(password, ast):
    alpha_checker = password.isalpha()
    numeric_checker = password.isnumeric()
    lowercase_checker = password.islower()
    uppercase_checker = password.isupper()
  

    if lowercase_checker:
       print(f'Your password {ast} contains only lower case characters! Try another password.')
      
    elif uppercase_checker:
       print(f'Your password {ast} contains only upper case characters! Try another password.')
      
    elif alpha_checker:
       print(f'Your password {ast} contains only Alphabets! Try another password.')
  
    elif numeric_checker:
       print(f'Your password {ast} contains only Numbers! Try another password.')
      
    else:
       print(f'Your password {ast} is strong and it meets all the requirements')



def length_checker(length):
  
    if length < 12:
        print(f'The length of your password {ast} does not exceed 12 characters. Try another password.')
    
    else:  
        checker(password, ast)


length_checker(length)







