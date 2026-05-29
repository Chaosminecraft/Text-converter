import subprocess, json

def get_hosted_network_json():
    # netsh Befehl ausführen (cp850 für deutsche Umlaute in der CMD)
    result = subprocess.run(['netsh', 'wlan', 'show', 'hostednetwork'], capture_output=True, text=True, encoding='cp850')
    
    data = {}
    current_section = "allgemein"
    
    # Zeilenweise durchgehen
    for line in result.stdout.splitlines():
        line = line.strip()
        
        # Leere Zeilen oder Trennlinien überspringen
        if not line or line.startswith("---"):
            continue
            
        # Wenn eine Zeile keinen Doppelpunkt hat, ist es eine Überschrift (z.B. "Einstellungen des gehosteten Netzwerks")
        if ":" not in line:
            current_section = line.lower().replace(" ", "_")
            data[current_section] = {}
            continue
            
        # Schlüssel und Wert am Doppelpunkt trennen
        key, value = line.split(":", 1)
        key = key.strip().lower().replace(" ", "_")
        value = value.strip()
        length=len(value)
        if value[0:1]=='"' and value[length-1:length]=='"':
            value=value[1:length-1]
        
        # In die aktuelle Sektion einfügen
        if current_section in data and isinstance(data[current_section], dict):
            data[current_section][key] = value
        else:
            data[key] = value

    # Das Python-Dictionary in einen JSON-String umwandeln
    return json.dumps(data, indent=4, ensure_ascii=False)

if __name__=="__main__":
    input("CLOSE THAT RIGHT NOW!!!!")
    exit()