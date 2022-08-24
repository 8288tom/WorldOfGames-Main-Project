import Utils


# Need to go over this function:
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.
def add_score(difficulty):
    points_of_winning = (int(difficulty) * 3) + 5
    f = open(Utils.SCORES_FILE_NAME, "a+")
    f.write(str(points_of_winning) + ' ')
    f.seek(0)
    r = f.readline()
    if len(r[0]) > 1:
        r2=r[0][-1]
        total = int(r[0][-1])
        for num in r[0]:
            total += int(points_of_winning)
        f.truncate(0)
        f.write(str(total))
        f.close()
    else:
        f.close()





print(add_score(1))
