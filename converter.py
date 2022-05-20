import more_itertools, os
import random as ran

try:
    from problems import wrongtxt, notext
except:
    print(f"\n:)\n")

answer="thex"
language="en"

phex = { 'a': '01',    'A': '02', 'b': '03',    'B': '04', 'c': '05',    'C': '06', 'd': '07',    'D': '08',
            'e': '09',    'E': '0A', 'f': '0B',    'F': '0C', 'g': '0D',    'G': '0E', 'h': '0F',    'H': '11',
            'i': '12',    'I': '13', 'j': '14',    'J': '15', 'k': '16',    'K': '17', 'l': '18',    'L': '19',
            'm': '1A',    'M': '1B', 'n': '1C',    'N': '1D', 'o': '1E',    'O': '1F', 'p': '20',    'P': '21',
            'q': '22',    'Q': '23', 'r': '24',    'R': '25', 's': '26',    'S': '27', 't': '28',    'T': '29',
            'u': '2A',    'U': '2B', 'v': '2C',    'V': '2D', 'w': '2E',    'W': '2F', 'x': '30',    'X': '31',
            'y': '32',    'Y': '33', 'z': '34',    'Z': '35', '1': '36',    '6': '37', '2': '38',    '7': '39',
            '3': '3A',    '8': '3B', '4': '3C',    '9': '3D', '5': '3E',    '0': '3F', ' ': '40',    '!': '41',
            ':': '42',    '.': '43', ',': '44',    '@': '45', '[': '46',    ']': '47', '-': '48',    '+': '49',
            ')': '4A',    '(': '4B', '=': '4C',    '_': '4D', '&': '4E',    '^': '4F', '%': '50',    '$': '51',
            '£': '52',    '"': '53', "'": '54',    '<': '55', '>': '56',    '|': '57', '\\': '58',   '/': '59',
            '#': '5A',    '~': '5B', '`': '5C',    '*': '5D', '{': '5E',    '}': '5F', '?': '60',    'ö': '61',
            'Ö': '62',    'ü': '63', 'Ü': '64',    'ä': '65', 'Ä': '66',    '°': '67', '§': '68',    'ß': '70'}

pbinary = {'a': '00000001',    'A': '00000010', 'b': '00000011',    'B': '00000100', 'c': '00000101',    'C': '00000110', 'd': '00000111',    'D': '00001000',
           'e': '00001001',    'E': '00001010', 'f': '00001011',    'F': '00001100', 'g': '00001101',    'G': '00001110', 'h': '00001111',    'H': '00010000',
           'i': '00010001',    'I': '00010010', 'j': '00010011',    'J': '00010100', 'k': '00010100',    'K': '00010101', 'l': '00010110',    'L': '00010111',
           'm': '00010111',    'M': '00011000', 'n': '00011001',    'N': '00011010', 'o': '00011011',    'O': '00011100', 'p': '00011101',    'P': '00011110',
           'q': '00011111',    'Q': '00100000', 'r': '00100001',    'R': '00100010', 's': '00100011',    'S': '00100100', 't': '00100101',    'T': '00100110',
           'u': '00100111',    'U': '00101000', 'v': '00101001',    'V': '00101010', 'w': '00101011',    'W': '00101100', 'x': '00101101',    'X': '00101110',
           'y': '00101111',    'Y': '00110000', 'z': '00110001',    'Z': '00110010', '1': '00110011',    '6': '00110100', '2': '00110101',    '7': '00110110',
           '3': '00110111',    '8': '00111000', '4': '00111001',    '9': '00111010', '5': '00111011',    '0': '00111100', ' ': '00111101',    '!': '00111110',
           ',': '00111111',    '@': '01000000', '[': '01000001',    ']': '01000010', '-': '01000011',    '+': '01000100', ')': '01000101',    '(': '01000110',
           '=': '01000111',    '_': '01001000', '&': '01001001',    '^': '01001010', '%': '01001011',    '$': '01001100', '£': '01001101',    '"': '01001110',
           "'": '01001111',    '<': '01010000', '>': '01010001',    '|': '01010010', '\\':'01010011',    '/': '01010100', '#': '01010101',    '~': '01010110',
           '`': '01010111',    '*': '01011000', '{': '01011001',    '}': '01011010', '?': '01011011',    'ö': '01011100', 'Ö': '01011101',    'ü': '01011110',
           'Ü': '01011111',    'ä': '01100000', 'Ä': '01100001',    '°': '01100010', '§': '01100011',    'ß': '01100101'}

