import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineDownloadItem

def open_webview():
    app = QApplication(sys.argv)
    window = QMainWindow()
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    webview = QWebEngineView()

    # Create a custom download handler
    def download_requested(download: QWebEngineDownloadItem):
        # Prompt the user to choose the download path
        save_path, _ = QFileDialog.getSaveFileName(window, "Save File", os.path.expanduser("~"), "All Files (*.*)")
        if save_path:
            download.setPath(save_path)
            download.accept()

    # Set the custom download handler for the web view
    profile = QWebEngineProfile.defaultProfile()
    profile.downloadRequested.connect(download_requested)

    webview.load(QUrl('https://spotisongdownloader.com/spotify-artwork-downloader/'))

    layout.addWidget(webview)

    window.setCentralWidget(central_widget)
    window.setWindowTitle('SpotifyArtBandit')
    window.setGeometry(100, 100, 800, 450)
    window.show()

    # Set the window icon
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'G:\Software\py\Python Creations\Completed\Projects\SpotifyArtBandit\Images\spotifylogo1.ico')
    window.setWindowIcon(QIcon(icon_path))

    sys.exit(app.exec_())

app = QApplication(sys.argv)
button = QPushButton('Click for Spotify Artwork Downloader')
button.clicked.connect(open_webview)
layout = QVBoxLayout()
layout.addWidget(button)
central_widget = QWidget()
central_widget.setLayout(layout)
window = QMainWindow()
window.setCentralWidget(central_widget)
window.setWindowTitle('SpotifyArtBandit')
window.setGeometry(100, 100, 300, 100)
window.show()

# Set the window icon
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'G:\Software\py\Python Creations\Completed\Projects\SpotifyArtBandit\Images\spotifylogo1.ico')
window.setWindowIcon(QIcon(icon_path))


