"""This program uses loops and lists to collet the users fvoutie movies"""
movie = []
print("Hello please enter your favouite movies")
for i in range (3):
    movie.append(input("Please enter movie"))

for i in range(len(movie)):
    print(i+1, ":", movie[i])

