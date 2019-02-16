# -*- coding: utf-8 -*-

import wave
import numpy as np
from matplotlib import pyplot as plt
import struct

a = 1 #ふり幅
fs = 8000 #サンプリング周波数
f0 = 261.63 #周波数
sec = 5

swav = []

for n in np.arange(fs * sec):
    #正弦曲線の生成
    s = a * np.sin(2.0 * np.pi * f0 * n / fs)
    swav.append(s)

#正弦曲線を描画
plt.plot(swav[0:100])
plt.show()

swav = [int(x * 32767.0) for x in swav]

#バイナリ化
binwave = struct.pack("h" * len(swav), *swav)

#正弦曲線をwavfileとして書き出し
w = wave.Wave_write("output.wav")
p = (1,2,8000,len(binwave), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(binwave)
w.close()