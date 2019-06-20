def alphabet_position(alpha):
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    if alpha != " ":
        char_num = int(alphabet.get(alpha))
        return(char_num)
    else:
        return(" ")

def rotate_character(char, rot):
    
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    for c in char:
        new_char_num = (int(alphabet_position(c)) + int(rot))
        if new_char_num == (" "):
            return(" ")
        elif new_char_num > 25:
            nn_char_num = new_char_num % 26
            return[char for char, num in alphabet.items() if num == nn_char_num]
        else:
            return[char for char, num in alphabet.items() if num == new_char_num]
    
def rotate_string(text, rot):
    new_sentance = ""
    for character in text:
        if character.isalpha():
            if character == character.lower():
                char = rotate_character(character, rot)
                new_sentance += "".join(char)
            else:
                char = character.lower()
                new_char = (rotate_character(char, rot))
                upper_char = "".join(new_char)
                new_sentance += upper_char.upper()
        else:
            new_sentance += character
        
    nn_sentance = ''.join(new_sentance)
    return(str(nn_sentance))
       
            
def main():
    

    user_input = str(input("What would you like encrypted?"))
    user_rot = int(input("Rotate?"))
    print(encrypt(user_input, user_rot))
    
if __name__ == "__main__":
    main()

