import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.scatter(
    x_values, y_values, c=y_values, cmap=plt.cm.magma, s=10
)  # cor teal color=(0.2, 0.8, 0.7)

# Set chart title and label axes.
ax.set_title("Square Number", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")

plt.show()
