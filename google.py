import wikipedia
import sys
import time
from googlesearch import search

user_agent = 'MyAppName/1.0 (https://example.com; deveshsoman3575@gmail.com)'
wikipedia.set_user_agent(user_agent)

yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

def returnname():
    print("What's your name?")
    global name
    name = input(">>> ")
    if name.lower() == "exit":
        print("Goodbye!")
        sys.exit()
    else:
        print("Wow! Cool name, {}!".format(name))

def wiki_return_validate(x):
    if x in yes:
        return True
    elif x in no:
        return False
    else:
        return False

def wiki_return():
    print("Do you want to ask another question? (Yes/No)")
    x = input(">>> ")
    if x.lower() == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x.lower() == "no":
        print("Goodbye, {}! Have a great day!".format(name))
        sys.exit()
    elif x.lower() == "yes":
        return True
    else:
        wiki_validation_result = wiki_return_validate(x)
        while wiki_validation_result is False:
            print("Please enter a valid input (yes or no):")
            x = input(">>> ")
            wiki_validation_result = wiki_return_validate(x)
        return x in yes

def google_search(query):
    print("\nPerforming Google search...")
    results = []
    for result in search(query, num_results=5):
        results.append(result)
        print(result)
    return results

def wikichat():
    while True:
        print("Ask me anything! (Type 'exit' to quit)")
        query = input(">>> ")
        if query.lower() == "exit":
            print("Thank you! Goodbye, {}!".format(name))
            sys.exit()

        try:
            page_py = wikipedia.page(query)
            print("Here you go, {}:".format(name))
            print("Page - Title: {}".format(page_py.title))
            print("Page - Summary:")
            print(page_py.summary[:15000])  
        except wikipedia.exceptions.DisambiguationError as e:
            print("Ambiguous search term. Please choose one of the following:")
            for option in e.options[:10]:  
                print("-", option)
        except wikipedia.exceptions.PageError:
            print("Sorry, I couldn't find information on '{}'. Trying Google search...".format(query))
            google_results = google_search(query)
            if google_results:
                print("\nGoogle Search Results:")
                for result in google_results:
                    print(result)
            else:
                print("No results found on Google for '{}'. Please try another query.".format(query))

        if not wiki_return():
            print("Goodbye, {}! Have a great day!".format(name))
            sys.exit()

print("\n")
time.sleep(1)
returnname()
print("Welcome, {}! Let's get started!".format(name))
wikichat()
