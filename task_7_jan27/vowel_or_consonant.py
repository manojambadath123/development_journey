
char = input("enter a character=")

vowel = "aeiou"

match char:
    
    case "a":
        if char in vowel:
            print("it is a vowel")
    case "e":
        if char in vowel:
            print("it is a vowel")
    case "i":
        if char in vowel:
            print("it is a vowel")
    case "o":
        if char in vowel:
            print("it is a vowel")
    case "u":
        if char in vowel:
            print("it is a vowel")
    case _:
        print("it is a consonant")