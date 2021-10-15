import csv
from datetime import datetime


def append(expense, category):
    with open("mtable.csv", "r",newline="") as tb:
        reader = csv.reader(tb,delimiter=";")

        for row in reader:
            with open("mtable.csv", "a",newline="") as t:
                swriter = csv.writer(t, delimiter=";")
                if len(row):
                    pass
                """else:

                    f = open("mtable.csv", "w", newline="")
                    bwriter = csv.write(f, delimiter="")
                    lines = flist("mtable.csv")
                    for i in lines:
                        bwriter.writerow(i)"""

                swriter.writerow([expense, time(0), time(1), category])
                break

#additional code that I don't use, but It can help in future
def empty_cell():
    f = open("mtable.csv", "w", newline="")
    writer = csv.writer(f, delimiter=";")
    lines = flist("mtable.csv")
    for row in lines:
        writer.writerow(row)


#reads our table
def flist(file_to_read):
    lines = list()
    with open(file_to_read, 'r', newline="") as readFile:
        reader = csv.reader(readFile, delimiter=";")
        for row in reader:
            if len(row):
                lines.append(row)
            else:
                pass
    return lines


#removes last row
def remove_last_row(list):
    f = open("mtable.csv", "w", newline="")
    writer = csv.writer(f, delimiter=";")

    for s in list:
        if list[-1] == s:
            pass
        else:
            writer.writerow(s)


def time(x):
    now = datetime.now()
    if x == 0:
        return  now.strftime("%H:%M")
    elif x == 1:
        return now.strftime("%d/%m/%Y").replace("/", ".")


def plan(list):
    expense_list = []
    int_expense_list = []
    first_last_date = []

    for row in list:
        try:
            expense_list.append(row[0])
            if row == list[0]:
                first_last_date.append(row[2])
            elif row == list[-1]:
                first_last_date.append(row[2])
            else:
                pass

        except ValueError:
            pass
    for i in expense_list:
        i = float(i.replace(",", "."))
        int_expense_list.append(i)
    return "You spent " + str(sum(int_expense_list)) + f"€ from {first_last_date[0]} to {first_last_date[1]}"


def categories(lines):
    categ = {
        "food": 0,
        "drink": 0,
        "lego": 0,
        "clothing": 0,
        "transport": 0,
        "party": 0,
        "other": 0
    }

    for row in lines:
        row[0] = row[0].replace(",", ".")
        if row[3] == "food":
            categ["food"] = categ["food"] + float(row[0])
        elif row[3] == "drink":
            categ["drink"] = categ["drink"] + float(row[0])
        elif row[3] == "lego":
            categ["lego"] = categ["lego"] + float(row[0])
        elif row[3] == "clothing":
            categ["clothing"] = categ["clothing"] + float(row[0])
        elif row[3] == "transport":
            categ["transport"] = categ["transport"] + float(row[0])
        elif row[3] == "party":
            categ["party"] = categ["party"] + float(row[0])
        elif row[3] == "other":
            categ["other"] = categ["other"] + float(row[0])

    list_categ = []
    for cat in categ:
        row = f"{cat}: {categ[cat]}€\n"
        list_categ.append(row)

    return retList(list_categ)


def retList(list):
    string = " ".join([str(item) for item in list])
    string = string.replace(" ", "")
    string = string.replace(":", ": ")
    return string

