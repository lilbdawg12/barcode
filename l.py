import pyqrcode


def qrcode():
    q = pyqrcode.create(input())
    q.png('qrcode.png',scale=6)
    url = pyqrcode.create('http://uca.edu')
    print('new QW code Generated!')

if __name__ == '__path__':
    qrcode()