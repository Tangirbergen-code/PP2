movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Проверка фильма по рейтингу
def is_good_movie(movie):
    return movie['imdb'] > 5.5

# 2. Список фильмов с рейтингом выше 5.5
def good_movies(movies_list):
    return [movie for movie in movies_list if is_good_movie(movie)]

# 3. Фильмы по категории
def movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie['category'].lower() == category.lower()]

# 4. Средний рейтинг списка фильмов
def average_imdb(movies_list):
    if not movies_list:
        return 0
    total = sum(movie['imdb'] for movie in movies_list)
    return total / len(movies_list)

# 5. Средний рейтинг по категории
def average_imdb_by_category(movies_list, category):
    category_movies = movies_by_category(movies_list, category)
    return average_imdb(category_movies)

print("Проверка первого фильма:", is_good_movie(movies[0]))   

print("\nФильмы с рейтингом > 5.5:")
for m in good_movies(movies):
    print(m['name'], m['imdb'])

print("\nФильмы в категории 'Romance':")
for m in movies_by_category(movies, 'Romance'):
    print(m['name'], m['imdb'])

print("\nСредний рейтинг всех фильмов:", average_imdb(movies))
print("Средний рейтинг фильмов категории 'Romance':", average_imdb_by_category(movies, 'Romance'))