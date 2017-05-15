from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/process', methods=['POST'])
def show_result():
    name = request.form['name']
    print (len(name))
    if len(name) < 1:
        flash("Name cannot be empty!")
        return redirect ('/')
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(comment) > 10:
        flash("Comments cannot be greater than 120 characters!")
        return redirect ('/')
    if len(comment) < 1:
        flash("Comments aren't actually optional.")
        return redirect ('/')
    return render_template ("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True)
