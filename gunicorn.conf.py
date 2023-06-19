import multiprocessing

# Archivo de entrada de la aplicación
bind = '0.0.0.0:8080'
wsgi_app = 'your_application.wsgi:app'

# Configuración de Gunicorn
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2

# Logging
accesslog = '-'  # Muestra los registros de acceso en la consola
errorlog = '-'   # Muestra los registros de error en la consola
