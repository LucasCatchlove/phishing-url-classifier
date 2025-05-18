import whois
from datetime import datetime
from ping3 import ping
import requests


ISO_8601_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
  

class UrlWhois:

    def __init__(self, url):
        self.url = url
        self.whoisInfo = whois.whois(url)

    def whois_features(self):
        return {
            "qty_nameservers": self.quantity_name_servers(),
            "time_domain_activation": self.days_since_domain_creation(),
            "time_domain_expiration": self.days_till_domain_expiration(),
            "time_response": self.response_time_seconds()
        }

    def quantity_name_servers(self):
        return len(whois.whois(self.url).name_servers)

    def days_since_domain_creation(self):
        current_date = datetime.now().date()
        creation_date = datetime.strptime(self.whoisInfo.creation_date, ISO_8601_DATE_FORMAT)
        return (current_date - creation_date).days
    
    def days_till_domain_expiration(self):
        current_date = datetime.now().date()
        expiration_date = datetime.strptime(self.whoisInfo.expiration_date, ISO_8601_DATE_FORMAT)
        delta = (expiration_date - current_date).days
        return delta if len(delta) else 0
    
    def response_time_seconds(self):
        try:
            response = requests.get(self.url)
            return response.elapsed.total_seconds()

        except:
            print(f"Error retrieving {self.url}: {e}")
            
            
            
w = UrlWhois("https://google.ca")

w.response_time_seconds()

k=2