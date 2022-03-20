

#include<Wire.h>
const int MPU_addr=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;

const int JoyStick_pin = 2; //plug Joystick 'Button' into pin 8
const int X_pin = A0;       //plug joystick X direction into pin A0
const int Y_pin = A1;     //plug joystick Y direction into pin A1
int xc;
int yc;
const int JSButton = 2;
int buzzer = 7;              //Variable Decleration for Buzzer
int data;


void setup() {
  for (int i = 0; i < 2; i++) {
    digitalWrite(JSButton,HIGH);
  }
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);
  pinMode(buzzer,OUTPUT);    //Initialize digital pin 7 (buzzer) as an output.
  data = Serial.read();
}

void loop() {
  int x = analogRead(X_pin) - 517;  //read x direction value and -517 to bring back to around 0
  int y = analogRead(Y_pin) - 512;  //read y direction value and -512 to bring back to around 0

  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

   if (x <-500 || AcX > 10000) {         //joystick has off set of +/-8 so this negates that
    xc = 1;     //left
  }else if (x > 499 || AcX < -10000) {   
    xc = 2;    //right
  }else {
    xc = 3;
  }

   if (y <-499 || AcY > 5000) {
    yc = 1;   //down
  }else if (y >500  || AcY < -2000) {
    yc = 2;  //up
  }else {
    yc = 3;
  }

  if ((AcX > 10000 || AcX < -10000) && (AcZ > 17000)) {
    Serial.println("D330"); //Bonus Mode
    delay(30);
  }
  //Serial.print("D");  //start printing the data, format is Sxc,yc,buttonStates > S1,1,0
  Serial.print("D");
  Serial.print(xc);
  Serial.print(yc);
  Serial.println(digitalRead(JSButton));
  data = Serial.read();

    if (data == '1')
    {
      //digitalWrite(led, HIGH);
      //digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(buzzer, HIGH);
      delay(20);
      digitalWrite(buzzer, LOW);
    }
    else
    {
    }
  //Serial.println(AcX);
  //Serial.print("  A  ");
  //Serial.println(AcY);
  //Serial.println(AcZ);   
  //Serial.println(GyX);
  //Serial.print("  G  ");
  //Serial.println(GyY);
  //Serial.println("  ");
  //Serial.println(GyZ);
  //Serial.println("  ");

  delay(30);
}
