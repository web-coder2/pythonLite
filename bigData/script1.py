import pandas as pd
import numpy as np 

indexes = ["asd", "zxc", "one", "two", "op op op"]
ser1 = pd.Series([12, -6, 0.8, 23, -24.5], index = indexes)

print(ser1)
print(ser1.index)
ser1["op op op"] = 100500
print(ser1)

positiveSer1 = ser1[ser1 > 0]
print(positiveSer1)

print(np.sqrt(positiveSer1))

itData = {
	"python": 100,
	"javascript": 190,
	"java": 70,
	"c++": 90
}

serIt = pd.Series(itData)
serIt.name = "comunity"
serIt.index.name = "LP"

print(serIt[serIt > 80])
print(serIt.isnull())
print(serIt.notnull())