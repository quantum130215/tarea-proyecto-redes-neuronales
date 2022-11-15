# tarea-proyecto-redes-neuronales
proyecto de tarea 
INTRODUCCION

Se desarrolló un codigo de deteccion facial, que permite crear un registro accediendo
a la camara del dispositivo, haciendo imagenes que luego se usaran para tener una base
de datos para que la red neuronal pueda identificar a quien esta usando el dispositivo
en ese momento, esto teniendo algunas aplicaciones, como son la seguridad del mismo
dispositivo si no se quiere que alguien más acceda al mismo.

NOTA 
Cabe destacar que no se hizo un codigo de bloqueo que reaccione a este identificador
facial, solo se hizo la parte de detección. El codigo de identificacion y no de
recoleccion se puede correr sin tener que correr el codigo de recoleccion de datos una
vez este ya haya sido ejecutado, ya que el nombre y las imagenes estaran guardadas en
la computadora.

PLANTEAMIENTO DE LO QUE SE HIZO 

Me aleje de la idea original de detectar mi rostros con miles de imagenes, ya que por
lo limitado que es mi computadora, no tiene la capacidad de procesar tantas a tal
grado que intente hacer un poco de optimizacion arriegando el resultado de predicción
reduciendo la cantidad de imagenes en el codigo que comence al principio del proyecto,
pero aun asi mi computadora no podia terminar el trabajo, tardando bastante en hacer
la lectura de imagenes. Porcedí a leer lo que se nos pedia en la tarea y se me ocurrio
una red neuronal de detector de rostros como en los celulares, lo que al final se
termino desarrollando.

La biblioteca de OpenCV que se importa de manera "import cv2", ya que esta nos da
un gran catalogo de herramientas, aunque se tiene que descargar la biblioteca yendo
al cmd y teclear "pip install cv2" y con este tener todas estas herremientas. 
Usando el comando para poder acceder a la camara usando "cv2.VideoCapture()" y 
luego se escribio un clasificador de rostros pre entrenado de la seccion de 
herramientas de cv2 usando el comando 
de"cv2.CascadeClassifier(cv2.data.haarcascades), una vez que tuvimos esto y 
teniamos todo listo se coloco un input para poder darle un nombre al registro de 
las imagenes que se iban a sacar y un cilco for por si se vuelve a ingresar el 
mismo nombre pedir que se introduzca otro. Luego se hizo un ciclo for que será el que nos 
creé las imagenes dandole a esta variable un numero alto de imagenes al cual 
llegar, ya que, aunque podemos ponerle un número pequeño para que no tarde tanto, 
no es recomendable para que tenga una buena cantidad que pueda contrastar cuando se 
carguen varios nombres, la siguiente parte del codigo que es la parte de 
identificacción del rostro, se uso el mismo comando para acceder a la camara del 
dispositivo y se declaro como la variable cap esto con la finalidad de poder 
despues ajustar los parametros de la imagen, luego se uso la herramienta que nos 
permite dibujar rectangulos en las imagenes de hechas con la camara para que, con 
el clasificador que estamos usando, pueda este detectar y clasificar las imagenes 
que correspondan a la que se encuentra frente a la camara.






