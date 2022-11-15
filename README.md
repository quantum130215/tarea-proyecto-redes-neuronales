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

Me aleje de la idea original de detectar mi rostros con miles de imagenes, ya que por lo limitado que es mi computadora, no tiene la capacidad de procesar tantas 
a tal grado que intente hacer un poco de optimizacion arriegando el resultado de predicción reduciendo la cantidad de imagenes en el codigo que comence al principio
del proyecto,pero aun asi mi computadora no podia terminar el trabajo, tardando bastante en hacer la lectura de imagenes. Procedí a leer lo que se nos pedia en la
tarea y se me ocurriouna red neuronal de detector de rostros como en los celulares, lo que al final se termino desarrollando.

Se uso la biblioteca OpenCV, ya que investiando nos da una gran cantidad de herramientas de procesamiento de imágenes y videos para identificar objetos, rostros o
incluso la escritura a mano de un ser humano, usando varias de las herramientas se armo el codigo. 

Creamos una base de datos donde se guardaran nuestras imagenes, estas imagenes las mandamos a la carpeta images, en la seccion del if isExist, el codigo comparara la
base de datos ya existentes, si llegara a tener dos bases de datos el mismo nombre, el codigo lo notara y solicitara un nuevo nombre para poder guardar esta nueva
entrada de datos, si no comparten el mismo nombre, este solo creara la base de datos nueva. Luego pasando a la siguiente parte del codigo, generaremos la base de datos 
sacando los frames de un video que se realiza con la camara conectada al dispositivo.

Para la siguiente parte del codigo, mediante la herramienta de VideoCapture obtenemos informacion deseada y la comparará con la base de datos que existe en la
computadora, cargamos el modelo con una base de datos que queremos, y al final se hace un ciclo que comparará las imagenes de entrada con el rostro que esta siendo 
grabado, generando un recuadro con la herramienta "rectangle" , que permité comparar las imagenes de la base de datos con la entrada de datos generada por el video
generado.
