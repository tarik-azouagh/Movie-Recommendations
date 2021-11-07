# importing csv and numpy
import csv as csv

## The different columns in the CSV file are: 
## movieName, Metascore_w, Author, AuthorHref, Date, Summary, InteractionsYesCount, InteractionsTotalCount, InteractionsThumbUp, InteractionsThumbDown

#Make lists to define author, score and moviename (specify delimiter(;) because this is not a standard(,))
with open('/home/pi/RSL/userReviews.csv', 'r', encoding= 'utf-8-sig') as userReviews:
    csv_reader = csv.reader(userReviews, delimiter=';')

    X = []
    moviename = []
    score = []

    for col in csv_reader:
        X.append(col[2])
        score.append(col[1])
        moviename.append(col[0])


#Make a second list Y (which is a subset of X) which is filtered on the moviename: The Godfather Part III
## Degine X and moviename columns
with open('/home/pi/RSL/userReviews.csv', 'r', encoding= 'utf-8-sig') as userReviews:
    csv_reader = csv.reader(userReviews, delimiter=';')

    X = []
    moviename = []
    score = []

    for col in csv_reader:
        X.append(col[2])
        score.append(col[1])
        moviename.append(col[0])
        print(moviename)

#Zip the lists X and moviename

movienameX = list(zip(moviename, X))

#Filter the list with names of the authors where the moviename = The Godfather Part III 

D = list(filter(lambda x: x[0] == 'the-godfather-part-iii', movienameX))

print(D)

Y = [x[1] for x in D]

print(Y)

#For every author in Y make a third list Z, in which other movies which have been reviewed by the same author is specified
## 'Inner Join movienameX, Y and score as moviesZ
import numpy as np

moviesZ = list(zip(moviename, X, score))

print(moviesZ)

Q = list(filter(lambda c: c[1] == ('pabloaimar', 'JamesE', 'EddieM.', 'DouglasM', 'HudsonT', 'PatrickM.', 'Moviebuffreview', 'Compi24', 'joseap84', 'EricR.', 'RexG.', 'AAD', 'JaredK.', 'JamesL.', 'RonD.', 'JoyceC.', 'asylumspadez', 'Schmit93', 'aaronpaul121', 'sinadoom', 'spadenx', 'TheWalrus2000', 'JohnnyStephens', 'LaMagiadeVirue', 'joao1198pedro', 'CharlesB', 'MarkG.', 'KeithM.', 'JaradC.', 'JCA.', 'GottlobF.', 'devo-nc', 'RegOz', 'Spangle', 'axelkoch', 'gzayas91', 'MovieGuys', 'Marick', 'MovieManiac83', 'OverreachTHIS', 'DanteGodfather7', 'peraveen', 'aadityamudhar', 'domnels234', 'duckhost', 'Ggslm', 'Broyax', 'soumyadeepdas'), moviesZ))

print(Q)

#Compute which movies these authors liked better than The Godfather Part III
