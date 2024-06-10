import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

print(f"Pandas Version: {pd.__version__}")
print(f"NumPy Version: {np.__version__}")

model=Sequential([
    Dense(units=32, activation='relu', input_dim=5),
    Dense(units=64),
    Dense(units=32),
    Dense(units=1, activation='tanh')
])

model.compile(optimizer='adam', loss='mse')
print(model.summary())