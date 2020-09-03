import sounddevice as sd


wave_length = 5
sample_rate = 16000
print("rec start!!")
data = sd.rec(int(wave_length * sample_rate), sample_rate, channels=1)
sd.wait()



data


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")




x = np.arange(0.01, 100)
f = np.log(x)

plt.plot(x, f)
plt.ylabel("percentage")
plt.xlabel("PH")
plt.show()



z = 1.0 + 2.0j
u = 2.0 + 3.0j

print(z)
print(u)

print(np.real(z))
print(np.imag(z))


print(np.conjugate(z))
print(np.abs(z))


v = z + u
print(v)


print(z - u)


print(z * u)


print(z/u)


import wave as wave
import pyroomacoustics as pa


pa.datasets.CMUArcticCorpus(basedir="./CMU_ARCTIC", download=True, speaker=["aew", "axb"])


sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
data = wav.readframes(wav.getnframes())
wav.close()


wav.getframerate()





import scipy.signal as sp

sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
data = wav.readframes(wav.getnframes())
wav.close()

data = np.frombuffer(data, dtype=np.int16)

f, t, stft_data = sp.stft(
    data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256
)

print("after stft, shape: ", np.shape(stft_data))
print(f"{f} [Hz]")
print(f"{t} [sec]")


fig = plt.figure(figsize=(10, 8))

spectrum, freqs, t, im = plt.specgram(
    data, NFFT=512, noverlap=512/16*15, Fs=wav.getframerate()
)

fig.colorbar(im).set_label("Instensity [dB]")
plt.xlabel("Time [Sec]")
plt.ylabel("Frequency [Hz]")
plt.show()


t, data_post = sp.istft(stft_data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256)
data_post = data_post.astype(np.int16)

wave_out = wave.open("./istft_post_wave.wav", "w")
wave_out.setnchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(wav.getframerate())
wave_out.writeframes(data_post)
wave_out.close()
wav.close()


# 特定の周波数を消した音を再生する

stft_data[100:, :] = 0
t, data_post = sp.istft(
    stft_data, fs=wav.getframerate(), window="hann", nperseg=512, noverlap=256
)

data_post = data_post.astype(np.int16)
sd.play(data_post, wav.getframerate())
print("play start")
status = sd.wait()
wav.close()



