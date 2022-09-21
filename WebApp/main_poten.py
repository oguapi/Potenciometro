#importamos la librerias necesarias
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
import pickle

#Cargar los datos de un dataset
iris= datasets.load_iris()

x= iris.data #variable donde poner los datos
y= iris.target #variable de entrenamiento o objetivo

#Separar los datos en entrenamiento y en prueba
x_train, x_test, y_train, y_test= train_test_split(x, y)

lin_reg= LinearRegression()
log_reg= LogisticRegression()
svc_m= SVC()

#Entrenar modelos
lin_regr= lin_reg.fit(x_train,y_train)
log_regr= log_reg.fit(x_train,y_train)
svc_mo= svc_m.fit(x_train,y_train)

#Creamos un archivo para guardar los datos, es como json
with open('lin_reg.pkl', 'wb') as li:
    pickle.dump(lin_regr, li)

with open('log_reg.pkl', 'wb') as lo:
    pickle.dump(log_regr, lo)

