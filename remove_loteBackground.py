import os, os.path, subprocess
from PIL import Image
import shutil, errno
from rembg.bg import remove
import numpy as np
import io

caminho_entrada = input('Digite o Caminho da foto com extensão: ')
caminho_entrada = caminho_entrada.replace("",'').replace("",'').strip()

saida = '/home/ale/Workspace'

#Define a saida da conversão do arquivo de jpg para png
caminho_temp = input('Digite o Caminho da pasta para arquivo temporário: ')
caminho_temp = caminho_temp.replace("",'').replace("",'').strip()  

caminho_saida = input('Digite o Caminho da pasta salvar a foto: ')
caminho_saida = caminho_saida.replace("",'').replace("",'').strip()

root_src_dir = caminho_entrada   
root_dst_dir = saida  


for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)

       

cwd = os.getcwd()
for arquivo in os.listdir(cwd):
    if arquivo.endswith('.jpg'):
      image = Image.open(arquivo)
      nome = arquivo.split('.')[0]
      image.save(caminho_temp + nome +".png", "PNG")

#input_path = caminho_temp +nome +'.png'
output_path = caminho_saida + nome + '_sf.png' 

arm = os.getcwd() 
for arquivo in os.listdir(arm): 
   if arquivo.endswith('.png'):
        im = Image.open(arquivo)
        f = np.fromfile(arquivo)
        result = remove(f)
        im = Image.open(io.BytesIO(result)).convert("RGBA")
        im.save(output_path)
        im.show
          