#Helper Function to grab the most_frequent_genre
def most_frequent_genre(user_data):
    #Assign empty dict, int, and list to variables
    genre_dict = {}
    highest_count = 0
    most_frequent_genre = []

    #loop through the user_data watched movie
    for user in user_data["watched"]:
        #if the movie genre is not in the genre dictionary
        #then assign the genre and initiate the count as 0 
        # (key: genre, value: count)
        if user["genre"] not in genre_dict:
            genre_dict[user["genre"]] = 0
            count = 0
        #sum up the count for each different genre
        genre_dict[user["genre"]] += 1
        count += 1
        #Figure out the highest count
        if count > highest_count:
            highest_count = count
    #grab the genre(key) related to the highest count and add them to the list
    for genre, count in genre_dict.items():
        if count == highest_count:
            most_frequent_genre.append(genre)
        
    return most_frequent_genre
