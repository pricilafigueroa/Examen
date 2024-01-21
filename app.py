# app.py

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_por_tarro

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        descuento_realizado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_realizado

        mensaje = f'Hola {nombre}, el total sin descuento es ${total_sin_descuento:.2f}, ' \
                  f'se aplicó un descuento del {descuento * 100}%, ' \
                  f'el descuento realizado es ${descuento_realizado:.2f}, ' \
                  f'y el total a pagar es ${total_con_descuento:.2f}.'

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               descuento_realizado=descuento_realizado, total_con_descuento=total_con_descuento,
                               mensaje=mensaje)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        usuarios_validos = {
            'juan': 'admin',
            'pepe': 'user'
        }

        if usuario in usuarios_validos and usuarios_validos[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
