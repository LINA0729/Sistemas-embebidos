cpp
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