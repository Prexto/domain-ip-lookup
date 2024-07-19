# Domain IP Lookup

This script resolves the IP address of a given domain name. It handles domains with or without the 'www.' prefix and ignores 'http://' and 'https://' prefixes.

## Features

- Resolves domain names to their IP addresses.
- Handles domains with or without 'www.' prefix.
- Ignores 'http://' and 'https://' prefixes.
- Continues to run in a loop until '0' is entered to exit.

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

Enter the domain to get the IP (or 0 to exit): example.com
The IP of www.example.com is 93.184.216.34

Enter the domain to get the IP (or 0 to exit): 0
Exiting...


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Prexto - [https://github.com/Prexto](https://github.com/Prexto)
