# -*- coding = utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = 'logger.txt'
data = pd.read_table(file, sep=" ", header=None)
print(data)
