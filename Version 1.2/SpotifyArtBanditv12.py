import sys
import os
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QFileDialog,
    QAction,
    QToolBar,
    QLabel,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineDownloadItem

def open_webview():
    webview.show()
    button.hide()


    # Create a custom download handler
    def download_requested(download: QWebEngineDownloadItem):
        # Prompt the user to choose the download path
        save_path, _ = QFileDialog.getSaveFileName(
            window, "Save File", os.path.expanduser("~"), "All Files (*.*)"
        )
        if save_path:
            download.setPath(save_path)
            download.accept()

    # Set the custom download handler for the web view
    profile = QWebEngineProfile.defaultProfile()
    profile.downloadRequested.connect(download_requested)

    webview.load(QUrl("https://spotisongdownloader.com/spotify-artwork-downloader/"))

    layout.addWidget(webview)
    button.hide()

    # Hide the webview and show the button when Home is clicked
    home_action.triggered.connect(lambda: (webview.hide(), button.show()))


def show_main_window():
    webview.hide()
    button.show()


def go_back():
    webview.back()


def go_forward():
    webview.forward()


def set_spotify_style(widget):
    # Set Spotify-like styles for the widget
    widget.setStyleSheet(
        """
        QWidget {
            background-color: #191414;
            color: #ffffff;
        }

        QPushButton {
            background-color: #1DB954;
            color: #ffffff;
            border: 2px solid #1DB954;
            border-radius: 8px;
            padding: 8px;
        }

        QPushButton:hover {
            background-color: #1ED760;
            border: 2px solid #1ED760;
        }

        QPushButton:pressed {
            background-color: #1AA34A;
            border: 2px solid #1AA34A;
        }

        QToolBar {
            background-color: #191414;
            border-bottom: 1px solid #1DB954;
        }

        QToolButton {
            color: #ffffff;
        }
    """
    )

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()

# Create a QHBoxLayout to organize the button and GIF label vertically
layout = QHBoxLayout(central_widget)

# Create a QLabel to display the GIF image
gif_label = QLabel()
gif_path = "G:\Software\py\Python Creations\Completed\Projects\SpotifyArtBandit\Images\spotifyartworkanimated2.gif"  # Replace this with the actual path to your GIF image
gif_movie = QMovie(gif_path)
gif_label.setMovie(gif_movie)
gif_movie.start()

# Create the button and add it to the layout
button = QPushButton("Click for Spotify ArtBandit")
button.clicked.connect(open_webview)
layout.addWidget(button)

window.setCentralWidget(central_widget)
window.setWindowTitle("Spotify ArtBandit")
window.setGeometry(150, 50, 600, 450)  # Set the window dimensions here (width=800, height=600)

# Set the window icon
icon_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "G:\Software\py\Python Creations\Completed\Projects\SpotifyArtBandit\Images\spotifylogo1.ico",
)
window.setWindowIcon(QIcon(icon_path))

# Add a toolbar for navigation buttons
toolbar = QToolBar()
toolbar.setMovable(False)  # Make the toolbar non-movable
window.addToolBar(toolbar)

# Add icons and actions for home, back, and forward buttons
home_action = QAction(QIcon("home.png"), "Home", window)
home_action.triggered.connect(
    show_main_window
)  # Show the main window when Home is clicked
toolbar.addAction(home_action)

back_action = QAction(QIcon("back.ico"), "Back", window)
back_action.triggered.connect(go_back)
toolbar.addAction(back_action)

forward_action = QAction(QIcon("forward.ico"), "Forward", window)
forward_action.triggered.connect(go_forward)
toolbar.addAction(forward_action)

webview = (
    QWebEngineView()
)  # Create the webview here so that it can be accessed by other functions

set_spotify_style(window)
set_spotify_style(button)

window.show()
app.exec_()
