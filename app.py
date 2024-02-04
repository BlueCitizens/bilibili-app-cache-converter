from flask import Flask, render_template
# from flask_cors import cross_origin
import signal

app = Flask(__name__)


@app.route('/')
def homepage():
    home = 'flask_welcome.html'
    return render_template(home)

@app.route('/hello')
def hello():
    return 'hello'


def signal_handler(sig, frame):
    print('Received SIGINT, shutting down flask server')
    # Perform any cleanup desired here
    # app.stop()


if __name__ == "__main__":
    # signal.signal(signal.SIGINT, signal_handler)
    app.run(host='127.0.0.1', port=5001, use_reloader=False)
    # 注意，如果没有指定use_reloader=False，后续将其打包成exe后，运行exe会产生两个进程，在electron窗口关闭时kill掉进程时，会有一个守护进程无法kill掉