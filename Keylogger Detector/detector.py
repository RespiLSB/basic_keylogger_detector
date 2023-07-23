import os
import hashlib
import psutil
import time
import requests

# Virus Total API Key, must register to get your private API Key. (This will not work if you use my API key)
VTAPIKEY = 'ed673c505adcf45d5cdcd8e1c9b07899b2a5fad62d52afe47c371c5edfd20715'

# Reads the hashes from 'hash.txt', (The detector application must be in the same directory as the hash.txt for this to work.)
with open("hash.txt", "r") as file:
    known_hashes = set(line.strip() for line in file) # Will try to match the captured hash with every hash on a new line.

# Gets the hashes from the details in the task manager.
def get_process_hashes():
    process_hashes = {}
    for process in psutil.process_iter(['pid', 'name', 'exe']): # gets the process ID for recognition, the name and the file type.
        try:
            exe = process.info['exe']
            if exe:
                name = process.info['name'] # gives the process info a name
                path = process.info['exe'] # gives the application type
                with open(exe, 'rb') as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest() # Takes the hashes from each file, converts it into sha256 hash.
                process_hashes[process.info['pid']] = {'hash': file_hash, 'name': name, 'path': path} # GEts the hash of the file, the name and the path to output in the end.
        except Exception as e:
            pass
    return process_hashes

# This section is responsible for processing the hash through virus total.
def check_virustotal(hash):
    try:
        url = f"https://www.virustotal.com/api/v3/files/{hash}" # The URL link to with the {hash} tag at the end to process the to send the hash to virus total.
        headers = {"x-apikey": VTAPIKEY} # Checks for API key.
        response = requests.get(url, headers=headers) # Receiving response from Virus Total
        data = response.json()
        if "data" in data and "attributes" in data["data"] and "last_analysis_results" in data["data"]["attributes"]:
            for scan in data["data"]["attributes"]["last_analysis_results"].values():
                if scan.get("result") and ("keylogger" in scan["result"].lower() or "spy" in scan["result"].lower() or "spyware" in scan["result"].lower()): # This is the section which validates a keylogger, if it comes back as "spy", "spyware" or "keyloggeer" it immediately informs the user.
                    return True
        return False
    except Exception as e:
        print(e)
        return False

def main():
    while True:
        process_hashes = get_process_hashes()
        for pid, process in process_hashes.items(): # Giving the process an ID for the application ro recognize
            if process['hash'] not in known_hashes: # if the hash doesn't match with known hashes .txt
                is_keylogger = check_virustotal(process['hash'])
                if is_keylogger: # if the value comes back as 'keylogger, spyware or spy' from virus total then its recognized as a keylogger.
                    print(f"Keylogger detected: PID {pid}, Name {process['name']}, Path {process['path']}") # The response here is what we get in the end result, validation for keylogger detector, ID of process, Name of file and path of file.
        time.sleep(60) # Puts the application on timeout to not overload VirusTotal or itself.

if __name__ == "__main__":
    main()
