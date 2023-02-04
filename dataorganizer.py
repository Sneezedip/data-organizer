import time
import pandas as pd


df = pd.read_excel("database.xlsx")


def final():
    try:
        qst = int(input('''
        Do you want to save it in a txt file?
        [1] - Yes
        [2] - No
        ➞ '''))
    except ValueError:
        print("Invalid input, expected a number.")
        time.sleep(1)
        final()

    if qst == 1:
        df.to_csv("final_product.txt", sep="\t", index=False)
        time.sleep(0.4)
        print("Saved!")
    elif qst == 2:
        pass
    else:
        print("Something went wrong!")
        time.sleep(0.2)
        final()


def search():
    global result
    result = None
    search_criteria = int(input('''
    What do you want to search by?
    [1] - Name
    [2] - Age
    [3] - Rank
    ➞ '''))

    if search_criteria == 1:
        name = input("Enter the name: ").lower()
        try:
            result = df.loc[df["Client"].str.lower() == name]
        except ValueError:
            print("Something went wrong/nothing found. Be careful with capitals.")
            time.sleep(1)
            search()
    elif search_criteria == 2:
        try:
            age = int(input("Enter the age: "))
        except ValueError:
            print("Only numbers are allowed.")
            time.sleep(1)
            search()

        result = df.loc[df["Age"] == age]

    elif search_criteria == 3:
        rank = input("Enter the Rank: ")
        try:
            result = df.loc[df["Rank"] == rank]
        except ValueError:
            print("Something went wrong. Make sure the rank you wrote exists.")
            time.sleep(1)
            search()
    else:
        print("Something went wrong!")
        time.sleep(0.2)
        search()

    if result.empty:
        print("Nothing found. Be careful with capital letters.")
        time.sleep(1)
        search()
    else:
        print(result)
        time.sleep(1)
        finalsearch()


def finalsearch():
    try:
        qst = int(input('''
            Do you want to save it in a txt file?
            [1] - Yes
            [2] - No
            ➞ '''))
    except ValueError:
        print("Invalid input, expected a number.")
        time.sleep(1)
        final()

    if qst == 1:
        if result is not None:
            result.to_csv("final_product.txt", sep="\t", index=False)
            time.sleep(0.4)
            print("Saved!")
        else:
            print("No matching data was found.")
    elif qst == 2:
        pass
    else:
        print("Something went wrong!")
        time.sleep(0.2)
        final()


def ranks():
    ranks = ["Platinum", "Gold", "Silver", "Bronze"]
    df["Rank"] = pd.Categorical(df["Rank"], categories=ranks, ordered=True)

    df.sort_values("Rank", inplace=True)

    print(df)

    time.sleep(1)

    final()


def age():
    df.sort_values("Age", ascending=True, inplace=True)

    print(df)

    time.sleep(1)

    final()


def main():
    try:
        qst = int(input('''
    Do you want to:
    [1] - Sort by age
    [2] - Sort by rank
    [3] - Search for a person
    ➞ '''))

    except ValueError:
        print("Invalid input, expected a number.")
        time.sleep(1)
        main()

    if qst == 1:
        age()
    elif qst == 2:
        ranks()
    elif qst == 3:
        search()
    else:
        print("Something went wrong")
        main()


main()
search()
