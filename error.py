import model as md
import matplotlib.pyplot as plt

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(md.record.history["loss"])