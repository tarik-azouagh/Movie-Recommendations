# %%
#import csv
import csv as csv

# %%
#read csv and put the first three columns in different lists to imitate a dataframe
with open(r'/home/pi/RSL/userReviews.csv', 'r', encoding= 'utf-8-sig') as userReviews:

    csv_reader = csv.reader(userReviews, delimiter=';')
    next(csv_reader, None)
    author = []
    moviename = []
    score = []
    count = 0
    sum = 0
    avg = 0

    #for col in csv_reader:
    #    author.append(col[2])
    #    score.append(float(col[1]))
    #    moviename.append(col[0])
    for i in csv_reader:
        if (i[0]) == 'the-godfather-part-iii':
            sum+=float(i[1])
            count = count+1
    avg = sum/count
    print (avg)
    m = avg

# %%
print("Compare Tarik's userscore ( 9 ) to the average user score on Metacritic(",m,")")
print("the difference is =", 9 - m,'points')

# %%
## 3. Print out all movies (recommendations as proof of working) that comply to the 
#following restrictions:
#- The reviewers that rated The Godfather III
with open(r'/home/pi/RSL/userReviews.csv', 'r', encoding= 'utf-8-sig') as userReviews:
    csv_reader = csv.reader(userReviews, delimiter=';')
    next(csv_reader, None)
    authorsgf3 = []
    author=i[2]
    mymovie = 'the-godfather-part-iii'
    for i in csv_reader:
        if (i[0]) == mymovie:
            sum+=float(i[1])
            count = count + 1
            author = i[2]
            authorsgf3.append(i[2]) 
    print(authorsgf3)

# %%
# Other movies these reviews have seen and where the score of the movie is equal or greater than m (the average).
with open(r'/home/pi/RSL/userReviews.csv', 'r', encoding= 'utf-8-sig') as userReviews:
    csv_reader = csv.reader(userReviews, delimiter=';')
    finalauthor = []
    finalmovie = []
    finalscore = []

    for i in csv_reader:
        if (i[2]) in authorsgf3 and float(i[1]) > float(avg):
            finalauthor.append(i[2])
            finalmovie.append(str(i[0]))
            finalscore.append((i[1]))

#rec = tuple(zip(finalauthor, finalmovie, finalscore))
rec = list(map(list, zip(finalauthor, finalmovie, finalscore)))

# %%
# Load this 'dataframe' into a csv file
fields = ['Author', 'Movie', 'Userscore']
with open(r"/home/pi/RSL/userRecommendations.csv", 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rec)