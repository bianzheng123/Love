from flask import Flask, render_template
import random

app = Flask(__name__)


# 返回html界面
@app.route('/', methods=['GET'])
def index():
    rand_num = random.randint() % 2
    if rand_num == 0:
        return app.send_static_file('timetable_code.html')
    elif rand_num == 0:
        return app.send_static_file('book.html')
    return app.send_static_file('wrong.html')


@app.route('/timetable_code', methods=['GET'])
def timetable_code():
    return app.send_static_file('timetable_code.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 8080, threaded=True)
