# Word Cloud

## Visualize long texts with a word cloud

## Requirements

```
pip install pillow
pip install matplotlib
pip install numpy
pip install wordcloud
```

## Running it

```
$ python snake_wordcloud.py
```

It should create `snakes.png`.

## Key Remarks

We turn the image into a mask with `mask = np.array(Image.open("pythonlogo.png"))`. Then create the word cloud with `wc = WordCloud()` and save it with `wc.to_file()`. `blue_color_func()` simply allows us to create some variation in the colors for the text.

## Resources

[The wordcloud repo](https://github.com/amueller/word_cloud)

## Note

The text was from [Project Gutenberg](https://www.gutenberg.org/), which offers over 57,000 free books.
