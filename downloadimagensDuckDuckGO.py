# import DuckDuckGoImages as ddg		#pip install DuckDuckGoImages


filtro = 'soja'
destino = 'home/amf/soja/dataset'

print('Iniciando downloads...')
try:
    ddg.download(filtro, folder=destino, remove_folder=False, parallel=True)
except Exception as e:
    print("type error: ", e)
print('Downloads concluidos...')


#./darknet detector train /SVN/YOLO/soja.data /SVN/YOLO/soja.cfg yolov4.conv.137
# como treinar algoritmo com dark web
