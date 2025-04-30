import streamlit as st
from ultralytics import YOLO
from ultralytics.solutions import object_counter


import imutils
import os
from os import mkdir
from datetime import date
from datetime import datetime
from getpass import getuser
import supervision as sv
from PIL import Image

import matplotlib.path as mplPath
import matplotlib.pyplot as plt



from PIL import Image
import PIL

from ultralytics import YOLO
from ultralytics.solutions import object_counter


import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import imutils
import gdown
import cv2



def deteccion(image):
    
    

    

   
    
    
    model = YOLO("Models25/ArbolesChihuahua.pt")
    imagen = image
    result = model(imagen,imgsz = 640, conf = 0.1, show_labels=False,show_conf=False)[0]
    resultados = model.predict(imagen, imgsz = 640, conf = 0.1)
    detections = sv.Detections.from_ultralytics(result)
    alta = detections[detections.confidence > 0.1]
    
    leng = len(resultados)
    
    anotaciones = resultados[0].plot()
    haber = imutils.resize(anotaciones,width=640)
    
    
    haber = imutils.resize(anotaciones,width=1024)
    route = os.getcwd()
    route2 = str(route)

    directory = route2
    os.chdir(directory)
    filename = 'Imagen_Resultados25.jpg'

    cv2.imwrite(filename, haber)

    
    
    
    
    return anotaciones



def deteccion2(image):
    
    model = YOLO("Models25/ArbolesChihuahua.pt")
    imagen = image
    result = model(imagen,imgsz = 640, conf = 0.1, show_labels=False,show_conf=False)[0]
    resultados = model.predict(imagen, imgsz = 640, conf = 0.1)
    detections = sv.Detections.from_ultralytics(result)
    alta = detections[detections.confidence > 0.1]
    
    
    leng = len(resultados)
    
    anotaciones = resultados[0].plot()
    haber = imutils.resize(anotaciones,width=640)
    
    leng = len(alta)
    leng2 = str(leng)
    
    haber = imutils.resize(anotaciones,width=1024)
    
    
    
    
    return leng2




