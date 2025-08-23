import heapq
from collections import deque
from datetime import datetime, timedelta

class Patient:
    def __init__(self, name, severity="regular"):
        self.name = name
        self.severity = severity  
        self.arrival_time = datetime.now()

    def __str__(self):
        return f"{self.name} ({self.severity.capitalize()}) - Arrived at {self.arrival_time.strftime('%H:%M:%S')}"

class HospitalQueue:
    def __init__(self):
        self.critical_queue = []  
        self.regular_queue = deque()  

    # Add patient
    def add_patient(self, patient):
        if patient.severity.lower() == "critical":
          
            heapq.heappush(self.critical_queue, (patient.arrival_time, patient))
            print(f"🚨 Critical patient added: {patient.name}")
        else:
            self.regular_queue.append(patient)
            print(f"🩺 Regular patient added: {patient.name}")

    def serve_patient(self):
        if self.critical_queue:
            _, patient = heapq.heappop(self.critical_queue)
            print(f"🚑 Serving critical patient: {patient.name}")
        elif self.regular_queue:
            patient = self.regular_queue.popleft()
            print(f"👨‍⚕️ Serving regular patient: {patient.name}")
        else:
            print("⚠️ No patients in queue.")

   
    def display_queues(self):
        print("\n--- Hospital Queue Status ---")

        print("\nCritical Patients:")
        if not self.critical_queue:
            print("(none)")
        else:
            for i, (_, patient) in enumerate(self.critical_queue, start=1):
                wait = timedelta(minutes=i*5) 
                print(f"{patient.name} - Est. wait: {wait}")

        print("\nRegular Patients:")
        if not self.regular_queue:
            print("(none)")
        else:
            for i, patient in enumerate(self.regular_queue, start=1):
                wait = timedelta(minutes=(len(self.critical_queue)+i)*5)
                print(f"{patient.name} - Est. wait: {wait}")


def main():
    hospital = HospitalQueue()

    while True:
        print("\n=== Hospital Patient Queue ===")
        print("1) Add patient")
        print("2) Serve next patient")
        print("3) Show queue status")
        print("0) Exit")

        choice = input("Select option: ").strip()

        if choice == "0":
            print("👋 Exiting system. Goodbye!")
            break
        elif choice == "1":
            name = input("Enter patient name: ")
            severity = input("Enter severity (critical/regular): ").strip().lower()
            if severity not in ["critical", "regular"]:
                print("⚠️ Invalid severity. Defaulting to regular.")
                severity = "regular"
            patient = Patient(name, severity)
            hospital.add_patient(patient)
        elif choice == "2":
            hospital.serve_patient()
        elif choice == "3":
            hospital.display_queues()
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()

