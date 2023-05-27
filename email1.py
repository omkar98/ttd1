import smtplib


import requests
import json
import time

while True:
  url = "https://online.tirupatibalaji.ap.gov.in/sdn/rest/v1/acc/get_availability?for=dashboard&location=TIRUMALA"
  print(url)
  payload={}
  headers = {
    'authority': 'online.tirupatibalaji.ap.gov.in',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
    'authtoken': 'c55f2febd9afba21dcd8d4961eb41453edf40e531584038060',
    'content-type': 'application/json',
    'cookie': '_ga=GA1.5.834326753.1670903926; _gid=GA1.3.2036348688.1684908791; _gid=GA1.5.2036348688.1684908791; _ga=GA1.1.834326753.1670903926; user_id=2459287; authtoken=c55f2febd9afba21dcd8d4961eb41453edf40e531584038060; valid_till=2025-05-26 10:55:32; valid_till_in_utc=2025-05-26 05:25:32; mobileNum=7798576939; accesstype=; router=JPG; redirect_type=acc; flow_type=acc; _gat_UA-56816637-81=1; ticket_id=4916063; _ga_MT8JLQ6M96=GS1.1.1685076913.12.1.1685077307.0.0.0',
    'referer': 'https://online.tirupatibalaji.ap.gov.in/accommodation/slot-booking?flow=acc&flowIdentifier=acc',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
    'userid': '2459287'
  }
  print("now making request")
  try:
    response = requests.request("GET", url, headers=headers, data=payload)
  except:
    print("Error from TTD")
  print("made request")
  avl = (response.json().get('result').get('20230723').get('avl'))
  print(avl);
  message = 'Subject: {}\n\n{}'.format(json.dumps(response.json().get('result').get('20230723')), "Available for 23rd July")
  if(avl>=0):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("edu.omkar@gmail.com", "cxkgerjsjtutairg")



    # sending the mail
    s.sendmail("sender_email_id", "edu.omkar1@gmail.com", message)

    # terminating the session
    s.quit()
  time.sleep(10)
