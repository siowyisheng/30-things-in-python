# Data Science

## Predict the survival chance of a person on the [Titanic](https://en.wikipedia.org/wiki/Sinking_of_the_RMS_Titanic).

## Requirements

```
pip install pandas
pip install sklearn
```

If the above fails, you can also try setting up with **Miniconda** or [**Anaconda**](https://www.anaconda.com/).

## Running it

Run the [jupyter notebook](https://www.youtube.com/watch?v=jZ952vChhuI).

## Key Remarks

We load the csv data in with `pd.read_csv()`, then choose a classifier(model) with `clf = DecisionTreeClassifier()`, then train it with `clf.fit(features, target)` and finally use it to make predictions with `clf.predict()` and `clf.predict_proba()`.
