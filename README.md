# Mediassist Chatbot

This repository contains a simple chatbot application. Automated tests are
provided using `pytest`.

## Running Tests

1. Install dependencies (for the tests we only need `pytest`, `numpy` and `nltk`):

```bash
pip install -r requirements.txt
```

Alternatively, install the packages individually:

```bash
pip install pytest numpy nltk
```

2. Run the test suite from the repository root:

```bash
pytest
```

This will discover tests in the `tests/` directory and execute them.
