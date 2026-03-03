Sistema de Detección de Postura con Visión Artificial y Control Embebido

Descripción General.

Este proyecto pone en marcha un sistema de detección de la postura en tiempo real que permite saber si una persona está sentada o de pie, mediante visión por computadora y procesamiento geométrico de puntos del cuerpo.

El sistema incorpora procesamiento en Python y comunicación serial con un Arduino Uno, que opera como módulo de salida física a través de LEDs indicadores.

Objetivo

Demostrar la integración entre:

* Visión artificial
* Análisis geométrico
* Comunicación serial
* Sistemas embebidos

Flujo de funcionamiento.

Cámara Web
-->
Procesamiento en Python
-->
Detección de pose con MediaPipe
-->
Cálculo del ángulo de la rodilla
-->
Clasificación de postura
-->
Comunicación serial
-->
Control de LEDs con Arduino

Fundamento Técnico
1. Captura de Video.

Se utiliza la librería OpenCV: 
```python
cap = cv2.VideoCapture(0)
```
Cada frame es procesado individualmente.

2. Detección de Landmarks Corporales.
Se utiliza: MediaPipe Pose

Este modelo tiene la capacidad de identificar 33 puntos anatómicos del cuerpo humano.

Para el proyecto, se emplean:
* Cadera
* Rodilla
* Tobillo
  
3. Cálculo Geométrico del Ángulo

Se calcula el ángulo en la rodilla mediante producto punto:

$$
\theta = \cos^{-1}\left(\frac{\vec{BA}\cdot\vec{BC}}{|\vec{BA}||\vec{BC}|}\right)
$$


