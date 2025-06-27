from search import search_wikipedia, search_arxiv, search_duckduckgo
from scraper import scrape_text
from openrouter_api import summarize

class ResearchAgent:
    def __init__(self):
        self.memory = []  # List of {"role": "user"/"assistant", "content": str}

    def add_message(self, role, content):
        self.memory.append({"role": role, "content": content})

    def research_topic(self, topic):
        self.add_message("user", f"Research the topic: {topic}")

        results = {
            "wikipedia": "",
            "web": [],
            "arxiv": []
        }

        # Wikipedia
        wiki = search_wikipedia(topic)
        if wiki:
            summary = summarize(wiki, memory=self.memory)
            results["wikipedia"] = summary
            self.add_message("assistant", f"Wikipedia Summary:\n{summary}")
        else:
            results["wikipedia"] = "No Wikipedia content found."
            self.add_message("assistant", "No Wikipedia content found.")

        # DuckDuckGo Web Results
        urls = search_duckduckgo(topic)
        for url in urls:
            page = scrape_text(url)
            if page:
                summary = summarize(page, memory=self.memory)
                results["web"].append(summary)
                self.add_message("assistant", f"Web Article Summary from {url}:\n{summary}")

        # Arxiv Results
        abstracts = search_arxiv(topic)
        for abstract in abstracts:
            summary = summarize(abstract, memory=self.memory)
            results["arxiv"].append(summary)
            self.add_message("assistant", f"ArXiv Summary:\n{summary}")

        return results

    def compile_summary(self, topic, results):
        output = f"\n# 🧠 Research Summary: {topic}\n"
        output += f"\n## 📚 Wikipedia\n{results['wikipedia']}\n"

        output += "\n## 🌐 Web Results\n"
        for i, w in enumerate(results["web"]):
            output += f"### Article {i+1}\n{w}\n"

        output += "\n## 🧪 Arxiv Papers\n"
        for i, a in enumerate(results["arxiv"]):
            output += f"### Paper {i+1}\n{a}\n"

        return output
