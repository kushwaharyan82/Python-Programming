import matplotlib.pyplot as plt

subjects = ["Python", "DSA", "SQL", "ML", "AI"]
study_hours = [5, 3, 2, 4, 3]

plt.pie(
    study_hours,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Study Time Distribution")

plt.show()
