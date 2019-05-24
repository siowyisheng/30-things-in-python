# Jupyter Notebook

## Tie a jupyter notebook to the .py equivalent, and edit either from the other

## Requirements

```
$ pip install jupytext
$ jupyter notebook --generate-config
```

Edit `~/.jupyter/jupyter_notebook_config.py` and append the following:

```
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
```

## Creating the duality

To enable paired notebooks, open the notebook, then within the menu, _Edit_ --> _Edit Notebook Metadata_, and add `"jupytext": {"formats": "ipynb,py"},` to the metadata within the outermost `{}`.

```
{
  "jupytext": {"formats": "ipynb,py"},
  "kernelspec": {
    (...)
  },
  "language_info": {
    (...)
  }
}
```

## Resources

[The repo](https://github.com/mwouts/jupytext)
