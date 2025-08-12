from os import getenv
from FlaskExercise import app

if __name__ == "__main__":
    host = getenv("SERVER_HOST", "localhost")
    port = int(getenv("SERVER_PORT", "5555"))
    app.run(host=host, port=port, debug=True)
