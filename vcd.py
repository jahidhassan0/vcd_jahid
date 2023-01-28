import argparse
import matplotlib.pyplot as plt

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Time-based simulation of aquaplaning braking distance.')

# Add arguments
parser.add_argument('--velocity', type=float, default=20, help='Initial velocity of the vehicle (m/s)')
parser.add_argument('--time', type=int, default=10, help='Duration of the simulation (s)')
parser.add_argument('--water_depth', type=float, default=0.1, help='Depth of the water on the road (m)')
parser.add_argument('--static_friction', type=float, default=0.05, help='Coefficient of static friction')
parser.add_argument('--dynamic_friction', type=float, default=0.1, help='Coefficient of dynamic friction')

# Parse the command-line arguments
args = parser.parse_args(['--velocity', '20', '--time', '10'])

# Extract the values of the arguments
velocity = args.velocity
time = args.time
water_depth = args.water_depth
static_friction = args.static_friction
dynamic_friction = args.dynamic_friction
g = 9.8 #m/s^2

#initialize time, distance and velocity lists
times = []
distances = []
velocities = []

#calculate deceleration and distance
for t in range(1, time+1):
    deceleration = g*(static_friction + (dynamic_friction - static_friction)*(1 - (water_depth/velocity)*t))
    d = velocity*t + 0.5*deceleration*t**2
    v = max(velocity + deceleration*t,0)
    times.append(t)
    distances.append(d)
    velocities.append(v)

# Plot the results
plt.figure()
plt.subplot(211)
plt.plot(times, distances, 'bo-', label='Distance')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()

plt.subplot(212)
plt.plot(times, velocities, 'ro-', label='Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()

plt.show()
