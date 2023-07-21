import smtplib
import logging 
import requests
import json
import time

counter = 1

logging.basicConfig()

if __name__ == "__main__":
    logger = logging.getLogger("Syslog")
    logger.warning("Inside Main")
    while True:
      url = "https://online.tirupatibalaji.ap.gov.in/sdn/rest/v1/acc/get_availability?for=dashboard&location=TIRUMALA"
      payload={}
      headers = {
        'authority': 'online.tirupatibalaji.ap.gov.in',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'authtoken': 'dbe994e5459905930a8884e16e49892d16288f31639199834',
        'content-type': 'application/json',
        'cookie': '_ga=GA1.5.834326753.1670903926; _gid=GA1.5.2036348688.1684908791; _gid=GA1.3.1408227557.1685176566; _ga=GA1.1.834326753.1670903926; user_id=9441154; authtoken=dbe994e5459905930a8884e16e49892d16288f31639199834; valid_till=2026-05-27 14:37:08; valid_till_in_utc=2026-05-27 09:07:08; mobileNum=8669175196; _gat_UA-56816637-81=1; _ga_MT8JLQ6M96=GS1.1.1685176570.16.1.1685176693.0.0.0',
        'referer': 'https://online.tirupatibalaji.ap.gov.in/accommodation/slot-booking?flow=acc&flowIdentifier=acc',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
        'userid': '9441154'
      }
      try:
        response = requests.request("GET", url, headers=headers)
        logger.warning("Response"+str(response.status_code)) 
      except:
        logger.critical("ERROR from TTD") 
      if(response.status_code == 200 and not response.json().get('status') == 'fail'):
        avl1 = (response.json().get('result').get('20230723').get('avl'))
        avl2 = 0
        if (avl1==0): 
          avl2 = (response.json().get('result').get('20230724').get('avl'))
        if (avl1>0):
          message = 'Subject: {}\n\n{}'.format(json.dumps(response.json().get('result').get('20230723')), "TIRUMALA - Available for 23 July")
        if (avl2>0):
          message = 'Subject: {}\n\n{}'.format(json.dumps(response.json().get('result').get('20230724')), "TIRUMALA - Available for 24 July")
        if(avl1>0 or avl2>0):
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
        time.sleep(5)
        counter+=1
        logger.warning("counter: "+str(counter)+" | Available23: "+str(avl1)+" | Available24: "+str(avl2) ) 
        if counter == 300:
          counter = 1
          s = smtplib.SMTP('smtp.gmail.com', 587)
          s.starttls()
          s.login("edu.omkar@gmail.com", "cxkgerjsjtutairg")
          s.sendmail("sender_email_id", "edu.omkar1@gmail.com", "Subject: Service is Up")
          logger.warning("Service Up Email is sent") 
          s.quit()
