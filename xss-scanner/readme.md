# XSS-Scanner

## TARGET 

- https://hub.docker.com/r/vulnerables/web-dvwa
```

docker run --rm -it -p 80:80 vulnerables/web-dvwa
Username: admin
Password: password
```

- https://github.com/webpwnized/mutillidae-docker


## USAGE 

```python
# DVWA TARGET 
# docker run --rm -it -p 80:80 vulnerables/web-dvwa
target_url = "http://localhost" # DVWA
links_to_ignore = [
    'http://localhost/logout.php'
]

vuln_scanner = Scanner(url=target_url,ignore_links=links_to_ignore)
login = f"{target_url}/login.php"
token = vuln_scanner.extract_csrf_token(vuln_scanner.session, url=login)
dvwa_login = {
    "username": 'admin',
    "password": 'password',
    "Login": 'submit',
    "user_token": token
}
vuln_scanner.session.post(login, data=dvwa_login)

test_url = "http://localhost/vulnerabilities/xss_r/" 
forms = vuln_scanner.extract_forms(test_url)
print(forms) # LIST of forms

# response = vuln_scanner.submit_form(form=forms[0], value='testtest',url=test_url)
# print(response.text)

# EXPLOIT XSS in FORMS
# TEST for SINGLE FORM
response = vuln_scanner.test_xss_in_form(form=forms[0], url=test_url)
print(response)

# EXPLOIT XSS in LINK
# TEST FOR SINGLE LINK
response = vuln_scanner.test_xss_in_link(f"{test_url}?name=test")
print(response)

# Automated Discovery
vuln_scanner.crawl()
vuln_scanner.run_scanner()

```
![xss_scanner](./docs/xss-scanner.gif)