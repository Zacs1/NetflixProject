import pandas as pd
import matplotlib.pyplot as plt

# Open and import the CSV file with correct formatting as a Pandas DataFrame

data = open(r"C:\Users\smith\Desktop\Netflix Project\netflix_data.csv", encoding='utf8')
netflixdata = pd.read_csv(data)
print(netflixdata)

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflixdata[netflixdata["type"]=="Movie"]

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title','country','genre','release_year','duration']]

# Filter for durations shorter than 60 minutes
short_movies = pd.DataFrame(netflix_movies_col_subset[netflix_movies_col_subset["duration"]<60])

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"],netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release Year")
plt.ylabel("Duration(min)")

# Show the plot
plt.show()