from flask import Flask, render_template

app = Flask(__name__)

#1 App Route di flask "hello word"
@app.route('/')
def home():
    return "Halo, selamat datang di dunia bulbul!"

#2 App Route di flask
@app.route("/aplikasi/")
def aplikasi():
     return "<p>Selamat datang di Aplikasi zikzik</p>"

#3 App Route dengan HTML 
@app.route("/about/")
def about():
     return render_template('about_without_bostrapp.html')

#4 App Route dengan HTML with bostrapp
@app.route("/about-bostrapp/")
def about_bostrapp():
     return render_template('about.html')

#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
     return "nama anda adalah {}".format(nama_mahasiswa)


if __name__ == '__main__':

    app.run(debug=True)

