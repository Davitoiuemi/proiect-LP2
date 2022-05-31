# apelam biblioteciile necesare

import numpy as np
from scipy import signal as sg
import matplotlib.pyplot as plt
freq = 2
amp = 2
time = np.linspace(0, 2, 1000)
signal1 = amp*np.sin(2*np.pi*freq*time)
plt.plot(time, signal1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
signal2 = amp*sg.square(2*np.pi*freq*time, duty=0.3)
plt.figure(figsize=(10,4))
plt.plot(time, signal2)
plt.xlabel('in2array_likeTime (s)')
plt.ylabel('Amplitude')
plt.show()

import pylops
from pylops.utils.wavelets import ricker
#incepem prin a creea un semnal 0 al lungimii nt si vom plasa un semnal unitar in centru
nt = 1001
dt = 0.004
t = np.arange(nt) * dt
x = np.zeros(nt)
x[int(nt / 2)] = 1
h, th, hcenter = ricker(t[:101], f0=30)

Cop = pylops.signalprocessing.Convolve1D(nt, h=h, offset=hcenter, dtype="float32") # am ctreat pentry operatorul pyplos
y = Cop * x

xinv = Cop / y

fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.plot(t, x, "k", lw=2, label=r"$x$")
ax.plot(t, y, "r", lw=2, label=r"$y=Ax$")
ax.plot(t, xinv, "--g", lw=2, label=r"$x_{ext}$")
ax.set_title("Convolve 1d data", fontsize=14, fontweight="bold")
ax.legend()
ax.set_xlim(1.9, 2.1)


Cop = pylops.signalprocessing.Convolve1D(nt, h=h, offset=hcenter - 3, dtype="float32")
y = Cop * x
y1 = Cop.H * x
xinv = Cop / y

fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.plot(t, x, "k", lw=2, label=r"$x$")
ax.plot(t, y, "r", lw=2, label=r"$y=Ax$")
ax.plot(t, y1, "b", lw=2, label=r"$y=A^Hx$")
ax.plot(t, xinv, "--g", lw=2, label=r"$x_{ext}$")
ax.set_title(
    "Convolve 1d data with non-zero phase filter", fontsize=14, fontweight="bold"
)
ax.set_xlim(1.9, 2.1)
ax.legend()
plt.show()
