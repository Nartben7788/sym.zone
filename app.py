from flask import Flask, render_template, redirect, flash, url_for

app=Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')


