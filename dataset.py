
import numpy as np
import pandas as pd

# Dictionary to Define Features and Class Values
data = {
    'meal_consumption': ['Ate', 'Fasted'],
    'satiety_level': ['Full', 'Hungry'],
    'nutritional_value': ['Healthy', 'Unhealthy'],
    'enticement_level': ['Tasty', 'Unenticing'],
    'choice': ['Dessert', 'Water']
}

# Creates Empty DataFrame
dataframe = pd.DataFrame(columns=data.keys())

np.random.seed(88)
# Create 10,000 random instance with for loop
observations = 10000                # number of observations
for i in range(observations):
    dataframe.loc[i, 'meal_consumption'] = str(
                            np.random.choice(data['meal_consumption'], 1)[0])
    dataframe.loc[i, 'satiety_level'] = str(
                            np.random.choice(data['satiety_level'], 1)[0])
    dataframe.loc[i, 'nutritional_value'] = str(
                            np.random.choice(data['nutritional_value'], 1)[0])
    dataframe.loc[i, 'enticement_level'] = str(
                            np.random.choice(data['enticement_level'], 1)[0])
    dataframe.loc[i, 'choice'] = str(np.random.choice(data['choice'], 1)[0])



# Store dataframe as txt
try:
    with open('dessertdataframe.txt', 'a') as f1:
        dataframeAsString = dataframe.to_string(header = False, index = False)
        f1.write(dataframeAsString)
except:
    print('Writing to file f1 failed.')

# Read the file back in
df= open('dessertdataframe.txt', 'r')



