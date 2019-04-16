A Car Registration App built using Python Flask Web Framework 

Contains server/client code to manage user registration.
User also has ability to:
                           sign up
                           add their registration to a remote database
                           check a registration exist in database
                           sign into account

Server code:
    app.py   # manages client's reqs,resps.  
            # Queries mySQL database(RAW data and Stored Procedures)
            # Password hashing.
Client code:
    templates:
         index.hmml   //homepage
         signin.htm   //to get user data, check against database
         signup.htm   //get user data, attempt to store in database
         signedup.htm //Update client
         checkdb.htm  //queries the database for the particular database
         error.htm    //page to display errors

         Could add:
              -edit user credentials 
              -secure payment
              -admin    view camera ? 
                        debug ? 
                        edit database
                        export data to spreadsheet or sumthing
    static
         javascript:
               signin.js   // get user data, post to server using AJAX
               signup.js   // get user data, post to server, return AJAX response
               checkdb.js 
   css
         signin.css,signup.css [removed] using JumboTron 
   
   
   
   

https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
