#include <ros.h>
#include <rosserial_arduino/Adc.h>
ros::NodeHandle nh;
rosserial_arduino::Adc adc_msg;
ros::Publisher p("adc",&adc_msg);
const int analog_pin = A0;
void setup()
{
  nh.initNode();
  nh.advertise(p);
}
void loop()
{
  adc_msg.adc0 =kalman(analog_pin);   
  p.publish(&adc_msg);
  nh.spinOnce();
}
float kalman (int pin_num)
{
  
  float aValue = analogRead(pin_num);
  float input = map(aValue, 102, 922, -640, 640);
  float kalman_old;
  float cov_old;
  float kalman_new = kalman_old; //eski değer alınır
  float cov_new = cov_old + 0.50;//yeni kovaryans değeri belirlenir. Q=0.50 alınmıştır
  float kalman_gain = cov_new / (cov_new + 0.9); //kalman kazancı hesaplanır. R=0.9 alınmıştır
  float kalman_calculated = kalman_new + (kalman_gain * (input - kalman_new)); //kalman değeri hesaplanır
  cov_new = (1 - kalman_gain) * cov_old; //yeni kovaryans değeri hesaplanır
  cov_old = cov_new; //yeni değerler bir sonraki döngüde kullanılmak üzere kaydedilir
  kalman_old = kalman_calculated;
  return kalman_calculated; //hesaplanan kalman değeri çıktı olarak verilir
}
