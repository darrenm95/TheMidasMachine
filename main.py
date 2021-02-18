from flask import Flask, request, render_template
import yfinance as yf
import requests 
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('index.html')

@app.route('/<ticker>', methods=['GET', 'POST'])
def display_company_name(ticker):

      msft = yf.Ticker(ticker)
      results = msft.info
    
      return results 



if __name__ == "__main__":
    app.run()