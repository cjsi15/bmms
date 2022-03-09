import pyqrcode

a="https://www.pornhub.com/"

url=pyqrcode.create(a)
url.svg("static/images/qrcode.svg",scale=4)
