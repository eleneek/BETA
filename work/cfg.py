import os
class Config:
    def __init__(self, mode = 'conv',nfilt = 26, nfft = 512, rate = 16000):
        self.mode = mode
        self.nfilt = nfilt
        self.rate = rate
        self.nfft = nfft
        self.step = int(rate/10)
        self.model_path = os.path.join('models',
                                       mode + ".model")
        self.p_path = os.path.join('pickles', mode + '.p')

