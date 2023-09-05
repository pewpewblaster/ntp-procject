import sys
import requests
import time
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar, QLineEdit


class DownloadThread(QThread):
    update_progress = pyqtSignal(int, int, int)
    download_complete = pyqtSignal()
    download_stopped = pyqtSignal()

    def __init__(self, url, filename, speed_limit_kb, parent=None):
        super().__init__(parent)
        self.url = url
        self.filename = filename
        self.speed_limit_kb = speed_limit_kb
        self.stopped = False

    def run(self):
        response = requests.get(self.url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        with open(self.filename, 'wb') as file:
            start_time = time.time()
            downloaded = 0
            for chunk in response.iter_content(chunk_size=1024):
                if self.stopped:
                    break

                elapsed_time = max(1, time.time() - start_time)  # Ensure elapsed_time is at least 1 second
                if self.speed_limit_kb and elapsed_time < downloaded / self.speed_limit_kb:
                    time.sleep((downloaded / self.speed_limit_kb) - elapsed_time)

                file.write(chunk)
                downloaded += len(chunk)
                download_speed_kb = int(downloaded / elapsed_time)
                self.update_progress.emit(downloaded * 100 // total_size, downloaded // 1024, download_speed_kb)


            if not self.stopped:
                self.download_complete.emit()
            else:
                self.download_stopped.emit()


class DownloaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('HTTP Downloader')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.url_label = QLabel('URL:')
        self.url_input = QLineEdit()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        self.speed_label = QLabel('Speed Limit (KB/s):')
        self.speed_input = QLineEdit()
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_input)

        self.progress_label = QLabel('Progress:')
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)

        self.percentage_label = QLabel('Percentage: 0%')
        self.speed_label = QLabel('Download Speed: 0 KB/s')
        self.downloaded_label = QLabel('Downloaded: 0 KB')
        layout.addWidget(self.percentage_label)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.downloaded_label)

        self.download_button = QPushButton('Download')
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        self.stop_button = QPushButton('Stop Download')
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_download)
        layout.addWidget(self.stop_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.download_thread = None

    def start_download(self):
        url = self.url_input.text()
        speed_limit = int(self.speed_input.text()) if self.speed_input.text().isdigit() else 0
        filename = url.split('/')[-1]

        self.progress_bar.setValue(0)
        self.percentage_label.setText('Percentage: 0%')
        self.speed_label.setText('Download Speed: 0 KB/s')
        self.downloaded_label.setText('Downloaded: 0 KB')
        self.download_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        self.download_thread = DownloadThread(url, filename, speed_limit)
        self.download_thread.update_progress.connect(self.update_progress)
        self.download_thread.download_complete.connect(self.download_complete)
        self.download_thread.download_stopped.connect(self.download_stopped)
        self.download_thread.start()

    def stop_download(self):
        if self.download_thread:
            self.download_thread.stopped = True
            self.stop_button.setEnabled(False)

    def update_progress(self, percentage, downloaded_kb, speed_kb):
        self.progress_bar.setValue(percentage)
        self.percentage_label.setText(f'Percentage: {percentage}%')
        self.speed_label.setText(f'Download Speed: {speed_kb} KB/s')
        self.downloaded_label.setText(f'Downloaded: {downloaded_kb} KB')

    def download_complete(self):
        self.download_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        print("Download complete!")

    def download_stopped(self):
        self.download_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        print("Download stopped.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec())
