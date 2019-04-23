from tkinter import *
import winsound
gun1 = winsound.PlaySound('9_mm_gunshot-mike-koenig-123',winsound.SND_FILENAME)
root = Tk()
root.title("Response")
T = Text(root, height=20, width=60)  #to change font and size font=("Helvetica", 20)
T.pack()
T.insert(END, "9 mm gunshot was found!")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()


gun2 = winsound.PlaySound('40_smith_wesson_single-mike-koenig',winsound.SND_FILENAME)
root = Tk()
root.title("Response")
T = Text(root, height=20, width=60)
T.pack()
T.insert(END, "40 smith wesson was found!")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()

gun3 = winsound.PlaySound('380_gunshot',winsound.SND_FILENAME)
root = Tk()
root.title("Response")
T = Text(root, height=20, width=60)
T.pack()
T.insert(END, "12 Ga Winchester shotgun was found!")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()


gun4 = winsound.PlaySound('380_gunshot_single-mike-koenig',winsound.SND_FILENAME)
root = Tk()
root.title("Response")
T = Text(root, height=20, width=60)
T.pack()
T.insert(END, "380 gunshot was found!")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()


flute= winsound.PlaySound('flute',winsound.SND_FILENAME)
root = Tk()
root.title("Response")
T = Text(root, height=20, width=60)
T.pack()
T.insert(END, "Flute sound was found!")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()



drums = winsound.PlaySound('drums',winsound.SND_FILENAME)
root = Tk()
root.title("Response")
T = Text(root, height=20, width=60)
T.pack()
T.insert(END, "Drums sound was found!")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()
