import socket
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style
import time

colorama.init(autoreset=True)

def get_private_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json()["ip"]
    except requests.RequestException as e:
        print(f"Error retrieving public IP: {e}")
        return None

def get_ip(domain):
    domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as err:
        print(f"Could not obtain IP for {domain}: {err}")
        return None

def scrape_data(domain):
    try:
        response = requests.get(f"http://{domain}")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {
            "title": soup.title.string if soup.title else "No title found",
            "headings": [heading.get_text().strip() for heading in soup.find_all(['h1', 'h2', 'h3'])],
            "paragraphs": [para.get_text().strip() for para in soup.find_all('p')],
            "links": [link.get('href') for link in soup.find_all('a', href=True)],
            "images": [img.get('src') for img in soup.find_all('img', src=True)],
            "meta_tags": {meta.get('name'): meta.get('content') for meta in soup.find_all('meta', attrs={'name': True, 'content': True})}
        }
        return data
    except requests.RequestException as e:
        print(f"Could not scrape the website: {e}")
        return None

def display_ip_and_data(ip, data):
    print(f"\n{Fore.GREEN}IP Address: {ip}\n")
    if data:
        print(f"{Fore.CYAN}Title: {data['title']}\n")
        print(f"{Fore.CYAN}Headings:")
        for heading in data['headings']:
            print(f"  {heading}")
        print(f"\n{Fore.CYAN}Paragraphs:")
        for para in data['paragraphs']:
            print(f"  {para}")
        print(f"\n{Fore.CYAN}Links:")
        for link in data['links']:
            print(f"  {link}")
        print(f"\n{Fore.CYAN}Images:")
        for img in data['images']:
            print(f"  {img}")
        print(f"\n{Fore.CYAN}Meta Tags:")
        for name, content in data['meta_tags'].items():
            print(f"  {name}: {content}")

def display_ascii_art():
    ascii_art = r"""
  _____  _____  ________   _________ ____  
 |  __ \|  __ \|  ____\ \ / /__   __/ __ \ 
 | |__) | |__) | |__   \ V /   | | | |  | |
 |  ___/|  _  /|  __|   > <    | | | |  | |
 | |    | | \ \| |____ / . \   | | | |__| |
 |_|    |_|  \_\______/_/ \_\  |_|  \____/ 
"""
    print(Fore.MAGENTA + ascii_art)
    time.sleep(0.5)
    print(Style.RESET_ALL)

def main():
    display_ascii_art()
    while True:
        print(f"\n{Fore.YELLOW}Main Menu:")
        print("1. Get My Own IP Address")
        print("2. Get IP Address of a Domain")
        print("3. Scrape Data from a Domain")
        print("4. Get IP Address and Scrape Data from a Domain")
        print("5. Exit")
        choice = input("Select an option (1, 2, 3, 4, or 5): ")

        if choice == '1':
            private_ip = get_private_ip()
            public_ip = get_public_ip()
            print(f"\n{Fore.GREEN}Private IP: {private_ip}")
            if public_ip:
                print(f"{Fore.GREEN}Public IP: {public_ip}")
            else:
                print(f"{Fore.RED}Could not retrieve public IP.")
        elif choice == '2':
            domain = input("Enter the domain to get the IP (e.g., example.com): ")
            ip = get_ip(domain)
            if ip:
                print(f"\n{Fore.GREEN}The IP address of {domain} is {ip}")
            else:
                print(f"{Fore.RED}Could not retrieve IP for {domain}.")
        elif choice == '3':
            domain = input("Enter the domain to scrape data from (e.g., example.com): ")
            data = scrape_data(domain)
            if data:
                display_ip_and_data("", data)
            else:
                print(f"{Fore.RED}Could not scrape data for {domain}.")
        elif choice == '4':
            domain = input("Enter the domain to get the IP and scrape data from (e.g., example.com): ")
            ip = get_ip(domain)
            data = scrape_data(domain)
            if ip:
                print(f"\n{Fore.GREEN}The IP address of {domain} is {ip}\n")
            if data:
                display_ip_and_data(ip, data)
            else:
                print(f"{Fore.RED}Could not retrieve IP and/or scrape data for {domain}.")
        elif choice == '5':
            print(f"\n{Fore.YELLOW}Exiting...")
            time.sleep(1)
            break
        else:
            print(f"{Fore.RED}Invalid option. Please try again.")

    print(f"{Fore.CYAN}\nConnect with me on X: https://x.com/messino_james")
    print(f"{Fore.CYAN}Check out my GitHub: https://github.com/Prexto")

if __name__ == "__main__":
    main()
