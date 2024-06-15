#importing modules
import more_itertools, base64
from brainfuckery import Brainfuckery

#importing the logger module
from logger import log_system, log_info, log_error
from helpfunctions import converterhelp


class lists:
    #the tables For some other conversion methods.
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

    pbinary_legacy = { 'a': '10110100',    'A': '00011001',    '1': '00110010',    '6': '00110111',
                'b': '00000001',    'B': '00011010',    '2': '00110011',    '7': '00111000',
                'c': '00000010',    'C': '00011011',    '3': '00110100',    '8': '00111001',
                'd': '00000011',    'D': '00011100',    '4': '00110101',    '9': '00111010',
                'e': '01011010',    'E': '00011101',    '5': '00110110',    '0': '00111011',
                'f': '00000100',    'F': '00011110',    ' ': '10000100',    '!': '101100100',
                'g': '00000101',    'G': '00011111',    ':': '10110010',    '.': '10110111',
                'h': '00000110',    'H': '00100000',    ',': '11101110',    '@': '11100100',
                'i': '00000111',    'I': '00100001',    '[': '10101010',    ']': '10101011',
                'j': '00001000',    'J': '00100010',    '-': '10101000',    '+': '11001010',
                'k': '00001001',    'K': '00100011',    ')': '11101010',    '(': '10001101',
                'l': '00001010',    'L': '00100100',    '=': '10001100',    '_': '10001000',
                'm': '00001011',    'M': '00100101',    '&': '10110000',    '^': '10110001',
                'n': '00001100',    'N': '00100110',    '%': '10110101',    '$': '11010101',
                'o': '00001101',    'O': '00100111',    '£': '11110101',    '"': '11111101',
                'p': '00001110',    'P': '00101000',    "'": '11111111',    '<': '11011111',
                'q': '00001111',    'Q': '00101001',    '>': '11011101',    '|': '01011101',
                'r': '00010000',    'R': '00101010',    '\\': '01001101',   '/': '01001001',
                's': '00010001',    'S': '00101011',    '#': '01001000',    '~': '01101000',
                't': '00010010',    'T': '00101100',    '`': '01101100',    '*': '01101110',
                'u': '00010011',    'U': '00101101',    '{': '11001111',    '}': '11001110',
                'v': '00010100',    'V': '00101110',
                'w': '00010101',    'W': '00101111',
                'x': '00010110',    'X': '100010011',
                'y': '00010111',    'Y': '00110000',
                'z': '00011000',    'Z': '00110001',
                '?': '10110110' }

#Variables
class variables:
    content=""
    out=""

#the main function of the converter
def convert(command, language, logg, name):
    variables.content=""
    variables.out=""
    try:
        if command=="phex":
            text_list=lists.phex
        elif command=="pbin":
            text_list=lists.pbinary
        elif command=="legacy bin":
            text_list=lists.pbinary_legacy

        while True:
            if language=="de":
                answer=input("Convert oder Deconvert? ").lower()
            elif language=="en":
                answer=input("Convert or Deconvert? ").lower()
            else:
                answer=input("Convert or Deconvert? ").lower()
            
            if answer=="help":
                converterhelp(command, language, answer)
            
            if answer=="convert" or answer=="deconvert":
                variables.content=input(">> ")
                break

        if answer=="convert":
            if command=="hex":
                variables.out="".join(more_itertools.intersperse(" ", variables.content.encode().hex(), n=2))
                print(variables.out)
                
            elif command=="bin":
                part1=bytes(variables.content, "ascii")
                variables.out=" ".join(["{0:b}".format(x) for x in part1])
                print(variables.out)
                
            elif command=="phex" or command=="pbin" or command=="legacy pbin":
                variables.out=" ".join(text_list[c] for c in variables.content)
                print(variables.out)
                
            elif command=="ascii":
                variables.out=" ".join(str(ord(c)) for c in variables.content)
                print(variables.out)
                
            elif command=="brainfuck":
                variables.out=Brainfuckery().convert(variables.content)
                print(variables.out)
                
            elif command=="base64":
                part1=variables.content.encode("ascii")
                part2=base64.b64encode(part1)
                variables.out=bytes.decode(part2)
                print(variables.out)
            
            else:
                if language=="en":
                    print(f"\nThat option is not there however you got that in.\n")
                elif language=="de":
                    print(f"\nDiese option ist nicht da, wie auch immer du es geschafft hast.\n")
                else:
                    print(f"\nThat option is not there however you got that in.\n")

        elif answer=="deconvert":
            if command=="hex":
                variables.out=bytes([int(x, 16) for x in variables.content.split()]).decode()
                print(variables.out)
            
            elif command=="bin":
                part1=variables.content.split()
                for content in part1:
                    content=int(content, 2)
                    content=chr(content)
                    variables.out+=content
                print(variables.out)
            
            elif command=="phex" or command=="pbin" or command=="legacy bin":
                variables.out="".join(list(text_list.keys())[list(text_list.values()).index(c)] for c in variables.content.split())
                print(variables.out)
            
            elif command=="ascii":
                variables.out="".join(map(lambda x: chr(int(x)), variables.content.split()))
                print(variables.out)
            
            elif command=="brainfuck":
                variables.out=Brainfuckery().interpret(variables.content)
                print(variables.out)
            
            elif command=="base64":
                part1=bytes(variables.content, encoding="utf-8")
                part2=base64.b64decode(part1)
                variables.out=str(part2, encoding="utf-8")
                print(variables.out)
            
            else:
                if language=="en":
                    print(f"\nThat option is not there however you got that in.\n")
                elif language=="de":
                    print(f"\nDiese option ist nicht da, wie auch immer du es geschafft hast.\n")
                else:
                    print(f"\nThat option is not there however you got that in.\n")

        try:
            del part1
        except:
            pass

        try:
            del part2
        except:
            pass

        return variables.out
    except KeyboardInterrupt:
        print()
        return
        
        