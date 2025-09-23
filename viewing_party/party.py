# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #print(rating)
    # if any attributes false then return None
    if not (title and genre and rating):
        #print('None')
        return None
    else:
    # if truthy then return dict of movie data
        movie_data = {
            'title': title,
            'genre': genre,
            'rating': rating,
        }
        #print(movie_data)
        return movie_data

def add_to_watched(user_data, movie):
    # append movie to watched list
    user_data['watched'].append(movie)

    #print(user_data)
    return user_data

def add_to_watchlist(user_data, movie):
    #located the watchlist in user_data and add movie into watchlist
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #assign watchlist into a variable
    waiting_watch = user_data["watchlist"]
    for movie in waiting_watch: #loop through the waiting_watch list
        if title == movie["title"]: # Compare if title is equal to the title in waiting_watch
            user_data["watched"].append(movie) #If above condition is true then add the movie into the watched list in user_data
            waiting_watch.remove(movie) #and remove the movie from the waiting_watch list
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_list = user_data['watched']
    #print(watched_list)
    sum = 0

    # Access dict value to check if empty, if empty then return a rating of 0.0
    for value in user_data.values():
        if value == []:
            #print(0.0)
            return 0.0
    # loop through watched list to get rating of movies and total it to the sum
    for watched in watched_list:
        #print(watched)
        rating = watched['rating']
        #print(f"this is the rating: {rating}")
        sum += rating
        #print(f'this is sum: {sum}')
    # Divide sum with length of the watched_list to get thte average rating
    average_rating = sum / len(watched_list)
    #print(average_rating)
    return average_rating

def get_most_watched_genre(user_data):
    watched_list = user_data['watched']
    counts = {}
    # Access dict value to check if empty, if empty then return None
    for value in user_data.values():
        if value == []:
            # print(None)
            return None

    for watched in watched_list:
        genre = watched['genre']

        if genre not in counts:
            # Add it into count dict
            counts[genre] = 1
        else:
            # If already in count dict then increase its number
            counts[genre] = counts[genre] + 1

    highest_count = 0
    highest_genre = None

    for genre, count in counts.items():
        # Compare if count value greater then the current highest
        if count > highest_count:
            # If true then set the highest count to be the count and set highest genre to genre
            highest_count = count
            highest_genre = genre

    #print(highest_genre)
    return highest_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

#get_most_watched_genre(USER_DATA_2)