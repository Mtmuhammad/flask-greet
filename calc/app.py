from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/math/<operation>')
def math(operation):
   """Returns the sum of arguments submitted."""
   math = {"add":add, "sub":sub, "mult": mult, "div":div}
   a, b = request.args.values()
   equation = math[operation]
   return f'{equation(int(a), int(b))}'