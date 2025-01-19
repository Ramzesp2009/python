import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import numpy as np

abtastrate, werte = wf.read("C:\\Users\\Umschueler\\tada.wav")
print(f"Abrastrate: {abtastrate} Werte / sec.")
print("Anzahl Werte:", werte.shape[0])
lehgth = werte.shape[0] / abtastrate
print(f"Lange: {round(lehgth, 2)} sec.")

zeit = np.linspace(0, lehgth, werte.shape[0])
plt.plot(zeit, werte[:, 0], label="Links")
plt.plot(zeit, werte[:, 1], label="Rechts")
# plt.legend("Hier ist Legend")
plt.xlabel("sec.")
plt.ylabel("Amplitude")
plt.show()
