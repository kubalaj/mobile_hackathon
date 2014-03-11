from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home/")
def landing():
    return render_template('index.html')
    
@app.route('/portfolio')
def view_portfolio():    
    return render_template('portfolio_view.html')
	
if __name__ == "__main__":
    app.run(debug=True)
