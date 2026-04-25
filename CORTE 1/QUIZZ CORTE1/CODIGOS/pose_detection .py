import cv2
import mediapipe as mp
import numpy as np
import serial
import time

# ======= CONEXIÓN ARDUINO =======
arduino = serial.Serial('COM3', 9600)  # CAMBIA COM3 SI ES NECESARIO
time.sleep(2)  # Esperar que Arduino inicie

# ======= INICIALIZAR MEDIAPIPE =======
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

# ======= FUNCIÓN PARA CALCULAR ÁNGULO =======
def calcular_angulo(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cos_angulo = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angulo = np.degrees(np.arccos(cos_angulo))

    return angulo

# ======= INICIAR CÁMARA =======
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo acceder a la cámara")
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            landmarks = results.pose_landmarks.landmark

            # Pierna izquierda
            cadera = [landmarks[23].x, landmarks[23].y]
            rodilla = [landmarks[25].x, landmarks[25].y]
            tobillo = [landmarks[27].x, landmarks[27].y]

            angulo = calcular_angulo(cadera, rodilla, tobillo)

            # ======= CLASIFICACIÓN =======
            if angulo > 160:
                estado = "PARADO"
                color = (0, 0, 255)  # ROJO en pantalla
                arduino.write(b'R')  # LED rojo
            else:
                estado = "SENTADO"
                color = (0, 255, 0)  # VERDE en pantalla
                arduino.write(b'G')  # LED verde

            # Mostrar estado
            cv2.putText(frame, estado, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, color, 3)

            # Mostrar ángulo
            cv2.putText(frame, f"Angulo: {int(angulo)}", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 255), 2)

        cv2.imshow("Deteccion Parado/Sentado + Arduino", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
            break

finally:
    # ======= APAGAR LEDs AL CERRAR =======
    print("Apagando LEDs...")
    arduino.write(b'X')  # Señal para apagar todo
    time.sleep(1)

    cap.release()
    cv2.destroyAllWindows()
    arduino.close()

    print("Programa cerrado correctamente.")
