import argparse
import os
import sys

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

os.system('cls' if sys.platform.startswith('win') else 'clear')

morse_code_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char
    return morse_code.strip()

def main():
    parser = argparse.ArgumentParser(description='Convert text to Morse code.')
    parser.add_argument('text', metavar='text', type=str, help='python Text2Morse.py <Text>')
    args = parser.parse_args()

    result = text_to_morse(args.text)
    print(
        f"""{Colors.CYAN}
 _______ _______ _     _ _______ _______  _____   ______ _______ _______
    |    |______  \___/     |    |  |  | |     | |_____/ |______ |______
    |    |______ _/   \_    |    |  |  | |_____| |    \_ ______| |______
                                                                        
    {Colors.RESET}"""
    )
    print(f'{Colors.BLUE}Text: {args.text}{Colors.RESET}')
    print(f'{Colors.GREEN}Morse Code: {result}{Colors.RESET}')

if __name__ == '__main__':
    main()
