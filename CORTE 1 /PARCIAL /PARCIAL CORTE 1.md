PARCIAL CORTE 1
Conceptual
1. ¿que son los microcontroladores y los microprosesadores?
Microcontroladores: Son circuitos integrados que se pueden programar y que contienen, en un solo chip, la unidad central de procesamiento (CPU), la memoria y los periféricos. En los sistemas embebidos se emplean para supervisar tareas concretas.

Microprocesadores: Son circuitos que cumplen las funciones de la CPU, aunque requieren memoria y dispositivos periféricos externos. Se emplean en su mayoria en computadoras y sistemas de gran rendimiento.

2. Defina la arquitectura Von Neumann y la arquitectura de Harvard además: exponer sus características, ventajas y diferencias.
Arquitectura Von Neumann vs Arquitectura Harvard

Arquitectura	Características	Ventajas	Diferencias
Von Neumann	- Emplea una única memoria para las instrucciones y los datos.
- La CPU tramita las instrucciones de manera secuencial.
- Para la transferencia de datos y programas, emplea un único bus.	- Diseño sencillo.
- Menor complejidad de hardware.
- Se puede implementar con facilidad en computadoras de uso general.	- Instrucciones y datos comparten la misma memoria.
- Un solo bus provoca un acceso más lento.
Harvard	- Utiliza memorias distintas para las instrucciones y los datos.
- Posee buses independientes.
- Posibilita el acceso simultáneo a instrucciones y datos.	- Procesamiento más rápido.
- Mejores resultados en sistemas embebidos.
- Eficiencia más alta.	- Las instrucciones y los datos se guardan en memorias distintas.
- Permite un procesamiento simultáneo y más veloz.
3. ¿Que son los procesadores tipos RISC y tipo CISC?.
RISC: Procesadores con instrucciones mínimas y sencillas, lo que posibilita una mayor rapidez y eficiencia.

CISC: Procesadores con instrucciones complejas, capaces de realizar varias operaciones en una sola instrucción.

4. ¿Que es ARM?
ARM es un conjunto de arquitecturas de procesadores que se fundamenta en el diseño RISC (Reduced Instruction Set Computer). Su propósito es optimizar el rendimiento y la eficiencia energética en dispositivos con recursos escasos. Se usa mucho en dispositivos móviles, sistemas embebidos e Internet de las cosas (IoT). La arquitectura ARM proporciona un consumo energético reducido, lo que posibilita que los dispositivos tengan una mayor duración de la batería. Asimismo, usa instrucciones sencillas que optimizan la eficacia del procesamiento, producen menos calor y tienen un menor coste de fabricación.

5. ¿Cuál es la arquitectura de Arduino y qué características tiene?
Arduino emplea microcontroladores que se fundamentan en la arquitectura AVR. Esta última sigue el modelo Harvard y hace uso de un grupo de instrucciones RISC. Esta arquitectura posibilita la existencia de memorias individuales para los datos y el programa, lo que optimiza la eficacia del procesamiento.

Las principales caracteristicas son que tiene entradas y salidas analógicas y digitales, comunicación serie, temporizadores y consume poca energía. Asimismo, es fácil programarlo y se usa mucho para hacer proyectos electrónicos, sistemas embebidos y aplicaciones de IoT.

6. ¿Cuál es la arquitectura del PIC 16F887 y sus principales características?
El PIC 16F887 es un microcontrolador de la familia PIC, creado por Microchip. Su arquitectura, que sigue el modelo Harvard, está basada en RISC y emplea memorias distintas para datos y programa.

Este microcontrolador tiene como caracteristicas principales la capacidad de controlar distintos aparatos electrónicos, además de tener memoria Flash para guardar programas, de integrar periféricos y de consumir poca energía. Asimismo, por su eficiencia y facilidad de implementación, se usa mucho en proyectos de electrónica, sistemas embebidos y automatización.

Diseño
1. ¿Cómo plantearía el desarrollo de una base de datos con imágenes de los diferentes elementos de un laboratorio de telecomunicaciones?
La creación de la base de datos se llevaría a cabo por medio de un procedimiento que consiste en recolectar, organizar y etiquetar imágenes de los variados equipos que se encuentran en el laboratorio de telecomunicaciones. En primer lugar, se determinarían los componentes que quieren ser reconocidos, los cuales incluyen osciloscopios, routers, switches, generadores de señal, multímetros y cables de red. Con el objetivo de conseguir un conjunto de datos diverso que favorezca la mejora del entrenamiento del modelo de reconocimiento, luego se tomarían numerosas fotografías de cada elemento desde distintas distancias, perspectivas y condiciones de iluminación.

