#include <SoftwareSerial.h>

#include <Wire.h>                     //LCD 라이브러리
#include <LiquidCrystal_I2C.h>        //I2C LCD 라이브러리
#include <DHT.h>                      //온습도센서 라이브러리
#include <Emotion.h>                  //특수 문자 라이브러리
#define DHTPIN 4                      //온습도센서 핀 번호
#define DHTTYPE DHT11                 //온습도센서 센서 타입

LiquidCrystal_I2C lcd(0x27, 16, 2);   //LCD 초기화 (LCD 주소값, x축, y축)
DHT dht(4, DHT11);                    //온습도센서 초기화(온습도센서 핀 번호, 센서 타입)

SoftwareSerial BTSerial(13,12);   //블루투스 모듈 tx,rx 값



//Dust라는 변수 선언과 미세먼지 값, 습도 값, 온도 값 문자열을 담기위한 배열 선언
int Dust = 0;
char str1[10];                        //미세먼지 값
char str2[10];                        //습도 값
char str3[10];                        //온도 값

//각 핀과 연결된 핀 번호를 저장할 변수 선언 
int Vo = A0 ;
int V_LED = 2 ;
int FAN = 3 ;
int R_LED = 5 ;
int Y_LED = 6 ;
int G_LED = 7 ;


//미세먼지값 측정을 위한 데이터값 변수 선언
float Vo_value = 0;
float Voltage = 0;
float a = 0;




void setup()
{     
// 시리얼 통신 시작
Serial.begin(9600);
BTSerial.begin(9600);


//핀모드 입출력 설정
pinMode(V_LED,OUTPUT);
pinMode(Vo,INPUT);
pinMode(FAN,OUTPUT);
pinMode(R_LED,OUTPUT);
pinMode(Y_LED,OUTPUT);
pinMode(G_LED,OUTPUT);

//전원을 켰을 때 LCD 초기값 설정
lcd.begin();
lcd.clear();
lcd.noBacklight();
delay(500);
lcd.backlight();
delay(500);
lcd.setCursor(0,0);
lcd.print("CJ");
delay(1000);
lcd.setCursor(6,0);
lcd.print("FACTORY");
delay(1000);
lcd.setCursor(0,1);
lcd.print("AIR PURIFIER");
delay(1000);
lcd.clear();

//특수 문자 선언
lcd.createChar(0, ug1);
lcd.createChar(1, ug2);
lcd.createChar(2, temp);
lcd.createChar(3, C);
lcd.createChar(4, humi);
lcd.createChar(5, per);


}


void loop()
{
  
//온습도값을 저장 할 변수 선언
int t = dht.readTemperature();
int h = dht.readHumidity();

 Serial.println(t);
 Serial.println(h);
 BTSerial.print("온도 : ");
 BTSerial.print(t);
 BTSerial.println("C");
 BTSerial.print("습도 : ");
 BTSerial.println(h);
 BTSerial.print("미세먼지 : ");
 BTSerial.print(Dust);
 BTSerial.print("μg/m^3");



//적외선 발광 다이오드(IRED)와 포토다이오드가 대각선으로 배치되어 공기 중 먼지의 반사광을 감지 
//미세먼지 센서의 데이터값 계산을 통한 미세먼지값 측정
  digitalWrite(V_LED,LOW);
  delayMicroseconds(280);
  Vo_value = analogRead(Vo);
  delayMicroseconds(40);
  digitalWrite(V_LED,HIGH);
  delayMicroseconds(9680);

  
/*
전압[V] = (아날로그 핀 값) * 5.0 / 1024
미세먼지 센서의 출력전압(Vo)는 먼지가 없을 때의 출력전압(Voc)과 미세먼지 농도에 비례하여 출력 
 */
 

  Voltage = Vo_value * 5.0 / 1024.0;
 

 
 
 if( Voltage < 0.1 ){

  Dust = 0 ;
  
 } 

 else if ( Voltage < 0.8){
  
  Dust =10*(5*(Voltage - 0.1));
         
 }
 
 else if ( Voltage < 1 ){

  Dust = 10 + 15*((Voltage - 0.8)*10);
  
 }
 
 else if( Voltage > 1){

  Dust = 40 + 16*((Voltage - 1)*10);
  


 }
 

 Serial.println(Dust);
  
  
  delay(1000);
 
  lcd.setCursor(1,0);
  lcd.print("Dust : ");
  sprintf(str1,"%03d",Dust);
  lcd.print(str1);
  lcd.write(0);
  lcd.print("g/m");
  lcd.write(1);     //특수 문자와 3글자로 된 미세먼지 값 출력

  lcd.setCursor(1,1);
  lcd.write(2);
  lcd.print("  ");
  sprintf(str2,"%02d",t);
  lcd.print(str2);
  lcd.write(3);     //특수 문자와 2글자로 된 온도 값 출력
  lcd.print("  "); 
  lcd.write(4);
  lcd.print("  ");
  sprintf(str3,"%02d",h);
  lcd.print(str3);
  lcd.write(5);     //특수 문자와 2글자로 된 습도 값 출력

   delay(1000);
if(Serial.available()){
    BTSerial.write(Serial.read());
  }
  if(BTSerial.available()){
    Serial.write(BTSerial.read());
  }


if( (t > 20) || (h > 30) ||  (Dust > 50) ){digitalWrite(FAN,HIGH);}
else {digitalWrite(FAN,LOW);}

if(Dust > 50){digitalWrite(G_LED,HIGH);}
else {digitalWrite(G_LED,LOW);}

if( h > 30 ){digitalWrite(Y_LED,HIGH);}
else {digitalWrite(Y_LED,LOW);}
        
if(t >  20 ){digitalWrite(R_LED,HIGH);}
else {digitalWrite(R_LED,LOW);}




 

}
