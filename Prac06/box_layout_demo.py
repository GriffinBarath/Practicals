from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handleGreet(self):
        print("greet")
        self.root.ids.outputLabel.text = "Hello " + self.root.ids.inputName.text

    def handleClear(self):
        self.root.ids.outputLabel.text = "Enter your name"
        self.root.ids.inputName.text = ''


BoxLayoutDemo().run()
