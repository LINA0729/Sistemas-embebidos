#define MOTOR_RELE_PIN 7

void setup() {
  Serial.begin(9600);
  pinMode(MOTOR_RELE_PIN, OUTPUT);
  digitalWrite(MOTOR_RELE_PIN, LOW);
  Serial.println("LISTO");
}

void loop() {
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    
    if (cmd == "OPEN") {
      digitalWrite(MOTOR_RELE_PIN, HIGH);
      delay(5000);
      digitalWrite(MOTOR_RELE_PIN, LOW);
      Serial.println("ABIERTO");
    }
    if (cmd == "CLOSE") {
      digitalWrite(MOTOR_RELE_PIN, HIGH);
      delay(5000);
      digitalWrite(MOTOR_RELE_PIN, LOW);
      Serial.println("CERRADO");
    }
  }
}