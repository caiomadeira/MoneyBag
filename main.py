from pprint import pprint
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from DataModel import DataModel
from TempList import mouth, internet

# cuidado ao plotar numeros em string pois muda o resultado grafico
model = DataModel(xdata=mouth, ydata=internet)
data = model.joinData()

size = (14, 8)
pprint(f"dict returned: {data}", width=80)
plt.suptitle = "Internet spending (2022)"
fig, ax = plt.subplots()

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.2f}'.format(x)))

plt.bar(data.keys(), data.values())
plt.grid(axis='y', linestyle='-')

# plt.scatter(data.keys(), data.values())
plt.show()
