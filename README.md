# xshodan

This repository contains a Python script to search Shodan, optionally fetch CVE information, and output the results either to the console or a JSON file.

## Features

- Search Shodan using a query.
- Optionally fetch CVE information for vulnerabilities.
- Output results to the console or save to a JSON file.

## Requirements

- Python 3.x
- `requests` library
- `shodan` library
- `python-dotenv` library
- `colorama` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/xssec/xshodan.git
   cd xshodan

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required libraries:
   ```bash
   pip install requests shodan python-dotenv colorama

4. Create a .env file in the root of the project and add your Shodan API key:
   ```bash
   echo 'SHODAN_API_KEY=your_shodan_api_key'>.env

## Usage

### Basic Search
To perform a basic search and print the results to the console:
```bash
./shodan-search.py <search query>
```

### Search with CVE Information
To perform a search, fetch CVE information, and print the results to the console:
```bash
./shodan-search.py <search query> --fetch-cve
```

### Save Results to JSON File
To perform a search, optionally fetch CVE information, and save the results to a JSON file:
```bash
./script_name.py <search query> [--fetch-cve] --output <output_file>
```
### Example Output
Example output when running the script:
```json
[
    {
        "ip": "8.8.8.8",
        "hostnames": "dns.google",
        "organization": "Google LLC",
        "info": "N/A",
        "snmp": "N/A",
        "product": "N/A",
        "os": "N/A",
        "domains": "google.com",
        "ports": 53,
        "transport": "udp",
        "vulns": "CVE-2014-1234, CVE-2016-5678",
        "cves": [
            {
                "id": "CVE-2014-1234",
                "description": "Example vulnerability description",
                "references": [
                    "https://example.com/CVE-2014-1234"
                ]
            },
            {
                "id": "CVE-2016-5678",
                "description": "Another example vulnerability description",
                "references": [
                    "https://example.com/CVE-2016-5678"
                ]
            }
        ],
        "timestamp": "2024-05-30T10:00:00Z"
    }
]
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author
xssec
