import webbrowser
import time
import random
from urllib.parse import quote

# Configure browser (using Firefox as default)
FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(FIREFOX_PATH))

# Expanded list of search queries with more variety
SEARCH_QUERIES = [
    # Bing rewards related
    'bing rewards program',
    'how to earn bing points',
    'bing rewards redeem option',
    'microsoft rewards dashboard',
    'bing points conversion rate',
    'bing rewards levels',
    'max bing points per day',
    'bing mobile search points',
    
    'weather today',
    'latest tech news',
    'best restaurants near me',
    'python programming tips',
    'how to improve productivity',
    'current stock market trends',
    'healthy breakfast ideas',
    'upcoming movie releases',
    
    # Microsoft related
    'microsoft surface deal',
    'xbox game pass ultimate',
    'windows 11 features',
    'office 365 tips',
    'azure cloud services',
    
    # Random knowledge
    'how many planets in solar system',
    'world population 2023',
    'history of the internet',
    'benefits of meditation',
    'how to make perfect coffee'
]

def get_random_query():
    """Return a random query with optional variation"""
    base_query = random.choice(SEARCH_QUERIES)
    
    # 30% chance to add a modifier to the query
    if random.random() < 0.3:
        modifiers = ['best', 'top', 'how to', 'review', 'compare', 'latest']
        return f"{random.choice(modifiers)} {base_query}"
    return base_query

def random_delay(min_sec=5, max_sec=20):
    """Random delay with human-like variation"""
    base_time = random.randint(min_sec, max_sec)
    # Add small random variation to appear more natural
    return base_time + random.random() * 2

def main():
    try:
        for _ in range(40):
            query = get_random_query()
            encoded_query = quote(query)
            url = f'https://www.bing.com/search?q={encoded_query}'
            
            print(f"Searching: {query}")  # For logging purposes
            
            webbrowser.get('firefox').open_new_tab(url)
            
            # Random delay with some longer pauses occasionally
            if random.random() < 0.1:  # 10% chance for a longer "reading" pause
                time.sleep(random_delay(30, 60))
            else:
                time.sleep(random_delay())
                
    except KeyboardInterrupt:
        print("\nScript stopped by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
