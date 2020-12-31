from PIL import Image
import base64

def padding(arr):
    curr=0
    l=[]
    for i in arr:
        if len(i) > curr:
            curr = len(i)
    for i in arr:
        l.append(i.rjust(curr, '0'))
    return l
text = input("text: ")
text = base64.b64encode(text.encode("utf8")).decode("utf8")
print(text)
binary_text = list(format(ord(x), 'b') for x in text)
binary_text = padding(binary_text)
print(binary_text)

width = len(binary_text[0])
height = len(binary_text)

image = Image.new("RGB", (width, height), (0,0,0))
im = image.load()

for y in range(0, height):
    bb = list(binary_text[y])
    for x in range(0, width):
        if bb[x] == "1":
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)

        im[x, y] = color

image.save("output.png")
