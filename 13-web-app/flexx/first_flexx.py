from flexx import flx

class Example(flx.Widget):

    def init(self):
        flx.Button(text='Hello')
        flx.Button(text='World')

app = flx.App(Example)
app.launch('app')
flx.init_notebook()
