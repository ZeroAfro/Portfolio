"""Visually plotting dice rolls"""

from dice import Die
import plotly.express as px


# Create two dice
die_1 = Die()
die_2 = Die()

# Roll the dice 1,000 times and store results
results: list[int] = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyze the frequency of each possible result
max_result = die_1.num_sides + die_2.num_sides
poss_results: range = range(2, max_result + 1)
frequencies: list[int] = [results.count(value) for value in poss_results]

# Create bar chart
title = "Results of Rolling two d6 dice, 1,000 times"
labels: dict[str, str] = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Format and display chart
fig.update_layout(xaxis_dtick=1)
fig.show()
