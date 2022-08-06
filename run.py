from market import app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(port=5000, debug=True)
