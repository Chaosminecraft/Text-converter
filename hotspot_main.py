import os, sys, time, json, subprocess, socket

from hotspot_detect import get_hosted_network_json

class options:
    module=True

def watchdog():
    print(f"Watchdog starting...\n")

    while True:
        start=time.time()
        os.system("cls")
        try:
            json_data=get_hosted_network_json()
            data=json.loads(json_data)
            status_info = data.get("status_des_gehosteten_netzwerks", {})
            status = status_info.get("status", "Unbekannt")
            anzahl_clients=int(status_info.get("anzahl_clients", "0"))
            ssid = data.get("einstellungen_für_das_gehostete_netzwerk", {}).get("ssid-name", "Unbekannt") #thisfuckinglinedrivesmecrazyplshelp
        except Exception as e:
            print(f"[Fehler] Info konnte nicht gelesen werden: {e}")
            elapsed_time=time.time()
            wait_time=max(2, elapsed_time * 2)
            time.sleep(wait_time)
        
        # Schicke Konsolen-Anzeige basteln
        print("=" * 50)
        print("         HOTSPOT WATCHDOG AKTIV")
        print("=" * 50)
        print(f" Hotspot SSID:  {ssid}")
        print(f" Status:        {status}")
        print(f" Clients:       {anzahl_clients}")
        print("-" * 50)

        # Logik: Was soll passieren?
        if status != "Gestartet":
            print("[!] Hotspot ist AUS! Starte neu...")
            # Hotspot aktivieren
            subprocess.run(['netsh', 'wlan', 'stop', 'hostednetwork'], capture_output=True)
            subprocess.run(['netsh', 'wlan', 'start', 'hostednetwork'], capture_output=True)
            print("[+] Startbefehl gesendet.")
        else:
            print("[i] Warte auf Clients... Alles läuft normal.")

        print("=" * 50)
        print("Nächster Check in 2 Sekunden... (Beenden mit Strg+C)")
        
        try:
            elapsed_time=time.time()
            wait_time=max(2, elapsed_time * 2)
            time.sleep(wait_time)
        except KeyboardInterrupt:
            print("\nWatchdog wird sauber beendet. Tschau!")
            os.system("cls")
            if options.module==False:
                sys.exit(0)

if __name__=="__main__":
    options.module=False
    watchdog()