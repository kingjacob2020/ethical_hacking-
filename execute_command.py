#!/usr/bin/env python



import subprocess, smtplib



command = "msg * you have been hacked"

subprocess.Popen(command, shell=True)
