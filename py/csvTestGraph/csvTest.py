import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("./NZX.NZ.csv")

# print(data["Adj Close"])

date = data.Date[0:15]
openVal = data.Open[0:15]
high = data.High[0:15]
low = data.Low[0:15]
close = data.Close[0:15]
adjClose = data["Adj Close"][0:15]
volume = data.Volume[0:15]

for x in range(0, 1):
    print(" Date: " + date[x] + "\n",
          "Open: " + str(openVal[x]) + "\n",
          "High: " + str(high[x]) + "\n",
          "Low: " + str(low[x]) + "\n",
          "Close: " + str(close[x]) + "\n",
          "Vol: " + str(volume[x]) + "\n")

# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

y = []
for i in np.arange(0, openVal.max() + 1):
    y.append(i)
    print(y)
x = np.arange(len(date[0:8]))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 1, openVal[0:8], width, label='Open', color="r")
rects2 = ax.bar(x + width / 3, high[0:8], width, label='High', color="g")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Values')
ax.set_title('Open Close Values')
#ax.set_yticks(y)
#ax.set_yticklabels((y))
ax.set_xticks(x)
ax.set_xticklabels((date[0:8]))
ax.legend()

ax.bar_label(rects1, padding=20, color="r")
ax.bar_label(rects2, padding=10, color="g")

plt.ylim(0,2)

fig.autofmt_xdate()
fig.tight_layout()

plt.show()
