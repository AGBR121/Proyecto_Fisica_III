import numpy as np
import matplotlib.pyplot as plt
import os

def generar_dataset(carpeta, n=500):
    os.makedirs(carpeta + "/MAS", exist_ok=True)
    os.makedirs(carpeta + "/MAA", exist_ok=True)

    t = np.linspace(0, 10, 300)

    for i in range(n):
        A = np.random.uniform(1, 3)
        w = np.random.uniform(1, 3)
        phi = np.random.uniform(0, np.pi)

        # -------- MAS --------
        x_mas = A * np.cos(w * t + phi)
        plt.figure(figsize=(6, 3))
        plt.plot(t, x_mas, linewidth=2, color='blue')

        # Ejes X y Y
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)

        # Quitar todo lo demás
        plt.axis('off')  # quita números y bordes
        plt.box(False)   # sin marco

        plt.savefig(f"{carpeta}/MAS/mas_{i}.png", bbox_inches='tight', pad_inches=0)
        plt.close()

        # -------- MAA --------
        gamma = np.random.uniform(0.1, 0.5)
        x_maa = A * np.exp(-gamma * t) * np.cos(w * t + phi)
        plt.figure(figsize=(6, 3))
        plt.plot(t, x_maa, linewidth=2, color='red')

        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.axis('off')
        plt.box(False)

        plt.savefig(f"{carpeta}/MAA/maa_{i}.png", bbox_inches='tight', pad_inches=0)
        plt.close()

generar_dataset("dataset", 500)
