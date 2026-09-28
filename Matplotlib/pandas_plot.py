import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [20, 35, 30, 45, 50, 65]
}

df = pd.DataFrame(data)

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
