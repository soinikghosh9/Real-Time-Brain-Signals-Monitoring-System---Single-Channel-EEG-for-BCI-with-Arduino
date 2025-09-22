import serial
import csv
import time
import os
import tkinter as tk
from tkinter import messagebox

# Function to open the serial port
def open_serial_port(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
        return None

# Function to get the next filename
def get_next_filename(directory, base_name):
    i = 1
    while True:
        filename = os.path.join(directory, f"{base_name}_{i}.csv")
        if not os.path.exists(filename):
            return filename
        i += 1

# Function to record data for a given task
def record_data(ser, directory, task, duration, status_label):
    filename = get_next_filename(directory, task)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Timestamp', 'Filtered Value'])  # Write the header row

        start_time = time.time()
        while time.time() - start_time < duration:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Received line: {line}")  # Debugging print
                try:
                    filtered_value = float(line)
                    timestamp = int((time.time() - start_time) * 1000)  # Generate timestamp in milliseconds
                    csvwriter.writerow([timestamp, filtered_value])
                except ValueError as e:
                    print(f"Error parsing data: {e}")
        status_label.config(text=f"{task.capitalize()} task completed and saved as {filename}")

# Function to handle recording for the 'close' task
def handle_close_task():
    if ser:
        status_label.config(text="Recording 'close' task...")
        root.update()
        record_data(ser, directory, 'close', 5, status_label)
    else:
        messagebox.showerror("Error", "Failed to open the serial port. Please check the port and try again.")

# Function to handle recording for the 'open' task
def handle_open_task():
    if ser:
        status_label.config(text="Recording 'open' task...")
        root.update()
        record_data(ser, directory, 'open', 5, status_label)
    else:
        messagebox.showerror("Error", "Failed to open the serial port. Please check the port and try again.")

# Create the directory for saving files
directory = 'eeg_data'
os.makedirs(directory, exist_ok=True)

# Initialize serial port
ser = open_serial_port('COM5', 115200)  # Update COM port as needed

# Create the GUI
root = tk.Tk()
root.title("EEG Data Recorder")

frame = tk.Frame(root)
frame.pack(pady=20)

close_button = tk.Button(frame, text="Record Close Task", command=handle_close_task, width=20)
close_button.pack(pady=10)

open_button = tk.Button(frame, text="Record Open Task", command=handle_open_task, width=20)
open_button.pack(pady=10)

status_label = tk.Label(root, text="Click a button to start recording.", font=("Helvetica", 12))
status_label.pack(pady=20)

root.mainloop()

if ser:
    ser.close()
    print("Serial port closed.")
