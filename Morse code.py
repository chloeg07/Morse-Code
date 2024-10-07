#Morse code detecter
# Dictionary for morse code for alphabets, digits, and some special characters
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', '\'': '.----.', '!': '-.-.--', 
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Function to translate a string into Morse code
def string_to_morse(input_string):
    morse_code = []

    # Loop through each character in the input string
    for char in input_string.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # To handle any unsupported characters

    # Join the morse code list with spaces
    return ' '.join(morse_code)

# Main function to take user input and output Morse code
def main():
    # Take input from user
    input_string = input("Enter a string to convert to Morse code: ")
    
    # Get Morse code translation
    morse_translation = string_to_morse(input_string)
    
    # Output the Morse code
    print(f"Morse Code: {morse_translation}")

if __name__ == "__main__":
    main()
    