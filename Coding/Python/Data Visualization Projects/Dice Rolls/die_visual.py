"""Visually plotting dice rolls"""
from dice import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()


results = [die_1.roll() + die_2.roll() for _ in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

frequencies = [results.count(value) for value in poss_results]

title = "Resaults of Rolling two d6 dice, 1,000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

fig.show()
