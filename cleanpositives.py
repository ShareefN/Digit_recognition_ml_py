import cv2
import os
from tkinter import *

path = 'data/positives'

for f in os.listdir(path):
    for i in os.listdir(f'{path}/{f}'):
        window = Tk()
        img = cv2.imread(f'{path}/{f}/{i}')

        # cv2.imshow(f'{path}/{f}/{i}', img)
        window.title(f'{path}/{f}/{i}')
        btn=Button(window, text="This is Button widget")
        btn.place(x=80, y=100)
        window.geometry("300x200+10+20")
        window.mainloop()

        # if cv2.waitKey(0) & 0xff == ord('q'):
        #     pass


def remove_image(path):
    print(f'remove this {path}')
