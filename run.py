from market import app

# Dealing with circular imports
if __name__ == '__main__':
    app.run(port=5000, debug=True)
