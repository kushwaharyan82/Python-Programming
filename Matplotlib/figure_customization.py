import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 35, 30, 45, 50, 65]
profit = [10, 18, 15, 25, 30, 40]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Sales chart
axes[0].plot(months, sales, marker="o")
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Sales")

# Profit chart
axes[1].bar(months, profit)
axes[1].set_title("Monthly Profit")
axes[1].set_xlabel("Months")
axes[1].set_ylabel("Profit")

fig.suptitle("Sales and Profit Analysis")

plt.tight_layout()
plt.show()
