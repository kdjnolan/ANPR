from flask import Flask, render_template, json, request, url_for
from flask import session                                 # used to restrict unauthorised Access to Logged In Page
from flask import redirect                                # to redirect user

from flaskext.mysql import MySQL #pip install flask-mysql
from werkzeug import generate_password_hash, check_password_hash # for password hashing and de-hashing

mysql = MySQL()
app = Flask(__name__)
#app.secret_key = 'secret key for user session'


# Configure and init the python MySQL module
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB']       = 'users'
app.config['MYSQL_DATABASE_HOST']     = '192.168.1.1'
mysql.init_app(app)

#####################################################################################################################
#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('page_not_found.html'),404

# Render the homepage
@app.route('/')
def main():
    return render_template('index.html')

# Sign up page
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# Notify client of SignUp success
@app.route('/showSignedUp')
def showSignedUp():
    return render_template('signedup.html')

# Sign in page
@app.route('/showSignIn')
def showSignIn():
    #return render_template('signin.html')
    #if session.get('user'):
    if 'user' in session:
        return render_template('userHome.html')
    else:
        return render_template('signin.html')

# User Signed In
@app.route('/userHome')
def userHome():
    print('In userHome')
    #if session.get('user'):
    if 'user' in session:
        return render_template('userHome.html')
        #return redirect('/userHome.html', code=302)
    else:
        return render_template('error.html',error = 'Unauthorized')


# Logout - done by making session variable = null
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

# Check database for a plate page
@app.route('/showCheckDB')
def showCheckDB():
    return render_template('checkdb.html')

# Error page
@app.route('/error')
def error():
    return render_template('error.html')

###################################################################################################################

# check database for a plate
@app.route('/checkDB', methods=['POST','GET'])
def checkDB():
    try:
         _registration = request.form['inputRegistration']
         # validate the received value
         if _registration:
             # got reg. Connect to DB. Check for reg
             print("Server received registration data.\nConnecting to database...")
             conn = mysql.connect()
             cursor = conn.cursor()

             # Compare to DB
             print("Connected.\nQuerying the database for reg...")
             cursor.callproc('sp_findPlate', (_registration, ) ) # **comma after only parameter IS NEEDED here
             data=cursor.fetchall();
             #print({'Data is:  ':str(data[0])})
             #print(len(data))
             if len(data) == 1:
                 print("Registration found in database")
                 #conn.commit()
                 #return json.dumps({'SUCCESS!':' registration in DB'})
                 return json.dumps({'html':'<span>Record of registration found in database</span>'})
             else:
                 return json.dumps({'html':'<span>No record of registration in database</span>'})
                 #return json.dumps({'ERROR. JSON DUMP: ':str(data[0])})
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
        _email = request.form['inputEmail'] # save the serialised form data from HTML page to variable
        _registration = request.form['inputRegistration']
        _password = request.form['inputPassword']
        # Validate the received values
        if _name and _email and _registration and _password:
            print("Server received name, email, registration and password")
            print("Connecting to Database...")
            conn = mysql.connect()
            cursor = conn.cursor()

            # Password hashing
            print("Connected.\nHashing the password...\nOriginal Password:\n    " + _password )
            _hashed_password = generate_password_hash(_password, method='sha256')
            print("Password Hashed(sha256):\n    " + _hashed_password )

            # Send all data to database
            print("Storing all data in DB using stored procedure 'sp_createUser'")
            cursor.callproc('sp_createUser',( _name, _email, _registration, _hashed_password))

            # Receive result from database
            data = cursor.fetchall()
            print("User created")          #print({'Data sent back from database:  ':str(data) })
            if len(data) is 0:
                conn.commit()
                # read the json dumps in browser's console window
                return json.dumps({'SUCCESS!':'User created !'})
            else:
                return json.dumps({'ERROR.JSON DUMP= ':str(data[0])})
            cursor.close()
            conn.close()
        else:
            return json.dumps({'html':'<span>Enter all required fields</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    #finally:
    #    cursor.close()
    #    conn.close()






# for sign in, get email and password and then compar the database
@app.route('/signIn', methods=['POST','GET'])
def signIn():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _email and _password:
            # Have user data so connect to database
            print("\n\nServer has received the email and password.\nConnecting to SQL Database...")
            conn = mysql.connect()
            cursor = conn.cursor()
            print("Connected.\nChecking if username exists, if so, DB will return the password...")

            # Check for email and return password if it exists
            #cursor.callproc('sp_checkUser'(_email, _hashed_password,))   #not used
            cursor.execute("SELECT user_password FROM sprocedure_user WHERE user_username=%s", _email)
            data=cursor.fetchone()                               # now we have the password
            pdata = str(data[0])                                 # extract the password, convert to string
            print("Hashed Password is:\n    " +pdata)


            if len(pdata) > 0:
		if check_password_hash( pdata, _password):       # returns bool- true for pass
                    print("User password match")
                    session['user'] = _email
                    return url_for('userHome') # process this with js as AJAX redirects dont work


		    #return redirect(url_for('userHome'), code=200 )     #userHome
                    # Read the json dumps in browser's console window
                    #return json.dumps({'SUCCESS!':'User credentials validated'})
                else:
                    print("Passwords dont match")
                    return render_template('error.html', error = "Wrong Email or Password")
            else:
                print(   json.dumps({'ERROR. JSON DUMP data is: ':str(data[0])})    )
                return render_template('error.html', error = "Wrong Email or Password")

            cursor.close()
            conn.close()



        else:
            return json.dumps({'html':'<span>Enter all required fields</span>'})

    except Exception as e:
        return render_template('error.html',error = str(e))
        #return json.dumps({'error':str(e)})
    #finally:
    #    cursor.close()
    #    conn.close()




if __name__ == "__main__":
    #app.run(port=5001,debug="True")
    # To make the server externally visible to other computers on the network
    # either dont use debugger OR if u trust the computers, change the run() method
    app.debug = True
    app.run(host = '0.0.0.0', port=5001)
    # this tells OS to listen on public IP
