# author name  : mindula dilthushan
# author email : minduladilthushan1@gmail.com
# project name : flask mongodb rest api

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'Flask & MongoDB REST API!'


if __name__ == '__main__':
    app.run()
