# import webbrowser

# webbrowser.open("https://apple.com")

import webbrowser

# Specify the browser to use
chrome_path = '/usr/bin/google-chrome'  # Adjust the path if necessary
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open the URL using the specified browser
webbrowser.get('chrome').open("https://apple.com")

