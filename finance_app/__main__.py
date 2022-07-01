from app import app

from layouts import main_layout


app.layout = main_layout()

from callbacks import *

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
