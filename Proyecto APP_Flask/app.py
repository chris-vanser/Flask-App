from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener datos del formulario
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Calcular estado de aprobación o reprobación
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

        return render_template('resultado_ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encontrar el nombre con más caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template('resultado_ejercicio2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
