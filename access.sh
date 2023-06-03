read -p "Ingresa tu usuario de Docencia: " username
read -p "Ingresa tu contraseña: " password

SSHPASS=$password sshpass -e ssh -tt -L *:5000:localhost:5000 -o StrictHostKeyChecking=no -p 8080 $username@200.14.84.16 'date; /bin/bash'