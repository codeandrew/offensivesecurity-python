
import requests

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

domain_list = "subdomains.txt" 
#"https://raw.githubusercontent.com/codeandrew/SecLists/master/Miscellaneous/subdomain-list.txt"
target_url = raw_input("Enter Target URL: \n")

discovered_subdomain_list = []

with open(domain_list, 'r') as wordlist_file:
    for line in wordlist_file:
        full_url = "{}.{}".format(line.strip(), target_url)
        response = request(full_url)
        if response:
            print("[+] Discovered subdomain --> {}".format(full_url))
            discovered_subdomain_list.append(full_url)


with open("{}-subdomains.txt".format(target_url), 'w') as f:
    for item in discovered_subdomain_list:
        print >> f, item
        