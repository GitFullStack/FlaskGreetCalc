# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add():
    """Add parameters a and b."""
    
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    
    return str(result)

@app.route("/sub")
def sub():
    """Subtract parameters a and b."""

    # a = int(request.args.get("a"))
    # b = int(request.args.get("b"))
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mult():
    """Multiply parameters a and b."""

    # a = int(request.args.get("a"))
    # b = int(request.args.get("b"))
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)

    return str(result)

@app.route("/div")
def div():
    """Divide parameters a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # a = int(request.args["a"])
    # b = int(request.args["b"])
    result = div(a, b)

    return str(result)


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<operation>")
def do_math(operation):
    """Perform math operations on parameters a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)

    return str(result)

