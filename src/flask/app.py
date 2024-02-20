from flask import Flask, request
from flask_cors import cross_origin
import signal, json

from scripts import bili

app = Flask(__name__)


@app.route('/hello')
def hell():
    return 'hello'

@app.route('/convert',methods=['POST'])
@cross_origin()
def convert():
    if request.method == 'POST':
        data = json.loads(request.data)
        # path = json.dumps(data['form'])
        res = bili.convert(data['form'])
    
    return res


def signal_handler(sig, frame):
    print('Received SIGINT, shutting down flask server')
    # Perform any cleanup desired here
    # app.stop()


if __name__ == "__main__":
    # signal.signal(signal.SIGINT, signal_handler)
    app.run(host='127.0.0.1', port=5001, use_reloader=False)
    # 注意，如果没有指定use_reloader=False，后续将其打包成exe后，运行exe会产生两个进程，在electron窗口关闭时kill掉进程时，会有一个守护进程无法kill掉