from rembg.bg import remove
import numpy as np
import io
from PIL import Image
import os     
import os.path
#Defina a entrada da imagem
caminho_entrada = input('Digite o Caminho da foto com extensão: ')
caminho_entrada = caminho_entrada.replace("",'').replace("",'').strip()
  

#Define a saida da conversão do arquivo de jpg para png
caminho_temp = input('Digite o Caminho da pasta para arquivo temporário: ')
caminho_temp = caminho_temp.replace("",'').replace("",'').strip()  

#Local ou pasta onde irá salvar o arquivo sem fundo
caminho_saida = input('Digite o Caminho da pasta salvar a foto: ')
caminho_saida = caminho_saida.replace("",'').replace("",'').strip()


#abrir imagem do caminho entrada
image = Image.open(caminho_entrada)

(name, extension) = os.path.splitext('filepath')
#salvar imagem na pasta temporaria que vc definiu
image.save(caminho_temp + name + ".png")

     
input_path = caminho_temp + name +'.png'
output_path = caminho_saida + name + '_sf.png' 
f = np.fromfile(input_path)
result = remove(f)
img = Image.open(io.BytesIO(result)).convert("RGBA")
img.save(output_path) 
img.show()  
         