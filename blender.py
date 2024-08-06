#import bpy
import math
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/rotate', methods=['GET'])
def rotate():
    # Obtener los grados de rotación desde la solicitud
    degrees = request.json.get('degrees', 0)

    url = 'http://127.0.0.1:5000/rotate'
    data = {'degrees': 30}
    headers = {'Content-Type': 'application/json'}

    response = request.get(url, json=data, headers=headers)
    print(response.json())
    
    # Importar el cubo FBX
    #bpy.ops.import_scene.fbx(filepath="C:\Users\danie\OneDrive\Escritorio\cubo.fbx")
    
    # Seleccionar el cubo importado
    #cube = bpy.context.selected_objects[0]
    
    # Rotar el cubo en el eje Z
    #cube.rotation_euler.z = math.radians(degrees)
    
    # Actualizar la escena
    #bpy.context.view_layer.update()
    
    # Guardar el resultado (opcional)
    #bpy.ops.wm.save_as_mainfile(filepath="C:\Users\danie\OneDrive\Escritorio\resultado.blend")
    
    return jsonify({"message": f"Cubo rotado {degrees} grados en el eje Z"})

if __name__ == '__main__':
    # Iniciar Blender en modo background
    #bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Iniciar la aplicación Flask
    app.run(debug=True)


