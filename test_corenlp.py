from nlplogic.corenlp import search_wikipedia, summarize_wikipidia, get_text_blob, get_phrases

def test_get_phrases():
    assert 'golden state' in get_phrases("Golden State Warriors")