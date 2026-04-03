#password strength checker

password = input("Enter a password: ")

if len(password) <=6:
print("Password is too short.")
else:
for ch in password:
if ch.isdigit():
has_digit = True
if ch.isalpha():
has_alpha = True
if len(password) >=6 and has_digit and has_alpha:
print("Password is strong.")
else:    print("Password is weak.")
