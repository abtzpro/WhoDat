import requests
import argparse
import re

# Define the command line arguments
parser = argparse.ArgumentParser(description="OSINT framework")
parser.add_argument("target", help="Target URL or IP address")
parser.add_argument("-whois", action="store_true", help="Perform a WHOIS lookup")
parser.add_argument("-geoip", action="store_true", help="Perform a GeoIP lookup")
parser.add_argument("-reverse", action="store_true", help="Perform a reverse DNS lookup")
args = parser.parse_args()

# Define the regular expression for matching IP addresses
ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Define the functions for performing various lookups
def perform_whois_lookup(target):
  url = f"https://www.whois.com/whois/{target}"
  response = requests.get(url)
  if response.status_code == 200:
    content = response.text
    print(f"\nWHOIS lookup results for {target}:")
    print("-----------------------------")
    print(content)
  else:
    print(f"Failed to perform WHOIS lookup for {target}")

def perform_geoip_lookup(target):
  url = f"https://ipinfo.io/{target}/json"
  response = requests.get(url)
  if response.status_code == 200:
    content = response.json()
    print(f"\nGeoIP lookup results for {target}:")
    print("-----------------------------")
    for key, value in content.items():
      print(f"{key}: {value}")
  else:
    print(f"Failed to perform GeoIP lookup for {target}")

def perform_reverse_lookup(target):
  url = f"https://api.hackertarget.com/reverseiplookup/?q={target}"
  response = requests.get(url)
  if response.status_code == 200:
    content = response.text
    matches = re.findall(ip_regex, content)
    if len(matches) > 0:
      print(f"\nReverse DNS lookup results for {target}:")
      print("-----------------------------")
      for match in matches:
        print(match)
    else:
      print(f"No results found for {target}")
  else:
    print(f"Failed to perform reverse DNS lookup for {target}")

# Main program logic
if args.whois:
  perform_whois_lookup(args.target)
if args.geoip:
  perform_geoip_lookup(args.target)
if args.reverse:
  perform_reverse_lookup(args.target)
