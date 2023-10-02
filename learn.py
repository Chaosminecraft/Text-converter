import webbrowser as web
from logger import log_info
#from settings import ad_makefile

def free_ad(language, logg):
    while True:
        try:
            try:
                if language=="de":
                    print(f"\n[AD] Spiel mal while True: learn(), es ist ein gutes spiel.\nWo man das Spiel holen kann sieht man mit dem command: get game\nWenn du diese werbung nicht mer sehen willst, schreib: ad setting")
                if language=="en":
                    print(f"\n[AD] Play while True: learn(), it's a good game.\nYou can see where you can get the game with the command: get game\nIf you don't want to see this ad again, write: ad setting")
                text="Ad has been delivered."
                log_info(text, logg)
                return
            except FileNotFoundError:
                #ad_makefile(logg)
                temp=""

        except KeyboardInterrupt:
            return

def get_game(language, logg):
    while True:
        try:
            if language=="de":
                print("Da sind diese Stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. luden.io\n11. Exit geht zurück zum text converter Projekt.")
                ans=input("Von welchem store möchtest du es: ")
                text=ans
                log_info(text, logg)
                if ans.lower()=="steam" or ans.lower()=="1":
                    web.open("https://store.steampowered.com/app/619150/while_True_learn/")
                if ans.lower()=="epic games store" or ans.lower()=="2":
                    web.open("https://www.epicgames.com/store/en-US/p/while-true-learn")
                if ans.lower()=="humble" or ans.lower()=="3":
                    web.open("https://www.humblebundle.com/store/while-true-learn")
                if ans.lower()=="google play" or ans.lower()=="4":
                    web.open("https://play.google.com/store/apps/details?id=com.nival.wtlm")
                if ans.lower()=="apple store" or ans.lower()=="5":
                    web.open("https://itunes.apple.com/app/while-true-learn/id1443569124")
                if ans.lower()=="switch store" or ans.lower()=="6":
                    web.open("https://www.nintendo.com/games/detail/while-true-learn-switch/")
                if ans.lower()=="playstation 4" or ans.lower()=="7":
                    web.open("https://store.playstation.com/en-us/product/UP3390-CUSA20449_00-AAAAAAA000000001")
                if ans.lower()=="galaxy store" or ans.lower()=="8":
                    web.open("http://galaxystore.samsung.com/detail/com.nival.wtlm.gs")
                if ans.lower()=="gog" or ans.lower()=="9":
                    web.open("https://www.gog.com/game/while_true_learn")
                if ans.lower()=="luden.io" or ans.lower()=="10":
                    web.open("https://luden.io/wtl/")
                if ans.lower()=="exit" or ans.lower()=="11":
                    print()
                    return
                else:
                    print(f"sorry, dieser store hat das spiel in der version von diesem Werbung modul. :(\n")

            if language=="en":
                print("there are those stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. Exit goes to the Text converter Project.")
                ans=input("from what store do you want it: ")
                text=ans
                log_info(text)
                if ans.lower()=="steam" or ans.lower()=="1":
                    web.open("https://store.steampowered.com/app/619150/while_True_learn/")
                if ans.lower()=="epic games store" or ans.lower()=="2":
                    web.open("https://www.epicgames.com/store/en-US/p/while-true-learn")
                if ans.lower()=="humble" or ans.lower()=="3":
                    web.open("https://www.humblebundle.com/store/while-true-learn")
                if ans.lower()=="google play" or ans.lower()=="4":
                    web.open("https://play.google.com/store/apps/details?id=com.nival.wtlm")
                if ans.lower()=="apple store" or ans.lower()=="5":
                    web.open("https://itunes.apple.com/app/while-true-learn/id1443569124")
                if ans.lower()=="switch store" or ans.lower()=="6":
                    web.open("https://www.nintendo.com/games/detail/while-true-learn-switch/")
                if ans.lower()=="playstation 4" or ans.lower()=="7":
                    web.open("https://store.playstation.com/en-us/product/UP3390-CUSA20449_00-AAAAAAA000000001")
                if ans.lower()=="galaxy store" or ans.lower()=="8":
                    web.open("http://galaxystore.samsung.com/detail/com.nival.wtlm.gs")
                if ans.lower()=="gog" or ans.lower()=="9":
                    web.open("https://www.gog.com/game/while_true_learn")
                if ans.lower()=="luden.io" or ans.lower()=="10":
                    web.open("https://luden.io/wtl/")
                if ans.lower()=="exit" or ans.lower()=="11":
                    print()
                    return
                else:
                    print(f"i'm sorry, that shop has in that module version not the game. :(\n")
        except KeyboardInterrupt:
            return