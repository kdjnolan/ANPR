from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL #pip install flask-mysql
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# Configure and init the python MySQL module
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB']       = 'users'
app.config['MYSQL_DATABASE_HOST']     = '192.168.1.12'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _registration = request.form['inputRegistration']
        _password = request.form['inputPassword']
        #conn = mysql.connect()
        #cursor = conn.cursor()

        # validate the received values
        if _name and _email and _registration and _password:
            # got data for  all fields
            # save data to sql
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)

            #print("Hashed Password is: "+_hashed_password )
            cursor.callproc('sp_createUser',(_name,_email,_registration,_hashed_password))
            data = cursor.fetchall()
            #print "D"
            #print(data)
            if len(data) is 0:
                conn.commit()
                # read the json dumps in browser's console window
                return json.dumps({'SUCCESS!':'User created !'})
            else:
                return json.dumps({'ERROR. JSON DUMP: ':str(data[0])})
            cursor.close()
            conn.close()

        else:
            return json.dumps({'html':'<span>Enter all required fields</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    #finally:
        #cursor.close()
        #conn.close()

if __name__ == "__main__":
    app.run(port=5001,debug="True")
