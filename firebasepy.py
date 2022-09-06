import firebase_admin  #Base de datos
from firebase_admin import credentials
from firebase_admin import db
#from firebase import firebase
#import random

#para no inicializar mas de una vez la app de firebase
if not firebase_admin._apps:
    #cargo el certificado de mi proyecto firebase
    firebase_sdk= credentials.Certificate('esp32base-64b3f-firebase-adminsdk-i4rwi-27859964f5.json')

    #Hacemos referencia a la base de datos en tiempo real de firebase
    firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://esp32base-64b3f-default-rtdb.firebaseio.com/'})

""" 
#Creo una coleccion con el nombre productos con un producto
ref= db.reference('/Lecturas')
ref.push({'A0':'0.05','A1':'0.5','A2':'0.012'})
 """

""" 
#Modificar un dato
ref= db.reference('Productos')
producto_ref= ref.child('-NAal5O8FzWQiW1jQP-f')#damos la referencia del producto a modificar
producto_ref.update({'modelo':'Two'})
 """
""" 
#Agregar un producto mas
ref= db.reference('Lecturas')
producto= {'A0':'0.03','A1':'0.035','A2':'0.047'}
lectura_ref= ref.push(producto)
 """
""" #Modificar varios datos
ref= db.reference("Productos")
ref.update({
    '-NAal5O8FzWQiW1jQP-f/modelo':'Three',
    '-NAakEnuagtQlquc1xr3/marca':'Espol'
}) """

#Leemos la base de datos usando metodo GET
def extraerVal(referencia):
    ref= db.reference(referencia)
    snapshot= ref.get()
    #for key, muestras in snapshot.items():
    #    print(muestras)
    return snapshot

#Leemos la base de datos usando metodo GET
""" #ref= db.reference('Productos')
snapshot= ref.get()
print(snapshot)
for key, muestras in snapshot.items():
    #print(muestras)#imprimo todos los valores
    for entrada, valor in muestras.items():
        #print(valor)
        break
 """

##snapshot= ref.orderByValue.limit_to_last(1).get()
#print(snapshot)

#karen= ['la belleza de lo desagradable','falsos recuerdos','perderme para encontrarte','pecados placenteros','fuego', 'the dare','un beso bajo la lluvia','los cuervos','still with you','boulevard']
#print(random.choice(karen))
