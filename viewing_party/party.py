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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------