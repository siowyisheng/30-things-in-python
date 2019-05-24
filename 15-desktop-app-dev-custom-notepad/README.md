# Natural Language Processing

## Summarise article text straight from a URL

## Requirements

```
pip install PyQt5
```

## Running it

```
$ python snakepad.py
```

## Key Remarks

The `PyQt5.QtGui.QPlainTextEdit` object provides a nice framework out of the box for a textinput GUI object.

```
snakey_action = QAction(QIcon(os.path.join('images', 'snake.png')), "Snake", self)
snakey_action.setStatusTip("Get snaked")
snakey_action.triggered.connect(self.snake)
edit_toolbar.addAction(snakey_action)
edit_menu.addAction(snakey_action)
```

This creates an action with a button/icon in the toolbar, connected to `self.snake`, which we define below.

```
    def snake(self):
        self.editor.insertPlainText("Ssssssss I'm a sssssnake")
```

## Credit

This code was adapted from [no2pads from 15-minute-apps](https://github.com/mfitzp/15-minute-apps/tree/master/notepad).

## Resources

[PyQt5 Tutorial on pythonspot](https://pythonspot.com/pyqt5/)
