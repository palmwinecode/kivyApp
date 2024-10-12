from kivy.app import App # type: ignore
from kivy.uix.gridlayout import GridLayout # type: ignore
from kivy.uix.label import Label # type: ignore
from kivy.uix.textinput import TextInput # type: ignore
from kivy.uix.button import Button # type: ignore

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

        # Print button
        self.print_btn = Button(text="Submit")
        self.print_btn.bind(on_press = self.print_details)
        self.add_widget(self.print_btn)

    # Function to print details
    def print_details(self, instance):
        # Print details
        print(f"Name of student is {self.student_name.text}")
        print(f"Score of student is {self.student_score.text}")
        print(f"Gender of student is {self.student_gender.text}")

        # Print newline
        print()

# Base class
class StudentApp(App):
    
    def build(self):
        return ChildApp()
    
if __name__ == "__main__":
    StudentApp().run()