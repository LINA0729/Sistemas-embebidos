# PARQUEADERO AUTOMATIZADO CON DETECCIÓN DE VEHÍCULOS

**Curso:** Aplicaciones en Sistemas Embebidos  
**Universidad:** Fundación Universitaria Compensar  
**Docente:** Diego Alejandro Barragán Vargas
**Autores:** Carlos Alberto Castro Castillo, Karen Stefania Rivera Carrero y Lina Marcela Contreras Sanabria.
---

# PARTE 1: CONCEPTUAL

## 1. ¿Qué es un Sistema de Parqueadero Automatizado?

Un sistema de parqueadero automatizado es un conjunto de tecnologías de hardware y software que permite la apertura y cierre automático de puertas de acceso. 

**Componentes principales:**
- **Hardware de control:** Arduino UNO (microcontrolador)
- **Actuadores:** Motor DC (9V) controlado por relé
- **Sensores:** Cámara Celular para captura visual
- **Inteligencia artificial:** YOLO (You Only Look Once) para detección de vehículos
- **Indicadores:** LEDs de estado (verde: abierto, rojo: cerrado)

---

## 2. ¿Cuál es la relación entre Arduino y los Microcontroladores?

**Arduino UNO** es una plataforma de desarrollo basada en el microcontrolador **ATmega328P**.

**En el parqueadero:** Arduino ejecuta la lógica de control del motor y LEDs, recibiendo comandos desde la computadora mediante comunicación serial (USB).

---

## 3. ¿Qué es YOLO (You Only Look Once)?

YOLO es un algoritmo de visión artificial basado en redes neuronales convolucionales (CNN) que permite la **detección de objetos en tiempo real**.

### Características de YOLO:

- **Velocidad:** Procesa imágenes completas en una sola pasada
- **Precisión:** Detecta múltiples objetos simultáneamente
- **Clases detectadas:** En nuestro caso, vehículos (autos, motos, camiones, buses)

**En el parqueadero:** YOLO identifica vehículos en el video de la cámara la cantidad de espacios libres y ocupados.

---

## 4. ¿Cuál es la Arquitectura del Sistema Completo?

### Arquitectura Propuesta:

```
┌─────────────────────────────────────────────────────────────┐
│                        CAPA DE PRESENTACIÓN                │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │ Monitor     │  │ LEDs (RGB)   │  │ Log en Consola  │   │
│  │ Serial IDE  │  │ Verde/Rojo   │  │ (Python)        │   │
│  └─────┬───────┘  └──────┬───────┘  └────────┬────────┘   │
└────────┼──────────────────┼──────────────────┼─────────────┘
         │                  │                  │
         │         ┌────────▼──────────────────▼──────┐
         │         │   CAPA DE APLICACIÓN             │
         │         │  ┌──────────────────────────┐    │
         │         │  │ Arduino IDE               │    │
         │         │  │ Python (YOLO/Voz)        │    │
         │         │  │ OpenCV                   │    │
         │         │  └──────────────────────────┘    │
         │         └────────┬───────────────────────────┘
         │                  │
         │    ┌─────────────▼──────────────┐
         │    │  CAPA DE COMUNICACIÓN      │
         │    │  USB Serial (9600 baud)   │
         │    └─────────────┬──────────────┘
         │                  │
    ┌────▼──────────────────▼────────────────┐
    │  CAPA DE CONTROL (Arduino)             │
    │  ┌──────────────────────────────────┐  │
    │  │ Lógica de control                │  │
    │  │ Gestión de pines                 │  │
    │  │ Timer/Temporizador              │  │
    │  └──────────────────────────────────┘  │
    └────┬──────────────────────────────┬────┘
         │                              │
    ┌────▼────┐                  ┌─────▼──────┐
    │ Relé 5V │                  │ LEDs (11,12)│
    │ (Pin 7) │                  └──────┬──────┘
    └────┬────┘                         │
         │                     (Verde 11, Rojo 12)
    ┌────▼──────────────┐
    │ Motor DC 9V      │
    │ + Polea + Cuerda  │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ PUERTA MÓVIL      │
    │ (Sube/Baja)       │
    └───────────────────┘
```

<img width="900" height="1600" alt="WhatsApp Image 2026-04-24 at 12 25 39 PM" src="https://github.com/user-attachments/assets/20c38b79-d086-42bc-b812-f086df6dacae" />

---

## 5. ¿Cuál es el Protocolo de Control del Sistema?

El sistema implementa un protocolo simple basado en comandos de texto:

### Protocolo de Comunicación:

