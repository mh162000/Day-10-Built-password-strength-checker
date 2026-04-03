# password strength checker

password = input("Enter a password: ")

has_digit = False
has_alpha = False

if len(password) <= 6:
    print("Password is too short.")
else:
    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isalpha():
            has_alpha = True

    if has_digit and has_alpha:
        print("Password is strong.")
    else:
        print("Password is weak.")