import os
import time
import sys
import json
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from Ui_DTS2AC3 import Ui_MainWindow
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


class DTS2AC3Converter(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Load JSON file
        with open("config.json", "r") as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError:
                self.show_message_box(
                    "Error: Invalid JSON format in config file.")
                exit()
        # Check if JSON is empty or deprecated
        if not config or "output_dir" not in config:
            self.show_message_box("Error: Invalid config file format.")
            exit()
        # Get output directory from JSON
        self.output_dir = config["output_dir"]
        # Initialize UI elements
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)
        self.converting.setVisible(False)
        self.lineEdit_2.setText(self.output_dir)
        self.pushButton.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.select_input_file)
        self.pushButton_3.clicked.connect(self.select_output_dir)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Input MKV File", "", "MKV Files (*.mkv)")
        if file_path:
            self.lineEdit.setText(file_path)

    def select_output_dir(self):
        output_dir = QFileDialog.getExistingDirectory(
            self, "Select Output Directory", "")
        if output_dir:
            self.lineEdit_2.setText(output_dir)

    def convert(self):
        input_file = self.lineEdit.text()
        output_dir = self.lineEdit_2.text()

        if not input_file:
            self.show_message_box("Please select the input file.")
            return

        if not output_dir:
            self.show_message_box("Please select output directory.")
            return

        if not os.path.isfile(input_file):
            self.show_message_box("Input file is not valid.")
            return

        if os.path.splitext(input_file)[1].lower() != '.mkv':
            self.show_message_box("Input file is not an MKV file.")
            return

        if not os.path.isdir(output_dir):
            self.show_message_box("Output directory is not valid.")
            return

         # Write new output directory to JSON file if checkbox is checked
        if self.checkBox.isChecked():
            with open('config.json', 'w') as f:
                config = {'output_dir': output_dir}
                json.dump(config, f)

        output_file = os.path.join(output_dir, os.path.basename(input_file))

        command = f"ffmpeg -i \"{input_file}\" -c:v copy -c:a ac3 \"{output_file}\""
        self.run_command(command)
        self.pushButton.setText("Cancel")
        self.progressBar.setVisible(True)
        self.converting.setVisible(True)
        self.pushButton.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        if self.pushButton.text() == "Cancel":
            self.pushButton.setText("Canceling...")
            self.converting.setText("Terminating...")
            current_dir = os.getcwd()
            batch_file_path = os.path.join(current_dir, 'cancel.bat')
            subprocess.call(batch_file_path)
            time.sleep(3)
            QMessageBox.information(
                self, "Button Clicked", "Conversion canceled")
            # Initialize UI elements
            self.setupUi(self)
            self.progressBar.setValue(0)
            self.progressBar.setVisible(False)
            self.converting.setVisible(False)
            self.lineEdit_2.setText(self.output_dir)
            self.pushButton.clicked.connect(self.convert)
            self.pushButton_2.clicked.connect(self.select_input_file)
            self.pushButton_3.clicked.connect(self.select_output_dir)
            self.pushButton.setText("Convert")

    def run_command(self, command):
        self.thread = FFmpegThread(command)
        self.thread.progress.connect(self.update_progress)
        self.thread.finished.connect(self.on_finished)
        self.thread.start()

    def update_progress(self, value):
        self.progressBar.setValue(value)
    
    def on_finished(self):
        if self.pushButton.text() == "Cancel":
            self.progressBar.setValue(100)
            self.pushButton.setText("Resets...")
            self.converting.setText("Please wait...")
            QMessageBox.information(
                self, "Conversion complete", "Conversion completed successfully")
            time.sleep(3)
            # Initialize UI elements

            def __init__(self):
                super().__init__()
            # Load JSON file
            with open("config.json", "r") as f:
                try:
                    config = json.load(f)
                except json.JSONDecodeError:
                    self.show_message_box(
                        "Error: Invalid JSON format in config file.")
                    exit()
            # Check if JSON is empty or deprecated
            if not config or "output_dir" not in config:
                self.show_message_box("Error: Invalid config file format.")
                exit()
            # Get output directory from JSON
            self.output_dir = config["output_dir"]
            # Initialize UI elements
            self.setupUi(self)
            self.progressBar.setValue(0)
            self.progressBar.setVisible(False)
            self.converting.setVisible(False)
            self.lineEdit_2.setText(self.output_dir)
            self.pushButton.clicked.connect(self.convert)
            self.pushButton_2.clicked.connect(self.select_input_file)
            self.pushButton_3.clicked.connect(self.select_output_dir)
            self.pushButton.setText("Convert")

    def show_message_box(self, message):
        QMessageBox.warning(self, "DTS2AC3", message)


class FFmpegThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        process = subprocess.Popen(
            self.command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        duration_seconds = None

        while process.poll() is None:
            line = process.stderr.readline().strip()
            if "Duration:" in line:
                duration = line.split("Duration:")[1].strip().split(",")[0]
                duration_seconds = self.time_to_seconds(duration)

            if "time=" in line:
                time = line.split("time=")[1].strip().split()[0]
                time_seconds = self.time_to_seconds(time)
                progress = int(time_seconds / duration_seconds * 100)
                self.progress.emit(progress)

        # read any remaining output
        for line in process.stderr:
            pass

        process.wait()

    def time_to_seconds(self, time_str):
        hours, minutes, seconds = time_str.split(":")
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = DTS2AC3Converter()
    converter.show()
    sys.exit(app.exec_())
