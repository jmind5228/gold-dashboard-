
📘 วิธีใช้ Gold Market Dashboard

1. เปิดใช้งาน (สำหรับไฟล์ .zip):
   - ติดตั้ง Python และ Streamlit ด้วยคำสั่ง:
     pip install streamlit pandas openpyxl

   - เปิดด้วยคำสั่ง:
     streamlit run app.py

2. หากคุณได้รับเวอร์ชัน .exe:
   - ดับเบิลคลิกเพื่อใช้งานได้ทันทีบน Windows

ข้อมูลในไฟล์ต้องประกอบด้วย:
- Sheet แรก: ราคาทองย้อนหลัง (มีคอลัมน์ "วันที่", "ราคาทอง (USD/Oz)")
- Sheet ที่สอง: ปริมาณถือครองทองคำของ SPDR ("วันที่", "SPDR ถือทอง (ตัน)")
