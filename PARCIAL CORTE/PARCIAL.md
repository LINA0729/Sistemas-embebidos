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
