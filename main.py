from kivy.app import App # type: ignore
from kivy.uix.gridlayout import GridLayout # type: ignore
from kivy.uix.label import Label # type: ignore
from kivy.uix.textinput import TextInput # type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.uix.popup import Popup # type: ignore

class ChildApp(GridLayout):

    def __init__(self, **kwargs):
        # Inherit init from parent class
        super(ChildApp, self).__init__()

        # Define number of columns
        self.cols = 1

        # Create an inner grid
        self.inner_grid = GridLayout()

        # Define number of columns
        self.inner_grid.cols = 2
        
        # Add title
        self.add_widget(Label(text="STUDENT DETAILS"))

        # Create labels and fields
        # Student name
        self.inner_grid.add_widget(Label(text="Name"))
        self.student_name = TextInput(multiline=False)
        self.inner_grid.add_widget(self.student_name)

        # Student score
        self.inner_grid.add_widget(Label(text="Score"))
        self.student_score = TextInput(multiline=False)
        self.inner_grid.add_widget(self.student_score)

        # Student gender
        self.inner_grid.add_widget(Label(text="Gender"))
        self.student_gender = TextInput(multiline=False)
        self.inner_grid.add_widget(self.student_gender)
        
        # Add inner grid to main grid
        self.add_widget(self.inner_grid)

        # Submit button
        self.submit_btn = Button(text="Submit")
        self.submit_btn.bind(on_press = self.on_submit)
        self.add_widget(self.submit_btn)

    # Function to popup details
    def on_submit(self, instance):
        # Are fields empty?
        if not self.student_name.text.strip() or not self.student_score.text or not self.student_gender.text:
            message = "Please fill in all fields"

        # Is score an integer?
        elif not self.student_score.text.isdigit():
            message = "Score must be an integer"

        # Is score in valid range(0-100)?
        elif not int(self.student_score.text).strip() in range(0, 101):
            message = "Score is not valid"

        # Is gender valid?
        elif not self.student_gender.text.lower() in ["male", "female"]:
            message = "Gender not valid\nHint: Male or Female"

        else:        
            # Message to pop up
            message = f"{self.student_name.text} is {self.student_gender.text} and scored {self.student_score.text}"

        # Create popup window
        popup = Popup(title="Prompt", content=Label(text=message), size_hint=(None, None), size=(400, 200))

        # Open popup
        popup.open()

# Base class
class StudentApp(App):
    
    def build(self):
        return ChildApp()
    
if __name__ == "__main__":
    StudentApp().run()