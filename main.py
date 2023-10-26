#Adam H file

# Nate achinger new challenger @ 8:34pm

# Are we back???

# Were so back - Nate

def encoder(word):
    new_pass = ''
    for char in word:
        digit = int(char) + 3
        if digit > 9:
            digit = digit % 10
        new_pass += str(digit)
    return new_pass


def main():
    global new_password, password
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            new_password = encoder(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            print(f'The encoded password is {new_password}, and the original password is {password}.')



if __name__ == "__main__":
    main()
