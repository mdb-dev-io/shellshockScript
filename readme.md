# Shellshock Exploitation Script

## Introduction
This Python script was developed as a practical tool to understand and demonstrate the exploitation of the Shellshock vulnerability in web applications. It was specifically created to complement the learning experience within the "Attacking Common Applications" module on Hack The Box Academy. The script allows for automated sending of HTTP requests with headers containing the Shellshock payload, aimed at vulnerable CGI scripts on web servers.
- https://nvd.nist.gov/vuln/detail/CVE-2014-6271
- I know it's an old vulnerability.....

## Purpose
The primary purpose of this script is educational. It serves as a hands-on tool for penetration testers and security enthusiasts to get a better grasp of the Shellshock vulnerability by testing and observing its impact in a controlled environment.

## Features
- Sends customized HTTP requests with Shellshock payloads in headers.
- Supports sending requests through a proxy for traffic inspection.
- Saves responses from the server in a specified output file for analysis.

## Prerequisites
- Python 3.x
- `requests` library installed in Python (`pip install requests`)

## Setup
1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed and accessible from your command line or terminal.
3. Install the `requests` library using pip if you haven't already:

   ```bash
   pip install requests
   ```

4. Prepare a text file (`headers.txt`) with the headers you want to test. Each header should be on a new line, without the payload.

## Usage
Run the script from your command line or terminal, specifying the headers file, the target URL, and optionally a proxy:

```bash
python shellshockExploit.py -w headers.txt -url http://<target-url> -p http://127.0.0.1:8080
```

- `-w` or `--wordlist`: Path to the wordlist file containing header names.
- `-url`: The target URL where the vulnerable CGI script is hosted.
- `-p` or `--proxy` (optional): Proxy URL to inspect the traffic (e.g., for use with Burp Suite or similar tools).

After execution, check the `responses.txt` file for the outcomes of each request.

## Disclaimer
This script is intended for educational purposes and authorized penetration testing only. Always seek explicit permission before testing any system. Misuse of this script can result in significant consequences, including legal action.

## Acknowledgments
This script was inspired by the educational content provided by Hack The Box Academy, particularly the "Attacking Common Applications" module. Special thanks to the cybersecurity community for continuous learning and knowledge sharing.
```
