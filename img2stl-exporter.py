import numpy as np
from stl import mesh
from PIL import Image
from os import listdir
from pathlib import Path

SOURCEFOLDER = '011_img_sources/junction_traffic_gray/'
RESULTFOLDER = '010_stl_results'
VIDEO           = 'junction_traffic_gray'


path = Path(RESULTFOLDER+'/'+VIDEO+'/')
path.mkdir(parents=True, exist_ok=True)


max_size=(500,500)
max_height=100
min_height=1

img_list = listdir(SOURCEFOLDER)

for imagename in img_list:
    img = Image.open(SOURCEFOLDER+imagename).convert('L') #graustufenbild
    data = np.asarray(img)

    img.thumbnail(max_size)
    imageNp = np.array(img)
    maxPix=imageNp.max()
    minPix=imageNp.min()

    (ncols,nrows)=img.size

    vertices=np.zeros((nrows,ncols,3))

    for x in range(0, ncols):
        for y in range(0, nrows):
            pixelIntensity = imageNp[y][x]
            z = (pixelIntensity * max_height) / maxPix
            #print(imageNp[y][x])
            vertices[y][x]=(x, y, z)

    faces=[]
    for x in range(0, ncols - 1):
        for y in range(0, nrows - 1):
            # create face 1
            vertice1 = vertices[y][x]
            vertice2 = vertices[y+1][x]
            vertice3 = vertices[y+1][x+1]
            face1 = np.array([vertice1,vertice2,vertice3])

            # create face 2 
            vertice1 = vertices[y][x]
            vertice2 = vertices[y][x+1]
            vertice3 = vertices[y+1][x+1]

            face2 = np.array([vertice1,vertice2,vertice3])

            faces.append(face1)
            faces.append(face2)

    facesNp = np.array(faces)
    # Create the mesh
    surface = mesh.Mesh(np.zeros(facesNp.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            surface.vectors[i][j] = facesNp[i][j]
            
    print(f'save mesh into {imagename}.stl')
    surface.save(f"{RESULTFOLDER+'/'+VIDEO+'/'+imagename.replace('.jpg','.stl')}")