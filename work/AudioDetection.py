from tkinter import Tk

from thinker import *
import thinker.messagebox

root = Tk()
thinker.messagebox.showinfo("Window Title", "Hello Georgia,there we go!")
root.mainloop()





















"""
import winsound
gun1 = winsound.PlaySound('9_mm_gunshot-mike-koenig-123',winsound.SND_FILENAME)
file_to_open = open("Response.txt", "a")
file_to_open.write("%s\r\n" % "9 mm gunshot was found!")
file_to_open.close()
print("9 mm gunshot was found!")

gun2 = winsound.PlaySound('40_smith_wesson_single-mike-koenig',winsound.SND_FILENAME)
print("40 smith wesson was found!")
file_to_open = open("Response.txt", "a")
file_to_open.write("%s\r\n" % "9 mm gunshot was found!")
file_to_open.close()

gun3 = winsound.PlaySound('380_gunshot',winsound.SND_FILENAME)
print("380 gunshot was found!")
file_to_open = open("Response.txt", "a")
file_to_open.write("%s\r\n" % "9 mm gunshot was found!")
file_to_open.close()

gun4 = winsound.PlaySound('380_gunshot_single-mike-koenig',winsound.SND_FILENAME)
print("12 Ga Winchester shotgun was found!")
file_to_open = open("Response.txt", "a")
file_to_open.write("%s\r\n" % "9 mm gunshot was found!")
file_to_open.close()

flute= winsound.PlaySound('flute',winsound.SND_FILENAME)
print("Flute sound was playing!")
file_to_open = open("Response.txt", "a")
file_to_open.write("%s\r\n" % "9 mm gunshot was found!")
file_to_open.close()

drums = winsound.PlaySound('drums',winsound.SND_FILENAME)
print("Drums was found!")
file_to_open = open("Response.txt", "a")
file_to_open.write("%s\r\n" % "9 mm gunshot was found!")
file_to_open.close()
"""


#from scipy.io import  wavfile
"""
fs, data1 = wavfile.read('9_mm_gunshot-mike-koenig-123.wav')
fs, data2 = wavfile.read('9_mm_gunshot-mike-koenig-123.wav')
fs, data3 = wavfile.read('40_smith_wesson_single-mike-koenig.wav')
fs, data4 = wavfile.read('40_smith_wesson_single-mike-koenig.wav')
fs, data5 = wavfile.read('380_gunshot.wav')
fs, data6 = wavfile.read('380_gunshot.wav')
fs, data7 = wavfile.read('380_gunshot_single-mike-koenig.wav')
fs, data8 = wavfile.read('380_gunshot_single-mike-koenig.wav')
"""

"""
total = 1
for i in label_list:
    file_to_open.write("%i)%s\r\n" % (total,i))
    total +=1
file_to_open.close()
"""

"""
if data1.all() == data2.all():
    file_to_open = open("Response.txt","w")
    file_to_open.writelines("9 mm gunshot was found!")
    file_to_open.close()
if data3.all() == data4.all():
    file_to_open = open("Response.txt", "w")
    file_to_open.writelines("40 smith wesson was found!")
    file_to_open.close()
if data5.all() == data6.all():
    file_to_open = open("Response.txt", "w")
    file_to_open.writelines("380 gunshot was found!")
    file_to_open.close()
if data7.all() == data8.all() :
    file_to_open = open("Response.txt", "w")
    file_to_open.writelines("12 Ga Winchester shotgun was found!")
    file_to_open.close()
else:
    file_to_open = open("Response.txt", "w")
    file_to_open.writelines("Gunshot sound was not found!")
    file_to_open.close()
"""





