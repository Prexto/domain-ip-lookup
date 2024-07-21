import socket
import requests
from bs4 import BeautifulSoup

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

def basic_scraping(domain):
    urls = [f"http://{domain}", f"https://{domain}"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Added a timeout to handle slow responses
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title
            title = soup.title.string if soup.title else 'No title found'
            
            # Extract all headings
            headings = {f'h{i}': [tag.text.strip() for tag in soup.find_all(f'h{i}')] for i in range(1, 7)}
            
            # Extract all paragraphs
            paragraphs = [p.text.strip() for p in soup.find_all('p')]
            
            # Extract all links
            links = [a['href'] for a in soup.find_all('a', href=True)]
            
            # Extract all images
            images = [img['src'] for img in soup.find_all('img', src=True)]
            
            # Extract all meta tags
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
            print(f"Could not scrape the website {url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while scraping {url}: {e}")
    
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
                data = basic_scraping(domain)
                if data:
                    print(f"Title: {data['title']}")
                    print("Headings:")
                    for tag, texts in data['headings'].items():
                        print(f"  {tag}: {', '.join(texts)}")
                    print("Paragraphs:")
                    for paragraph in data['paragraphs']:
                        print(f"  {paragraph}")
                    print("Links:")
                    for link in data['links']:
                        print(f"  {link}")
                    print("Images:")
                    for image in data['images']:
                        print(f"  {image}")
                    print("Meta Tags:")
                    for name, content in data['metas'].items():
                        print(f"  {name}: {content}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
