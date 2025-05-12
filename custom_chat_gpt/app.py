# Starting point of the entire project

# Actual flask app code will be insidet the ./app folder (create_app).
# But we will call the create_app function from app.py to start the flask application

import os
from app import create_app


print("Current working directory:" , os.getCwd())

# Create an instance of the flask application
app = create_app()

if __name__ == '__main__':
    # Run the Flask application on all available IPs and specify the port
    print("Flask app running on http://127.0.0.1:5000/")

    app.run(host = '127.0.0.1', port = 5000, debug=True)

