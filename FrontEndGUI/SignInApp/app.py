from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL #pip install flask-mysql
from werkzeug import generate_password_hash, check_password_hash

#
mysql = MySQL()
app = Flask(__name__)

# Configure and init the python MySQL module
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB']       = 'users'
app.config['MYSQL_DATABASE_HOST']     = '192.168.1.1' # .12
mysql.init_app(app)


# homepage
@app.route('/')
def main():
    return render_template('index.html')

# sign up page
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

#@app.route('/showSignedUp')
#def showSignedUp():
    #return render_template('signedup.html')
    #return "Done.."

# sign in page
@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

# check database for a plate page
@app.route('/showCheckDB')
def showCheckDB():
    return render_template('checkdb.html')


# check database for a plate
@app.route('/checkDB',methods=['POST','GET'])
def checkDB():
    try:
         _registration = request.form['inputRegistration']
         # validate the received value
         if _registration:
             # got data for  all fields
             # check data on sql database
             conn = mysql.connect()
             cursor = conn.cursor()
             #compare to DB
             #print(_registration)
             cursor.callproc('sp_findPlate', (_registration) )
             data=cursor.fetchall();
             
             #print({' ':str(data[0])})
             if len(data) is 0:
                 conn.commit()
                 print "Checked"
                 return json.dumps({'SUCCESS!' 'checked !'})
             else:
                 return json.dumps({'ERROR. JSON DUMP: ':str(data[0])})
             cursor.close()
             conn.close()
         else:
             return json.dumps({'html':'<span>Enter all required fields</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})





@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _registration = request.form['inputRegistration']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _registration and _password:
            # got data for  all fields
            # save data to sql
            conn = mysql.connect()
            cursor = conn.cursor()

            #password hashing
            print("Hashed Password is: "+_hashed_password )
            _hashed_password = generate_password_hash(_password)
            print("Hashed Password is: "+_hashed_password )

            #send all data to database
            cursor.callproc('sp_createUser',(_name,_email,_registration,_hashed_password))

            data = cursor.fetchall()
            #print({'databack:  ':str(data[0])})
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






# for sign in, get email and password and then compar the database
@app.route('/signIn',methods=['POST','GET'])
def signIn():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _email and _password:
            # got data for  all fields
            # check data against sqlDB
            conn = mysql.connect()
            cursor = conn.cursor()

            #check for email&password match on SQL database
            cursor.callproc('sp_checkUser'(_email, _hashed_password))
	    data=cursor.fetchall()
            print({' ':str(data[0])})
            #print({'databack:  ':str(data[0])})


            if len(data) is 0:
                conn.commit()
                # to read the json dumps in browser's console window
                return json.dumps({'SUCCESS!':'User found'})
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
