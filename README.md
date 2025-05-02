# 🔍 SQL Injection Scanner

A lightweight Python script to detect basic SQL Injection vulnerabilities in HTML forms.

## 🧰 Requirements

```
pip install requests beautifulsoup4
```

## 🚀 Usage

```
python sql_injection_scanner.py
```

You will be prompted to:

```
Enter Your User-Agent Here: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Paste the URL to be checked: http://example.com
```

## 🧪 Example Output

```
[+] Detected 2 forms on http://example.com
[+] Submitting malicious payload to http://example.com/login
[-] No SQL Injection vulnerability detected in form at: http://example.com/login
[+] Submitting malicious payload to http://example.com/register
[!] SQL Injection vulnerability detected in form at: http://example.com/register
```

## 🔒 Disclaimer

```
⚠️ For educational and authorized testing purposes only.
Unauthorized use on websites you do not own or have permission to test is illegal.
```

## 📁 File Structure

```
sql_injection_scanner.py   # Main scanner script
README.md                  # Project documentation
```


