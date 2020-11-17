# https://en.wikipedia.org/wiki/Lenna

from pathlib import Path
import os

suffix = ".jpg"
input_path = Path.home() / "Desktop/UNI/SCAV/P1"
file_paths = [subp for subp in input_path.rglob('*') if suffix == subp.suffix]
file_paths.sort()

output_path = Path.home() / "Desktop/UNI/SCAV/P1/processed"
output_path.mkdir(parents=True, exist_ok=True)

# este script cogerá los archivos .jpg y los comprimirá con -q:v x, donde
# x es un número de 1 a 30 (a mayor x, peor calidad y menos tamaño)

#tendrás que cambiar el path sieso
#tendrás que escribir y/n si ya hay algo creado y quieres sobreescribir

for file_p in file_paths:
    input = str(file_p)
    output = str(output_path / file_p.name)
    command = f"ffmpeg -i {input} -q:v 20 {output}"
    os.system(command)
