import numpy as np
import matplotlib.pyplot as plt

# Parámetros
f = float(input("Introduce la frecuencia en Hz: "))  # Frecuencia en Hz
t = np.linspace(0, 1, 1000)  # Tiempo en segundos (0 a 1s con 1000 muestras)
A = 1  # Amplitud

# Onda senoidal
x_t = A * np.sin(2 * np.pi * f * t)

# Visualización
plt.plot(t, x_t)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title(f"Onda senoidal con frecuencia {f} Hz")
plt.grid()
plt.show()
