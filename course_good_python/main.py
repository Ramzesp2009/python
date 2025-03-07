import ipaddress


def berechne_subnetz_details(subnetz: str):
    """
    Berechnet anhand der Netzangabe (CIDR oder IP/Subnetzmaske) die
    erste Adresse (Netzadresse), die letzte Adresse (Broadcast) und die Anzahl
    der nutzbaren Hosts.
    """
    try:
        net = ipaddress.ip_network(subnetz, strict=False)
    except ValueError as e:
        print("Fehlerhafte Subnetz-Angabe:", e)
        return None, None, None

    erste_ip = net.network_address
    letzte_ip = net.broadcast_address if isinstance(net, ipaddress.IPv4Network) else None
    gesamt_ips = net.num_addresses

    # Bei Subnetzen mit mehr als 2 Adressen werden die Netzwerk- und Broadcastadresse
    # nicht als Hosts gezählt. Bei IPv6 gibt es keine Broadcast-Adresse.
    if isinstance(net, ipaddress.IPv4Network) and gesamt_ips > 3:
        # Ziehe Netzwerk-, Broadcast-Adresse und Gateway ab
        nutzbare_hosts = gesamt_ips - 3
    elif isinstance(net, ipaddress.IPv6Network) and gesamt_ips > 2:
        # Ziehe Netzwerkadresse und Gateway ab (kein Broadcast bei IPv6)
        nutzbare_hosts = gesamt_ips - 2
    else:
        nutzbare_hosts = max(0, gesamt_ips - 1)  # Mindestens 0 nutzbare Hosts

    return erste_ip, letzte_ip, nutzbare_hosts


def berechne_details_von_ip_mit_maske(ip: str, maske: str):
    """
    Erzeugt aus einer IP-Adresse und einer Subnetzmaske (in Punkt-Notation)
    eine Netzangabe im Format 'IP/Maske' und berechnet die Netzdetails.
    Unterstützt sowohl IPv4 als auch IPv6.
    """
    net_string = f"{ip}/{maske}"
    return berechne_subnetz_details(net_string)


def netmask_to_prefix(netmask_str: str) -> int:
    """
    Wandelt eine Subnetzmaske in Punkt-Notation (z. B. 255.255.255.0)
    in die entsprechende Präfixlänge (/24) um.
    """
    try:
        # Erzeuge ein Netzwerkobjekt mit Basisadresse 0.0.0.0
        return ipaddress.IPv4Network("0.0.0.0/" + netmask_str).prefixlen
    except ValueError as e:
        print("Ungültige Subnetzmaske:", e)
        return None


def split_network(network_str: str, new_netmask_str: str):
    """
    Teilt das angegebene Netzwerk (z.B. 192.168.178.0/16 oder 2001:db8::/32) in kleinere
    Subnetze, basierend auf der neuen Subnetzmaske (z.B. 255.255.255.0 oder /64).
    """
    try:
        # Erstelle das Netzwerkobjekt
        net = ipaddress.ip_network(network_str, strict=False)
    except ValueError as e:
        print("Ungültige Netzwerkadresse:", e)
        return

    new_prefix = netmask_to_prefix(new_netmask_str)
    if new_prefix is None:
        return

    # Die neue Präfixlänge muss größer sein als die ursprüngliche, um
    # das Netzwerk in kleinere Subnetze aufzuteilen.
    if new_prefix <= net.prefixlen:
        print("Die neue Subnetzmaske muss mehr Bits enthalten als das ursprüngliche Präfix.")
        return

    # Erzeuge die Liste der Subnetze
    subnets = list(net.subnets(new_prefix=new_prefix))
    print(f"Das Netzwerk {net} wird in {len(subnets)} Subnetze aufgeteilt:")
    for sn in subnets:
        print(f"Subnetz: {sn}, Neue Subnetzmaske: {sn.netmask}")


