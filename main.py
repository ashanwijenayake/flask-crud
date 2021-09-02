from flask import Flask, render_template, request, redirect
import services as dbo

app = Flask(__name__)


# The endpoint returns the whole music repository as a model object to the front-end
@app.route('/')
def read():
    ds = dbo.getMusic()
    ds_singer = dbo.getSingerList()
    return render_template('home.html', rows=ds, singer=ds_singer)


# The endpoint accepts GET and POST actions. POST is responsible for inserting a new entry to the database
@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html')  # Return the html view

    elif request.method == 'POST':
        dbo.createMusic(request.form)  # Service method responsible to create a new entry
        return redirect("/write")  # Redirect back to the same page


# The endpoint accepts GET and POST actions. POST is responsible for updating an existing record in the db
@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        ds = dbo.getMusicById(id)  # Service method responsible to get the relevant music entry
        return render_template('update.html', row=ds)  # Return the html view along with relevant entry

    elif request.method == 'POST':
        dbo.updateMusic(request.form)  # Service method responsible to update the music entry
        return redirect("/")  # Redirect back to main screen


# Admin end-point
@app.route('/clean')
def clean():
    dbo.clearDb()
    return redirect("/")


if __name__ == '__main__':
    app.run(port=5000)
