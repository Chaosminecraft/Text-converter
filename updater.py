import requests
import os

link="https://github.com/Chaosminecraft/Text-converter/releases/"
rversion="2.1"
bversion="2.1"
release=""

def update(release):
    lang="en"
    try:
        if release=="false":
            content = open("lang.txt", "r")
            lang = content.read()
            content.close()
            try:
                url = 'https://www.dropbox.com/s/a5wc7oon68nz9io/version-beta.txt?dl=1'

                r = requests.get(url, allow_redirects=True)

                open('version.txt', 'wb').write(r.content)
                loadf=open("version.txt", "r")

                version=loadf.read()

                loadf.close()
                
                if version>bversion:
                    if lang.lower() == "en":
                        print(f"There is an new Beta version: {version}\nThere is the site to download:↓\n{link}\n")
                        return

                    if lang.lower() == "de":
                        print(f"Da ist eine neue Beta Version: {version}\nHier ist die seite zum herunterladen:↓\n{link}\n")
                        return

                    else:
                        print(f"There is an new Beta version: {version}\nThere is the site to download:↓\n{link}\n")
                        return

                if version==bversion:
                    if lang.lower() == "en":
                        print(f"The Beta version is the latest version at the moment.\n")
                        return

                    if lang.lower() == "de":
                        print(f"Das ist die aktuelle Beta version im moment.\n")
                        return

                    else:
                        print(f"The version is the latest Beta version at the moment.\n")
                        return

                else:
                    print(f"Hol up: your version is in the Future...  the latest Beta version is: {version}\n")
                    return
                    
                return

            except:
                if lang.lower() == "en":
                    print(f"updater is unable to Fetch Version list.\n")
                    return

                if lang.lower() == "de":
                    print(f"Update konnte nicht zum server verbinden.\n")
                    return

                else:
                    print(f"updater is unable to Fetch Version list.\n")
                    return

        else:
            content = open("lang.txt", "r")
            lang = content.read()
            content.close()
            try:
                url = 'https://www.dropbox.com/s/h9cwtlx43bkbro2/version.txt?dl=1'

                r = requests.get(url, allow_redirects=True)

                open('version.txt', 'wb').write(r.content)
                loadf=open("version.txt", "r")

                version=loadf.read()

                loadf.close()
                
                if version>rversion:
                    if lang.lower() == "en":
                        print(f"There is an new version: {version}\nThere is download the link:↓\n{link}\n")
                        return

                    if lang.lower() == "de":
                        print(f"Da ist eine neue Version: {version}\nDa ist der link zum herunterladen:↓\n{link}\n")
                        return

                    else:
                        print(f"There is an new version: {version}\nThere is the download link:↓\n{link}\n")
                        return

                if version==rversion:
                    if lang.lower() == "en":
                        print(f"The version is the latest version at the moment.\n")
                        return

                    if lang.lower() == "de":
                        print(f"Das ist die neuste version im moment.\n")
                        return

                    else:
                        print(f"The version is the latest version at the moment.\n")
                        return

                else:
                    print(f"Hol up: your version is in the Future...  the latest release version is: {version}\n")
                    return
                    
                #os.remove("version.txt") #deactivated to make helping on code probably better...
                return

            except:
                if lang.lower() == "en":
                    print(f"updater is unable to Fetch Version list.\n")
                    return

                if lang.lower() == "de":
                    print(f"Update konnte nicht zum server verbinden.\n")
                    return

                else:
                    print(f"updater is unable to Fetch Version list.\n")
                    return

    except FileNotFoundError:
            return
