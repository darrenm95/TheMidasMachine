from flask import Flask, request, render_template
import yfinance as yf
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('index.html')
    

@app.route('/display_company_name', methods=['GET', 'POST'])
def display_company_name():

    ticker=request.form['ticker']
    ticker_obj = yf.Ticker(ticker)
    company_name_short = ticker_obj.info['shortName']
    company_name_long = ticker_obj.info['longName']
    return f"Short Name: {company_name_short}, Long Name: {company_name_long}"
if __name__ == "__main__":
    app.run()