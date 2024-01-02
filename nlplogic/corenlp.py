from textblob import TextBlob
import wikipedia

# wikipedia.search("Golden State Warriors")
# golden_state_warriors_text = wikipedia.summary("Golden State Warriors")
# blob = TextBlob(golden_state_warriors_text)

def search_wikipedia(name):
    """Search wikipeida"""

    print(f"Searching for name: {name}")
    return wikipedia(name)

def summarize_wikipidia(name):
    """Summarize wikipedia"""

    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """Getting text blob object and returns"""

    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """Find wikipedia name and return back phrases"""

    text = summarize_wikipidia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases



