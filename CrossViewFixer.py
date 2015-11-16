from SimpleCV import Image, Display
import training_set
from converter import CV
from SimpleCV import Display



def showMotion(right, left):
    right.show()
    motion = left.findMotion(right, window=right.width/5)
    print(len(motion))
    motion.draw(width=3)


wrong = 0
sum_wrong = 0
sum_right = 0
attempted = 0

for u in training_set.p:
    right, left = CV.split(u)
    print(u)
    dx = CV.is_cross_view(right, left)
    attempted += 1
    if not dx:
        wrong += 1
        sum_wrong += dx
        print(u + " doesn't compute right")
    else:
        sum_right += dx
    dx = CV.is_cross_view(left, right)
    attempted += 1
    if dx:
        wrong += 1
        sum_wrong += dx
        print(u + " doesn't compute right inverted")
    else:
        sum_right += dx

if wrong == 0:
    print("everything was right")
    wrong = 1E-200
print(float(wrong)/attempted)
