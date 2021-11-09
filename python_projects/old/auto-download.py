import urllib.request
name="kot.jpg"
def download(url):
    urllib.request.urlretrieve(url,name)
download("https://memepedia.ru/wp-content/uploads/2018/06/kto-prochital-tot-sdohnet.jpg")
