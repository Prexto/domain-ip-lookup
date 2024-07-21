# Domain to IP Resolver

This script resolves the IP address of a given domain name. It handles domains with or without the 'www.' prefix and ignores 'http://' and 'https://' prefixes.

## Features

- Resolves domain names to their IP addresses.
- Handles domains with or without 'www.' prefix.
- Ignores 'http://' and 'https://' prefixes.
- Continues to run in a loop until '3' is entered to exit.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/Prexto/domain-ip-lookup.git
    ```

2. Navigate to the directory:

    ```bash
    cd domain-ip-lookup
    ```

3. Run the script:

    ```bash
    python main.py
    ```

4. Enter a domain name (e.g., `example.com`) to get its IP address. Type `0` to exit the script.

## Example

1. **Get my own IP address**:
    ```
    Main Menu:
    1. Get my own IP address
    2. Get IP address of a domain
    3. Exit
    Select an option (1, 2, or 3): 1
    Your IP address is 192.168.1.2
    ```

2. **Get IP address of a domain**:
    ```
    Main Menu:
    1. Get my own IP address
    2. Get IP address of a domain
    3. Exit
    Select an option (1, 2, or 3): 2
    Enter the domain to get the IP (e.g., example.com): example.com
    The IP of www.example.com is 93.184.216.34
    ```

3. **Exit**:
    ```
    Main Menu:
    1. Get my own IP address
    2. Get IP address of a domain
    3. Exit
    Select an option (1, 2, or 3): 3
    Exiting...
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Prexto - [https://github.com/Prexto](https://github.com/Prexto)
