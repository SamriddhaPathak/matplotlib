# Importing necessary libraries
import matplotlib.pyplot as plt  # For creating visualizations
import pandas as pd  # For data manipulation and analysis
from collections import Counter  # For counting occurrences of items in data

# Applying a pre-defined style for better aesthetics of the plots
plt.style.use('fivethirtyeight')

# Initializing a Counter object to count the occurrences of IDEs
ide_counter = Counter()

# Reading survey data from a CSV file
data = pd.read_csv("survey_results_public.csv")  # Make sure the file is in the correct path

# Extracting the column related to collaborative tools and filling missing values with an empty string
ide_data = data["NEWCollabToolsHaveWorkedWith"].fillna("")

# Iterating through the data and updating the counter
# Splitting the data in each row by ';' to handle multiple tools listed together
for items in ide_data:
    ide_counter.update(items.split(";"))

# Getting the 10 most common IDEs/tools from the Counter object
ide_counter_NEW = ide_counter.most_common(10)

# Printing the most common tools for verification/debugging
print(ide_counter_NEW)

# Initializing lists to store the IDE names and their respective counts
number_of_people = []  # Stores the number of people using each IDE/tool
ide_number = []  # Stores the names of the IDEs/tools

# Iterating through the most common tools to populate the lists
for response in ide_counter_NEW:
    print(response)  # Print each response for debugging/verification
    ide_number.append(response[0])  # Append the IDE/tool name
    number_of_people.append(response[1])  # Append the count of users

# Reversing the lists to align the bar chart from smallest to largest (for horizontal bars)
number_of_people.reverse()
ide_number.reverse()

# Creating a horizontal bar chart to visualize the popularity of IDEs/tools
plt.barh(ide_number, number_of_people)  # Plotting IDE names on the y-axis and their counts on the x-axis

# Adding labels and title to the chart
plt.xlabel("Number of People")  # Label for the x-axis
plt.title("IDE's Popularity from the Annual Stack Overflow Survey of 2023")  # Title of the chart

# Adjusting the layout to prevent clipping of elements
plt.tight_layout()

# Displaying the plot
plt.show()
