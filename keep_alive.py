from flask import Flask, send_file
from threading import Thread
import os

app = Flask("")

@app.route('/')
def _home():
    return "BOT Alive and healthy! <a href=/logs/servers/>logs "

@app.route("/help")
def _help():
	return("soon")

@app.route("/logs/servers/")
def _log_servers():
	string = "Servers:<ul>"
	for i in os.listdir("logs"):
		string += (f"<li><a href=/logs/servers/{i}>{i}")
	return string

@app.route("/logs/servers/<path:path>/")
def _channels_inserver(path):
	string = "Channels:<ul>"
	for i in os.listdir(f"logs/{path}"):
		string += (f"<li><a href=/logs/servers/{path}/{i}>{i}")
	return string

@app.route("/logs/servers/<path:serverid>/<path:channelid>")
def _get_logfile(serverid, channelid):
	return send_file(os.path.join("logs",serverid,channelid))

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()