import pywhatkit
import wikipedia
import random
import datetime
import webbrowser

greeting = [
    "Hello",
    "hi", "how do you do"
]
greet = random.choice(greeting)
    

def wish():
    """The function is to greet user!"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("good morning")

    elif hour >= 12 and hour < 18:
        print("good afternoon")
    else:
        print("good evening")
    print("what do you want today!")


def play_on_youtube(user_query):
    """it will play anything on youtube(according to user query of course!)"""
    pywhatkit.playonyt(user_query)


def get_wikipedia_summary(user_query):
    """this function is for searching something from wikipedia"""
    print("from wikipedia..\n")
    result = wikipedia.summary(user_query, sentences=5)
    print(result+"\n")


def command():
    """this function is used to take input from user"""
    print("user:", end="")
    user_query = input()
    return user_query
# Function to get news headlines using OpenAI
def get_news_headlines():
    # Prompt for the news category
    print("Which category of news headlines would you like to see?")
    category = input()
    prompt = f"Get me the top news headlines in the {category} category."
    
    # Fetch the headlines using OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    news_headlines = response.choices[0].text.strip()
    print(f"Here are the top news headlines in the {category} category:\n{news_headlines}")

if __name__ == "__main__":
    print(greet)
    wish()
    while (True):
        user_query = command().lower()
        if 'hi' in user_query:
            print(greet+"I am here to help!")
        elif 'play' in user_query:
            user_query = user_query.replace("play", "")
            play_on_youtube(user_query)
        elif 'wikipedia' in user_query:
            user_query = user_query.replace("wikipedia", "")
            get_wikipedia_summary(user_query)
        elif 'search' in user_query:
            pywhatkit.info(user_query, lines=4)
        elif 'chat gpt' in user_query:
            webbrowser.open('https://chat.openai.com/chat')
        elif 'news' in user_query:
            get_news_headlines();
        elif 'bye' in user_query:
            print("bye have a great day!")
            break
