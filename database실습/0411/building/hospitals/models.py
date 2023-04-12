from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name} 전문의"
    
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"



class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)# 의사가 사라지면 환자도 사라진다.
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)# 의사가 사라지면 환자도 사라진다.
    # ========================================== 이부분까지가 기본 장고 제공과 똑같음
    
    # 추가적으로 만들기
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor_id}번 의사의 {self.patient_id}번 환자"