def converter(answer, languageuage):#the Main usage that is expected of that code, because why wouldn't it be the Second longest function?
    
    if answer.lower()=="phex":
        text=phex

    if answer.lower()=="pbin":
        text=pbinary
        
    if answer.lower()=="thex":
        text="truehex"

    if answer.lower()=="tbin":
        text="truebinary"
    content=answer

    while True:
        try:
            try:
                if language.lower() == "en":
                    answer = input("Encode or Decode? ")

                if language.lower() == "de":
                    answer = input("Enoder oder Decode? ")

                if answer.lower() == 'decode':
                    if text=="truehex":
                        decode_s=input(">> ")

                        print(bytes([int(x, 16) for x in decode_s.split()]).decode())
                        data=bytes.fromhex(decode_s)

                        converted = decode_s, data

                    if text=="truebinary":
                        a_binary_string = input(">> ")

                        binary_values = a_binary_string.split()
                        ascii_string = ""

                        for binary_value in binary_values:
                            an_integer = int(binary_value, 2)

                            ascii_character = chr(an_integer)

                            ascii_string += ascii_character

                        print(ascii_string)

                    if text=="phex" or text=="pbinary":
                        decode_s = input(">> ")
                        print(f"\n", ''.join(list(text.keys())[list(text.values()).index(c)] for c in decode_s.split()), "\n")

                if answer.lower() == 'encode':
                    if text=="truehex":
                        encode_s=input(">> ")

                        print(''.join(more_itertools.intersperse(" ", encode_s.encode().hex(), n=2)))

                        data=encode_s.encode("utf-8").hex()

                        converted=encode_s, data

                    if text=="truebinary":
                        a = input(">> ")
                        a_bytes = bytes(a, "ascii")
                        print(" ".join(["{0:b}".format(x) for x in a_bytes]))

                    if text=="phex" or text=="pbinary":
                        encode_s = input(">> ")

                        print(f"\n{content}:", ' '.join(text[c] for c in encode_s), "\n")

                        data=c.join(text[c] for c in encode_s)

                        converted=encode_s, data

                elif answer.lower() == 'help':#help site of converter. (converter function help)
                    helpsite(content, language)

                elif answer.lower() == "exit":#to return to the main console.
                    #os.system('cls')
                    return

                elif answer.lower() == "":#The thing that shows text because you didn't input anything..
                    notext(language)

                else:
                    wrongtxt(answer, language)

            except KeyboardInterrupt:
                close()

        except ValueError:
            print("Wut?")

def helpsite(content, language):#the helpsite for the converter.
    if content == "pbin":
        text1="Pseudo Binary"

    if content == "phex":
        text1="Pseudo HEX"

    if content == "thex":
        text1="HEX"

    if content == "tbin":
        text1="Binary"

    if language.lower() == "en":
        print(f"Here is the Help site of the converter:\n")
        print(f"encode Converts text zu {text1}.")
        print(f"decode Converts {text1} zu text.")
        print(f"Exit brings you to the Main menu.\n")
        return

    if language.lower() == "de":
        print(f"Hier sind ein paar commands:\n")
        print(f"encode Convertiert text zu {text1}.")
        print(f"decode Convertiert {text1} zu text.")
        print(f"Exit bringt dich zum hauptmenü.\n")

    else:
        print(f"\nno language supplied. :(\n")
        return
