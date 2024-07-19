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

if __name__ == "__main__":
    while True:
        domain = input("Enter the domain to get the IP (or 0 to exit): ")
        if domain == '0':
            print("Exiting...")
            break
        domain = clean_domain(domain)
        ip = get_ip(domain)
        if ip:
            print(f"The IP of {domain} is {ip}")
