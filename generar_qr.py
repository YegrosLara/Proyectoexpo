import qrcode

def generar_qr(url, nombre_archivo="qr_tiempo_reaccion.png"):
    # Crear QR con configuración optimizada
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Crear imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)
    print(f"QR generado: {nombre_archivo}")

# Cambiar por tu URL cuando despliegues
url_sitio = "https://tu-app.herokuapp.com"  # Reemplaza con tu URL real
generar_qr(url_sitio)