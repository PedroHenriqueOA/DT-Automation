import glob
import os
import pandas as pd
from pandas import DataFrame

powerBI = pd.read_excel(r"C:\Users\peuh1\Downloads\SOLICITAÇÕES.xlsx")

print(powerBI.loc[1, "Solicitados"])
