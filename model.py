import tensorflow as tf
import numpy as np

celsius = np.array([-20, -10, 0, 15, 23, 37, 42, 50, 75, 100], dtype = float)
kelvin = np.array([253.15, 263.15, 273.15, 288.15, 296.15, 310.15, 315.15, 323.15, 348.15, 373.15], dtype = float)

layer = tf.keras.layers.Dense(units = 1, input_shape = [1])
model = tf.keras.Sequential([layer])

model.compile(
    optimizer = tf.keras.optimizers.Adam(0.5),
    loss = 'mean_squared_error'
)

print("Training: ")
record = model.fit(celsius, kelvin, epochs = 2000, verbose = False)
print("Training complete.")