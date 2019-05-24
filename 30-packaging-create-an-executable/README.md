# Packaging into Executable

## Turn a script into an executable, runnable without Python installed

## Requirements

```
$ pip install pyinstaller
```

## Running it

```
$ pyinstaller --onefile --windowed snake_textgen.py
```

This should create a .app and a .exe, which write a `out.txt`(probably to the home folder) when executed.

## Resources

[PyInstaller docs](https://pyinstaller.readthedocs.io/en/stable/index.html)
