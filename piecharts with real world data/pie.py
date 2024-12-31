import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd 

plt.style.use('fivethirtyeight')

data = pd.read_csv("survey_results_public1.csv")
AI_tools_name = data["AISearchDevHaveWorkedWith"].fillna("Dont use any AI tools")
AI_tools_counter = Counter()

for AI in AI_tools_name:
    AI_tools_counter.update(AI.split(";"))
    
AI_tools = []
no_of_people = []


AI_tools_counter_new = AI_tools_counter.most_common(6)
AI_tools_counter_new.pop(1)
explode =  [0.1, 0, 0, 0, 0]
for items in AI_tools_counter_new: 
    AI_tools.append(items[0])
    no_of_people.append(items[1])

plt.pie(no_of_people, labels = AI_tools, explode = explode, autopct = "%1.1f%%", shadow = True)
plt.title("Popularity of AI Tools according to the Annual Stack OverFlow Developers Survey of 2024")
plt.legend()
plt.show()