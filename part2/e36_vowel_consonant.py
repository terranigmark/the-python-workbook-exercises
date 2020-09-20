"""
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
"""

def main(consonants, user_letter):
    if user_letter.lower() in consonants:
        return print(f"The letter '{user_letter}' is a consonant")
    elif user_letter.lower() == 'y':
        return print(f"Sometimes the leter 'y' is a vowel, and sometimes is a consonant")
    else:
        print(f"The letter {user_letter} is a vowel")

if __name__ == "__main__":
    consonants = ['a', 'e', 'i', 'o', 'u']

    print("This program reads a letter input by the user and determines if it is a vowel or consonant")
    user_letter = str(input("Enter a letter to know it's type: "))

    main(consonants, user_letter)