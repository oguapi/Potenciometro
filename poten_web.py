#Importar librerias
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image  #Para poner imagen

import firebasepy

#Extraer los archivos pickle
with open('lin_reg.pkl', 'rb') as li:
    lin_reg= pickle.load(li)

with open('log_reg.pkl', 'rb') as lo:
    log_reg= pickle.load(lo)


def chequeo_contrasena():
    #Retorna true si el usuario tiene una contrasena correcta
    def contrasena_entrada():
        #Chequea si la contrasena entrada por el usuario es correcta
        nombre= st.session_state["username"]
        contrasena= st.session_state["password"]
        usuarios=["Andres","Kevin"]
        contrasenas=["12345"]
        if nombre in usuarios:
            if contrasena in contrasenas:
                st.session_state["password_correct"]= True
            else:
                st.session_state["password_correct"]= False
        else:
            st.session_state["password_correct"]= False
    
    if "password_correct" not in st.session_state:
        nprototipo= Image.open('image/nombrePrototipo.JPG') #Abrimos la imagen
        st.image(nprototipo,width=150)
        #Primero corremos la app, mostramos para ingresar usuario y contrasena
        st.text_input("Usuario", on_change=contrasena_entrada, key="username")
        st.text_input("Contraseña", type="password", on_change=contrasena_entrada, key="password")
        imagen= Image.open('image/logo espol.png') #Abrimos la imagen
        st.sidebar.image(imagen,None)
        return False
    elif not st.session_state["password_correct"]:
        #Contrasena incorrecta, mostrar lo entrado y error
        st.text_input("Usuario", on_change=contrasena_entrada, key="username")
        st.text_input(
            "Contrasena", type="password", on_change=contrasena_entrada, key="password"
        )
        st.error("😕 Usuario desconocido o contrasena incorrecta")
        imagen= Image.open('image/logo espol.png') #Abrimos la imagen
        st.sidebar.image(imagen,None)
        return False
    else:
        #contrasena correcta
        return True

def main():
    if chequeo_contrasena():
        col1, col2= st.columns(2) #Para ubicar en un contenedor con forma columna
        with col1:
            st.title("Potenciostato")  #titulo de la pagina
        with col2:
            #st.header("Representacion") #Encabezado
            st.image('image/potenciostatoRep.jpg',None,150)

        #SIDEBAR
        #----------------------------------------------------------
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
        if st.sidebar.button('Iniciar'):
            m=0
        #    if model == 'Linear Regression':
        #        st.success(classify(lin_reg.predict(df)))
        #    elif model == 'Logistic regression':
        #        st.success(classify(log_reg.predic(df)))
        st.sidebar.subheader("  ")
        st.sidebar.subheader("  ")
        #------------------------------------------------------------

        #Haremos el llamado del scrip q maneja la bd
        referencia= 'Lecturas'     #nodo donde se almaceno la informacion recolectada
        claves= firebasepy.claves(referencia) #extraemos el momento en que se hicieron las pruebas
        #El usuario escoja
        eleccion = st.selectbox("Cual prueba le gustaría mostrar?",claves)
        if st.button('Mostrar'):
            newvals= firebasepy.extraerVal(referencia+'/'+eleccion)
            m=0
            tabla= pd.DataFrame(newvals)
            #tabla1= tabla.transpose()
            st.subheader('Valores leidos')
            #st.write(tabla)
            #Manipulando el dataframe para mostrarla mejor
            #print(tabla['Bit'])
            #fila= tabla['Bit'].to_numpy.tolist()# la columna de interes la cambiamos a lista
            #print(fila)
            #tabla1= tabla.loc[:,('A0','A1','A2')]
            tabla1= tabla.set_index('Bit') #establesco la columna bit como el nuevo indice
            st.write(tabla1)
            #st.line_chart(tabla1['A0'])
            #st.bar_chart(tabla1.sort_index(False))

            if st.button('Descargar datos'):
            #   Boton para descargar los datos
                b=0
                tabla1.to_excel(file_name)
        #for key, muestras in newvals.items():
        #    tabla= pd.DataFrame(muestras, index=[m])
        #    m+=1

    #df.to_csv() #para exportarlo a csv

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

        st.subheader('Valores procesados')
        st.write(vals)

        #st.subheader(model)
        #st.write(df)
        
        #Boton para salir de la seccion
        if st.button("Cerrar"):
            st.session_state["password_correct"]= False


if __name__ == '__main__':
    main()
