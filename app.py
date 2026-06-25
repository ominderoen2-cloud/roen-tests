from database.database import create_table
from routes.routes import member_bp
from flask import Flask
app = Flask(__name__)
app.register_blueprint(member_bp)
@app.route("/")
def home():
    return {"status":"api running"}
create_table()
if __name__ == "__main__":
    app.run(host ="0.0.0.0" , port = 432 , debug=True)