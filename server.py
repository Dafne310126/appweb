from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', titulo='UDL-ICO', mensaje='¡Bienvenido a UDL-ICO!')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Estos son los servicios que ofrecemos en UDL-ICO')

@app.route('/Contacto')
def Contacto():
    return render_template('Contacto.html', titulo='Contacto', mensaje='Aquí puedes encontrar nuestros contactos')


@app.route('/Productos')
def Productos():
    return render_template('Productos.html', titulo='Productos', mensaje='Aquí puedes encontrar nuestros productos')


if __name__ == '__main__':
    app.run(debug=True, port=5050)
    

