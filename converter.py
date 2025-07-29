import subprocess, sys, base64, platform

class modules:
    more_itertools_module=True
    brainfuckery_module=True
    helpfunctions_module=True

class variables:
    exit=False
    out=""

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
    
    convert = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "0": "j", " ": "4", ",": "0", ".": "1", "?": "2", "!": "3", "a": "!", "b": "@", "c": "#", "d": "$", "e": "%", "f": "^", "g": "&", "h": "*", "i": "(", "j": ")", "k": "-", "l": "_", "m": "=", "n": "+", "o": "[", "p": "]", "q": "{", "r": "}", "s": ":", "t": ";", "u": "<", "v": ">", "w": ",", "x": ".", "y": "/", "z": "?", "'": "©"}

    deconvert = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0", " ": " ", "4": " ", "0": ",", "1": ".", "2": "?", "3": "!", "!": "a", "@": "b", "#": "c", "$": "d", "%": "e", "^": "f", "&": "g", "*": "h", "(": "i", ")": "j", "-": "k", "_": "l", "=": "m", "+": "n", "[": "o", "]": "p", "{": "q", "}": "r", ":": "s", ";": "t", "<": "u", ">": "v", ",": "w", ".": "x", "/": "y", "?": "z", "©": "'"}

try:
    import more_itertools
except ImportError:
    try:
        if input("The 'more_itertools' Module is missign, do you wanna install it? (Yes/No) ").lower() == "yes":
            if platform.system()=="Windows":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "more_itertools"])
            elif platform.system()=="Linux":
                subprocess.check_call(["sudo", "apt", "install", "python3-pip", "more_itertools"])
            import more_itertools
        
        else:
            print("The more_itertools module isn't installed, that simply means that there is no Hex conversion.")
            modules.more_itertools_module=False

    except subprocess.CalledProcessError:
        print("There is no internet connection, or some other problem, Please retstart the program later. (Manual retry attempts may be implemented in the future.)")
        modules.more_itertools_module=False

try:
    import brainfuckery
except ImportError:
    try:
        if input("The 'brainfuckery' Module is missign, do you wanna install it? (Yes/No) ").lower() == "yes":
            if platform.system()=="Windows":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "brainfuckery"])
            elif platform.system()=="Linux":
                subprocess.check_call(["sudo", "apt", "install", "python3-pip", "brainfuckery"])
            import brainfuckery
        
        else:
            print("The brainfuckery module isn't installed, that simply means that there is no brainfuck conversion.")
            modules.brainfuckery_module=False

    except subprocess.CalledProcessError:
        print("There is no internet connection, or some other problem, Please retstart the program later. (Manual retry attempts may be implemented in the future.)")
        modules.brainfuckery_module=False

try:
    from helpfunctions import converterhelp
except ImportError:
    print("The help page module can't be loaded, that is currently then not available. I might move the Help site to the relevant modules.")
    modules.helpfunctions_module=False

def parse_input(config, **kwargs):
    convert_list=""
    try:
        if kwargs["mode"]=="phex" or kwargs["mode"]=="pseudo hex":
            convert_list=lists.phex
        elif kwargs["mode"]=="pbin" or kwargs["mode"]=="pseudo binary":
            convert_list=lists.pbinary
        elif kwargs["mode"]=="lpbin" or kwargs["mode"]=="legacy pseudo binary":
            convert_list=lists.pbinary_legacy

        if config.gui==False:
            while True:
                if config.language=="de":
                    convert_mode=input("Convert oder Deconvert? ").lower()
                else:
                    convert_mode=input("Convert or Deconvert? ").lower()

                if convert_mode=="help":
                    if modules.helpfunctions_module==True:
                        converterhelp(config, mode=kwargs["mode"])

                elif convert_mode=="convert" or convert_mode=="deconvert":
                    content=input(">> ")
                    break

                elif convert_mode=="exit" or convert_mode=="go back":
                    variables.exit=True
                    break

        elif config.gui==True:
            convert_mode=kwargs["guimode"]
            content=kwargs["convdata"]

        if variables.exit==False:
            process(config, charset=convert_list, mode=convert_mode, content=content, convert=kwargs["mode"])

        print()
        
        return variables.out
                    
    except KeyboardInterrupt:
        print()
        return

