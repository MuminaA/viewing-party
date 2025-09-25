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
def get_unique_watched(user_data):
    user_unique_watched = []
    friend_movie_title = []
    for friend in user_data["friends"]:
        friend_list = friend["watched"]
        for movie in friend_list:
            friend_movie_title.append(movie["title"])
    for user in user_data["watched"]:
        if user["title"] not in friend_movie_title:
            user_unique_watched.append(user)
    return user_unique_watched


def get_friends_unique_watched(user_data):
    user_movie_title = []
    friend_unique_watched = []
    result = []

    for user in user_data["watched"]:
        user_movie_title.append(user["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:          
            if movie["title"] not in user_movie_title \
                and movie["title"] not in friend_unique_watched:
                result.append(movie)
                friend_unique_watched.append(movie["title"])

    return result


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_watched_movies = [] # store users watched movies
    recommended_movies = [] #store recommended movies

    # loop through waht user has watched
    for user_movie in user_data['watched']:
        # add users watched movies into empty list to track
        user_watched_movies.append(user_movie['title'])

    for friend in user_data['friends']:
        for movie in friend['watched']:
            # if user has not watched and friend(s) has watched
            if movie['title'] not in user_watched_movies:
                    # print(f'user has not watched: {movie['title']}, check if have host')
                    # if user has host for that movie
                    if movie['host'] in user_data['subscriptions']:
                        #print(f'user has host: {movie['host']} for {movie['title']}')
                        #if movie not already in recommended
                        if movie not in recommended_movies:
                            # then add movie to recommended
                            recommended_movies.append(movie)
                    #print(f'user does not have {movie['host']} for {movie['title']}')

    #return list
    #print(recommended_movies)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    user_watched = []
    friend_watched = []
    all_rec_movie = []
    genre_rec_movie = []

    if genre_rec_movie == []:
        return None

    for user in user_data["watched"]:
        user_watched.append(user["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:          
            if movie["title"] not in user_watched \
                and movie["title"] not in friend_watched:
                all_rec_movie.append(movie)
                friend_watched.append(movie["title"])
    
    most_f_genre = most_frequent_genre(user_data)
    for sel_movie in all_rec_movie:
        if sel_movie["genre"] in most_f_genre:
            genre_rec_movie.append(sel_movie)

    return genre_rec_movie


def get_rec_from_favorites(user_data):
    friend_watched = []
    rec_from_fav = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie["title"])
    
    for user_favorite in user_data["favorites"]:
        if user_favorite["title"] not in friend_watched:
            rec_from_fav.append(user_favorite)
        
    return rec_from_fav

def most_frequent_genre(user_data):
    genre_dict = {}
    highest_count = 0
    most_frequent_genre = []

    for user in user_data["watched"]:
        if user["genre"] not in genre_dict:
            genre_dict[user["genre"]] = 0
            count = 0
        genre_dict[user["genre"]] += 1
        count += 1
        if count > highest_count:
            highest_count = count
    for genre, count in genre_dict.items():
        if count == highest_count:
            most_frequent_genre.append(genre)
        
    return most_frequent_genre

        




