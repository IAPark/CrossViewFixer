from SimpleCV import Image, Display
import training_set


def is_cross_view(url):
    image = Image(url)
    image = image.scale(200.0/image.width)
    left = image.crop(0, 0, image.width/2, 300)
    right = image.crop(image.width/2, 0, image.width/2, 300)
    motion = left.findMotion(right)
    dx = 0
    for m in motion:
        dx += m.dx * 3
    print(len(motion))
    return dx / float(len(motion))


wrong = 0
sum_wrong = 0
sum_right = 0
attempted = 0
'''
for u in training_set.p:
    dx = is_cross_view(u)
    if dx > 0:
        wrong += 1
        sum_wrong += dx
        print(u + " doesn't compute right")
    else:
        sum_right += dx
'''
for u in training_set.c:
        dx = is_cross_view(u)
        attempted += 1
        if dx < 0:
            wrong += 1
            sum_wrong += dx
            print(u + " doesn't compute right")
        else:
            sum_right += dx


print(float(wrong)/attempted)
print(sum_right/(attempted - float(wrong)))
print(sum_wrong/float(wrong))
