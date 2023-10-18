import datetime
import subprocess
import sys
import threading

# Replace 'your_password' with your actual decryption password
decryption_password = 'your_password'

def run_decryption(timestamp, output_file, success_flag):
    try:
        openssl_command = f'echo "{decryption_password}" | openssl enc -d -aes-256-cbc -in ciphertext -out "{output_file}" <<< "{timestamp}"'
        subprocess.run(openssl_command, shell=True, check=True)
        print(f"Decryption successful with timestamp: {timestamp}")
        success_flag[0] = True
    except subprocess.CalledProcessError:
        print(f"Decryption failed with timestamp: {timestamp}")
        success_flag[0] = False

def loop():
    if len(sys.argv) != 2:
        print("Usage: python script.py <output_file>")
        return

    output_file = sys.argv[1]
    start_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
    end_date = datetime.datetime(2023, 1, 1, 23, 59, 59)
    current_date = start_date

    decryption_successful = [False]  # Use a list to store a mutable flag

    with open(output_file, 'wb') as decrypted_output:
        while not decryption_successful[0]:
            timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
            decryption_thread = threading.Thread(target=run_decryption, args=(timestamp, output_file, decryption_successful))
            decryption_thread.start()
            decryption_thread.join()

            if not decryption_successful[0]:
                current_date += datetime.timedelta(seconds=1)

    print("Decryption successful. Continuing to the next timestamp...")

if __name__ == "__main__":
    while True:
        loop()

