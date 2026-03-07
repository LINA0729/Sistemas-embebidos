# **PARCIAL CORTE1**

## **Conceptual**

**1. ¿que son los microcontroladores y los microprosesadores?**

Microcontroladores:
Son circuitos integrados que se pueden programar y que contienen, en un solo chip, la unidad central de procesamiento (CPU), la memoria y los periféricos. En los sistemas embebidos se emplean para supervisar tareas concretas. 

Microprocesadores:
Son circuitos que cumplen las funciones de la CPU, aunque requieren memoria y dispositivos periféricos externos. Se emplean en su mayoria en computadoras y sistemas de gran rendimiento. 

**2. Defina la arquitectura Von Neumann y la arquitectura de Harvard además: exponer sus características, ventajas y diferencias.**

## Arquitectura Von Neumann vs Arquitectura Harvard

| Arquitectura | Características | Ventajas | Diferencias |
|---|---|---|---|
| **Von Neumann** | - Emplea una única memoria para las instrucciones y los datos.<br>- La CPU tramita las instrucciones de manera secuencial.<br>- Para la transferencia de datos y programas, emplea un único bus. | - Diseño sencillo.<br>- Menor complejidad de hardware.<br>- Se puede implementar con facilidad en computadoras de uso general. | - Instrucciones y datos comparten la misma memoria.<br>- Un solo bus provoca un acceso más lento. |
| **Harvard** | - Utiliza memorias distintas para las instrucciones y los datos.<br>- Posee buses independientes.<br>- Posibilita el acceso simultáneo a instrucciones y datos. | - Procesamiento más rápido.<br>- Mejores resultados en sistemas embebidos.<br>- Eficiencia más alta. | - Las instrucciones y los datos se guardan en memorias distintas.<br>- Permite un procesamiento simultáneo y más veloz. |

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

