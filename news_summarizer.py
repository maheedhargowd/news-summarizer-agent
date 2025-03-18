import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
from langchain_openai import OpenAI
import requests

load_dotenv()
app = Flask(__name__)

# Set up the OpenAI LLM with your API key
llm = OpenAI(
    openai_api_key=os.getenv("OPEN_API_KEY"),
    model="gpt-3.5-turbo-instruct",
    temperature=0  
    )

# Set up your NewsAPI key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Function to fetch a news article using NewsAPI
def fetch_news_article(query="technology", language="en"):
    url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"NewsAPI Response: {data}")
        if data["status"] == "ok" and data["articles"]:
            article = data["articles"][0]
            content = article.get("description", "No description available.")
            if "content" in article and article["content"]:
                content = article["content"]
            print(f"Fetched Article Content: {content}")
            return content
        print("No articles found in response.")
        return "No articles found."
    except requests.RequestException as e:
        print(f"Error in fetch_news_article: {str(e)}")
        return f"Error fetching news: {str(e)}"

# Function to summarize a news article
def summarize_news(article):
    if not article or article.lower() == "exit":
        return None
    prompt = (f"Condense the following news article into EXACTLY 3 sentences, no more and no less, by summarizing its key points. "
              f"Each sentence must be complete, concise, and end with a period. Article: {article}")
    try:
        summary = llm.invoke(prompt)
        sentences = [s.strip() for s in summary.split(".") if s.strip()]
        if len(sentences) != 3:
            if len(sentences) < 3:
                while len(sentences) < 3:
                    sentences.append("Further updates on this story are anticipated.")
            elif len(sentences) > 3:
                sentences = sentences[:3]
        summary = ". ".join(sentences)
        if not summary.endswith("."):
            summary += "."
        print(f"Generated Summary: {summary}")
        return summary
    except Exception as e:
        print(f"Error in summarize_news: {str(e)}")
        return f"Error: {str(e)}. Please check your OpenAI API key or quota."

@app.route('/', methods=['GET', 'POST'])
def index():
    article = None
    summary = None
    error = None

    if request.method == 'POST':
        option = request.form.get('option', 'none')
        if option == 'manual':
            article = request.form.get('article', '').strip()
            if article:
                summary = summarize_news(article)
                if not summary:
                    error = "Failed to generate summary. Check OpenAI API quota or key."
            else:
                error = "Please enter a news article."
        elif option == 'fetch':
            topic = request.form.get('topic', '').strip()
            if topic:
                article = fetch_news_article(query=topic)
                if "Error fetching news" in article or article == "No articles found.":
                    error = article
                else:
                    summary = summarize_news(article)
                    if not summary:
                        error = "Failed to generate summary for fetched article."
            else:
                error = "Please enter a topic."

        return render_template('index.html', 
                               article=article, 
                               summary=summary, 
                               error=error, 
                               request=request)

    return render_template('index.html', article=article, summary=summary, error=error, request=request)



if __name__ == '__main__':
    app.run(debug=True)