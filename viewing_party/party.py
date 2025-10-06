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
            break   
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_list = user_data['watched']
    #print(watched_list)
    sum = 0

    # If empty then return a rating of 0.0
    if not watched_list:
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
    # Check if empty, if empty then return None
    if not watched_list:
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
def get_unique_watched(user_data):
    #Assign empty list to variables
    user_unique_watched = []
    friend_movie_title = []

    #loop through wantched list from friend
    for friend in user_data["friends"]:
        friend_list = friend["watched"]
        for movie in friend_list:
            #add movie title into friend_movie_title list
            friend_movie_title.append(movie["title"])

    #loop through user's watched list 
    for user in user_data["watched"]:
        # if user's watched list movie not in friend's list then add it to the user_unique_watched list
        if user["title"] not in friend_movie_title:
            user_unique_watched.append(user)
    return user_unique_watched


def get_friends_unique_watched(user_data):
    #Assign empty list to variables
    user_movie_title = []
    friend_unique_watched = []
    f_uni_watched_rm_dup = []

    for user in user_data["watched"]:
        user_movie_title.append(user["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            #remove duplicate titles          
            if movie["title"] not in user_movie_title \
                and movie["title"] not in friend_unique_watched:
                f_uni_watched_rm_dup.append(movie)
                friend_unique_watched.append(movie["title"])

    return f_uni_watched_rm_dup


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_unique_movies = get_friends_unique_watched(user_data)

    # Recommend only movies available on user’s subscriptions
    recommended = [
        movie for movie in friend_unique_movies
        if movie["host"] in user_data["subscriptions"]
    ]

    #print(recommended)
    return recommended

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    #Assign empty list to variables
    user_watched = []
    friend_watched = []
    all_rec_movie = []
    genre_rec_movie = []

    #add user watched movie title into user_watched
    for user in user_data["watched"]:
        user_watched.append(user["title"])

    #add friend watched movie title into friend_watched 
    #and recommendation movie list 
    #Also remove duplicate
    for friend in user_data["friends"]:
        for movie in friend["watched"]:          
            if movie["title"] not in user_watched \
                and movie["title"] not in friend_watched:
                all_rec_movie.append(movie)
                friend_watched.append(movie["title"])
    
    #call helper function
    most_f_genre = get_most_watched_genre(user_data)
    #match the genre and add it into a new list
    for sel_movie in all_rec_movie:
        if sel_movie["genre"] in most_f_genre:
            genre_rec_movie.append(sel_movie)

    return genre_rec_movie


def get_rec_from_favorites(user_data):
    friend_watched = []
    rec_from_fav = []

    #add all friend watched list into the friend_watched list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie["title"])
    
    #if friend did not watch and is in user's favorite list 
    #then add them to rec_from_fav list
    for user_favorite in user_data["favorites"]:
        if user_favorite["title"] not in friend_watched:
            rec_from_fav.append(user_favorite)
        
    return rec_from_fav

        




