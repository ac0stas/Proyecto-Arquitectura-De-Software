trap 'kill %1; kill %2; kill %3' SIGINT
python3 ./src/services/serv1.py & \
python3 ./src/services/serv2.py & \
python3 ./src/services/serv3.py & 
