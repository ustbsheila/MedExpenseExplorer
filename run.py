from app import create_app

# Get the Flask app instance using the application factory pattern
app = create_app()

if __name__ == "__main__":
    # Run the app on the development server
    app.run(debug=True)