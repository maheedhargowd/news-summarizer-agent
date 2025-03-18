# 📌 News Summarizer AI Agent

A web-based News Summarizer application built using Flask, OpenAI's GPT model, and NewsAPI. This app fetches news articles automatically or summarizes manually inputted articles into concise, three-sentence summaries.

---

## 🚀 Features

- **Automatic Article Fetching**: Retrieve the latest news articles automatically based on user-entered topics.
- **Manual Article Input**: Allows users to paste or type articles directly for summarization.
- **AI-powered Summarization**: Utilizes OpenAI's GPT-3.5-turbo model to generate precise three-sentence summaries.
- **Dynamic UI**: Intuitive interface with dynamic input fields based on user selection.

---

## 📦 Technology Stack

- **Frontend**:
  - HTML/CSS
  - JavaScript

- **Backend**:
  - Flask (Python)
  - LangChain & OpenAI GPT (AI Integration)

- **APIs**:
  - [OpenAI](https://platform.openai.com/api-keys)
  - [NewsAPI](https://newsapi.org)

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/news-summarizer-agent.git
cd news-summarizer-agent
```

### Step 2: Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install Flask requests langchain-openai
```

### Step 4: API Keys Configuration

Replace your API keys in `news_summarizer.py`:

```python
llm = OpenAI(
    openai_api_key="YOUR_OPENAI_API_KEY",
    model="gpt-3.5-turbo-instruct",
    temperature=0
)

NEWS_API_KEY = "YOUR_NEWSAPI_KEY"
```

> Get your keys here:
> - [OpenAI API](https://platform.openai.com/api-keys)
> - [NewsAPI](https://newsapi.org)

---

## ▶️ Running the Application

```bash
python news_summarizer.py
```

The app runs locally at:

```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
.
├── static
│   └── styles.css
├── templates
│   └── index.html
├── news_summarizer.py
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

_Add relevant screenshots of your app here._

---

## ✅ Usage Instructions

- Visit the homepage.
- Select between entering an article manually or fetching automatically.
- Submit to receive a three-sentence summary powered by OpenAI.

---

## 🚨 Troubleshooting

- Check console logs for detailed error messages.
- Ensure your API keys are valid and active.

---

## 🤝 Contribution

Contributions, suggestions, or bug fixes are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -am 'Add YourFeature'`
4. Push to your branch: `git push origin feature/YourFeature`
5. Create a pull request.

---

## ⭐️ Acknowledgements

- OpenAI GPT-3
- NewsAPI.org

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

