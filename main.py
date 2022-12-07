# import libraries
from kivymd.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
import re

# set the size of the app window
Window.size = (500, 700)


class MyLayout(Widget):
    # create a function to clear the text input
    def clear(self):
        self.ids.calc_input.text = '0'

    # create a variable that contains the number when pressed
    def button_press(self, button):
        prior = self.ids.calc_input.text
        # Test fo r error first
        if 'Error' in prior:
            prior = ''
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # aad the math signs to the text string when clicked
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        signs = ['+', '-', '*', '÷']
        last = prior[-1]
        if last in signs:
            pass
        else:
            self.ids.calc_input.text = f'{prior}{sign}'

    # The calculator should be able to accept decimals
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = re.split('\*|\+|÷|-', prior)
        if '.' not in num_list[-1]:
            self.ids.calc_input.text = f'{prior}.'
        else:
            pass

    def percent(self):
        prior = self.ids.calc_input.text
        try:
            percentage = float(prior) / 100
            self.ids.calc_input.text = str(percentage)
        except:
            self.ids.calc_input.text = 'Error'

    # create a function to delete input
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # set number to negative or pistive

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if '-' in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Evaluate the input text
    def equals(self):
        prior = self.ids.calc_input.text
        prior = prior.replace('÷', '/')
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
