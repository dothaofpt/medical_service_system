import mysql.connector
from mysql.connector import Error
from datetime import datetime

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',      
            password='',  
            database='medical_service'
        )
        print("Kết nối thành công!")
    except Error as e:
        print(f"Lỗi '{e}' xảy ra khi kết nối đến cơ sở dữ liệu")
    return connection

def add_patients(connection):
    cursor = connection.cursor()
    for i in range(3):
        full_name = input("Nhập tên bệnh nhân: ")
        date_of_birth = input("Nhập ngày sinh (YYYY-MM-DD): ")
        gender = input("Nhập giới tính: ")
        address = input("Nhập địa chỉ: ")
        phone_number = input("Nhập số điện thoại: ")
        email = input("Nhập email: ")

        cursor.execute(
            "INSERT INTO patients (full_name, date_of_birth, gender, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)",
            (full_name, date_of_birth, gender, address, phone_number, email)
        )
    connection.commit()
    print("Thêm bệnh nhân thành công!")

def add_doctors(connection):
    cursor = connection.cursor()
    for i in range(5):
        full_name = input("Nhập tên bác sĩ: ")
        specialization = input("Nhập chuyên môn: ")
        phone_number = input("Nhập số điện thoại: ")
        email = input("Nhập email: ")
        years_of_experience = int(input("Nhập số năm kinh nghiệm: "))

        cursor.execute(
            "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)",
            (full_name, specialization, phone_number, email, years_of_experience)
        )
    connection.commit()
    print("Thêm bác sĩ thành công!")

def add_appointments(connection):
    cursor = connection.cursor()
    for i in range(3):
        patient_id = int(input("Nhập ID bệnh nhân: "))
        doctor_id = int(input("Nhập ID bác sĩ: "))
        appointment_date = input("Nhập ngày hẹn (YYYY-MM-DD HH:MM): ")
        reason = input("Nhập lý do: ")

        cursor.execute(
            "INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)",
            (patient_id, doctor_id, appointment_date, reason)
        )
    connection.commit()
    print("Thêm lịch hẹn thành công!")

def generate_report(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT a.appointment_id, p.full_name, p.date_of_birth, p.gender, p.address,
               d.full_name, a.reason, a.appointment_date
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
    """)
    appointments = cursor.fetchall()

    print("\n--- Báo cáo lịch hẹn ---")
    print("No | Patient Name | Birthday | Gender | Address | Doctor Name | Reason | Date")
    print("-" * 80)
    for i, appointment in enumerate(appointments):
        print(f"{i + 1} | {appointment[1]} | {appointment[2]} | {appointment[3]} | {appointment[4]} | {appointment[5]} | {appointment[6]} | {appointment[7]}")

def get_appointments_today(connection):
    cursor = connection.cursor()
    today = datetime.now().date()
    cursor.execute("""
        SELECT p.full_name, p.date_of_birth, p.gender, d.full_name, a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE DATE(a.appointment_date) = %s
    """, (today,))
    appointments = cursor.fetchall()

    print("\n--- Lịch hẹn hôm nay ---")
    print("No | Patient Name | Birthday | Gender | Doctor Name | Status")
    print("-" * 50)
    for i, appointment in enumerate(appointments):
        print(f"{i + 1} | {appointment[0]} | {appointment[1]} | {appointment[2]} | {appointment[3]} | {appointment[4]}")

def main():
    connection = create_connection()
    if connection:
        add_patients(connection)
        add_doctors(connection)
        add_appointments(connection)
        generate_report(connection)
        get_appointments_today(connection)
        connection.close()

if __name__ == "__main__":
    main()
