from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


# 返回html界面
@app.route('/', methods=['GET'])
def get_index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 8080, threaded=True)
