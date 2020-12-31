from PIL import Image
import base64

image = Image.open("output.png")
im = image.load()
(width, height) = image.size

result = ""
for y in range(0, height):
    c = ""
    for x in range(0, width):
        if im[x, y] == (0,0,0):
            c+="0"
        else:
            c+="1"
    result += chr(int(c, 2))

print("b64 " + result)
print("text " + base64.b64decode(result).decode("utf8"))
