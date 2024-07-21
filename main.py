import socket

def clean_domain(domain):
    # Remove 'http://' and 'https://' prefixes
    if domain.startswith('http://'):
        domain = domain[len('http://'):]
    elif domain.startswith('https://'):
        domain = domain[len('https://'):]
    
    # Add 'www.' to the domain if it's not present
    if not domain.startswith('www.'):
        domain = 'www.' + domain

    return domain

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as err:
        print(f"Could not get the IP for {domain}: {err}")
        return None

def get_own_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as err:
        print(f"Could not get the own IP: {err}")
        return None

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Get my own IP address")
        print("2. Get IP address of a domain")
        print("3. Exit")

        choice = input("Select an option (1, 2, or 3): ")

        if choice == '1':
            ip = get_own_ip()
            if ip:
                print(f"Your IP address is {ip}")

        elif choice == '2':
            domain = input("Enter the domain to get the IP (e.g., example.com): ")
            domain = clean_domain(domain)
            ip = get_ip(domain)
            if ip:
                print(f"The IP of {domain} is {ip}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
