trap 'kill %1; kill %2' SIGINT
python3 services/buscar_producto.py & \
python3 services/crear_producto.py & \
python3 services/eliminar_producto.py