from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Pobranie danych z API NBP
def get_exchange_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"
    response = requests.get(url)
    data = response.json()
    return data[0]['rates']

# Strona główna i przeliczanie waluty
@app.route('/', methods=['GET', 'POST'])
def index():
    rates = get_exchange_rates()
    result = None
    selected_currency = None
    amount = None

    if request.method == 'POST':
        amount = float(request.form['amount'])
        selected_currency = request.form['currency']
        rate = next((item for item in rates if item["code"] == selected_currency), None)

        if rate:
            result = round(amount * rate['ask'], 2)  # Wartość kupna danej waluty

    return render_template('index.html', rates=rates, result=result, selected_currency=selected_currency, amount=amount)

if __name__ == "__main__":
    app.run(debug=True)