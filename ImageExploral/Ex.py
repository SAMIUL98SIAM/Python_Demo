from PIL import Image
siam = Image.open('Siam_edit.png')
bg = Image.open('Diego.jpg')
bg.paste(siam,(0,0),siam)
bg.show()