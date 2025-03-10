# services/browser.py
import webbrowser


class BrowserService:
    def search(self, query):
        try:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}"
        except Exception as e:
            return f"Error performing search: {str(e)}"
