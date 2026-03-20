import os
import webbrowser
import subprocess

def open_apps():
    # Open default browser (or specify one)
    webbrowser.open("https://www.gmail.com")  # Replace with your homepage
    webbrowser.open("https://www.google.com")
    # Open Webex (adjust path if installed elsewhere)
    webex_path = r"C:\Users\jothi\AppData\Local\CiscoSparkLauncher\CiscoCollabHost.exe"
    if os.path.exists(webex_path):
        subprocess.Popen([webex_path])
    else:
        print("Webex path not found. Please update the script.")

    # Open Zoom (adjust path if installed elsewhere)
    zoom_path = r"C:\Users\jothi\AppData\Roaming\Zoom\bin\Zoom.exe"
    if os.path.exists(zoom_path):
        subprocess.Popen([zoom_path])
    else:
        print("Zoom path not found. Please update the script.")

if __name__ == "__main__":
    open_apps()