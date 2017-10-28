void setup() {
  Serial.begin(9600);
}

double Getterm(int RawADC) {
  double temp = 0;
  temp = log(((10240000 / RawADC) - 10000));
  temp = 1 / (0.001129148 + (0.000234125 * temp) + (0.0000000876741 * temp * temp * temp));
  temp = temp - 273.15;
  return temp;
}

void loop() {
  Serial.println(Getterm(analogRead(4)));
  delay(1000);
}
