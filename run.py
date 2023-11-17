from app import create_app
from updatedata.updateScheduler import start_scheduler

# Get the Flask app instance using the application factory pattern
app = create_app()

# Start the scheduler when the Flask application starts
start_scheduler()

if __name__ == "__main__":
    # Run the app on the development server
    app.run(debug=True)
