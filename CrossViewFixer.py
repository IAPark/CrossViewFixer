from SimpleCV import Image, Display

disp = Display()


image = Image("https://c2.staticflickr.com/8/7508/16283544985_9875dac79d_b.jpg")

image = image.scale(250.0/image.width)

left = image.crop(0, 0, image.width/2, image.height)
right = image.crop(image.width/2, 0, image.width/2, image.height)
motion = left.findMotion(right)

dx = 0
for m in motion:
    dx += m.dx

print(dx)


first = True

while disp.isNotDone():
        if disp.leftButtonDown:
                first = not first
        if first:
            left.save(disp)
        else:
            right.save(disp)
