# Importing necessary libraries
from matplotlib.animation import FuncAnimation  # For creating animations
import random  # For generating random numbers
from itertools import count  # For creating an infinite counter
import matplotlib.pyplot as plt  # For plotting

# Setting a style for the plot for better aesthetics
plt.style.use("fivethirtyeight")

# Initializing values for the first line ("Our Dedication")
x1_values = [0]  # X-axis values start with 0
y1_values = [0]  # Y-axis values start with 0
x1 = count()  # Infinite counter for generating x1 values

# Initializing values for the second line ("Negativity and Distractions")
x2_values = [0]  # X-axis values start with 0
y2_values = [0]  # Y-axis values start with 0
x2 = count()  # Infinite counter for generating x2 values

# Defining the function to update the plot for each frame
def animation(i):
    """
    Updates the data and re-renders the plot for each animation frame.
    
    Args:
        i: The frame index (automatically handled by FuncAnimation).
    """
    # Adding the next x1 value (incrementing by 1 automatically)
    x1_values.append(next(x1))
    
    # Generating a random positive increment for "Our Dedication"
    increment1 = random.randint(1, 10)
    y1_values.append(y1_values[-1] + increment1)  # Adding the increment to the last y1 value
    
    # Adding the next x2 value (matches x1 values)
    x2_values.append(next(x1))
    
    # Generating a random positive increment and slightly reducing it for "Negativity and Distractions"
    increment2 = random.randint(1, 10)
    y2_values.append(y1_values[-1] + increment2 - 7)  # Adjusts increment to simulate distractions
    
    # Clearing the previous plot to avoid overlapping
    plt.cla()
    
    # Plotting the first line: "Our Dedication"
    plt.plot(x1_values, y1_values, label="Our Dedication")
    
    # Plotting the second line: "Negativity and Distractions"
    plt.plot(x2_values, y2_values, color="orange", label="Negativity and Distractions")
    
    # Adding axis labels
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    
    # Adding a legend in the upper left corner
    plt.legend(loc="upper left")

# Creating the animation object
ani = FuncAnimation(
    plt.gcf(),  # Gets the current figure
    animation,  # Function to call for updating the plot
    interval=1000  # Interval between updates in milliseconds (1 second)
)

# Adjusting the layout to prevent clipping of elements
plt.tight_layout()

# Displaying the animated plot
plt.show()
