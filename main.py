import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Change Title
        self.setWindowTitle("First Window")

        # Set Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create Label
        my_label = qtw.QLabel("What is your name?")
        # Change Font Size
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)

        # Create an Entry Box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a button
        my_button = qtw.QPushButton("Submit", clicked = lambda: press_it())

        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            # Add Name to Label
            my_label.setText(f'Hello {my_entry.text()}')
            # Reset the Entry Box
            my_entry.setText("")



app = qtw.QApplication([])

# Initialize Main Window
mw = MainWindow()

# Run the app
app.exec_()