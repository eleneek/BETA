import winsound
import ctypes
gun1 = winsound.PlaySound('9_mm_gunshot-mike-koenig-123',winsound.SND_FILENAME)
ctypes.windll.user32.MessageBoxW(0, "9 mm gunshot was found!", "Your title", 1)
gun2 = winsound.PlaySound('40_smith_wesson_single-mike-koenig',winsound.SND_FILENAME)
ctypes.windll.user32.MessageBoxW(0, "40 smith wesson was found!", "Your title", 1)
gun3 = winsound.PlaySound('380_gunshot',winsound.SND_FILENAME)
ctypes.windll.user32.MessageBoxW(0, "12 Ga Winchester shotgun was found!", "Your title", 1)
gun4 = winsound.PlaySound('380_gunshot_single-mike-koenig',winsound.SND_FILENAME)
ctypes.windll.user32.MessageBoxW(0, "380 gunshot was found!", "Your title", 1)
flute= winsound.PlaySound('flute',winsound.SND_FILENAME)
ctypes.windll.user32.MessageBoxW(0, "Flute sound was found!", "Your title", 1)
drums = winsound.PlaySound('drums',winsound.SND_FILENAME)
ctypes.windll.user32.MessageBoxW(0, "Drums sound was found!", "Your title", 1)