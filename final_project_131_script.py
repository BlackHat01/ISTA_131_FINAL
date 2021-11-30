"""
Developed by Corey Miller
ISTA 131 Final Project Visual Code
Group Members: Cory Shen, Beverly Perez
---
This code analyzes the csv data from https://www.kaggle.com/gregorut/videogamesales 
and visually displays (using bar graphs) the top selling platforms for each of the three main regions 
the data contains: North America, Europe, and Japan.
This interpretation of this data could serve many use cases
such as which platform a game developer might want to develop for if they intend to release
in a specific language or part of the world.
""" 


# Import needed modules
import matplotlib.pyplot as plt
import pandas as pd
import sys

def get_reg():
    '''
    Funtion to handle user input of desired region data.
    This is used to set some variables that will be used to access the desired data later on without 
    the need for multiple files per output graph.

    Returns
    -------
    use_index : int
    sales_col : str
    label : str

    '''
    # User input to get the desired region data. use_index is for determining which sales column of the csv to use.
    reg_na = ['north america', 'na']
    reg_eu = ['europe', 'eu']
    reg_jp = ['japan', 'jp']
    # Case insensitive input collection
    region = str(input("Enter desired region [North America / NA, Europe / EU, Japan / JP] : "))
    if region.lower() in reg_na:
        use_index = 6
        sales_col = 'NA_Sales'
        label = 'North America'
    elif region.lower() in reg_eu:
        use_index = 7    
        sales_col = 'EU_Sales'
        label = 'Europe'
    elif region.lower() in reg_jp:
        use_index = 8
        sales_col = 'JP_Sales'
        label = 'Japan'
    else:
        print("Invalid region. Try again.")
        get_reg()
    return use_index, sales_col, label
        
def main():
    '''
    Main funtion. Handles all data processing and graph creation.

    Returns
    -------
    None.

    '''

    user_inputs = get_reg()
    
    # Read in the csv file. This directory is hardcoded to my local directory and will need to be adjusted for use.
    data = pd.read_csv("C:\\Users\\17606\Desktop\\131_final_dataset\\vgsales.csv")
    
    # Create a dataframe of the entire dataset and sort by appropriate regional sales.
    df = pd.DataFrame(data)
    df.sort_values(by=[user_inputs[1]], inplace=True, ascending=False)
    
    
    # Get platform column from dataframe into a list      
    platform = list(df.iloc[:, 2])

    # Get the top 20 selling platforms in the set region. This helps narrow the x axis into more useful data.
    platform_top_twenty = list(platform[:20])
    
    # I don't think this is needed but I clean up the top 20 platforms list to contain no duplicates.
    # This converts the list into a 6-8 entry list with the same meaning. 
    platform_clean = []
    for p in platform_top_twenty:
        if p not in platform_clean:
            platform_clean.append(p)
            
    # Put the 6-8 top platforms into a dictionary that totals the sales for each respective platform.        
    dict = {}
    for p in platform_clean:
        dict[p] = 0
    for row in df.itertuples(name=None , index=False):
        if row[2] in platform_clean:
            dict[row[2]] += row[user_inputs[0]] 
            
    # Use matplotlib to create a simple bar graph displaying the total sales of the top 5-6 platforms in the set region.
    plt.bar(dict.keys(), dict.values(), color='b')
    plt.title("Top Selling Gaming Platforms in " + user_inputs[2])
    plt.xlabel("Platform")
    plt.ylabel("Number of Sales (millions)")
    plt.show()
    
    # Give user option to run again.
    # Case insensitive input collection.
    again = str(input("Would you like to use again? [Y/N]: "))
    if again == "y":
        main()
    else:
        sys.exit()
        
        
main()