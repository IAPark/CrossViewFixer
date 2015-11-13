from SimpleCV import Image, Display
import training_set
from converter import CV


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
    right, left = CV.split(u)
    dx = CV.is_cross_view(right, left)
    attempted += 1
    if dx < 0:
        wrong += 1
        sum_wrong += dx
        print(u + " doesn't compute right")
    else:
        sum_right += dx

    dx = CV.is_cross_view(left, right)
    attempted += 1
    if dx > 0:
        wrong += 1
        sum_wrong += dx
        print(u + " doesn't compute right inverted")
    else:
        sum_right += dx

if wrong == 0:
    print("everything was right")
    wrong = 1E-200
print(float(wrong)/attempted)
print(sum_right/(attempted - float(wrong)))
print(sum_wrong/float(wrong))
