import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Create a session and set the user-agent
session = requests.Session()
user_agent = input("Enter Your User-Agent Here: ")
session.headers["User-Agent"] = user_agent

# Function to get all forms from a page
def get_forms(url):
    res = session.get(url)
    soup = BeautifulSoup(res.content, "html.parser")  # fixed typo from "html.pasrse"
    return soup.find_all("form")

# Function to extract form details
def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({
            "type": input_type,
            "name": input_name,
            "value": input_value
        })

    details['action'] = action
    details['method'] = method
    details['inputs'] = inputs
    return details

# Function to detect possible SQLi vulnerability
def is_vulnerable(response):
    errors = {
        "quoted string not properly terminated",
        "unclosed quotation mark after the character string",
        "you have an error in your sql syntax"
    }
    content = response.content.decode().lower()
    return any(error in content for error in errors)

# Main function to test forms for SQLi
def scan_sql_injection(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        details = get_form_details(form)
        for c in "\"'":
            data = {}
            for input in details["inputs"]:
                if input["type"] == "hidden" or input["value"]:
                    data[input["name"]] = input["value"] + c
                elif input["type"] != "submit":
                    data[input["name"]] = f"test{c}"

            target_url = urljoin(url, details["action"])
            print(f"[+] Submitting malicious payload to {target_url}")
            if details["method"] == "post":
                res = session.post(target_url, data=data)
            else:
                res = session.get(target_url, params=data)

            if is_vulnerable(res):
                print(f"[!] SQL Injection vulnerability detected in form at: {target_url}")
            else:
                print(f"[-] No SQL Injection vulnerability detected in form at: {target_url}")

if __name__ == "__main__":
    target_url = input("Paste the URL to be checked: ")
    scan_sql_injection(target_url)
    