```
COMANDO ENVIADO DESDE PYTHON:    ACCIÓN EN ARDUINO:
────────────────────────────────────────────────────
"OPEN"      (+ Enter)       →    Activa Pin 7 (HIGH)
                                 Motor gira 5 segundos
                                 LED VERDE enciende
                                 LED ROJO apaga

"CLOSE"     (+ Enter)       →    Activa Pin 7 (HIGH)
                                 Motor gira inverso 5 seg
                                 LED ROJO enciende
                                 LED VERDE apaga

"ESTADO"    (+ Enter)       →    Responde estado actual
                                 (ABIERTO/CERRADO)
```

<img width="380" height="457" alt="image" src="https://github.com/user-attachments/assets/e5028be9-cbfd-49b2-82d1-d0b6d9465925" />

---

## 6. ¿Cuáles son los Modos de Operación del Sistema?

### Modo Manual (Arduino IDE)

```
Entrada: Monitor Serial de Arduino IDE
Proceso:
  1. Usuario escribe "OPEN" o "CLOSE"
  2. Arduino recibe comando directamente
  3. Ejecuta acción correspondiente
Salida: Puerta se abre/cierra
Requiere: Arduino IDE + Cable USB
```

---

## 7. ¿Cuál es el Diagrama de Flujo del Sistema?

```
                    ┌──────────────┐
                    │   INICIO     │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │ Inicializar  │
                    │ Arduino/Cámara│
                    └──────┬───────┘
                           │
                    ┌──────▼───────────────┐
                    │  comandos    │
                    │ (YOLO, Texto)  │
                    └──────┬───────────────┘
                           │
                 ┌─────────┼─────────┐
                 │         │         │
            ┌────▼──┐ ┌────▼──┐ ┌───▼────┐
            │"OPEN" │ │"CLOSE"│ │"ESTADO"│
            └────┬──┘ └────┬──┘ └───┬────┘
                 │         │        │
            ┌────▼──┐ ┌────▼──┐    │
            │Activa │ │Activa │    │
            │Motor  │ │Motor  │    │
            │avance │ │retro  │    │
            └────┬──┘ └────┬──┘    │
                 │         │        │
            ┌────▼──┐ ┌────▼──┐ ┌──▼───────┐
            │LED    │ │LED    │ │Responde  │
            │VERDE  │ │ROJO   │ │estado    │
            └────┬──┘ └────┬──┘ └──┬───────┘
                 │         │        │
                 └─────────┼────────┘
                           │
                    ┌──────▼───────┐
                    │ Esperar 5 seg│
                    │ sin comandos │
                    └──────┬───────┘
                           │
              ┌────────────▼────────────┐
              │ Si hay detección/comando│
              │ Repetir ciclo           │
              │ Si no → Cerrar          │
              └────────────┬────────────┘
                           │
                    ┌──────▼───────┐
                    │   FIN        │
                    └──────────────┘
```

---

# PARTE 2: DISEÑO

## 1. ¿Cómo Plantearía el Desarrollo del Sistema de Parqueadero Automatizado?

### Fase 1: Diseño de Hardware.

**Selección de Componentes:**

| Componente | Especificación | Justificación |
|---|---|---|
| Microcontrolador | Arduino UNO (ATmega328P) | Bajo costo, comunidad grande, suficiente para control |
| Relé | SRD-05VDC 5V | Aislamiento galvánico, bajo consumo |
| Motor | DC 9V, 100 RPM reductor | Potencia suficiente, velocidad controlable |
| Fuente | 9V, 5A | Alimenta motor y sistema |
| Cámara | Celular | Captura video en tiempo real |

**Circuito Esquemático:**

```
GND COMÚN:
Arduino GND ═══ Fuente 12V(-) ═══ Motor GND

CONTROL:
Arduino Pin 7 ──→ Relé Coil+ ──→ Motor ON/OFF

POTENCIA:
Fuente 9V(+) ──→ Relé NO ──→ Motor(+)

INDICADORES:
Arduino Pin 11 ──→ LED Verde (puerta abierta)
Arduino Pin 12 ──→ LED Rojo (puerta cerrada)
```

https://youtu.be/TZLvSnj9IYc

**Plan de Pruebas:**

| Prueba | Método | Criterio de Aceptación |
|---|---|---|
| Hardware | Continuidad con multímetro | GND común verificado, voltajes correctos |
| Motor | Activación manual | Gira ambas direcciones sin ruidos |
| Comunicación | Monitor Serial | Arduino responde a comandos |
| YOLO | Video en tiempo real | Detección confiable |
| Integración | Ciclo completo | Apertura/cierre automático sin errores |

---
