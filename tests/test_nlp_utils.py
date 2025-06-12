import ast
import pathlib
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from unittest.mock import patch


def load_functions():
    path = pathlib.Path(__file__).resolve().parents[1] / "chatbot" / "chatgui.py"
    module = ast.parse(path.read_text())
    env = {
        'nltk': nltk,
        'WordNetLemmatizer': WordNetLemmatizer,
        'lemmatizer': WordNetLemmatizer(),
        'np': np,
    }
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name in ("clean_up_sentence", "bow"):
            code = ast.Module([node], [])
            exec(compile(code, str(path), 'exec'), env)
    return env['clean_up_sentence'], env['bow'], env['lemmatizer']


clean_up_sentence, bow, lemmatizer = load_functions()


def test_clean_up_sentence():
    with patch('nltk.word_tokenize', return_value=['hello']), \
         patch.object(lemmatizer, 'lemmatize', side_effect=lambda w: w):
        assert clean_up_sentence('Hello!') == ['hello']


def test_bow():
    with patch('nltk.word_tokenize', return_value=['hello']), \
         patch.object(lemmatizer, 'lemmatize', side_effect=lambda w: w):
        result = bow('hello', ['hello', 'world'], show_details=False)
    assert result.tolist() == [1, 0]
