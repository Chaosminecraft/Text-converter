import random as ran

def notext(language):#if no text has been given that is used.
    num=ran.randint(1, 3)
    if language=="de":
        if num==1:
            print("Ups, Vielleicht etwas mehr text... nicht nur nichts")

        if num==2:
            print("hmmm. etwas ist mit UPS oder du hast nichts eingegeben...")

        if num=="3":
            print("DHL hat keine post gegeben, oder hast du nichts gesendet?")
        return

    if language=="en":
        if num==1:
            print(f"\n-_-\n")

        if num==2:
            print(f"\nHahaha, you typed nothing. :(\n\ntry it with help.\n")

        if num==3:
            print(f"\nA wild NULL appeared\n")

        return

def wrongtxt(answer, language):#if there is something written wrong.
    if language == "en":
        num=ran.randint(1, 5)
        if num==1:
            print(f"\nWhat? please use Help. not {answer}.\n")

        if num==2:
            print(f"\nWoops... please write help. not {answer}.\n")

        if num==3:
            print(f"\nNope, {answer} is not here. Use help.\n")

        if num==4:
            print(f"\nNo no no! not {answer}. Please use help\n")

        if num==5:
            print(f"\nWrite help. {answer} is not a Command.\n")
        
        return

    if language == "de":
        number=ran.randint(1, 5)
        if number == 1:
            print(f"\nWas? das itst kein Command! bitte gib help nicht {answer} ein.\n")
        if number == 2:
            print(f"\noh. Schreib einfach help. nicht {answer}.\n")
        if number == 3:
            print(f"\nNope, {answer} ist nicht hier Drinnen. nutz help.\n")
        if number == 4:
            print(f"\nNein nein nein! nicht {answer}. Bitte nutz help\n")
        if number == 5:
            print(f"\nSchreib help. {answer} ist kein command.\n")
        
        return
