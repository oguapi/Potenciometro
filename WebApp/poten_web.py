#Importar librerias
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image  #Para poner imagen

import firebasepy

#Extraer los archivos pickle
""" with open('lin_reg.pkl', 'rb') as li:
    lin_reg= pickle.load(li)

with open('log_reg.pkl', 'rb') as lo:
    log_reg= pickle.load(lo) """

#Funcion para clasificar las plantas
def classify(num):
    if num == 0:
        return "Setosa"
    elif num == 1:
        return "Vestinosa"
    else:
        return "Virginica"

def main():
    
    col1, col2= st.columns(2) #Para ubicar en un contenedor con forma columna
    with col1:
        st.title("Potenciostato")  #titulo de la pagina
    with col2:
        #st.header("Representacion") #Encabezado
        st.image('WebApp/image/potenciostatoRep.jpg',None,150)

    imagen= Image.open('image/logo espol.png') #Abrimos la imagen
    st.sidebar.image(imagen,None)

    st.sidebar.header("Interfaz de Usuario")  #entrada de datos del usuario

    def user_input_parameters():
        sepal_length= st.sidebar.slider('Rango minimo',-3300, 0, -250) #minimo, maxino, v
        sepal_width= st.sidebar.slider('Rango maximo',0, 3300, 250)
        #petal_length= st.sidebar.slider('Petal length',1.0, 6.9, 1.3)
        #petal_width= st.sidebar.slider('Petal length',0.1, 2.5, 0.2)
        data=  {'sepal_length': sepal_length,
                'sepal_width': sepal_width#,
                #'petal_length': petal_length,
                #'petal_width': petal_width,

                }
        features= pd.DataFrame(data, index=[0])
        return features

    df= user_input_parameters()
    

    #Haremos el llamado del scrip q maneja la bd
    referencia= 'Lecturas'
    newvals= firebasepy.extraerVal(referencia)
    m=0
    tabla= pd.DataFrame(newvals)
    tabla1= tabla.transpose()
    #for key, muestras in newvals.items():
    #    tabla= pd.DataFrame(muestras, index=[m])
    #    m+=1

    #El usuario escoja
    #option= ['Linear Regression','Logistic Regression', 'SVM']
    #model= st.sidebar.selectbox("Cual modelo te gustaria usar?",option)

    def get_db_firebase():
        prueba= {
            'Voltaje equivalente a Corriente': 0.5,
            'Voltaje de Control': 2.2
            }
        features= pd.DataFrame(prueba, index=[0])
        return features
    vals= get_db_firebase()


    st.subheader('Valores leidos')
    st.write(tabla1)

    st.subheader('Valores procesados')
    st.write(vals)

    #st.subheader(model)
    #st.write(df)

    if st.sidebar.button('Iniciar'):
        m=0
    #    if model == 'Linear Regression':
    #        st.success(classify(lin_reg.predict(df)))
    #    elif model == 'Logistic regression':
    #        st.success(classify(log_reg.predic(df)))
    st.sidebar.subheader("  ")
    st.sidebar.subheader("  ")

    st.line_chart(tabla1)
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



if __name__ == '__main__':
    main()
