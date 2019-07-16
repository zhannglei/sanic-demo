from sanic import Sanic


app = Sanic(__name__)

from demo.api.user import api

app.blueprint(api)


if __name__ == '__main__':
    app.run()
