import cv2
import numpy as np

# test_img = np.zeros((512, 512, 3), dtype = "uint8")
# cv2.imshow("test", test_img)
# cv2.waitKey(0)

print(7 // 3)
print(7 /  3)
print(7 %  3)

for i in range(1,10):
    print(i)

print(len([0]))

a = [1]
b = [2]
print(a+b)
a = [1,24,3,45,5,6,7,78,9,10]
print(a[4:], a[:4])

print(a[:4]+a[4:])
print(np.shape(a[4:]))
print(np.concatenate(a[:4]+a[4:]))