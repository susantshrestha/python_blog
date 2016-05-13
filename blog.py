from flask import Flask, render_template, request, redirect, url_for
from connect import connection

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew/', methods=['get', 'post'])
def new_student():
    return render_template('student.html')


# connection to the database
@app.route('/register')
def register():
    try:
        connection()
        return "connected"
    except Exception as e:
        return str(e)


@app.route('/addrec/', methods=['POST', 'GET'])
def addrec():
    print "entered bro"
    if request.method == 'POST':
        try:
            cursor, db = connection()
            print "connected"
            name = request.form['name']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            print name, addr, city, pin

            # cursor.execute("""INSERT INTO students(name, addr, city, pin) VALUES ('alex', 'gon', 'kon', 'fgjgh')""")
            cursor.execute("""INSERT INTO students(name, addr, city, pin) VALUES ('%s', '%s','%s','%s')"""
                           % (name, addr, city, pin))
            db.commit()
            cursor.close()
            # return redirect(url_for('home'))
            # db.close()
            msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html",msg=msg)
            db.close()


if __name__ == '__main__':
    app.run(debug=True)
