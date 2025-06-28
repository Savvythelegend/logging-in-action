from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="server.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Welcome to the Flask API!"

@app.route("/error")
def error():
    logging.error("Error endpoint triggered!")
    return "This is an error!", 500

if __name__ == "__main__":
    app.run(debug=True)
