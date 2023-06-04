trap 'kill %1; kill %2; kill %3' SIGINT
python3 serv1.py & \
python3 serv2.py & \
python3 serv3.py 
