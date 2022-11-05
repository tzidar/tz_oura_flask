from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    data = [
            ("2021-05-18", 48),
            ("2021-05-19", 48),
            ("2021-05-20", 49),
            ("2021-05-21", 52)
    ]

    df = pd.read_csv(
        'https://gist.githubusercontent.com/tzidar/752745bde496f0ae8290beffa620760c/raw/82eaaa973572296ebe498878080dc7ab928d10a3/sleep_data_05_27_2022.csv')
    aa = len(df)
    sleep_score = list(df.score.values)
    sleep_date = list(df.summary_date)
    hrv_avg = list(df.hr_average)

    labels = []
    values = []
    for row in data:
        labels.append(row[0])
        values.append(row[1])
    print('hit')
    return render_template("graph.html", labels=labels, values=values, dates=sleep_date, scores=sleep_score,
                           hrv_avgs=hrv_avg)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)