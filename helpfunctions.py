def converterhelp(command, language, answer):
    temp=""

def mainhelp(command, language):
    if language=="en":
        print(f"""
Common commands:
    Help gives the Help text
    Hex converts between hex and text
    phex converts between pseudo hex and text
    bin converts between Binary and text
    pbin converts between pseudo binary and text
    legagy pbin converts between an older version of Pseudo Binary and text
    ascii converts between ascii and text
    brainfuck converts between brainfuck and text
    base64 converts between base64 and text (only normal text for now)\n
Additional info:
    The settings currently can't be dynamicalyl be changed.\n""")
        
        return

    elif language=="de":
        print(f"""
Allgemeine Befehle:
    Hilfe gibt den Hilfetext aus
    Hex konvertiert zwischen Hex und Text
    phex konvertiert zwischen Pseudo-Hex und Text
    bin konvertiert zwischen Binär und Text
    pbin konvertiert zwischen Pseudobinärdatei und Text
    Legacy Pbin konvertiert zwischen einer älteren Version von Pseudo Binary und Text
    ASCII konvertiert zwischen ASCII und Text
    Brainfuck konvertiert zwischen Brainfuck und Text
    base64 konvertiert zwischen base64 und Text (vorerst nur normaler Text)\n
Zusätzliche Informationen:
    Die einstellungen können aktuell nicht dynamisch geändert werden.\n""")
        
        return
    
    else:
        print(f"""
Common commands:
    Help gives the Help text
    Hex converts between hex and text
    phex converts between pseudo hex and text
    bin converts between Binary and text
    pbin converts between pseudo binary and text
    legagy pbin converts between an older version of Pseudo Binary and text
    ascii converts between ascii and text
    brainfuck converts between brainfuck and text
    base64 converts between base64 and text (only normal text for now)\n
Additional info:
    The settings currently can't be dynamicalyl be changed.\n""")
        
        return