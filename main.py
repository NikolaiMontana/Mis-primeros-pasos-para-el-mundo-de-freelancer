import os
import shutil

print("--- BIENVENIDO AL ORGANIZADOR DE ARCHIVOS ---")
ruta = input("Introduce la ruta de la carpeta que deseas organizar: ")
if not os.path.exists(ruta):
    print("La ruta no existe. Por favor, verifica y vuelve a intentarlo.")


organizador = {
    ".png": "Capturas",
    ".mp4": "Videos",
    ".pdf": "Documentos",
    ".jpg": "Fotos",
    ".pptx": "Documentos"
    
    } 

for archivo in os.listdir(ruta):
    nombre, extension = os.path.splitext(archivo)
    extension = extension.lower()
    
    if extension in organizador:
        nombre_subcarpeta = organizador[extension] 
        ruta_destino = os.path.join(ruta, nombre_subcarpeta)
        
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)
            
        origen_completo = os.path.join(ruta, archivo)
        destino_completo = os.path.join(ruta_destino, archivo)
        
        try:
            shutil.move(origen_completo, destino_completo)
            print(f"Movido: {archivo} -> {nombre_subcarpeta}")
        except Exception as e:
            print(f"No se pudo mover {archivo}. Error: {e}")

print("--- Proceso finalizado ---")
input("\nPresiona Enter para salir...")
exit()
          




