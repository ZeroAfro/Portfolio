import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate a random walk
rw = RandomWalk()
rw.fill_walk()

# Set plot style
plt.style.use("classic")
fig, ax = plt.subplots()

# Plot the points in the walk
point_numbers = range(rw.num_points)
ax.scatter(
    rw.x_values,
    rw.y_values,
    c=point_numbers,
    cmap=plt.cm.Blues,
    edgecolors="none",
    s=5,
)

# Emphasize the start and end points
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Remove axes and fix aspect ratio
ax.set_aspect("equal")
ax.scatter(0, 0, c="green", edgecolors="none", s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

# Show plot
plt.show()
