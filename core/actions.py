# import subprocess


# def execute_action(text):

#     text = text.lower()

#     # YouTube
#     if "open youtube" in text:

#         subprocess.Popen(
#             "explorer https://www.youtube.com",
#             shell=True
#         )

#         return "Opening YouTube, sir."

#     # Google
#     if "open google" in text:

#         subprocess.Popen(
#             "explorer https://www.google.com",
#             shell=True
#         )

#         return "Opening Google, sir."

#     # Calculator
#     if "open calculator" in text:

#         subprocess.Popen(
#             "calc.exe"
#         )

#         return "Opening Calculator, sir."

#     # Notepad
#     if "open notepad" in text:

#         subprocess.Popen(
#             "notepad.exe"
#         )

#         return "Opening Notepad, sir."

#     return None

import subprocess


def execute_action(text):

    text = text.lower().strip()

    # Open YouTube
    if "open youtube" in text:
        subprocess.Popen(
            "explorer https://www.youtube.com",
            shell=True
        )
        return "Opening YouTube, sir."

    # Open Google
    elif "open google" in text:
        subprocess.Popen(
            "explorer https://www.google.com",
            shell=True
        )
        return "Opening Google, sir."

    # Open Calculator
    elif "open calculator" in text:
        subprocess.Popen("calc.exe")
        return "Opening Calculator, sir."

    # Open Notepad
    elif "open notepad" in text:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad, sir."

    # Open Chrome
    elif "open chrome" in text:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Opening Chrome, sir."

    return None