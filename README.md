# MRI_converter
Convert enhanced multiframe MRI to standard DICOM format using drag and drop GUI

This tool converts enhanced multi-frame DICOM MRIs into standard single-frame DICOM files that can be viewed in most DICOM viewers. Each image sequence is saved in its own folder and named for the patient and sequence type (e.g., SPGR, T2, DWI).
⚠️ Disclaimer: This tool is intended for research and educational purposes only. It is not validated for clinical use. Do not use this tool for clinical diagnosis or treatment.
________________________________________
📥 How to Install and Run 
1. Download and Install Python
Go to the official Python website and download Python for your operating system:
👉 https://www.python.org/downloads/
When installing Python:
•	On Windows, check the box that says Add Python to PATH before clicking "Install Now."
•	On macOS, you can also install Python using Homebrew (brew install python) if preferred.
After installation, open a terminal (or Command Prompt) and type:
python --version
You should see something like Python 3.11.0
________________________________________
2. Install pip (if it’s not already installed)
pip is Python’s package installer. It usually comes with Python, but if not:
On Windows:
•	Open Command Prompt
•	Run the following command:
•	python -m ensurepip --default-pip
On macOS or Linux:
•	Open Terminal
•	Run:
•	python3 -m ensurepip --default-pip
To test it, type:
pip --version
You should see the pip version if it was installed correctly.
________________________________________
3. Install Required Python Packages
Open your terminal or Command Prompt and type:
pip install pydicom tkinter tkinterdnd2
This installs the packages used in the script.
________________________________________
4. Download the Script
Download the Python script file E2S_mri_converter_gui.py from this repository.
Place it somewhere easy to find (like your Desktop).
________________________________________
5. Run the Script
Double-click the script file, or run it from terminal:
On Windows:
python E2S_mri_converter_gui.py
On macOS:
python3 E2S_mri_converter_gui.py
________________________________________
6. Use the GUI
A simple window will appear. Drag and drop your enhanced multi-frame DICOM files into the window, then click "Convert to Standard MRIs".
•	Converted images will appear in a new folder on your Desktop called “Standard MRIs”
•	Each image sequence will be saved in its own folder
•	You can now open these folders in your DICOM viewer 
________________________________________
📂 Output Structure Example
Standard MRIs/
├── Smith_SPGR_UID.../
│   ├── IMG_0001.dcm
│   ├── IMG_0002.dcm
│   └── ...
├── Smith_T2_UID.../
│   ├── IMG_0001.dcm
│   └── ...
________________________________________
🛠 Troubleshooting
•	If you get an error about pip not being found, ensure Python and pip are added to your PATH.
How to Add pip to PATH on Windows:
1.	Search for Environment Variables in the Windows search bar and open it.
2.	In the System Properties window, click Environment Variables.
3.	In the System Variables section, find and select the Path variable, then click Edit.
4.	Click New, and add the path to your pip installation. This is usually:
o	C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts (replace "YourUsername" and version number accordingly)
5.	Click OK to save and close all windows.
6.	Close and reopen your terminal or Command Prompt and type:
7.	pip --version
You should now see the pip version.
•	If the GUI doesn't appear, make sure you've installed tkinterdnd2 correctly and that your Python version includes tkinter
•	If you’re using macOS and get an error about security, you may need to right-click and choose "Open" instead of double-clicking the script
________________________________________
🧪 Disclaimer
This software is provided "as is" without any warranties. It is intended for educational or research purposes only and should not be used in clinical workflows.

