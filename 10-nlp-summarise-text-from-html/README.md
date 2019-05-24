# Natural Language Processing

## Summarise article text straight from a URL

## Requirements

```
pip install sumy
```

## Running it

```
$ python sumy_snakes.py
```

## Key Remarks

It first reads the html and splits the extracted relevant strings into tokens(words/pockets of meaning) with `HtmlParser.from_url(url, Tokenizer(LANGUAGE))`. Then, it creates a Summarizer for the language with `summarizer = Summarizer(stemmer)`. The summariser gets a list of stop words, which include grammatical words like 'the', 'is', 'are'.

## Credit

This code was adapted from [the example at the github repo](https://github.com/miso-belica/sumy#python-api).