def process(config, **kwargs):
    #print(kwargs["mode"], kwargs["convert"], kwargs["content"]) #Debugging während ich die GUI version erneuert habe
    if kwargs["mode"]=="convert":
        if kwargs["convert"]=="hex":
            variables.out="".join(more_itertools.intersperse(" ", kwargs["content"].encode().hex(), n=2))
            print(variables.out)
                
        elif kwargs["convert"]=="bin" or kwargs["convert"]=="binary":
            variables.out=""
            part1=bytes(kwargs["content"], "ascii")
            variables.out=" ".join(["{0:b}".format(x) for x in part1])
            print(variables.out)
                
        elif kwargs["convert"]=="phex" or kwargs["convert"]=="pseudo hex" or kwargs["convert"]=="pbin" or kwargs["convert"]=="pseudo binary" or kwargs["convert"]=="lpbin" or kwargs["convert"]=="legacy pseudo binary":
            variables.out=" ".join(kwargs["charset"][c] for c in kwargs["content"])
            print(variables.out)
                
        elif kwargs["convert"]=="ascii":
            variables.out=" ".join(str(ord(c)) for c in kwargs["content"])
            print(variables.out)
                
        elif kwargs["convert"]=="brainfuck":
            variables.out=brainfuckery.Brainfuckery().convert(kwargs["content"])
            print(variables.out)
                
        elif kwargs["convert"]=="base64":
            part1=kwargs["content"].encode("ascii")
            part2=base64.b64encode(part1)
            variables.out=bytes.decode(part2)
            print(variables.out)
            
        elif kwargs["convert"]=="symbenc":
            data=kwargs["content"].lower()
            unsupported_symbols=""
            for i in range(len(data)):
                if data[i] not in lists.convert:
                    unsupported_symbols += f"{data[i]}, "
            unsupported_symbols = unsupported_symbols[:-2]
            if unsupported_symbols=="":
                variables.out=""
                for e in range(len(data)):
                    variables.out += str(lists.convert[data[e]])
                print(variables.out)
                unsupported_symbols=""
            else:
                print(f"That symbol is not supported: {unsupported_symbols}")
            unsupported_symbols=""
            
        else:
            if config.language=="de":
                print(f"\nDiese option ist nicht da, wie auch immer du es geschafft hast.\n")
            else:
                print(f"\nThat option is not there however you got that in.\n")

    elif kwargs["mode"]=="deconvert":
        if kwargs["convert"]=="hex":
            variables.out=bytes([int(x, 16) for x in kwargs["content"].split()]).decode()
            print(variables.out)
            
        elif kwargs["convert"]=="bin" or kwargs["convert"]=="binary":
            variables.out=""
            part1=kwargs["content"].split()
            for data in part1:
                data=int(data, 2)
                data=chr(data)
                variables.out+=data
                print(data)
                print(variables.out)
            
            print(part1, data)

            print(variables.out)
            
        elif kwargs["convert"]=="phex" or kwargs["convert"]=="pseudo hex" or kwargs["convert"]=="pbin" or kwargs["convert"]=="pseudo binary" or kwargs["convert"]=="lpbin" or kwargs["convert"]=="legacy pseudo binary":
            variables.out="".join(list(kwargs["charset"].keys())[list(kwargs["charset"].values()).index(c)] for c in kwargs["content"].split())
            print(variables.out)
            
        elif kwargs["convert"]=="ascii":
            variables.out="".join(map(lambda x: chr(int(x)), kwargs["content"].split()))
            print(variables.out)
            
        elif kwargs["convert"]=="brainfuck":
            variables.out=brainfuckery.Brainfuckery().interpret(kwargs["content"])
            print(variables.out)
            
        elif kwargs["convert"]=="base64":
            part1=bytes(kwargs["content"], encoding="utf-8")
            part2=base64.b64decode(part1)
            variables.out=str(part2, encoding="utf-8")
            print(variables.out)
            
        elif kwargs["convert"]=="symbenc":
            data=kwargs["content"]
            unsupported_symbols=""
            for i in range(len(data)):
                if data[i] not in lists.deconvert:
                    unsupported_symbols += f'{data[i]}, '
            unsupported_symbols = unsupported_symbols[:-2]
            if unsupported_symbols=="":
                for _ in range(len(data)):
                    variables.out += str(lists.deconvert[data[_]])
                print(variables.out)
                unsupported_symbols=""
            else:
                print(f"Error: the symbols are not supported: {unsupported_symbols}")
                unsupported_symbols=""
        else:
            if config.language=="de":
                print(f"\nDiese option ist nicht da, wie auch immer du es geschafft hast.\n")
            else:
                print(f"\nThat option is not there however you got that in.\n")

if __name__=="__main__":
    input("Please don't open that file on it's own. This is a module!")
    exit()