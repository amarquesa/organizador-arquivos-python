import os
import shutil

pasta_origem = "arquivos_teste"
pasta_destino = "imagens"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

for arquivo in os.listdir(pasta_origem):
    if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
        shutil.move(
            os.path.join(pasta_origem, arquivo),
            os.path.join(pasta_destino, arquivo)
        )

print("Arquivos organizados com sucesso!")
