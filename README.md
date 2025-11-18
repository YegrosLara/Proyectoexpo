# ⚡ Calculadora de Tiempo de Reacción

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

**Una aplicación web interactiva para medir tu tiempo de reacción usando la prueba de la regla**

[🚀 Demo en Vivo](#) | [📖 Documentación](#instalación) | [🐛 Reportar Bug](#)

</div>

---

## 🎯 ¿Qué es esto?

La **Calculadora de Tiempo de Reacción** es una aplicación web que te permite medir tu tiempo de reacción utilizando el método científico de la "prueba de la regla". Solo necesitas una regla y tus reflejos.

### 🧪 ¿Cómo funciona?

1. **Sostén una regla** por la parte superior
2. **Suéltala** sin avisar
3. **Atrápala** lo más rápido posible
4. **Mide** dónde la atrapaste en centímetros
5. **Ingresa** el valor en la app
6. **¡Obtén** tu tiempo de reacción!

---

## ✨ Características

- 🎨 **Interfaz moderna** con gradientes y animaciones
- 📱 **Responsive design** - funciona en móviles y desktop
- ⚡ **Cálculo instantáneo** usando física real
- 🔢 **Precisión decimal** hasta 4 decimales
- 📊 **Fórmula científica**: `t = √((distancia × 2) ÷ 9.8)`
- 🌐 **Listo para deploy** en Heroku

---

## 🚀 Instalación

### Prerrequisitos
- Python 3.8+
- pip

### Instalación local

```bash
# Clonar el repositorio
git clone https://github.com/YegrosLara/Proyectoexpo.git
cd Proyectoexpo

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

---

## 📁 Estructura del Proyecto

```
proyecto/
├── 📄 app.py              # Aplicación Flask principal
├── 📄 generar_qr.py       # Generador de códigos QR
├── 📄 requirements.txt    # Dependencias Python
├── 📄 Procfile.txt       # Configuración Heroku
├── 📁 templates/
│   └── 📄 index.html     # Interfaz web principal
└── 📄 README.md          # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

<table>
<tr>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="50"/>
<br><strong>Python</strong>
</td>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="50"/>
<br><strong>Flask</strong>
</td>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="50"/>
<br><strong>HTML5</strong>
</td>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" width="50"/>
<br><strong>CSS3</strong>
</td>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="50"/>
<br><strong>JavaScript</strong>
</td>
</tr>
</table>

---

## 🔬 La Ciencia Detrás

### Fórmula Física
```
t = √((d × 2) ÷ g)
```

Donde:
- **t** = tiempo de reacción (segundos)
- **d** = distancia de caída (metros)
- **g** = aceleración gravitacional (9.8 m/s²)

### ¿Por qué funciona?
Esta fórmula se basa en las ecuaciones de caída libre. Cuando sueltas la regla, cae bajo la influencia de la gravedad, y el tiempo que tardas en reaccionar determina qué tan lejos cae antes de que la atrapes.

---

## 🌐 Deploy en Heroku

1. **Crear app en Heroku**
```bash
heroku create tu-app-tiempo-reaccion
```

2. **Deploy**
```bash
git push heroku main
```

3. **Generar QR** para acceso móvil
```bash
python generar_qr.py
```

---

## 📊 Valores de Referencia

| Tiempo de Reacción | Clasificación |
|-------------------|---------------|
| < 0.15s | 🏆 Excelente |
| 0.15s - 0.20s | 🥇 Muy Bueno |
| 0.20s - 0.25s | 🥈 Bueno |
| 0.25s - 0.30s | 🥉 Promedio |
| > 0.30s | 📈 Necesita práctica |

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la aplicación:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👥 Autores

- **YegrosLara** - *Desarrollo principal* - [@YegrosLara](https://github.com/YegrosLara)

---

<div align="center">

**¿Te gustó el proyecto? ¡Dale una ⭐!**

[⬆ Volver arriba](#-calculadora-de-tiempo-de-reacción)

</div>
