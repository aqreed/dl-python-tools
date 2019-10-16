import glob
import pandas as pd
from os import path, remove


train_annotations = 'train-annotations-bbox.csv'
test_annotations = 'test-annotations-bbox.csv'
validation_annotations = 'validation-annotations-bbox.csv'

df = pd.read_csv(validation_annotations)
lista_bbox = df['ImageID'].values

lista_img = glob.glob('*.jpg')

for img in lista_img:
    if not path.splitext(path.basename(img))[0] in lista_bbox:
        print(img, 'removed')
        remove(img)
