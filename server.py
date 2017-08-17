from flask import Flask

from item import Item
from store import Store


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')

    app.store = Store()
    app.store.add_item(Item('orange'))
    app.store.add_item(Item('mango'))

    return app


def main():
    app = create_app()
    port = app.config.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()