def main():
    
    st.header('Aplicación para el conteo de cítricos ')
    st.markdown('Aplicación desarrollada por la SEDAGRO. Detecta los cítricos que se encuentran en el árbol a partir de una imagen. Se muestran dos resultados: M = fruta madura   MN = fruta que aun no esta madura y presenta tonalidades verdosas. ')

    file_uploader = st.file_uploader('Sube tu imagen en los siguientes formatos: ', type=['jpg', 'png'])

    if file_uploader is not None:
        image = Image.open(file_uploader)
        archivo = file_uploader.name
        
        
    

        

        st.image(image)
        datos = deteccion(image)
        st.markdown('Los resultados de la imagen de salida fueron modificados con el fin de que sea más fácil para la red neuronal hacer las detecciones de las frutas.')
        deteccionn = deteccion((image))
        prueba =  st.image(deteccionn)
       

        st.markdown(deteccion2((image)) + ' Cítricos detectados')
        
        anomalias_detectadas = deteccion2((image))
        imagen_salida = deteccion((image))
        #st.markdown(imagen_salida + 'Esto es una prueba')
        

        #----------------------------------------------Se crea la automatizacion de los pdf---------------------
        import pathlib
        from fpdf import FPDF
        from datetime import datetime
        fecha_actual = datetime.now()

        año = fecha_actual.year
        mes = fecha_actual.month
        dia = fecha_actual.day
        hora = fecha_actual.hour
        minutos = fecha_actual.minute
        segundos = fecha_actual.second

        #Numero de folio
        import random
        random_integer = random.randint(1, 150000) 
        folio = str(random_integer)
        print(random_integer)
        archivo = pathlib.Path(archivo)
        
        
        if archivo:
            with open(archivo,'wb') as f:
                f.write(file_uploader.getbuffer())
        extension = archivo.suffix
        print(f"La extensión del archivo es: {extension}")

        import hashlib
        Usuario1 = 'Brayan Gutierrez'
        encoded = Usuario1.encode('utf-8')
        Usuario2 = 'Alfredo Murillo'
        encoded2 = Usuario2.encode('utf-8')
        numero = int(anomalias_detectadas)
        Estado = ''
        Accion = ''
        Explicacion = ''

        hash1 = hashlib.md5(encoded).hexdigest()
        hash11 = '45232dcff8ba7c48b38a273069af397d'
        hash2 = hashlib.md5(encoded2).hexdigest()
        hash22 = 'ba502bbd2dd1112f9d4bc2115bd4d70c'

        print(hash1)
        print(hash2)

        if numero <= 5:
            Estado = 'Buena'
            Accion = 'Ninguna'
            Explicacion = 'De acuerdo con las anomalías detectadas se llegó a la conclusión que no son un número tan significativo por lo que se puede decir que el cultivo se encuentra en buenas condiciones. Sin embargo, es importante seguir analizándolo.'
        if numero <= 10:
            Estado = 'Regular'
            Accion = 'Ir a campo a comprobar anomalías'
            Explicacion = 'De acuerdo con las anomalías detectadas se aconseja ir a campo a comprobar el porque de las anomalías. Esto para descartar posibles problemas en el cultivo.'
        if numero > 10:
            Estado = 'Mala'
            Accion = 'Dirigirse inmediatamente a campo'
            Explicacion = 'De acuerdo con las anomalías detectadas se recomienda ir a campo urgentemente ya que hay problemas en el cultivo.'

        class PDF2(FPDF):
            def header(self):
                self.image('imagen.jpeg',10,8,25)
                self.set_font('helvetica','B',20)
                self.cell(80)
                self.cell(100,10,'Resultados del análisis',border=True,ln=1, align='C')
                self.ln(20)


            def footer(self):
                self.set_y(-15)
                self.set_font('helvetica','I',10)
                self.alias_nb_pages()
                self.cell(0,10,f'Página {self.page_no()}', align='C')
        pdf2 = PDF2('P','mm','Letter')
        pdf2.set_auto_page_break(auto=True,margin=15)
        pdf2.add_page(orientation='landscape')
        pdf2.set_font('helvetica','BIU',16)
        pdf2.set_font('times','',12)
        pdf2.cell(85,20,'Fecha: ' + str(dia) + '/' + str(mes) + '/' + str(año),ln=False,border=True)
        pdf2.cell(85,20,'Hora: ' + str(hora) + ':' + str(minutos),border=True)
        pdf2.cell(85,20, 'Número de Folio: ' + folio,border=True,ln=True)
        pdf2.cell(85,20,'ID: ' + hash1 ,border=True)
        pdf2.cell(85,20, 'Versión utilizada:   YOLO v11', border=True, ln=False)
        pdf2.cell(85,20,'Extensión del archivo: ' + extension, border=True)
        pdf2.ln(40)

        pdf2.set_font('helvetica','B',10)
        pdf2.cell(w=0,h=5,text='Resultados Obtenidos',border=True,align='C',ln=True)
        pdf2.set_font('times','',12)
        pdf2.cell(85,20, 'Anomalías detectadas: ' + str(anomalias_detectadas), border=True)
        pdf2.cell(85,20, 'Estado del Cultivo: ' + Estado, border=True)
        pdf2.cell(89.5,20, 'Acción: ' + Accion, border=True, ln=True)
        pdf2.multi_cell(w=0,h=5,text=Explicacion,border=True)

        pdf2.ln(20)
        pdf2.set_font('helvetica','B',10)
        pdf2.cell(w=0,h=5,text='Resultados de imágenes',border=True,align='C',ln=True)
        pdf2.ln(40)
        pdf2.image(archivo,w=50,h=50,x=115)
        pdf2.set_font('helvetica','B',10)
        pdf2.cell(w=0,h=5,text='Imagen ingresada',border=False,align='C',ln=True)
        pdf2.ln(20)
        pdf2.image('Imagen_Resultados25.jpg',w=50,h=50,x=115)
        pdf2.set_font('helvetica','B',10)
        pdf2.cell(w=0,h=5,text='Imagen de salida',border=False,align='C',ln=True)

        folio_str = str(folio)
        

        pdf2.output('Prueba3.pdf')

        with open('Prueba3.pdf',"rb") as pdf_file:
            PDFbyte = pdf_file.read()
        
        
        st.download_button(label='Descargar Reporte',data=PDFbyte,file_name='Reporte.pdf',mime='application/octet-stream')


if __name__ == "__main__":
    main()