def split_network_by_subnet_count(network_str: str, subnet_count: int):
    """
    Teilt das angegebene Netzwerk (z.B. 192.168.178.0/16 oder 2001:db8::/32) in eine angegebene Anzahl
    von Subnetzen auf und gibt die neuen Subnetzmasken aus.
    """
    try:
        # Erstelle das Netzwerkobjekt
        net = ipaddress.ip_network(network_str, strict=False)
    except ValueError as e:
        print("Ungültige Netzwerkadresse:", e)
        return

    # Berechne die neue Präfixlänge basierend auf der Anzahl der Subnetze
    new_prefix = net.prefixlen + (subnet_count - 1).bit_length()
    if new_prefix > net.max_prefixlen:
        print("Die Anzahl der Subnetze ist zu groß für das gegebene Netzwerk.")
        return

    # Erzeuge die Liste der Subnetze
    subnets = list(net.subnets(new_prefix=new_prefix))
    print(f"Das Netzwerk {net} wird in {len(subnets)} Subnetze aufgeteilt:")
    for sn in subnets:
        print(f"Subnetz: {sn}, Neue Subnetzmaske: {sn.netmask}")


def main():
    print("Wählen Sie den Eingabetyp:")
    print("1. CIDR-Notation (z.B. 192.168.178.0/16 oder 2001:db8::/32)")
    print(
        "2. Getrennte Eingabe von IP-Adresse und Subnetzmaske (z.B. IP: 192.168.178.0, Maske: 255.255.255.0 oder IP: 2001:db8::1, Maske: /64)")
    print("3. Netzwerk in Subnetze aufteilen (mit Subnetzmaske)")
    print("4. Netzwerk in eine bestimmte Anzahl von Subnetzen aufteilen")

    wahl = input("Ihre Wahl (1/2/3/4): ").strip()

    if wahl == "1":
        eingabe = input("Bitte geben Sie die Netzangabe ein (z.B. 192.168.178.0/16 oder 2001:db8::/32): ").strip()
        erste_ip, letzte_ip, nutzbare_hosts = berechne_subnetz_details(eingabe)
        if erste_ip is not None:
            print(f"Erste IP: {erste_ip}")
            if letzte_ip is not None:
                print(f"Letzte IP: {letzte_ip}")
            print(f"Anzahl der nutzbaren Hosts: {nutzbare_hosts}")
    elif wahl == "2":
        ip_input = input("Bitte geben Sie die IP-Adresse ein (z.B. 192.168.178.0 oder 2001:db8::1): ").strip()
        maske_input = input("Bitte geben Sie die Subnetzmaske ein (z.B. 255.255.255.0 oder /64): ").strip()
        erste_ip, letzte_ip, nutzbare_hosts = berechne_details_von_ip_mit_maske(ip_input, maske_input)
        if erste_ip is not None:
            print(f"Erste IP: {erste_ip}")
            print(f"Letzte IP: {letzte_ip}")
            print(f"Anzahl der nutzbaren Hosts: {nutzbare_hosts}")
    elif wahl == "3":
        print("Netzwerk in Subnetze aufteilen (mit Subnetzmaske)")
        network_input = input("Bitte geben Sie das Netzwerk ein (z.B. 192.168.178.0/16 oder 2001:db8::/32): ").strip()
        new_netmask_input = input("Bitte geben Sie die neue Subnetzmaske ein (z.B. 255.255.255.0 oder /64): ").strip()
        split_network(network_input, new_netmask_input)
    elif wahl == "4":
        print("Netzwerk in eine bestimmte Anzahl von Subnetzen aufteilen")
        network_input = input("Bitte geben Sie das Netzwerk ein (z.B. 192.168.178.0/16 oder 2001:db8::/32): ").strip()
        subnet_count = int(input("Bitte geben Sie die Anzahl der gewünschten Subnetze ein: ").strip())
        split_network_by_subnet_count(network_input, subnet_count)
    else:
        print("Ungültige Wahl. Bitte starten Sie das Programm neu und wählen Sie 1, 2, 3 oder 4.")


if __name__ == '__main__':
    main()




