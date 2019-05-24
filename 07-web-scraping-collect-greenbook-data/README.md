# Web Scraping

## Get data from an online directory into a csv

## Requirements

```
pip install scrapy
pip install lxml
pip install cryptography
```

If the above fails, you can also try setting up with **Miniconda** or [**Anaconda**](https://www.anaconda.com/).

## Running it

```
$ cd greenbook
$ scrapy crawl greenbook -s LOG_FILE=scrapy.log -o data.csv
```

It will take a while to complete.

## Key Remarks

We only need to edit the `greenbook/greenbook/spiders/greenbook.py` file. The rest of the project is created by `$ scrapy startproject greenbook`. The key points in the code involve extracting the href attribute from certain links in the [DOM](https://www.w3schools.com/js/js_htmldom.asp) using [xpath](https://doc.scrapy.org/en/xpath-tutorial/topics/xpath-tutorial.html), following those links by yielding a `scrapy.Request()`, and then continuing on until we get to our required data, and yield that data by again selecting it using xpath.

## Resources

[Scrapy docs](https://doc.scrapy.org/en/latest/)
