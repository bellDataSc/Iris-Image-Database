import os

dataset_path = '/kaggle/input/casia-iris-interval'

for root, dirs, files in os.walk(dataset_path):
    print(f'Diretório: {root}')
    print(f'  Subpastas: {dirs}')
    print(f'  Arquivos: {files[:5]}')  # Mostra os 5 primeiros arquivos
    break  # tira o "recursivo" e mostra só o topo
