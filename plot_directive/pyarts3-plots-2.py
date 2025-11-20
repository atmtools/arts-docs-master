import matplotlib.pyplot as plt
import pyarts3 as pyarts

cia = pyarts.arts.ArrayOfCIARecord([pyarts.arts.CIARecord.fromxml("cia/O2-CIA-O2.xml")])
f, a = pyarts.plots.ArrayOfCIARecord.plot(cia, fig=plt.figure(figsize=(12, 6)))
a.set_yscale("log")
a.set_xlabel("Frequency [Hz]")
a.set_ylabel("Absorption [1/m]")
a.set_title("O$_2$-O$_2$ Collision-induced absorption")