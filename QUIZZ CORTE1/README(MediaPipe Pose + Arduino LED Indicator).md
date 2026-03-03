# **Sistema de Detección de Postura con Visión Artificial y Control Embebido**

## **Descripción General.**

Este proyecto pone en marcha un sistema de detección de la postura en tiempo real que permite saber si una persona está sentada o de pie, mediante visión por computadora y procesamiento geométrico de puntos del cuerpo.

El sistema incorpora procesamiento en Python y comunicación serial con un Arduino Uno, que opera como módulo de salida física a través de LEDs indicadores.

## **Objetivo**

Demostrar la integración entre:

* Visión artificial
* Análisis geométrico
* Comunicación serial
* Sistemas embebidos

## **Flujo de funcionamiento.**

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

## **Fundamento Técnico.**

**1. Captura de Video.**

Se utiliza la librería OpenCV: 
```python
cap = cv2.VideoCapture(0)
```
Cada frame es procesado individualmente.

**2. Detección de Landmarks Corporales.**
Se utiliza: MediaPipe Pose

Este modelo tiene la capacidad de identificar 33 puntos anatómicos del cuerpo humano.

Para el proyecto, se emplean:
* Cadera
* Rodilla
* Tobillo

  <img width="220" height="242" alt="image" src="https://github.com/user-attachments/assets/eee6083a-d97f-49b9-ac4d-7ad16c5930ae" />

  
**3. Cálculo Geométrico del Ángulo**

Se calcula el ángulo en la rodilla mediante producto punto:

$$
\theta = \cos^{-1}\left(\frac{\vec{BA}\cdot\vec{BC}}{|\vec{BA}||\vec{BC}|}\right)
$$

Donde:

A = Cadera

B = Rodilla

C = Tobillo

Se implementa con NumPy.

**4. Criterio de Clasificación**
   
| Ángulo  | Postura |
|----------|----------|
| > 160°   | PARADA   |
| ≤ 160°   | SENTADA  |

Se definió el umbral de maemnra experimental.

**5. Comunicación Serial**

Se establece comunicación con:

Arduino IDE
-->
Arduino Uno

Configuración:
```python
arduino = serial.Serial('COM3', 9600)
```
| Carácter | Significado     |
| -------- | --------------- |
| 'R'      | Persona parada  |
| 'G'      | Persona sentada |
| 'X'      | Apagar LEDs     |

<img width="407" height="782" alt="image" src="https://github.com/user-attachments/assets/0b31cbb9-abf0-4b80-9da7-46079a82479e" />
<img width="592" height="800" alt="image" src="https://github.com/user-attachments/assets/2b94215f-4fc8-4dae-b41e-e7e58035434b" />


**6. Control Embebido**

Arduino controla:

* LED Rojo --> PARADO
* LED Verde--> SENTADO

**7. estión Segura de Recursos**
Se estructura:
```python
try:
    # código principal
finally:
    arduino.write(b'X')
    cap.release()
    arduino.close()
```

## **Requisitos del Sistema**

**💻 Requisitos de Software**

* Python 3.11
* OpenCV
* MediaPipe
* NumPy
* PySerial
* Arduino IDE

Instalación:
```python
pip install opencv-python mediapipe numpy pyserial
```

**🔌Requisitos de Hardware**

* Cámara web
* Arduino Uno
* 2 LEDs
* 2 resistencias (220Ω – 330Ω)
* Protoboard
* Cables jumper

  <img width="357" height="456" alt="image" src="https://github.com/user-attachments/assets/b7ebf556-8bb7-470d-a13d-bb0427feb13d" />

## **Resultados Observados**

* Detección estable con buena iluminación
* Baja latencia serial
* Respuesta inmediata del hardware
* Apagado seguro automático

Video funcinamiento final: https://youtube.com/shorts/lY-rCZDFeJQ?feature=share

## **Conclusión.**

Este proyecto demuestra una integración funcional entre visión por computadora y sistemas embebidos, utilizando un enfoque geométrico eficiente para clasificación de postura.

## **Autores**

* Karen Stefania Rivera Carrero
* Lina Marcela Contreras Sanabria
* Carloa Alberto Castro Castillo

