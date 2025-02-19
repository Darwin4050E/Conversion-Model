import model as md
import numpy as np

celsius = float(input("Make a conversion! Enter a degree Celsius: "))
kelvin = md.model.predict(np.array([celsius]))

print(str(kelvin) + " degree Kelvin.")