def converterhelp(command, language, answer):
    temp=""

def mainhelp(command, language):
    if language=="en":
        print(f"""Help Site:
                  Common commands:
              Help gives the Help text
              Hex converts between hex and text
              phex converts between pseudo hex and text
              bin converts between Binary and text
              pbin converts between pseudo binary and text
              legagy pbin converts between an older version of Pseudo Binary and text
              ascii converts between ascii and text
              brainfuck converts between brainfuck and text
              base64 converts between base64 and text (only normal text for now)""")
        return