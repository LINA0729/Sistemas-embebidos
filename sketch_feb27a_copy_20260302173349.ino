char estado;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);  // LED Verde
  pinMode(9, OUTPUT);  // LED Rojo
}

void loop() {
  if (Serial.available()) {
    estado = Serial.read();

    if (estado == 'R') {      // PARADO
      digitalWrite(9, HIGH);
      digitalWrite(8, LOW);
    }
    else if (estado == 'G') { // SENTADO
      digitalWrite(9, LOW);
      digitalWrite(8, HIGH);
    }
    else if (estado == 'X') { // APAGAR TODO
      digitalWrite(9, LOW);
      digitalWrite(8, LOW);
    }
  }
}