#Keep the following columns, delete the rest
#name, host_id, host_name, host_is_superhost, neighbourhood, neighbourhood_cleansed, beds, price, review_scores_ratings
import pandas as pd 

file_path = "data/listings.csv"

dirty_data = pd.read_csv(file_path)

clean_data = dirty_data[
    [
        "host_id",
        "name", 
        "host_name", 
        "host_is_superhost", 
        "neighbourhood", 
        "neighbourhood_cleansed", 
        "beds", 
        "price", 
        "review_scores_rating"

    ]
]

clean_data.to_csv("data/listings_clean.csv")