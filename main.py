from flask import Flask, render_template, request, redirect
from database import DatabaseHandler
from routes.home import homeBlueprint
from routes.userManagement import signupBlueprint, createUserBlueprint


app=Flask(__name__)
app.config["SECRET_KEY"]="brownstorm"
db=DatabaseHandler("appData.db")
#db.createTables()

#routing
app.register_blueprint(homeBlueprint)

app.register_blueprint(signupBlueprint)

app.register_blueprint(createUserBlueprint)






######
app.run(debug=True)

