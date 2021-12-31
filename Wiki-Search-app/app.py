from flask import Flask, request, render_template
import wikipedia
import re

app = Flask(__name__)

# home view

# @app.route("/", methods=["POST", "GET"])
# def home():
#     if request.method == "GET":
#         return render_template("index.html");
#     else:
#         search = request.form["search"]
#         # Fetch data from wikipedia
#         # result = wikipedia.summary(search, sentences=2);
#         result = wikipedia.page(search).content
#         # return f"<h1>{result}</h1>"
#         pattern = re.findall("==(.*?)==", result);
#         str = "";
#         for ele in pattern:
#             str += ele;
#         return str

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html");
    else:
        search = request.form["search"]
        # Fetch data from wikipedia
        # result = wikipedia.summary(search, sentences=2);
        result = wikipedia.page(search).content
        # return f"<h1>{result}</h1>"
        return result

if __name__ == '__main__':
    app.run(debug=True)
