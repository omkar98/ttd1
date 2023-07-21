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
          'authtoken': '16202e94375972563f5f563e2647eb58b690c22d-1245772922',
          'content-type': 'application/json',
          'cookie': '_ga=GA1.5.1068875658.1682002300; _gid=GA1.5.1199907862.1689691573; _ga=GA1.1.1068875658.1682002300; _gat_UA-56816637-81=1; user_id=9441154; authtoken=16202e94375972563f5f563e2647eb58b690c22d-1245772922; valid_till=2024-07-21 10:24:32; valid_till_in_utc=2024-07-21 04:54:32; mobileNum=8669175196; _ga_MT8JLQ6M96=GS1.1.1689913461.25.1.1689913479.0.0.0',
          'referer': 'https://online.tirupatibalaji.ap.gov.in/accommodation/slot-booking?flow=acc&flowIdentifier=acc',
          'userid': '9441154'
        }
      proceed = True
      try:
          for x in range(6):
            response = requests.request("GET", url, headers=headers, data=payload)
            logger.warning("response: "+str(response) + "Status Code is: "+str(response.status_code))
            if response.status_code != 200:
                proceed = False
                
      except:
        proceed = False
        logger.critical("ERROR from TTD")
      if(proceed and not response.json().get('status') == 'fail'):
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
