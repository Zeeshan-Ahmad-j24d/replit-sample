from app import app, PORT, DEBUG, env

if __name__ == '__main__':
    print(f"Starting Flask application in {env} environment")
    print(f"Debug mode: {DEBUG}")
    print(f"Running on port: {PORT}")
    print("-" * 50)
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
