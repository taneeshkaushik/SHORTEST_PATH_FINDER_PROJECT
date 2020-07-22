from flask import Flask, render_template, request, redirect, url_for, flash, Response,session

# import bs4
import requests
app = Flask(__name__)


@app.route('/')
def index():
	
	return render_template('index.html')


if __name__== "__main__":
	app.jinja_env.add_extension('jinja2.ext.loopcontrols')

	app.run(debug=True)



