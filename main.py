import os
import openai
import re

openai.api_key = "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"

users = {}
genres = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Mystery", "Romance"]


def ask_for_id():
    id = int(input("What is your ID: "))
    while id not in users:
        print("User with this ID number does not exist")
        id = int(input("What is your ID: "))
    return id


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
    #openai.api_key = "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"

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


def tweet_classifier(tweet):
    #openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Decide whether a Tweet's sentiment is positive, neutral, or negative.\n\nTweet: " + tweet,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    print(response.choices[0].text)


while True:
    print("==MENU==")
    print("1. Add user")
    print("2. Insert rating")
    print("3. Create recommendations")
    print("4. Show dictionary")
    print("5. Tweet classifier")
    print("6. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        add_user()
    if choice == 2:
        insert_rating(ask_for_id())
    if choice == 3:
        id = ask_for_id()
        category = genres[users[id].index(max(users[id]))]
        create_recommendations(category)
    if choice == 4:
        show_dict()
    if choice == 5:
        tweet = input("Tweet: ")
        tweet_classifier(tweet)
    if choice == 6:
        exit()
