Descripción del proyecto
El proyecto utiliza MediaPipe Pose para identificar la postura del cuerpo en tiempo real desde la cámara.

El sistema determina si una persona esta:
🟢 Sentada
🔴 Parada

Según la postura detectada, se envía una señal por puerto serial a Arduino para encender un LED:

Estado  	Acción      Arduino
Sentado 	LED Verde   ON
Parado	  LED Rojo    ON
