"""Data Analysis Notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cRlck9bHcLWpHJNXcyrPETZr4Z5KfCSK

##Air Quality
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('air_quality_Nov2017.csv')
df['Generated Date Time'] = pd.to_datetime(df['Generated'])
df['Year'] = df['Generated Date Time'].dt.year
air_quality_mapping = {"Good": 1, "Moderate": 2}
df['Air Quality'] = df['Air Quality'].map(air_quality_mapping)
average_air_quality = df.groupby('Year')['Air Quality'].mean().reset_index()
print(average_air_quality)



"""##Bus Stops"""

# Load your CSV data into a Pandas DataFrame
# Replace 'your_file.csv' with the actual filename
df = pd.read_csv('bus_stops.csv')

# Create a new column 'Day Bus Stops' with 0 as the initial value
df['Day Bus Stops'] = 0

# Create a new column 'Night Bus Stops' with 0 as the initial value
df['Night Bus Stops'] = 0

# Update the 'Day Bus Stops' column based on the 'Transport' column
df.loc[df['Transport'] == 'Day bus stop', 'Day Bus Stops'] = 1

# Update the 'Night Bus Stops' column based on the 'Transport' column
df.loc[df['Transport'] == 'Night bus stop', 'Night Bus Stops'] = 1

# Group by 'District.Name' and sum the 'Day Bus Stops' and 'Night Bus Stops'
result = df.groupby('District.Name')[['Day Bus Stops', 'Night Bus Stops']].sum().reset_index()

# Print the resulting DataFrame
print(result)

import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data into a Pandas DataFrame
# Replace 'your_file.csv' with the actual filename
df = pd.read_csv('bus_stops.csv')

# Create a new column 'Day Bus Stops' with 0 as the initial value
df['Day Bus Stops'] = 0

# Create a new column 'Night Bus Stops' with 0 as the initial value
df['Night Bus Stops'] = 0

# Update the 'Day Bus Stops' column based on the 'Transport' column
df.loc[df['Transport'] == 'Day bus stop', 'Day Bus Stops'] = 1

# Update the 'Night Bus Stops' column based on the 'Transport' column
df.loc[df['Transport'] == 'Night bus stop', 'Night Bus Stops'] = 1

# Group by 'District.Name' and sum the 'Day Bus Stops' and 'Night Bus Stops'
result = df.groupby('District.Name')[['Day Bus Stops', 'Night Bus Stops']].sum().reset_index()

# Plot the data
plt.figure(figsize=(12, 6))
plt.bar(result['District.Name'], result['Day Bus Stops'], label='Day Bus Stops')
plt.bar(result['District.Name'], result['Night Bus Stops'], label='Night Bus Stops', bottom=result['Day Bus Stops'])
plt.xlabel('District Name')
plt.ylabel('Number of Bus Stops')
plt.title('Number of Day and Night Bus Stops per District')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

