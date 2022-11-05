from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    data = [
            ("2021-05-18", 48),
            ("2021-05-19", 48),
            ("2021-05-20", 49),
            ("2021-05-21", 52)
    ]

    labels = []
    values = []
    for row in data:
        labels.append(row[0])
        values.append(row[1])
    print('hit')
    return render_template("graph.html", labels=labels, values=values)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)