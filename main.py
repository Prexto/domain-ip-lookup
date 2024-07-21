import socket
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time
import sys

# Initialize Colorama
init(autoreset=True)

def clean_domain(domain):
    if domain.startswith('http://'):
        domain = domain[len('http://'):]
    elif domain.startswith('https://'):
        domain = domain[len('https://'):]
    
    if not domain.startswith('www.'):
        domain = 'www.' + domain

    return domain

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as err:
        print(Fore.RED + f"Could not get the IP for {domain}: {err}")
        return None

def get_own_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as err:
        print(Fore.RED + f"Could not get the own IP: {err}")
        return None

def basic_scraping(domain):
    urls = [f"http://{domain}", f"https://{domain}"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.title.string if soup.title else 'No title found'
            headings = {f'h{i}': [tag.text.strip() for tag in soup.find_all(f'h{i}')] for i in range(1, 7)}
            paragraphs = [p.text.strip() for p in soup.find_all('p')]
            links = [a['href'] for a in soup.find_all('a', href=True)]
            images = [img['src'] for img in soup.find_all('img', src=True)]
            metas = {meta.get('name', ''): meta.get('content', '') for meta in soup.find_all('meta', attrs={'name': True, 'content': True})}
            
            return {
                'title': title,
                'headings': headings,
                'paragraphs': paragraphs,
                'links': links,
                'images': images,
                'metas': metas
            }
        except requests.RequestException as e:
            print(Fore.RED + f"Could not scrape the website {url}: {e}")
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred while scraping {url}: {e}")
    
    return None

def print_ascii_banner():
    banner = r"""
  _____  _____  ________   _________ ____  
 |  __ \|  __ \|  ____\ \ / /__   __/ __ \ 
 | |__) | |__) | |__   \ V /   | | | |  | |
 |  ___/|  _  /|  __|   > <    | | | |  | |
 | |    | | \ \| |____ / . \   | | | |__| |
 |_|    |_|  \_\______/_/ \_\  |_|  \____/ 
                                           
    """
    # Print ASCII banner
    print(Fore.MAGENTA + banner + Style.RESET_ALL)

def display_exiting_animation():
    animation = ['.', '..', '...']
    for _ in range(3):
        for anim in animation:
            sys.stdout.write(Fore.RED + f"Exiting{anim}" + Style.RESET_ALL + "\r")
            sys.stdout.flush()
            time.sleep(0.5)
    print(Fore.RED + "Exiting..." + Style.RESET_ALL)

def display_ip(ip, label):
    print()
    for _ in range(3):
        sys.stdout.write(Fore.LIGHTCYAN_EX + f"{label} IP is {ip} " + "." * (3) + Style.RESET_ALL + "\r")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(Fore.LIGHTCYAN_EX + f"{label} IP is {ip}" + Style.RESET_ALL + "\r")
        sys.stdout.flush()
        time.sleep(0.2)
    print(Fore.LIGHTCYAN_EX + f"{label} IP is {ip}" + Style.RESET_ALL)

def main_menu():
    while True:
        print_ascii_banner()
        print("\n" + Fore.CYAN + "Main Menu:" + Style.RESET_ALL + "\n")  # Added a line space after Main Menu

        print(Fore.YELLOW + "1. Get my own IP address" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Get IP address of a domain" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Scrape data from a domain" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Get IP address and scrape data from a domain" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Exit" + Style.RESET_ALL)

        choice = input(Fore.GREEN + "Select an option (1, 2, 3, 4, or 5): " + Style.RESET_ALL)

        if choice == '1':
            ip = get_own_ip()
            if ip:
                display_ip(ip, "Your own")

        elif choice == '2':
            domain = input(Fore.CYAN + "Enter the domain to get the IP (e.g., example.com): " + Style.RESET_ALL)
            domain = clean_domain(domain)
            ip = get_ip(domain)
            if ip:
                display_ip(ip, domain)

        elif choice == '3':
            domain = input(Fore.CYAN + "Enter the domain to scrape data from (e.g., example.com): " + Style.RESET_ALL)
            domain = clean_domain(domain)
            data = basic_scraping(domain)
            if data:
                print(Fore.GREEN + f"Title: {data['title']}" + Style.RESET_ALL)
                print(Fore.BLUE + "Headings:" + Style.RESET_ALL)
                for tag, texts in data['headings'].items():
                    print(Fore.BLUE + f"  {tag}: {', '.join(texts)}" + Style.RESET_ALL)
                print(Fore.BLUE + "Paragraphs:" + Style.RESET_ALL)
                for paragraph in data['paragraphs']:
                    print(Fore.BLUE + f"  {paragraph}" + Style.RESET_ALL)
                print(Fore.BLUE + "Links:" + Style.RESET_ALL)
                for link in data['links']:
                    print(Fore.BLUE + f"  {link}" + Style.RESET_ALL)
                print(Fore.BLUE + "Images:" + Style.RESET_ALL)
                for image in data['images']:
                    print(Fore.BLUE + f"  {image}" + Style.RESET_ALL)
                print(Fore.BLUE + "Meta Tags:" + Style.RESET_ALL)
                for name, content in data['metas'].items():
                    print(Fore.BLUE + f"  {name}: {content}" + Style.RESET_ALL)

        elif choice == '4':
            domain = input(Fore.CYAN + "Enter the domain to get the IP and scrape data from (e.g., example.com): " + Style.RESET_ALL)
            domain = clean_domain(domain)
            ip = get_ip(domain)
            if ip:
                display_ip(ip, domain)
                print()  # Add space between IP and data
                data = basic_scraping(domain)
                if data:
                    print(Fore.GREEN + f"Title: {data['title']}" + Style.RESET_ALL)
                    print(Fore.BLUE + "Headings:" + Style.RESET_ALL)
                    for tag, texts in data['headings'].items():
                        print(Fore.BLUE + f"  {tag}: {', '.join(texts)}" + Style.RESET_ALL)
                    print(Fore.BLUE + "Paragraphs:" + Style.RESET_ALL)
                    for paragraph in data['paragraphs']:
                        print(Fore.BLUE + f"  {paragraph}" + Style.RESET_ALL)
                    print(Fore.BLUE + "Links:" + Style.RESET_ALL)
                    for link in data['links']:
                        print(Fore.BLUE + f"  {link}" + Style.RESET_ALL)
                    print(Fore.BLUE + "Images:" + Style.RESET_ALL)
                    for image in data['images']:
                        print(Fore.BLUE + f"  {image}" + Style.RESET_ALL)
                    print(Fore.BLUE + "Meta Tags:" + Style.RESET_ALL)
                    for name, content in data['metas'].items():
                        print(Fore.BLUE + f"  {name}: {content}" + Style.RESET_ALL)

        elif choice == '5':
            display_exiting_animation()
            break

        else:
            print(Fore.RED + "Invalid option. Please choose 1, 2, 3, 4, or 5." + Style.RESET_ALL)

    # Display social media links with space and color
    print("\n" + Fore.MAGENTA + "Connect with me on X (formerly Twitter): @https://x.com/messino_james" + Style.RESET_ALL)
    print(Fore.MAGENTA + "Check out my GitHub: github.com/Prexto" + Style.RESET_ALL + "\n")

if __name__ == "__main__":
    main_menu()