"""##Immigrants by Nationality"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('immigrants_by_nationality.csv')

# Exclude the rows where Nationality is 'Spain'
df_filtered = df[df['Nationality'] != 'Spain']

# Group the data by nationality and sum the number of immigrants over the years
nationality_counts = df_filtered.groupby('Nationality')['Number'].sum()

# Sort the nationalities by the total number of immigrants in descending order
top_nationalities = nationality_counts.sort_values(ascending=False).head(20)

# Create a bar plot
plt.figure(figsize=(12, 6))
top_nationalities.plot(kind='bar')
plt.xlabel('Nationality')
plt.ylabel('Total Number of Immigrants')
plt.title('Top 20 Immigrant Nationalities (Excluding Spain) Over the Years')
plt.xticks(rotation=90)
plt.show()

df = pd.read_csv('immigrants_by_nationality.csv')

# Group the data by 'Year', 'District Name', and 'Nationality', and sum the 'Number' column
result = df.groupby(['Year', 'District Name', 'Nationality'])['Number'].sum().reset_index()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# Print the resulting DataFrame
print(result['Nationality'].unique())

import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data into a Pandas DataFrame
# Replace 'your_file.csv' with the actual filename
df = pd.read_csv('immigrants_by_nationality.csv')

# Create a dictionary to map each nationality to its region
nationality_to_continent = {
    'Afghanistan': 'Asia',
    'Albania': 'Europe',
    'Algeria': 'Africa',
    'Andorra': 'Europe',
    'Angola': 'Africa',
    'Argentina': 'South America',
    'Armenia': 'Asia',
    'Australia': 'Australia',
    'Austria': 'Europe',
    'Azerbaijan': 'Asia',
    'Bahrain': 'Asia',
    'Bangladesh': 'Asia',
    'Barbados': 'North America',
    'Belarus': 'Europe',
    'Belgium': 'Europe',
    'Benin': 'Africa',
    'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe',
    'Brasil': 'South America',
    'Bulgaria': 'Europe',
    'Burkina Faso': 'Africa',
    'Burundi': 'Africa',
    'Cambodja': 'Asia',
    'Camerun': 'Africa',
    'Canada': 'North America',
    'Cape Verde': 'Africa',
    'Central African Republic': 'Africa',
    'Chile': 'South America',
    'China': 'Asia',
    'Colombia': 'South America',
    'Congo': 'Africa',
    'Costa Rica': 'North America',
    'Croatia': 'Europe',
    'Cuba': 'North America',
    'Cyprus': 'Asia',
    'Czech Republic': 'Europe',
    'Denmark': 'Europe',
    'Djibouti': 'Africa',
    'Dominica': 'North America',
    'Dominican Republic': 'North America',
    'Ecuador': 'South America',
    'Egypt': 'Africa',
    'El Salvador': 'North America',
    'Equatorial Guinea': 'Africa',
    'Estonia': 'Europe',
    'Ethiopia': 'Africa',
    'Finland': 'Europe',
    'France': 'Europe',
    'Gabon': 'Africa',
    'Gambia': 'Africa',
    'Georgia': 'Asia',
    'Germany': 'Europe',
    'Ghana': 'Africa',
    'Greece': 'Europe',
    'Grenada': 'North America',
    'Guatemala': 'North America',
    'Guinea': 'Africa',
    'Guinea-Bissau': 'Africa',
    'Haiti': 'North America',
    'Honduras': 'North America',
    'Hungary': 'Europe',
    'Iceland': 'Europe',
    'India': 'Asia',
    'Indonesia': 'Asia',
    'Iran': 'Asia',
    'Iraq': 'Asia',
    'Ireland': 'Europe',
    'Israel': 'Asia',
    'Italy': 'Europe',
    'Ivory Coast': 'Africa',
    'Jamaica': 'North America',
    'Japan': 'Asia',
    'Jordan': 'Asia',
    'Kazakhstan': 'Asia',
    'Kenya': 'Africa',
    'Kuwait': 'Asia',
    'Kyrgyzstan': 'Asia',
    'Latvia': 'Europe',
    'Lebanon': 'Asia',
    'Libya': 'Africa',
    'Lithuania': 'Europe',
    'Luxembourg': 'Europe',
    'Macedonia': 'Europe',
    'Madagascar': 'Africa',
    'Malaysia': 'Asia',
    'Maldives': 'Asia',
    'Mali': 'Africa',
    'Malta': 'Europe',
    'Mauritania': 'Africa',
    'Mauritius': 'Africa',
    'Mexico': 'North America',
    'Moldova': 'Europe',
    'Mongolia': 'Asia',
    'Montenegro': 'Europe',
    'Morocco': 'Africa',
    'Mozambique': 'Africa',
    'Namibia': 'Africa',
    'Nepal': 'Asia',
    'Netherlands': 'Europe',
    'New Zealand': 'Australia',
    'Nicaragua': 'North America',
    'Nigeria': 'Africa',
    'No information': 'Unknown',
    'Norway': 'Europe',
    'Oman': 'Asia',
    'Pakistan': 'Asia',
    'Palestinian territories': 'Asia',
    'Panama': 'North America',
    'Paraguay': 'South America',
    'Peru': 'South America',
    'Philippines': 'Asia',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Qatar': 'Asia',
    'Romania': 'Europe',
    'Russia': 'Europe/Asia',
    'Rwanda': 'Africa',
    'Saint Kitts and Nevis': 'North America',
    'Saudi Arabia': 'Asia',
    'Senegal': 'Africa',
    'Serbia': 'Europe',
    'Seychelles': 'Africa',
    'Sierra Leone': 'Africa',
    'Singapore': 'Asia',
    'Slovakia': 'Europe',
    'Slovenia': 'Europe',
    'Somalia': 'Africa',
    'South Africa': 'Africa',
    'South Korea': 'Asia',
    'Spain': 'Europe',
    'Sri Lanka': 'Asia',
    'Sudan': 'Africa',
    'Swaziland': 'Africa',
    'Sweden': 'Europe' ,
    'Switzerland': 'Europe',
    'Syria': 'Asia',
    'Taiwan': 'Asia',
    'Tanzania': 'Africa',
    'Thailand': 'Asia',
    'Togo': 'Africa',
    'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa',
    'Turkey': 'Asia',
    'Turkmenistan': 'Asia',
    'Uganda': 'Africa',
    'Ukraine': 'Europe',
    'United Kingdom': 'Europe',
    'United States': 'North America',
    'Uruguay': 'South America',
    'Uzbekistan': 'Asia',
    'Venezuela': 'South America',
    'Vietnam': 'Asia',
    'Yemen': 'Asia',
    'Zimbabwe': 'Africa',
    'East Timor': 'Asia',
    'Guyana': 'South America',
    'Lesotho': 'Africa',
    'Liberia': 'Africa',
    'Myanmar': 'Asia',
    'Niger': 'Africa',
    'North Korea': 'Asia',
    'Puerto Rico': 'North America',
    'San Marino': 'Europe',
    'State of Palestine': 'Asia',
    'Suriname': 'South America',
    'São Tomé and Príncipe': 'Africa',
    'Tajikistan': 'Asia',
    'The Bahamas': 'North America',
    'United Arab Emirates': 'Asia',
    'Zambia': 'Africa',
    'Antigua and Barbuda': 'North America',
    'Botswana': 'Africa',
    'Chad': 'Africa',
    'Eritrea': 'Africa',
    'Laos': 'Asia',
    'Malawi': 'Africa',
    'Solomon Islands': 'Australia'
}

# Map each nationality to its corresponding region using the 'region_to_continent' dictionary
df['Region'] = df['Nationality'].map(nationality_to_continent)

# Group the data by 'Region', 'Year', and sum the 'Number' column
result = df.groupby(['Region', 'Year'])['Number'].sum().reset_index()

# Get a list of unique regions excluding 'Unknown'
regions = result[result['Region'] != 'Unknown']['Region'].unique()

# Create a line graph for each region with unique colors
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

# Define a list of unique colors
unique_colors = list(plt.cm.tab20(np.linspace(0, 1, len(regions))))

for i, region in enumerate(regions):
    region_data = result[result['Region'] == region]
    plt.plot(region_data['Year'], region_data['Number'], label=region, color=unique_colors[i], marker='o')

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Immigrant Population by Region Over Time')
plt.xticks(np.arange(min(result['Year']), max(result['Year'])+1, 1), rotation=45)


# Move the legend outside of the plot area and make it shorter
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, title='Regions')

# Show the plot
plt.show()

"""##Immigrants by Net Amount"""

# Load your CSV data into a Pandas DataFrame
# Replace 'your_file.csv' with the actual filename
df = pd.read_csv('immigrants_emigrants_by_sex.csv')

# Group the data by 'Year' and 'District Name', and sum the 'Immigrants' and 'Emigrants' columns
result = df.groupby(['Year', 'District Name'])[['Immigrants']].sum().reset_index()

# Calculate the net immigrants by subtracting 'Emigrants' from 'Immigrants'
result['Net Immigrants'] = result['Immigrants'] - df['Emigrants']

# Print the resulting DataFrame
print(result)

import pandas as pd
import matplotlib.pyplot as plt

# Assuming you already have the DataFrame 'result' from your previous code

# Create a figure and axis for the single graph
fig, ax = plt.subplots(figsize=(12, 6))

# Get a list of unique district names
districts = result['District Name'].unique()

# Define a color palette for the lines
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple', 'orange', 'lime', 'pink', 'brown', 'gray', 'olive', 'teal']   
