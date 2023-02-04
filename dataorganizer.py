import time
import pandas as pd

df = pd.read_excel("database.xlsx")


def final():
    qst = int(input('''
    Do you want to save it in a txt file?
    [1] - Yes
    [2] - No
    ➞ '''))
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
    search_criteria = int(input('''
    What do you want to search by?
    [1] - Name
    [2] - Age
    [3] - Rank
    ➞ '''))

    if search_criteria == 1:
        name = input("Enter the name: ")
        result = df.loc[df["Name"] == name]
    elif search_criteria == 2:
        age = int(input("Enter the age: "))
        result = df.loc[df["Age"] == age]
    elif search_criteria == 3:
        rank = input("Enter the Rank: ")
        result = df.loc[df["Rank"] == rank]
    else:
        print("Something went wrong!")
        time.sleep(0.2)
        search()

    print(result)


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
    qst = int(input('''
    Do you want to:
    [1] - Sort by age
    [2] - Sort by rank
    [3] - Search for a person
    ➞ '''))

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
