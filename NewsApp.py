"""-----------NEWS APP--------
--------"""

# Python request module or how we can handle the requests using the Python requests library. The request module is a standard way for making HTTP requests in Python.
import requests
# Python provides the standard library Tkinter for creating the graphical user interface for desktop based applications.
import tkinter as tk

def getNews():
    # API keys are commonly used to control the utilization of the API’s interface and track how it is being used.

    api_key="0e5ba71e53a248548e7bdd3d10d5a634"
    # url of news
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news=requests.get(url).json()

    articles=news["articles"]
    my_articles=[]
    my_news=""

    # this for loop appednds the headline from site
    for article in articles:
        my_articles.append(article["title"])

    # this for loop fetches 20 headlines
    for i in range(20):
          my_news=my_news+str(i+1)+". "+ my_articles[i]+"\n"

    Label.config(text=my_news)

# A tkinter canvas can be used to draw in a window. Use this widget to draw graphs or plots. You can even use it to  create graphical editors.

canvas=tk.Tk()
canvas.geometry("1300x600") # size of gui window
canvas.title("NewsApp") # gives title of gui window

# button command makes button to reload the news headlines
button=tk.Button(canvas,font=24,text="reload",command=getNews)
button.pack(pady=20)


# Label widget implements a display box where you can place text or images. The text displayed by this widget can be updated at any time you want.
Label=tk.Label(canvas, font=18, justify="left")
Label.pack(pady=20)

getNews()
canvas.mainloop()
