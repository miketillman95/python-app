from flask import Flask, render_template, jsonify, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static',
)

# Index page rendering 'index.html'
@app.route('/')
def hello():
  return render_template('index.html')


incomes = [
  { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204


if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )