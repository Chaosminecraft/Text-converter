import webbrowser as web
from logger import *
from settings import set_ad_setting, get_lang

def while_true_learn_ad(language, logg): #an ad i added just for fun, but it might be gone in some time.
    try:
        text="ad Successfully run"
        log_info(text, logg)
        settings_ad=open("ad setting.txt", "r")
        adsetting=settings_ad.read()
        settings_ad.close()
        if adsetting.lower()=="yes":
            if language=="en":
                print(f"\n[AD] Try while True: learn(), it is a good game.\ni can personally say that 'Chaosminecraft'\nThe game can be get with the command Get Game\nif you want that ad removed, you can type: ad setting\n")
                return
            if language=="de":
                print("\n[AD] Versuch mal while True: learn(), es ist ein echt gutes spiel.\nich kann es persöhnlich empfehlen 'Chaosminecraft'\ndas Spiel kann man mit Get Game\nWenn du diese Werbung nicht mehr haben möchtest, schreib: ad setting\n")
                return
        else:
            return
    except FileNotFoundError:
        error_nofile="true"
        set_ad_setting(error_nofile, language)
        return error_nofile

def get_game(language, logg): #Loading lang.txt and reading it
    while True:
        try:
            if language == "de":
                lang="de"
                ask_shop(language, logg)
                return
            if language == "en":
                lang="en"
                ask_shop(language, logg)
                return
            else:
                get_lang()
                print("language misshap, press enter to continue")

        except FileNotFoundError:
            text="Language File Error, trying to make a New file."
            log_warning(text, logg)
            get_lang()

def ask_shop(language, logg):
    while True:
        if language=="de":
            print("Da sind diese Stores:\n1. steam\n2. epic games store\n3. humble\n4. Google Play\n5. Apple Store\n6. Nintendo\n7. Playstation 4\n8. Galaxy Store\n9. gog\n10. Exit geht zurück zum text converter Projekt.")
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
            if ans.lower()=="exit" or ans.lower()=="10":
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
            if ans.lower()=="exit" or ans.lower()=="10":
                print()
                return
            else:
                print(f"i'm sorry, that shop has in that module version not the game. :(\n")
