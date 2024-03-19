
import pandas as pd

def categorize_time(hour):
   
    """
    Categorizes the hour into different time categories.

    Parameters:
    - hour (int): The hour component extracted from the timestamp.

    Returns:
    - str: The time category.
    """
    
    if 0 <= hour < 9:
        return 'morning_rush'
    elif 9 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 14:
        return 'lunch_rush'
    elif 14 <= hour < 18:
        return 'afternoon'
    elif 18 <= hour < 20:
        return 'dinner_rush'
    else:
        return 'night'

def restaurant_transactions_by_time_day(filename):
    """
    Analyzes a restaurant transaction dataset to find the most popular item for each time category.

    Parameters:
    - filename (str): The path to the CSV file containing the dataset.

    Returns:
    - DataFrame: A DataFrame with the most popular items for each time category.
    """
        
    # Load the dataset
    df = pd.read_csv(filename)
        # Extract the hour from the timestamp
    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.hour
        # Create a new column for time categories
    df['Time_Category'] = df['Hour'].apply(categorize_time)

        # Find the most popular item for each time category
    result_df = df.groupby(['Time_Category', 'Item']).size().reset_index(name='Count')
    result_df = result_df.loc[result_df.groupby('Time_Category')['Count'].idxmax()]
    result_df = result_df[['Time_Category', 'Item']].rename(columns={'Time_Category': 'Time_Category', 'Item':'item'}).reset_index(drop=True)

    return result_df
#Sample code
fn = "BreadBasket_DMS.csv"
df = restaurant_transactions_by_time_day(fn)
print(df)