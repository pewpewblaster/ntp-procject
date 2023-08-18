import requests

new_partner_data = {
    "New Logistic Company": {
        "address": "123 Main St, City",
        "contact_number": "+123 456 7890",
        "contact_mail": "info@newlogistic.com"
    }
}

response = requests.post("https://127.0.0.1:443/api/logistic_partners", json=new_partner_data, verify=False)
print(response.json())