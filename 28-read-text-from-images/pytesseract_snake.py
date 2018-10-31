from PIL import Image
import pytesseract

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'~/.virtualenvs/playground/bin/pytesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
s = pytesseract.image_to_string(Image.open('readthis.png'))

# LANGUAGE = "english"
# SENTENCES_COUNT = 2

# if __name__ == "__main__":

#     parser = PlaintextParser.from_string(s, Tokenizer(LANGUAGE))
#     stemmer = Stemmer(LANGUAGE)

#     summarizer = Summarizer(stemmer)
#     summarizer.stop_words = get_stop_words(LANGUAGE)

#     for sentence in summarizer(parser.document, SENTENCES_COUNT):
#         print(sentence)