import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from Ui_DTS2AC3 import Ui_MainWindow
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


class DTS2AC3Converter(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.select_input_file)
        self.pushButton_3.clicked.connect(self.select_output_dir)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Input MKV File", "", "MKV Files (*.mkv)")
        if file_path:
            self.lineEdit.setText(file_path)

    def select_output_dir(self):
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory", "")
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

        output_file = os.path.join(output_dir, os.path.basename(input_file))

        command = f"ffmpeg -i \"{input_file}\" -c:v copy -c:a ac3 \"{output_file}\""
        self.run_command(command)

    def run_command(self, command):
        self.thread = FFmpegThread(command)
        self.thread.progress.connect(self.update_progress)
        self.thread.finished.connect(self.on_finished)
        self.thread.start()

    def update_progress(self, value):
        self.progressBar.setValue(value)

    def on_finished(self):
        self.progressBar.setValue(100)
        self.show_message_box("Conversion completed successfully.")

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