import os
import openai

users = {}
genres = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Mystery", "Romance"]
# API key: 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
def add_user():
    i = len(users) + 1
    print("Your id is " + str(i))
    users[i] = []


def insert_rating(id):
    for genre in genres:
        rating = int(input("What is your rating of " + genre + ": "))
        users[id].append(rating)


def show_dict():
    print(users)


def create_recommendations(category):
    prompt = "Give Recommendations of " + category + " movies from 2021"
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    print(response.choices[0].text)


while True:
    print("==MENU==")
    print("1. Add user")
    print("2. Insert rating")
    print("3. Create recommendations")
    print("4. Show dictionary")
    print("5. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        add_user()
    if choice == 2:
        ID = int(input("What is your id? "))
        insert_rating(ID)
    if choice == 3:
        id = int(input("What is your ID: "))
        category = genres[users[id].index(max(users[id]))]
        create_recommendations(category)
    if choice == 4:
        show_dict()
    if choice == 5:
        exit()
