# Laboratorio: Aplicaciones en Sistemas Embebidos

**Curso:** Aplicaciones en Sistemas Embebidos  
**Universidad:** Fundación Universitaria Compensar  
**Docente:** Diego Alejandro Barragán Vargas
**Autores:** Carlos Alberto Castro Castillo, Karen Stefania Rivera Carrero y Lina Marcela Contreras Sanabria.

---

## Contenido del Laboratorio

### 1. Piano Digital Interactivo (PIC16F887 + LM386N)
### 2. Detección de Objetos en Tiempo Real (YOLOv8)
### 3. Paisaje con Figuras de Lissajous (Osciloscopio)

---

## PUNTO 1: PIANO DIGITAL CON AMPLIFICADOR LM386N

### ¿Qué vamos a hacer?
Construir un piano digital que genere 8 notas musicales (Do a Do') usando PWM, con LEDs indicadores por nota y amplificación de audio mediante el integrado LM386N.

### Materiales
| Componente | Cantidad | Función |
|-----------|----------|---------|
| PIC16F887 | 1 | Microcontrolador principal |
| LM386N | 1 | Amplificador de audio |
| Botones pulsadores | 8 | Entrada de notas |
| LEDs | 8 | Indicador visual por nota |
| Resistencias 10kΩ | 8 | Pull-down para botones |
| Capacitores 10µF | 2 | Desacople y entrada PWM |
| Capacitor 33µF | 1 | Salida altavoz |
| Altavoz 8Ω | 1 | Reproducción de audio |
| Protoboard + cables | - | Montaje |

### Desarrollo

#### Paso 1: Configuración del PIC16F887
```c
OSCCON = 0b01110001;      // Oscilador interno 8 MHz
TRISB = 0xFF;             // PORTB como entrada (botones)
TRISD = 0x00;             // PORTD como salida (LEDs)
TRISC = 0b11111011;       // RC2 como salida PWM
```

#### Paso 2: Configuración del PWM
- **Timer2:** Período = 10ms (1 kHz base)
- **CCP1 (RC2):** Modo PWM para generar tonos
- **Frecuencias:** Do=261Hz, Re=293Hz, Mi=329Hz... Do'=523Hz

#### Paso 3: Función de Notas
```c
void Generar_Nota(unsigned int frecuencia) {
    switch(frecuencia) {
        case DO:      CCPR1L = 122; Encender_LED(0); break;
        case RE:      CCPR1L = 109; Encender_LED(1); break;
        case MI:      CCPR1L = 97;  Encender_LED(2); break;
        // ... resto de notas
    }
}
```

#### Paso 4: Conexión del LM386N
```
RC2 (PWM) ──[10µF]──→ PIN 3 (LM386 entrada+)
PIN 2 (entrada-) ────→ GND
PIN 6 (Vcc) ─────────→ +5V [10µF desacople]
PIN 7 (Bypass) ──[10µF]──→ GND
PIN 1 (Ganancia) ──[10kΩ + 10µF]──→ +5V (Ganancia 200x)
PIN 5 (Salida) ──[33µF]──→ ALTAVOZ
```

<img width="900" height="1600" alt="WhatsApp Image 2026-04-25 at 7 45 18 PM" src="https://github.com/user-attachments/assets/5de18a70-11c6-4bcd-a3e9-f81bb32a8e60" />

### Estructura del PIC16F887
```
Pin 1 (MCLR) → +5V vía resistencia 10kΩ
Pin 11 (VDD) → Carril positivo (+5V)
Pin 12 (VSS) → Carril negativo (GND)
Pin 32 (VDD) → Carril positivo (+5V)
Pin 31 (VSS) → Carril negativo (GND)
Pines BOTONES (RB0 a RB7):
Para cada botón: Un extremo a +5V, otro a su pin RB (33-40)
Colocar resistencia 10kΩ pull-down entre pin RB y GND
Ejemplo RB0: +5V ──[Button]── Pin 33, 10kΩ ──── GND

```
<img width="900" height="1600" alt="image" src="https://github.com/user-attachments/assets/362a04e0-eade-4ab6-b5a8-eddae6ee37a1" />

<img width="900" height="1600" alt="image" src="https://github.com/user-attachments/assets/ca957148-23d0-4551-87c5-668202f2d943" />


### Conclusiones
✓ El PIC genera correctamente las 8 notas musicales por PWM  
✓ El LM386N amplifica la señal débil del PWM a niveles audibles  
✓ Los LEDs proporcionan retroalimentación visual inmediata  

https://youtube.com/shorts/Q-mAMVIzH8Q?feature=share
---

##  PUNTO 2: DETECCIÓN DE OBJETOS CON YOLOv8

### ¿Qué vamos a hacer?
Clasificar objetos en tiempo real usando una cámara web con el modelo YOLOv8 entrenado. El programa detecta: motocicletas, carros, buses, peatones y bicicletas (versión juguete).

### Materiales
| Componente | Función |
|-----------|---------|
| Python 3.8+ | Lenguaje de programación |
| YOLOv8 (ultralytics) | Modelo de detección |
| OpenCV | Captura y procesamiento de video |
| Cámara web | Entrada de video en tiempo real |
| GPU (opcional) | Acelerar procesamiento |

### Desarrollo

#### Paso 1: Instalación de dependencias
```bash
pip install ultralytics opencv-python
python -m yolo detect predict model=yolov8n.pt source=0
```

#### Paso 2: Cargar modelo entrenado
```python
from ultralytics import YOLO
model = YOLO('runs/detect/train/weights/best.pt')
```

#### Paso 3: Capturar video en vivo
```python
import cv2
cap = cv2.VideoCapture(0)  # 0 = cámara por defecto

while True:
    ret, frame = cap.read()
    results = model(frame)
    
    # Dibujar detecciones
    annotated_frame = results[0].plot()
    cv2.imshow('YOLOv8 Detección', annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### Estructura del Código
```
main.py
├── Importar YOLO y OpenCV
├── Cargar modelo (best.pt)
├── Inicializar cámara
├── Loop principal:
│   ├── Capturar frame
│   ├── Enviar a YOLO
│   ├── Procesar detecciones
│   ├── Dibujar bounding boxes
│   └── Mostrar resultado
└── Liberar recursos
```

**Clases detectadas:**
- 🏍️ Motocicleta
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/a8c9ca66-a25b-4df7-952e-1bbc76e90274" />

- 🚗 Carro
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/3e8b404c-927e-414c-b2e1-87500d98d4c0" />

- 🚌 Bus
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/451031b1-ecf4-4bdb-b434-7bb07a683750" />

- 👤 Peatón
 <img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/51027267-5982-4f09-96b7-773f596ebe0d" />

- 🚲 Bicicleta
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/814bdd4d-fce1-4f28-a464-585d63f7573a" />

### Conclusiones
✓ YOLOv8 detecta objetos en tiempo real con alta precisión  
✓ Interfaz simple con OpenCV para visualización  
✓ Modelo entrenado específicamente para objetos juguete  
✓ Compatible con diferentes fuentes de video (USB, DroidCam)  
✓ Aplicable a sistemas de vigilancia y robótica autónoma

---

## PUNTO 3: FIGURAS DE LISSAJOUS EN OSCILOSCOPIO

### ¿Qué vamos a hacer?
Diseñar un paisaje mediante figuras de Lissajous en un osciloscopio, utilizando un sistema embebido (Arduino UNO) y componentes electrónicos básicos. El propósito es que los estudiantes comprendan la relación entre señales sinusoidales, generación de patrones gráficos y la interacción hardware–software.

### Materiales

| Componente | Cantidad | Función |
|-----------|----------|---------|
| Arduino UNO | 1 | Microcontrolador principal |
| Resistencias 1kΩ | 2 | Filtrado y suavizado de señal |
| Condensadores 0.47µF | 2 | Filtrado y suavizado de señal |
| Potenciómetro 1kΩ | 1 | Control de velocidad de dibujo |
| Osciloscopio (Proteus) | 1 | Visualización de patrones |
| Software Proteus | - | Simulación del circuito y carga del código Arduino |

### Justificación del montaje
Aunque inicialmente se recomendaba el uso de un multiplexor de 8 o 16 canales, se optó por una solución más sencilla con Arduino y componentes pasivos. Esto permite a los estudiantes repasar desde cero conceptos de:

- Generación de señales PWM en microcontroladores.
- Filtrado básico con resistencias y condensadores.
- Control de velocidad y forma de la figura mediante un potenciómetro.
- Visualización de patrones en osciloscopio.

### Desarrollo

#### Paso A: Diseño del circuito en Proteus

- Abrir Proteus y crear un nuevo proyecto.
- Presionar **P (Pick Devices)** y agregar los siguientes componentes:
  - Arduino UNO
  - Oscilloscope
  - Resistencias (2 × 1kΩ)
  - Condensadores (2 × 0.47µF)
  - Potenciómetro (1kΩ)
  - Ground (obligatorio para referencia de 0V)
- Conectar las salidas digitales del Arduino (pines 5 y 6) hacia el osciloscopio, pasando por las resistencias y condensadores para suavizar la señal.
- Conectar el potenciómetro al pin analógico A0 para controlar la velocidad de dibujo.

  <img width="921" height="352" alt="image" src="https://github.com/user-attachments/assets/810fb851-01e6-4e4f-8adc-244f8c07d7dd" />


#### Paso B: Programación del Arduino

```cpp
int X_pin = 6;
int Y_pin = 5;
int Pot   = A0;
int point_delay = 1000;

#define how_many_vertices 19

byte x_axis[how_many_vertices] = {9,9,3,9,4,9,6,9,8,10,12,11,14,11,16,11,17,11,11};
byte y_axis[how_many_vertices] = {3,6,6,10,10,14,14,17,17,19,17,17,14,14,10,10,6,6,3};

void setup() {
  pinMode(X_pin, OUTPUT);
  pinMode(Y_pin, OUTPUT);
  pinMode(Pot, INPUT);
}

void loop() {
  unsigned char loopcount;
  point_delay = map(analogRead(Pot), 0, 1023, 500, 3000);
  for (loopcount = 0; loopcount < how_many_vertices; loopcount++) {
    analogWrite(X_pin, map(x_axis[loopcount], 0, 19, 50, 200));
    analogWrite(Y_pin, map(y_axis[loopcount], 0, 19, 50, 200));
    delayMicroseconds(point_delay);
  }
}
```

#### Paso C: Funcionamiento esperado

- El Arduino genera señales PWM en los pines X e Y.
- El potenciómetro ajusta el **delay** entre puntos, modificando la velocidad de dibujo.
- El osciloscopio debería mostrar figuras similares a paisajes (árboles y montañas) mediante patrones de Lissajous.

#### Paso D: Resultados obtenidos

- El montaje en Proteus funcionó en cuanto a la generación de señales y visualización en el osciloscopio.
- Sin embargo, el **código no generó el paisaje esperado**, ya que la secuencia de coordenadas en los arrays `x_axis` y `y_axis` no estaba correctamente diseñada para formar figuras complejas.
- Se observó que el osciloscopio mostraba patrones, pero no representaban claramente árboles o montañas.

<img width="921" height="585" alt="image" src="https://github.com/user-attachments/assets/8bfcfa78-b18e-4133-a24b-28430268a31a" />


### Conclusiones

✓ El experimento permitió comprender cómo un microcontrolador puede generar figuras en un osciloscopio mediante señales PWM  
✓ Se evidenció la importancia de diseñar correctamente las coordenadas y tiempos de retardo para obtener figuras reconocibles  
✓ Aunque no se logró el paisaje esperado, el proceso fue útil para practicar diseño de circuitos en Proteus, programación básica en Arduino y uso del osciloscopio para visualizar señales  
