import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Generate galaxy data
num_stars = 10000
num_arms = 4
arm_separation = 2 * np.pi / num_arms

def generate_spiral_galaxy(num_stars, num_arms):
    arms = np.random.randint(0, num_arms, num_stars)
    r = np.random.power(0.5, num_stars) * 20  # Use power distribution for radial distance
    theta = arms * arm_separation + np.random.normal(0, 0.2, num_stars)
    theta += 0.5 * r  # This creates the spiral shape
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.random.normal(0, 0.1 * np.exp(-r/10), num_stars)  # Thinner at the edges
    return x, y, z

x, y, z = generate_spiral_galaxy(num_stars, num_arms)

# Set up the plot
scatter = ax.scatter(x, y, z, c=z, cmap='coolwarm', s=2, alpha=0.8)
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_zlim(-5, 5)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

# Remove axis labels and ticks
ax.set_axis_off()

# Animation update function
def update(frame):
    angle = np.radians(frame)
    x_new = x * np.cos(angle) - y * np.sin(angle)
    y_new = x * np.sin(angle) + y * np.cos(angle)
    scatter._offsets3d = (x_new, y_new, z)
    ax.view_init(30, frame)
    return scatter,

# Create the animation
anim = FuncAnimation(fig, update, frames=np.linspace(0, 360, 180), 
                     interval=50, blit=False)

plt.tight_layout()
plt.show()