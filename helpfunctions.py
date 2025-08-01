def converterhelp(config, **kwargs):
    if config.language=="de":
        print(f"""
Allgemeine commands:
    help zeigt diese seite
    convert convertiert den text zu {kwargs["mode"]} (Bei meinen eigenen methoden nur ascii)
    deconvert convertiert von {kwargs["mode"]} zu text
    exit bringt dich zum hauptmenü\n""")

    else:
        print(f"""
Common commands:
    help shows that site
    convert converts from text to {kwargs["mode"]} (My own formats have a limit to ascii only)
    deconvert converts from {kwargs["mode"]} to text
    exit returns to the main menu\n""")
    
    return

def mainhelp(language):
    #print(language) #debugging
    if language=="de":
        print(f"""
Allgemeine commands:
    Help gibt den Hilfetext aus
    Hex konvertiert zwischen Hex und Text
    phex konvertiert zwischen Pseudo-Hex und Text
    bin konvertiert zwischen Binär und Text
    pbin konvertiert zwischen Pseudobinärdatei und Text
    lpbin konvertiert zwischen einer älteren Version von Pseudo Binary und Text
    ASCII konvertiert zwischen ASCII und Text
    Brainfuck konvertiert zwischen Brainfuck und Text
    base64 konvertiert zwischen base64 und Text (vorerst nur normaler Text)\n
Zusätzliche Informationen:
    language Gibt dir eine auswahl zwischen Deutsch(de) und Englisch(en)
    prompt ändert den prompt look (direkt nach start den prompt)
    ad gibt dir die option ob du die Werbung sehen willst oder nicht
    update gibt dir die option nach updates zu schauen am start.
    logging gibt dir die option ob du Nicht essenzielle sachen loggen möchtest.
    ping ist ein einfacher ping command.\n""")
        
        return
    
    else:
        print(f"""
Common commands:
    Help gives the Help text
    Hex converts between hex and text
    phex converts between pseudo hex and text
    bin converts between Binary and text
    pbin converts between pseudo binary and text
    lpbin converts between an older version of Pseudo Binary and text
    ascii converts between ascii and text
    brainfuck converts between brainfuck and text
    base64 converts between base64 and text (only normal text for now)\n
Additional info:
    language let's you change between English(en) or German(de).
    prompt let's you change the prompt look. (After startup the prompt)
    ad let's you change if you wanna see the ad (currently broken)
    update let's you change the setting if you want to check for updates.
    logging let's you change if you wanna log non critical things. (critical things are like: Mid runtime there was a Recoverable or non recoverable error)
    ping is a simple ping command.\n""")
        
        return

if __name__=="__main__":
    input("Please don't open that file on it's own. This is a module!")
    exit()