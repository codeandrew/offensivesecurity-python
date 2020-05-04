
import requests

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

domain_list = "directories.txt" 
target_url = raw_input("Enter Target URL: \n")

discovered_path_list = []

with open(domain_list, 'r') as wordlist_file:
    for line in wordlist_file:
        full_url = "{}/{}".format(target_url(), line.strip())
        response = request(full_url)
        if response:
            print("[+] Discovered URL Path --> {}".format(full_url))
            discovered_path_list.append(full_url)


with open("{}-paths.txt".format(target_url), 'w') as f:
    for item in discovered_path_list:
        print >> f, item
        