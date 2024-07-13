import json
with open('lang.json', 'r', encoding='utf-8') as langfile:
    langs = json.load(langfile)
lang = input('Choose a language (English, Deutsch, Русский): ').lower()
if lang == "english" or lang == "en" or lang == "englisch" or lang == "английский":
    lang = "en"
elif lang == "deutsch" or lang == "de" or lang == "german" or lang == "немецкий":
    lang = "de"
elif lang == "russian" or lang == "ru" or lang == "русский" or lang == "russisch":
    lang = "ru"
else:
    print('Unknown language, using English.')
    lang = "en"
langi = langs[lang]
EoD = input(langi['Welcome'])
if EoD == "1":
    texttoencode = input(langi["TTE"]).lower()
    allowed = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "0": "j", " ": "4", ",": "0", ".": "1", "?": "2", "!": "3", "a": "!", "b": "@", "c": "#", "d": "$", "e": "%", "f": "^", "g": "&", "h": "*", "i": "(", "j": ")", "k": "-", "l": "_", "m": "=", "n": "+", "o": "[", "p": "]", "q": "{", "r": "}", "s": ":", "t": ";", "u": "<", "v": ">", "w": ",", "x": ".", "y": "/", "z": "?"}
    unsupported_symbols = ""
    for i in range(len(texttoencode)):
        print(i)
        if texttoencode[i] not in allowed:
            unsupported_symbols += f"{texttoencode[i]}, "
    unsupported_symbols = unsupported_symbols[:-2]
    if unsupported_symbols == "":
        newText = ""
        for _ in range(len(texttoencode)):
            print(_)
            newText += str(allowed[texttoencode[_]])
            print(newText)
        print(newText)
    else:
        print(str(langi["Errors"]["SymbolNotSupportedError"]).replace('{symbols}',unsupported_symbols))
elif EoD == "0":
    texttodecode = input(langi["TTD"]).lower()
    allowed = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0", "\"": "\"", " ": " ", "4": " ", "0": ",", "1": ".", "2": "?", "3": "!", "!": "a", "@": "b", "#": "c", "$": "d", "%": "e", "^": "f", "&": "g", "*": "h", "(": "i", ")": "j", "-": "k", "_": "l", "=": "m", "+": "n", "[": "o", "]": "p", "{": "q", "}": "r", ":": "s", ";": "t", "<": "u", ">": "v", ",": "w", ".": "x", "/": "y", "?": "z"}
    unsupported_symbols = ""
    for i in range(len(texttodecode)):
        if texttodecode[i] not in allowed:
            unsupported_symbols += f"{texttodecode[i]}, "
    unsupported_symbols = unsupported_symbols[:-2]
    if unsupported_symbols == "":
        newText = ""
        for _ in range(len(texttodecode)):
            newText += str(allowed[texttodecode[_]])
        print(newText)
    else:
        print(str(langi["Errors"]["SymbolNotSupportedError"]).replace('{symbols}',unsupported_symbols))
else:
    print(str(langi["Errors"]["UnknownTool"]).replace('{tool}',EoD))