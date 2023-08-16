

# pip install suds-jurko

import requests

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"


country_codes = {
    "Croatia": "HR",
    "United States": "US",
    "Canada": "CA",
    "Australia": "AU",
    "Great Britain": "GB",
    "China": "CN",
    "Japan": "JP",
    "Germany": "DE",
    "India": "IN",
    "France": "FR",
    "Brazil": "BR",
    "Italy": "IT",
    "South Korea": "KR",
    "Russia": "RU",
    "Spain": "ES",
    "Mexico": "MX",
    "Indonesia": "ID",
    "Netherlands": "NL",
    "Saudi Arabia": "SA",
    "Turkey": "TR",
    "Switzerland": "CH"
}

payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                  <sCountryISOCode>{country_codes['Croatia']}</sCountryISOCode>
                </CountryCurrency>
              </soap:Body>
            </soap:Envelope>
"""

# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# POST request
response = requests.request("POST", url, headers=headers, data=payload)
  
# prints the response
if response.status_code == 200:
    print(response.text)