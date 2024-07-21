# Domain IP and Data Scraper

This Python script provides functionalities to get the IP address of a domain and perform basic web scraping to extract detailed information from the website.

## Features

- Get your own IP address.
- Get the IP address of a specified domain.
- Perform basic web scraping on a specified domain.
- Get the IP address and perform web scraping on a specified domain.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Prexto/domain-ip-lookup.git
    cd domain-ip-lookup
    ```

2. Install the required libraries:

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

Run the script:

```bash
python main.py
```

Main Menu
Get my own IP address:

This option will display your own IP address.
Get IP address of a domain:

Enter a domain name (e.g., example.com) to get its IP address.
Scrape data from a domain:

Enter a domain name (e.g., example.com) to scrape data from the website. This includes:

Title
Headings ```(<h1> to <h6>)```
Paragraphs
Links
Images
Meta tags
Get IP address and scrape data from a domain:

Enter a domain name (e.g., example.com) to get its IP address and scrape data from the website.

Exit:

Exit the script.

## Example
1. **Get my own IP address**
```
Main Menu:
1. Get my own IP address
2. Get IP address of a domain
3. Scrape data from a domain
4. Get IP address and scrape data from a domain
5. Exit
Select an option (1, 2, 3, 4, or 5): 1
Your IP address is 192.168.1.2
```


2. **Get IP address of a domain**:
```
Main Menu:
1. Get my own IP address
2. Get IP address of a domain
3. Scrape data from a domain
4. Get IP address and scrape data from a domain
5. Exit
Select an option (1, 2, 3, 4, or 5): 2
Enter the domain to get the IP (e.g., example.com): example.com
The IP of www.example.com is 93.184.216.34
```

3. **Scrape data from a domain**:
```
Main Menu:
1. Get my own IP address
2. Get IP address of a domain
3. Scrape data from a domain
4. Get IP address and scrape data from a domain
5. Exit
Select an option (1, 2, 3, 4, or 5): 3
Enter the domain to scrape data from (e.g., example.com): example.com
Title: Example Domain
Headings:
  h1: Example Domain
Paragraphs:
  This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.
Links:
  http://www.iana.org/domains/example
Images:
Meta Tags:
```

4. **Get IP address and scrape data from a domain**:
```
Main Menu:
1. Get my own IP address
2. Get IP address of a domain
3. Scrape data from a domain
4. Get IP address and scrape data from a domain
5. Exit
Select an option (1, 2, 3, 4, or 5): 4
Enter the domain to get the IP and scrape data from (e.g., example.com): example.com
The IP of www.example.com is 93.184.216.34
Title: Example Domain
Headings:
  h1: Example Domain
Paragraphs:
  This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.
Links:
  http://www.iana.org/domains/example
Images:
Meta Tags:
```

5. **Exit**:
```
Main Menu:
1. Get my own IP address
2. Get IP address of a domain
3. Scrape data from a domain
4. Get IP address and scrape data from a domain
5. Exit
Select an option (1, 2, 3, 4, or 5): 5
Exiting...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Prexto - [https://github.com/Prexto](https://github.com/Prexto)
