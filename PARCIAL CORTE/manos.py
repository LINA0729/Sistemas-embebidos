import cv2
import mediapipe as mp

# Inicializar mediapipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Puntos del pulgar
PULGAR_IDS = [1, 2, 3, 4]


def detectar_pulgar(frame, resultados):
    h, w, _ = frame.shape

    if resultados.multi_hand_landmarks:
        for mano in resultados.multi_hand_landmarks:

            puntos_pulgar = []

            for id, punto in enumerate(mano.landmark):

                if id in PULGAR_IDS:

                    x = int(punto.x * w)
                    y = int(punto.y * h)

                    puntos_pulgar.append((x, y))

                    # dibujar punto
                    cv2.circle(frame, (x, y), 8, (255, 0, 0), -1)

            # unir los puntos del pulgar
            if len(puntos_pulgar) == 4:

                cv2.line(frame, puntos_pulgar[0], puntos_pulgar[1], (255, 0, 0), 3)
                cv2.line(frame, puntos_pulgar[1], puntos_pulgar[2], (255, 0, 0), 3)
                cv2.line(frame, puntos_pulgar[2], puntos_pulgar[3], (255, 0, 0), 3)

                cv2.putText(frame, "Pulgar Detectado", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 2)


def main():

    camara = cv2.VideoCapture(0)

    while True:

        ret, frame = camara.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        imagen_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resultados = detector.process(imagen_rgb)

        detectar_pulgar(frame, resultados)

        cv2.imshow("Detector de Pulgar", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    camara.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
