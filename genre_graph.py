"""
Developed by Cory Shen
ISTA 131 Final Project Visual Code
Group Members: Corey Miller, Beverly Perez
---
.csv data from: https://www.kaggle.com/gregorut/videogamesales 
Takes in the .csv file as a pandas dataframe and compares three regions and their
sales based on genre in a bar chart. Different regions may have different tastes in
game genre, and this is intended to see what genres are favored in which regions.
""" 
# numpy is needed for x-tick label positions
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import sys

def main():

    region_sales = ['NA_Sales', 'EU_Sales', 'JP_Sales']
    ### This is a local path for my computer, change if vgsales.csv is located elsewhere
    data = pd.read_csv(".\\vgsales.csv")
    ###
    df = pd.DataFrame(data)
    df.sort_values(by=region_sales, inplace=True, ascending=False)

    # Find the "Genre" column in dataframe and clean to just top 20
    genre = list(df.iloc[:, 4])
    genre_top_twenty = list(genre[:20])
    genre_clean = []
    for g in genre_top_twenty:
        if g not in genre_clean:
            genre_clean.append(g)
    
    # Initialize dictionaries for each of the 3 regions
    na_sales = {}
    eu_sales = {}
    jp_sales = {}
    # For all three regions added up
    total_sales = {}

    # For tick label positions
    x_axis = np.arange(len(genre_clean))

    # Intialize all sales figures per genre
    for g in genre_clean:
        na_sales[g] = 0
        eu_sales[g] = 0
        jp_sales[g] = 0
        total_sales[g] = 0
    for row in df.itertuples(name=None , index=False):
        if row[4] in genre_clean:
            na_sales[row[4]] += row[6]
            eu_sales[row[4]] += row[7]
            jp_sales[row[4]] += row[8]
            total_sales[row[4]] += row[6] + row[7] + row[8]
    plt.bar(x_axis - 0.2, na_sales.values(), width = 0.2, color = 'r', label = "NA Sales")
    plt.bar(x_axis, eu_sales.values(), width = 0.2, color = 'g', label = "EU Sales")
    plt.bar(x_axis + 0.2, jp_sales.values(), width = 0.2, color = 'b', label = "JP Sales")

    # Plots for regional sales per genre side-by-side (bar)
    plt.title("Top Selling Games By Genre")
    plt.xticks(x_axis, genre_clean, fontsize = 8)
    plt.xlabel("Game Genre")
    plt.ylabel("Number of Sales (millions)")
    plt.legend(loc = 'upper left')

    plt.figure()

    # Plots for regional sales per genre side-by-side (scatter)
    plt.scatter(na_sales.keys(), na_sales.values(), color = 'r', label = "NA Sales")
    plt.scatter(eu_sales.keys(), eu_sales.values(), color = 'g', label = "EU Sales")
    plt.scatter(jp_sales.keys(), jp_sales.values(), color = 'b', label = "JP Sales")
    plt.title("Top Selling Game Genres Global Scatter")
    plt.xticks(x_axis, genre_clean, fontsize = 8)
    plt.xlabel("Game Genre")
    plt.ylabel("Number of Sales (millions)")
    plt.legend(loc = 'upper left')

    plt.figure()

    # Plots for regional sales per genre total
    plt.bar(total_sales.keys(), total_sales.values(), color = 'b')
    plt.title("Top Selling Gaming Genres Total")
    plt.xticks(fontsize = 8)
    plt.xlabel("Genres")
    plt.ylabel("Number of Sales (millions)")

    plt.show()

main()