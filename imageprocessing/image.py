from PIL import Image , ImageFilter
img = Image.open('./image_folder/pikachu.jpg')
print(img)
print(img.mode)
print(img.format)
print(img.size)
print(img)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png','png')

img.thumbnail((200,200))
img.save('smooth.png','png')

