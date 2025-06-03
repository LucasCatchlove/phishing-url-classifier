from url_to_classify import UrlToClassify

url_str = "https://www.google.com/"

url = UrlToClassify(url_str)

pred = url.is_phishing()

print(pred)