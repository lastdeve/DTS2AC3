# Importing modules
import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QGridLayout

# Creating a custom widget class
class Converter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setting the window title and size
        self.setWindowTitle("MKV DTS to AC3 Converter")
        self.resize(400, 200)

        # Creating a grid layout
        layout = QGridLayout()

        # Creating a label for the input file
        self.input_label = QLabel("Input file: None")
        layout.addWidget(self.input_label, 0, 0)

        # Creating a button for choosing the input file
        self.input_button = QPushButton("Choose input file")
        self.input_button.clicked.connect(self.choose_input_file)
        layout.addWidget(self.input_button, 0, 1)

        # Creating a label for the output file
        self.output_label = QLabel("Output: None")
        layout.addWidget(self.output_label, 1, 0)

        # Creating a button for choosing the output file
        self.output_button = QPushButton("Choose output")
        self.output_button.clicked.connect(self.choose_output_file)
        layout.addWidget(self.output_button, 1, 1)

        # Creating a button for converting the file
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_file)
        layout.addWidget(self.convert_button, 2, 0, 1, 2)

        # Setting the layout for the widget
        self.setLayout(layout)

    def choose_input_file(self):
        # Opening a file dialog for choosing the input file
        filename, _ = QFileDialog.getOpenFileName(self, "Open input file", "", "MKV files (*.mkv)")
        
        # Checking if a valid file was chosen
        if filename:
            # Updating the input label and storing the filename
            self.input_label.setText(f"Input file: {filename}")
            self.input_filename = filename

    def choose_output_file(self):
        # Opening a file dialog for choosing the output file
        filename, _ = QFileDialog.getSaveFileName(self, "Save output file", "", "MKV files (*.mkv)")

        # Checking if a valid file was chosen
        if filename:
            # Updating the output label and storing the filename
            self.output_label.setText(f"Output file: {filename}")
            self.output_filename = filename

    def convert_file(self):
        # Checking if both input and output files are set
        if hasattr(self, "input_filename") and hasattr(self, "output_filename"):
            # Running the ffmpeg command with subprocess
            command = ["ffmpeg", "-i", self.input_filename, "-c:v", "copy", "-c:a", "ac3", self.output_filename]
            subprocess.run(command)
            
            # Showing a message that the conversion is done
            self.convert_button.setText("Done!")
        
# Creating an application instance
app = QApplication(sys.argv)

# Creating and showing the converter widget
converter = Converter()
converter.show()

# Starting the main loop
sys.exit(app.exec_())