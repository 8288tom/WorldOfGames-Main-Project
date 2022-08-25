import Utils


def add_score(difficulty):
    points_won = (int(difficulty) * 3) + 5
    f = open(Utils.SCORES_FILE_NAME, "a+")
    f.seek(0)
    data = f.readlines()
    if len(data) >= 1:
        list_of_points = [data[0]]
        f.seek(0)
        f.truncate()
        accumulated_score = int(list_of_points[0])
        new_score = points_won + accumulated_score
        f.write(str(new_score))
    elif len(data) == 0:
        f.seek(0)
        f.write(str(points_won))

