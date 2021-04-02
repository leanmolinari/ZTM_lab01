username = input('what is your username?')
password = input('wwhat is your password')

password_length = len(password)
hidden_password = '*' * password_length

print(f'your password is {hidden_password} and have {password_length} characters long')