Las imágenes se clasificarían en carpetas, según el tipo de dispositivo, y se etiquetarían con herramientas para la anotación de imágenes. Por último, los datos se guardarían en una base de datos o un repositorio estructurado que posibilitaría su acceso para entrenar modelos de visión artificial. Más tarde, este conjunto de datos será empleado para capacitar al sistema responsable del reconocimiento automático de los componentes del laboratorio.

2. ¿Cómo crearía un sistema clasificador de elementos con la librería MediaPipe?
Para desarrollar el sistema de clasificaciones, se emplearían modelos de aprendizaje automático, la librería MediaPipe y OpenCV para examinar imágenes en tiempo real.

El sistema empezaría a grabar video usando una cámara que estuviera conectada al ordenador. Se procesarían todas las imágenes capturadas con métodos de visión artificial para determinar los rasgos importantes de los objetos que se encuentran en el laboratorio.

Más adelante, el modelo de aprendizaje automático que se ha entrenado antes con la base de datos de imágenes podría clasificar los objetos identificados y establecer a qué categoría pertenecen, como un osciloscopio, un multímetro o un router.

MediaPipe posibilitaría el procesamiento efectivo de las imágenes y la identificación de componentes como partes del cuerpo o personas, en tanto que el modelo de clasificación se ocuparía de identificar los elementos específicos del laboratorio.

Por último, el sistema presentaría en la pantalla el nombre del elemento detectado y un nivel de confianza en la clasificación.

3. ¿Cómo reconocería el sistema la velocidad de las personas en el laboratorio?
La velocidad de las personas se identificaría mediante el uso de MediaPipe Pose, una herramienta que posibilita la detección en tiempo real de los puntos esenciales del cuerpo humano.

El sistema distinguiría diversas áreas del cuerpo, como pies, caderas, hombros y cabeza, y anotaría la ubicación de cada una en cada fotograma del video grabado. Luego se calcularía cómo se mueven estos puntos de una imagen a la siguiente.

A través de MediaPipe Pose, una herramienta que permite identificar en tiempo real los puntos claves del cuerpo humano, se puede determinar la velocidad de las personas.

El sistema identificará diferentes partes del cuerpo, como los pies, las caderas, los hombros y la cabeza, y registrará la posición de cada área en cada fotograma del video grabado. Después, se calcularía cómo estos puntos se desplazan de una imagen a la otra.

4. ¿Cómo haría un despliegue en una plataforma web o móvil?
La estructura del sistema consistiría en una interfaz de usuario, un backend y una base de datos.

El procesamiento de imágenes, la implementación del modelo de reconocimiento y el análisis del movimiento humano se llevarían a cabo en el backend mediante herramientas como OpenCV, MediaPipe y Python.

La base de datos guardaría las fotografías empleadas durante el entrenamiento, además de los registros de eventos y detección producidos por el sistema.

Por último, se crearía una interfaz web o móvil que posibilite observar el video en tiempo real, las alertas creadas por el sistema y los objetos detectados. Se podría crear esta interfaz empleando tecnologías como Flutter, React o aplicaciones web fundamentadas en HTML y JavaScript.

Así, los usuarios tendrían la posibilidad de supervisar el laboratorio a distancia y recibir datos acerca del uso de los equipos y el comportamiento de las personas en el ambiente.

Empirica
Explicación del codigo.

Se implementa un algoritmo sencillo en Python que utiliza la cámara web para detectar las manos en tiempo real y mostrar únicamente los puntos correspondientes al pulgar. Para ello se utiliza la librería MediaPi.

El algoritmo filtra únicamente los puntos del pulgar y los dibuja sobre la imagen capturada por la cámara.

Librerías utilizadas
OpenCV: Captura y procesamiento de video.
MediaPipe: Detección de manos y puntos clave.
import cv2
import mediapipe as mp
Inicio del detector
Se configura el modelo para detectar hasta dos manos y realizar seguimiento en tiempo real.

detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
Se identificación de los puntos del pulgar
MediaPipe identifica 21 puntos en cada mano, pero solo se utilizan los puntos correspondientes al pulgar.

ID	Parte del Pulgar
1	Base
2	Articulación
3	Articulación
4	Punta
Estos se almacenan:

PULGAR_IDS = [1, 2, 3, 4]
Detección del pulgar
El algoritmo examina todos los puntos de referencia identificados en la mano y solamente selecciona aquellos que son del pulgar.

Después, se trazan los puntos y se unen a través de líneas para tener una representación visual de la estructura del dedo.

cv2.circle(frame, (x, y), 8, (255, 0, 0), -1)
Además, se presenta un texto que señala que el dedo pulgar ha sido detectado.

Resultado: https://youtu.be/I-Zqk3_kME4
