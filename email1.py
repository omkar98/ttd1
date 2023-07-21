import requests
import json

url = "https://online.tirupatibalaji.ap.gov.in/cms/api/notifications"

payload = {}
headers = {
  'authority': 'online.tirupatibalaji.ap.gov.in',
  'accept': 'application/json',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'content-type': 'application/json',
  'cookie': '_ga=GA1.5.1068875658.1682002300; _gid=GA1.5.1199907862.1689691573; _gat_UA-56816637-81=1; _gid=GA1.3.508613201.1689916322; _gat=1; _ga=GA1.1.1068875658.1682002300; _ga_MT8JLQ6M96=GS1.1.1689916320.26.1.1689916347.0.0.0',
  'referer': 'https://online.tirupatibalaji.ap.gov.in/home/dashboard',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
