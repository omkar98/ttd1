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
  url = "https://online.tirupatibalaji.ap.gov.in/sdn/rest/v1/acc/get_availability?for=dashboard&location=TIRUMALA"
  payload={}
  headers = {
      'authority': 'online.tirupatibalaji.ap.gov.in',
      'accept': 'application/json',
      'authtoken': '16202e94375972563f5f563e2647eb58b690c22d-1245772922',
      'content-type': 'application/json',
      'cookie': '_ga=GA1.5.1068875658.1682002300; _gid=GA1.5.1199907862.1689691573; _ga=GA1.1.1068875658.1682002300; _gat_UA-56816637-81=1; user_id=9441154; authtoken=16202e94375972563f5f563e2647eb58b690c22d-1245772922; valid_till=2024-07-21 10:24:32; valid_till_in_utc=2024-07-21 04:54:32; mobileNum=8669175196; _ga_MT8JLQ6M96=GS1.1.1689913461.25.1.1689913479.0.0.0',
      'referer': 'https://online.tirupatibalaji.ap.gov.in/accommodation/slot-booking?flow=acc&flowIdentifier=acc',
      'userid': '9441154',
      'User-Agent': 'request'
    }
  proceed = True
  try:
      for x in range(6):
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.warning("response: "+str(response) + "Status Code is: "+str(response.status_code))
        print(response.text)
        if response.status_code != 200:
            proceed = False
  except:
    proceed = False
    logger.critical("ERROR from TTD")
