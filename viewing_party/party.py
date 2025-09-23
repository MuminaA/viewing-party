# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    #print(rating)
    if not (title and genre and rating):
        #print('None')
        return None
    else:
        movie_data = {
            'title': title,
            'genre': genre,
            'rating': rating,
        }
        #print(movie_data)
        return movie_data
    

    



def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    waiting_watch = user_data["watchlist"]
    for movie in waiting_watch:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            waiting_watch.remove(movie)
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

# create_movie("It Came from the Stack Trace", "Horror", 3.1)