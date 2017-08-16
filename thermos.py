from flask import Flask, render_template, url_for

app = Flask(__name__)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def initials(self):
        return ('{}. {}.'.format(self.first_name[0].upper(), self.last_name[0].upper()))

    def __str__(self):
        return ('{} {}'.format(self.first_name.title(), self.last_name.title()))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="This is the context title!",
                           user=User('eric', 'carlile'))


@app.route('/add')
def add():
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
