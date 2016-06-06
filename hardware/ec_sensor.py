import time
import requests
from serialdata import SerialData


def initialize():
    last_received = ''
    initial_sleep_time = 2
    sleep_time = 1
    run_times = 5
    upload_url = 'http://bonapetite.herokuapp.com/api/mister/'
    return (last_received, initial_sleep_time,
            sleep_time, run_times, upload_url)


def receiving(serial_port):
    global last_received
    buffer = ''
    while serial_port.isOpen():
        buffer += serial_port.read(serial_port.inWaiting()).decode('utf-8')
        if '\n' in buffer:
            lines = buffer.split('\n')  # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            # If the Arduino sends lots of empty lines, you'll lose the
            # last filled line, so you could make above statement conditional
            # like so: if lines[-2]: last_received = lines[-2]
            buffer = lines[-1]


def main():
    (last_received, initial_sleep_time, sleep_time,
     run_times, upload_url) = initialize()
    s = SerialData()
    time.sleep(initial_sleep_time)
    for i in range(run_times):
        # while True:
        time.sleep(sleep_time)
        pH_level = s.next()
        payload = {'pH_level': pH_level, 'temperature': 200}
        r = requests.post(upload_url, payload)
        print(pH_level)
        print('response:', r.text)


if __name__ == '__main__':
    main()
