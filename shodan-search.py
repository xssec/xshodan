#!/usr/bin/env python3
import shodan
import sys
import os
import requests
import json
import argparse
from colorama import Fore, Style
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

API_KEY = os.getenv('SHODAN_API_KEY')
api = shodan.Shodan(API_KEY)


def fetch_cve_info(cve_id):
    url = f'https://cvedb.shodan.io/cve/{cve_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        cve_info = response.json()
        return cve_info

    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Error fetching CVE info for {cve_id}: {e}{Style.RESET_ALL}')
        return None


def main():
    parser = argparse.ArgumentParser(description='Shodan search script with CVE fetching and JSON output options.')
    parser.add_argument('query', metavar='QUERY', type=str, help='Search query for Shodan')
    parser.add_argument('--fetch-cve', action='store_true', help='Option to fetch CVE information')
    parser.add_argument('--output', type=str, help='Output JSON file to store results')

    args = parser.parse_args()
    query = args.query
    fetch_cve = args.fetch_cve
    output_file = args.output

    try:
        result = api.search(query)
        dataList = []

        for service in result['matches']:
            ip_str = service.get('ip_str', 'N/A')
            hostnames = service.get('hostnames', [])
            product = service.get('product', 'N/A')
            ports = service.get('port', 'N/A')
            os = service.get('os', 'N/A')
            info = service.get('info', 'N/A')
            snmp = service.get('snmp', 'N/A')
            timestamp = service.get('timestamp', 'N/A')
            org = service.get('org', 'N/A')
            domains = service.get('domains', [])
            transport = service.get('transport', 'N/A')
            vulns = service.get('vulns', [])

            cves = []
            if fetch_cve:
                cves = [fetch_cve_info(cve_id) for cve_id in vulns if fetch_cve_info(cve_id)]

            dataList.append({
                'ip': ip_str,
                'hostnames': ', '.join(hostnames) if hostnames else 'N/A',
                'organization': org,
                'info': info,
                'snmp': snmp,
                'product': product,
                'os': os if os else 'N/A',
                'domains': ', '.join(domains) if domains else 'N/A',
                'ports': ports if ports else 'N/A',
                'transport': transport,
                'vulns': ', '.join(vulns) if vulns else 'N/A',
                'cves': cves,
                'timestamp': timestamp
            })

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(dataList, f, indent=4, ensure_ascii=False)
            print(f'{Fore.GREEN}Results saved to {output_file}{Style.RESET_ALL}')
        else:
            print(json.dumps(dataList, indent=4, ensure_ascii=False))

    except shodan.APIError as e:
        print(f'{Fore.RED}Error: {e}{Style.RESET_ALL}')
        sys.exit(1)


if __name__ == '__main__':
    main()
