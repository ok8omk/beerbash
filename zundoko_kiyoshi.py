#coding: UTF-8
import random
import time

zundoko = [ 'ズン', 'ドコ' ]

while True:
    song = ''
    song += zundoko[random.randint(0, 1)] + '・'
    song += zundoko[random.randint(0, 1)] + ' '
    song += zundoko[random.randint(0, 1)] + ' '
    song += zundoko[random.randint(0, 1)] + ' '
    song += zundoko[random.randint(0, 1)] + ' '
    time.sleep(0.5)
    if song == 'ズン・ズン ズン ズン ドコ ':
        song += 'キヨシ！'
        print song
        break
    else:
        print song
