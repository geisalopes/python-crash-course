from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("Chapter 16/weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract hight and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title("Daily Hight and Low Temperatures, 2021", fontsize=22)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
