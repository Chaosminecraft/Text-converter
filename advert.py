import webbrowser as web
from logger import log_info, log_system
from random import randint

def free_ad(language, logg):
    if language=="de":
        print(f"\n[AD] Spiel mal while True: learn(), es ist ein gutes spiel.\nWo man das Spiel holen kann sieht man mit dem command: get game\nWenn du diese werbung nicht mer sehen willst, schreib: ad setting")
    else:
        print(f"\n[AD] Play while True: learn(), it's a good game.\nYou can see where you can get the game with the command: get game\nIf you don't want to see this ad again, write: ad setting")

    if logg==True:
        text=randomtext()
        log_info(text=text, logg=logg)
    return

# that function is just to do a little joking on the log
def randomtext():
    random=randint(1, 5)
    if random==1:
        text="Why do i deliver that ad? i won't get paid anyways. [Sigh]... i delivered it anyways."
    if random==2:
        text="A... Ad delivered, please just don't disable it... Just kidding, i don't get paid for that."
    if random==3:
        text="HAHAHAHHAHHAHHAHHHA, Thanks for using that ad. i won'd get paid tho for that."
    if random==4:
        text="Thanks for running the ad i don't get paid for. :)"
    if random==5:
        text="Don... DON'T CODE WHILE HALF ASLEEP FOR THE LOVE OF GOD! there is an ad tho."
    return text

#that is the stores where the game is Available at
def get_game(language, logg, name):
    while True:
        try:
            if language=="de": #The German question of what store (some may be uncaught that are not working)
                print("Da sind diese Stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. luden.io\n11. Exit geht zurück zum text converter Projekt.")
                ans=input("Von welchem store möchtest du es: ")
                ans=ans.lower()
            
            else:#The English question of what store (some may be uncaught that are not working)
                print("there are those stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. Exit goes to the Text converter Project.")
                ans=input("from what store do you want it: ")
            
            if logg==True:#If the logging module is okay
                text=f"the user {name} chose the store: {ans}"
                log_info(text, logg)

            #The list of the Stores
            if ans=="steam" or ans=="1":
                web.open("https://store.steampowered.com/app/619150/while_True_learn/")
            elif ans=="epic games store" or ans=="2":
                web.open("https://www.epicgames.com/store/en-US/p/while-true-learn")
            elif ans=="humble" or ans=="3":
                web.open("https://www.humblebundle.com/store/while-true-learn")
            elif ans=="google play" or ans=="4":
                web.open("https://play.google.com/store/apps/details?id=com.nival.wtlm")
            elif ans=="apple store" or ans=="5":
                web.open("https://itunes.apple.com/app/while-true-learn/id1443569124")
            elif ans=="switch store" or ans=="6":
                web.open("https://www.nintendo.com/games/detail/while-true-learn-switch/")
            elif ans=="playstation 4" or ans=="7":
                web.open("https://store.playstation.com/en-us/product/UP3390-CUSA20449_00-AAAAAAA000000001")
            elif ans=="galaxy store" or ans=="8":
                web.open("http://galaxystore.samsung.com/detail/com.nival.wtlm.gs")
            elif ans=="gog" or ans.lower()=="9":
                web.open("https://www.gog.com/game/while_true_learn")
            elif ans=="luden.io" or ans=="10":
                web.open("https://luden.io/wtl/")
            elif ans=="exit" or ans=="11":
                print()
                return
            else:
                if language=="de":
                    print(f"i'm sorry, that shop has in that module version not the game. :(\n")
                else:
                    print(f"sorry, dieser store hat das spiel in der version von diesem Werbung modul. :(\n")

        except KeyboardInterrupt:
            print()
            return

#if __name__=="__main__":
#    free_ad(language="en", logg=False)