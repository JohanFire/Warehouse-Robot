const int pinENB =  0;
const int pinIN1B =  1;
const int pinIN2B =  2;
const int pinENBB = 3;
const int pinIN11B = 4;
const int pinIN22B = 5;
const int pinENA =  6;
const int pinIN1 =  7;
const int pinIN2 =  8;
const int pinENAA = 9;
const int pinIN11 = 10;
const int pinIN22 = 11;
const int lectura = 12;

const int speed = 150;    //velocidad de giro 80% (200/255)

void setup()
{
  pinMode(pinIN1B, OUTPUT);
  pinMode(pinIN2B, OUTPUT);
  pinMode(pinENB, OUTPUT);
  pinMode(pinIN11B, OUTPUT);
  pinMode(pinIN22B, OUTPUT);
  pinMode(pinENBB, OUTPUT);
  pinMode(pinIN1, OUTPUT);
  pinMode(pinIN2, OUTPUT);
  pinMode(pinENA, OUTPUT);
  pinMode(pinIN11, OUTPUT);
  pinMode(pinIN22, OUTPUT);
  pinMode(pinENAA, OUTPUT);
  pinMode(lectura,INPUT);
}

void loop()
{
  int estatus = digitalRead(lectura);

  if(estatus == HIGH){
  digitalWrite(pinIN1, HIGH);
  digitalWrite(pinIN2, LOW);
  analogWrite(pinENA, speed);
  digitalWrite(pinIN11, HIGH);
  digitalWrite(pinIN22, LOW);
  analogWrite(pinENAA, speed);
  digitalWrite(pinIN1B, HIGH);
  digitalWrite(pinIN2B, LOW);
  analogWrite(pinENB, speed);
  digitalWrite(pinIN11B, HIGH);
  digitalWrite(pinIN22B, LOW);
  analogWrite(pinENBB, speed);
  // delay(1000);
  }
  else if(estatus == LOW){
  digitalWrite(pinIN1, LOW);
  digitalWrite(pinIN2, LOW);
  analogWrite(pinENA, speed);
  digitalWrite(pinIN11, LOW);
  digitalWrite(pinIN22, LOW);
  analogWrite(pinENAA, speed);
  digitalWrite(pinIN1B, LOW);
  digitalWrite(pinIN2B, LOW);
  analogWrite(pinENB, speed);
  digitalWrite(pinIN11B, LOW);
  digitalWrite(pinIN22B, LOW);
  analogWrite(pinENBB, speed);
  // delay(1000);
  }
}