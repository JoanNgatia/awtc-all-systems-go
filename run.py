from main.manage import app, db

db.create_all()
app.run(debug=True)
