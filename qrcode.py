import pyqrcode

qrcode_formats =  qrcode.provided_barcodes

def qrcode():
    url = pyqrcode.create('http://youtube.com')
    q = pyqrcode.create(input())
    q.png('hello.png',scale=6)
    print('new QW code Generated!')

if __name__ == '__main__':
    qrcode()