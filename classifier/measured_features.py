import ssl
import dns
import ipwhois
import whois
from datetime import datetime
import requests
import socket
from url_parse_utils import split_url_into_sections

ISO_8601_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
  
class MeasuredFeatures:

    def __init__(self, url):
        self.url = url
        self.whois = None
        self.domain, self.directory, self.file, self.parameters = split_url_into_sections(url)
        
    def get_measured_features(self):
        return {
            "qty_redirects": self.quantity_redirects(),
            "tls_ssl_certificate": self.has_tls_ssl_certificate(),
            "ttl_hostname": self.ttl_hostname(),
            "qty_mx_servers": self.quantity_mail_exchange_servers(),
            "qty_nameservers": self.quantity_name_servers(),
            "qty_ip_resolved": self.quantity_ip_resolved(),
            "time_domain_activation": self.days_since_domain_creation(),
            "time_domain_expiration": self.days_till_domain_expiration(),
            "time_response": self.response_time_seconds(),
            "asn_ip": self.get_asn_ip()
        }
        
    def quantity_name_servers(self):
        try:
            answers = dns.resolver.query(self.domain, 'NS')
            return len(answers) if answers else 0
        except Exception as e:
            print(f"Error when determining quantity of name servers (NS): {e}")

    def quantity_mail_exchange_servers(self):
        try:
            answers = dns.resolver.query(self.domain, 'MX')
            return len(answers) if answers else 0
        except Exception as e:
            print(f"Error when determining quantity of mail exchange servers (MX): {e}")

    def days_since_domain_creation(self):
        if not self.whois: 
            self.whois = whois.whois(self.url)
            
        current_date = datetime.now()
        creation_date = datetime.strptime(str(self.whois.creation_date[0]), ISO_8601_DATE_FORMAT)
        return (current_date - creation_date).days
    
    def days_till_domain_expiration(self):
        if not self.whois: 
            self.whois = whois.whois(self.url)
            
        current_date = datetime.now()
        expiration_date = datetime.strptime(str(self.whois.expiration_date[0]), ISO_8601_DATE_FORMAT)
        return (expiration_date - current_date).days
    
    def response_time_seconds(self):
        try:
            response = requests.head(self.url, allow_redirects=True, timeout=5)
            return response.elapsed.total_seconds()
        except Exception as e:
            print(f"Error when determining response time: {e}")
            
    def quantity_ip_resolved(self):
        try:
            ips = socket.gethostbyname_ex(self.domain)[2]
            return len(ips)
        except Exception as e:
            print(f"Error when determining quantity of IPs resolved: {e}")
            
    def get_ip_from_domain(self):
        try:
            return socket.gethostbyname(self.domain)
        except Exception as e:
            print(f"Error when determining IP address: {e}")
        
    def ttl_hostname(self):
        try:
            try:
                answers = dns.resolver.query(self.domain, 'A')
            except dns.resolver.NoAnswer:
                answers = dns.resolver.query(self.domain, 'AAAA')
            return answers.ttl if answers else 0
        except Exception as e:
            print(f"Error when determining ttl: {e}")
    
    def has_tls_ssl_certificate(self):
        hostname = self.domain
        try:
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    ssock.getpeercert()
                    return 1
        except Exception as e:
            print(f"Error when creating ssl context: {e}")
    
    def quantity_redirects(self):
        try:
            response = requests.get(self.url, allow_redirects=True, timeout=10)
            return len(response.history)
        except Exception as e:
            print(f"Error when determining quantity of redirects: {e}")
        
    def get_asn_ip(self):
        ip_address = self.get_ip_from_domain()
        try:
            obj = ipwhois.IPWhois(ip_address)
            results = obj.lookup_rdap()
            # Return ASN as integer
            return int(results.get('asn')) if results and results.get('asn') else -1
        except Exception as e:
            print(f"Error when determining ASN number: {e}")