import argparse

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
    print(f'Text: {args.text}')
    print(f'Morse Code: {result}')

if __name__ == '__main__':
    main()
