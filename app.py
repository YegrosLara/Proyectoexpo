from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular_tiempo_reaccion():
    try:
        centimetros = float(request.json['centimetros'])
        
        # Convertir cm a metros
        metros = centimetros / 100
        
        # Aplicar fórmula: sqrt((metros * 2) / 9.8)
        tiempo_reaccion = math.sqrt((metros * 2) / 9.8)
        
        return jsonify({
            'tiempo_reaccion': round(tiempo_reaccion, 4),
            'centimetros': centimetros,
            'metros': metros
        })
    except (ValueError, KeyError):
        return jsonify({'error': 'Valor inválido'}), 400

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
