import os
from flask import Flask, render_template
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/')
def home():
	x = datetime.now(timezone("Asia/Kolkata"))
	date = x.strftime('%d/%m/%Y')
	time = x.strftime('%X')
	return render_template('index.html', date=date, time=time)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))