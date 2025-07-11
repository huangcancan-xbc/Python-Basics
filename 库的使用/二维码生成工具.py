import qrcode
img = qrcode.make('https://gitee.com/huang-cancan-xbc')
img.save('qrcode.png')