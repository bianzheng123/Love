from flask import Flask, render_template
import random

app = Flask(__name__)


# 返回html界面
@app.route('/', methods=['GET'])
def index():
    rand_num = random.randint(0, 2)
    if rand_num == 0:
        return app.send_static_file('timetable_code.html')
    elif rand_num == 1:
        return app.send_static_file('book.html')
    return app.send_static_file('wrong.html')


@app.route('/book', methods=['GET'])
def book():
    return app.send_static_file('src/steve-jobs/book.html')

@app.route('/timecount', methods=['GET'])
def timecount():
    return app.send_static_file('src/timecount/timecount.html')


if __name__ == "__main__":
    # app.run('0.0.0.0', 8080, threaded=True)
    app.run('127.0.0.1', 8080, threaded=True)
