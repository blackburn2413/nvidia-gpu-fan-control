import subprocess
import time
import os

def get_gpu_temperature():
    """Get the current GPU temperature using nvidia-smi."""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader,nounits'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        if result.returncode == 0:
            temperature = int(result.stdout.decode('utf-8').strip())
            return temperature

        else:
            print(f"Error getting GPU temperature: {result.stderr.decode('utf-8')}")

    except Exception as e:
        print(f"An exception occurred while getting GPU temperature: {e}")

    return None

def set_fan_speed(temperature):
    """Set fan speed based on the current GPU temperature."""
    if temperature is not None:
        try:
            if temperature > 45:
                # Increase fan speed when temp is above 50°C
                os.system('echo "255" > /sys/class/hwmon/hwmon1/pwm3')
                print("Fan speed set to maximum (temperature: {}°C)".format(temperature))
            else:
                # Decrease fan speed when temp is below or equal to 50°C
                os.system('echo "100" > /sys/class/hwmon/hwmon1/pwm3')
                print("Fan speed set to minimum (temperature: {}°C)".format(temperature))

        except Exception as e:
            print(f"Failed to execute command for fan speed control: {e}")

def main():
    previous_temp = None
    while True:
        temperature = get_gpu_temperature()

        if temperature is not None and temperature != previous_temp:
            set_fan_speed(temperature)
            previous_temp = temperature
        else:
            print("Current GPU Temperature: {}°C".format(temperature))

        # Wait for 10 seconds before checking again.
        time.sleep(10)

if __name__ == "__main__":
    main()
