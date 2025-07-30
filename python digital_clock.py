python digital_clock.py
def export_alarms(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM alarms")
    with open("alarms.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Message"])
        writer.writerows(cursor.fetchall())
    messagebox.showinfo("Success", "Alarms exported to alarms.csv!")

from cryptography.fernet import Fernet
def set_alarm(self):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(self.alarm_message_entry.get().encode()).decode()
    cursor = self.conn.cursor()
    cursor.execute("INSERT INTO alarms (time, message) VALUES (?, ?)", (self.alarm_time_entry.get(), encrypted_message))
    self.conn.commit()

