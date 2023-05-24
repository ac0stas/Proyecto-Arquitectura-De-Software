import argparse
from services.create_product import create_product
from services.delete_product import delete_product
from services.edit_product import edir_product

def main():
    parser = argparse.ArgumentParser(description='Gestor de Inventario')
    parser.add_argument('comando', choices=['crear', 'eliminar', 'editar'])
    parser.add_argument('--nombre')
    parser.add_argument('--precio', type=float)
    parser.add_argument('--sku', type=int)
    parser.add_argument('--stock', type=int)
    args = parser.parse_args()

    if args.comando == 'create':
        create_product(args.name, args.price, args.sku, args.stock)
    elif args.comando == 'delete':
        delete_product(args.sku)
    elif args.comando == 'edit':
        edir_product(args.name, args.price, args.sku, args.stock)

if __name__ == '__main__':
    main()
