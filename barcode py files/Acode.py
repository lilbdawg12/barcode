import qrcode
img = qrcode.make('QRCode Printed!!')
type(img)
count = 0
while(count + img< 10):
    count = count + img +1
    print('new Img')
img.save = str(input('type qrcode link here'))
img.save('hello.png')


#work in progress

#           goal is to get a working program, to produce 
#           QRCodes from a click of a button
#   