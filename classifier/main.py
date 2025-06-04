from url_to_classify import UrlToClassify

print("***************************************\nphishing url classifier 0.0.1-pre-alpha\n***************************************\n")
url_str = input("paste the url to verify here: ")

url = UrlToClassify(url_str)

pred = url.is_phishing()

print("phishing") if pred[0] else print("safe")

