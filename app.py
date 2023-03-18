from flask import Flask,render_template

# __name__ es una palabra resevada que hace referencia al nombre del archivo
# creamos objeto de la clase Flask
app = Flask(__name__) 

#Creamos Ruta inicial
@app.route('/')
def index() :    
    return render_template('home.html')


@app.route('/about')
def about() :    
    return render_template('about.html')

@app.route('/post')
def post() :
    return render_template('post.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#desplegamos el servidor
app.run(debug=True)