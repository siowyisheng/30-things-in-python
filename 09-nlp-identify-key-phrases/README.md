# Natural Language Processing

## Identify Significant Phrases in a Text

## Requirements

```
pip install textacy
python -m spacy download en
```

## Running it

```
$ python spacy_snakes.py
```

## Key Remarks

`doc = textacy.Doc(text)` turns the string into a parseable text, `textacy.keyterms.sgrank()` ranks significant phrases, and `textacy.TextStats(doc).readability_stats` gives us information about the text's readability.
