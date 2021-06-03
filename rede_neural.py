import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

def classificar(img):
    arquivo=open('classificador.json','r')
    estrutura=arquivo.read()
    arquivo.close()

    classificador=model_from_json(estrutura)
    classificador.load_weights('classificador.h5')

    image_test=image.load_img(img,target_size=(64,64))
    image_test=image.img_to_array(image_test)
    image_test=image_test/255
    image_test=np.expand_dims(image_test,axis=0)
    previsao=classificador.predict(image_test)
    print(previsao)
    if previsao > 0.5:
        return 'Gato'
    else:
        return 'Cachorro'
