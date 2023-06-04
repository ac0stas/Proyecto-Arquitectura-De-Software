trap 'kill %1; kill %2; kill %3' SIGINT
python3 services/serv1.py & \
python3 services/serv2.py & \
python3 services/serv3.py 
