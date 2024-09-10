from flask import Flask

app=Flask(__name__)
app.config["SECRET_KEY"]="brownstorm"










######
app.run(debug=True)

