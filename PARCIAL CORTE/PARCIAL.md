# **PARCIAL CORTE1**

## **Conceptual**

**¿que son los microcontroladores?**


**Defina la arquitectura Von 



## **Diseño**

**1. ¿Cómo plantearía el desarrollo de una base de datos con imágenes de los diferentes elementos de un laboratorio de telecomunicaciones?**

La creación de la base de datos se llevaría a cabo por medio de un procedimiento que consiste en recolectar, organizar y etiquetar imágenes de los variados equipos que se encuentran en el laboratorio de telecomunicaciones.
En primer lugar, se determinarían los componentes que quieren ser reconocidos, los cuales incluyen osciloscopios, routers, switches, generadores de señal, multímetros y cables de red. Con el objetivo de conseguir un conjunto de datos diverso que favorezca la mejora del entrenamiento del modelo de reconocimiento, luego se tomarían numerosas fotografías de cada elemento desde distintas distancias, perspectivas y condiciones de iluminación.

Las imágenes se clasificarían en carpetas, según el tipo de dispositivo, y se etiquetarían con herramientas para la anotación de imágenes. Por último, los datos se guardarían en una base de datos o un repositorio estructurado que posibilitaría su acceso para entrenar modelos de visión artificial. Más tarde, este conjunto de datos será empleado para capacitar al sistema responsable del reconocimiento automático de los componentes del laboratorio.


**2. ¿Cómo crearía un sistema clasificador de elementos con la librería MediaPipe?**

Para desarrollar el sistema de clasificaciones, se emplearían modelos de aprendizaje automático, la librería MediaPipe y OpenCV para examinar imágenes en tiempo real.

El sistema empezaría a grabar video usando una cámara que estuviera conectada al ordenador. Se procesarían todas las imágenes capturadas con métodos de visión artificial para determinar los rasgos importantes de los objetos que se encuentran en el laboratorio.

Más adelante, el modelo de aprendizaje automático que se ha entrenado antes con la base de datos de imágenes podría clasificar los objetos identificados y establecer a qué categoría pertenecen, como un osciloscopio, un multímetro o un router.

MediaPipe posibilitaría el procesamiento efectivo de las imágenes y la identificación de componentes como partes del cuerpo o personas, en tanto que el modelo de clasificación se ocuparía de identificar los elementos específicos del laboratorio.

Por último, el sistema presentaría en la pantalla el nombre del elemento detectado y un nivel de confianza en la clasificación.


**3. ¿Cómo reconocería el sistema la velocidad de las personas en el laboratorio?**

La velocidad de las personas se identificaría mediante el uso de MediaPipe Pose, una herramienta que posibilita la detección en tiempo real de los puntos esenciales del cuerpo humano.

El sistema distinguiría diversas áreas del cuerpo, como pies, caderas, hombros y cabeza, y anotaría la ubicación de cada una en cada fotograma del video grabado. Luego se calcularía cómo se mueven estos puntos de una imagen a la siguiente.

A través de MediaPipe Pose, una herramienta que permite identificar en tiempo real los puntos claves del cuerpo humano, se puede determinar la velocidad de las personas.

El sistema identificará diferentes partes del cuerpo, como los pies, las caderas, los hombros y la cabeza, y registrará la posición de cada área en cada fotograma del video grabado. Después, se calcularía cómo estos puntos se desplazan de una imagen a la otra.


**4. ¿Cómo haría un despliegue en una plataforma web o móvil?**

La estructura del sistema consistiría en una interfaz de usuario, un backend y una base de datos.

El procesamiento de imágenes, la implementación del modelo de reconocimiento y el análisis del movimiento humano se llevarían a cabo en el backend mediante herramientas como OpenCV, MediaPipe y Python.

La base de datos guardaría las fotografías empleadas durante el entrenamiento, además de los registros de eventos y detección producidos por el sistema.

Por último, se crearía una interfaz web o móvil que posibilite observar el video en tiempo real, las alertas creadas por el sistema y los objetos detectados. Se podría crear esta interfaz empleando tecnologías como Flutter, React o aplicaciones web fundamentadas en HTML y JavaScript.

Así, los usuarios tendrían la posibilidad de supervisar el laboratorio a distancia y recibir datos acerca del uso de los equipos y el comportamiento de las personas en el ambiente.

