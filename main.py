import webview
import os
import sys

# This class is exposed to JavaScript
class Api:
    def upload_file(self, filename, content):
        print("✅ File received from JS:", filename)
        print("Preview of content:", content[:200])  # print first 200 chars
        # Save the file if you want
        # with open(f"uploads/{filename}", "w", encoding="utf-8", errors="ignore") as f:
        #     f.write(content)

# Function needed for compiling with PyInstaller
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Path to your HTML file
# In your Tkinter code, use this function to get the correct path
html_file = resource_path("index.html")
# Now you can use `html_file` to load your HTML content

if __name__ == '__main__':
    api = Api()

    # Open the HTML file in a webview window
    webview.create_window("Upload App", f"file://{html_file}", js_api=api)
    webview.start()
