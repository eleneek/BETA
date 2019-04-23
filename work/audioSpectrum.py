import thinkplot
import thinkdsp
gun = thinkdsp.read_wave("gun10.wav")
gun.plot()
#gun_spec = gun.make_spectrum()
#gun_spec.plot()
thinkplot.show()
