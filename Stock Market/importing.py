import pandas as pd

import matplotlib.pyplot as plt
tata_motors=pd.read_csv("TATAMOTORS.csv")
tata_steel=pd.read_csv("TATASTEEL.csv")
tcs=pd.read_csv("TCS.csv")
print(tata_motors.head())
print(tata_motors.shape)