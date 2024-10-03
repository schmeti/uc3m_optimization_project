import time
import math
import matplotlib.pyplot as plt
import numpy as np

# Parameters
speed = 0.01  # Speed of the train (fraction of track length per second)
station_position = 0  # Position of the station on the track (fraction of total track length)

# Define the track shape (here, as a circle)
def circular_track(t, radius=5):
    """Returns the x, y coordinates of the train given position t on a circular track"""
    angle = 2 * np.pi * t  # Convert fraction t to angle in radians
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    return x, y

# Function to draw the track and simulate the train moving
def simulate_train(track_function, total_time=20, num_steps=500):
    global station_position
    fig, ax = plt.subplots()
    track_length = 1  # Track length in modular terms (for now it's normalized to 1)
    
    for step in range(num_steps):
        ax.clear()

        # Current train position along the track (as a fraction of total length)
        train_position = (step * speed) % track_length

        # Get the train's coordinates from the track function
        x_train, y_train = track_function(train_position)

        # Get the station's coordinates from the track function
        x_station, y_station = track_function(station_position)

        # Draw the track (circular case)
        t_vals = np.linspace(0, 1, 500)
        track_x, track_y = zip(*[track_function(t) for t in t_vals])
        ax.plot(track_x, track_y, 'k-', label='Track')

        # Draw the train
        ax.plot(x_train, y_train, 'ro', label='Train')

        # Draw the station
        ax.plot(x_station, y_station, 'bo', label='Station')

        # Set axis limits and aspect ratio
        ax.set_xlim(-7, 7)
        ax.set_ylim(-7, 7)
        ax.set_aspect('equal')

        # Check if the train reaches the station
        if abs(train_position - station_position) < 0.02:  # station stop threshold
            plt.title("Train stopped at the station")
            plt.pause(2)  # simulate the stop at the station for 2 seconds
        else:
            plt.title("Train is moving")

        plt.legend()
        plt.pause(0.05)  # Update the plot every 0.05 seconds

# Running the simulation with a circular track
simulate_train(circular_track)
