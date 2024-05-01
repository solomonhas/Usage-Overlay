import psutil
import time

def get_cpu_temp():
    return psutil.sensors_temperatures()['coretemp'][0].current

def get_gpu_temp():
    try:
        import nvidia_smi
        nvidia_smi.nvmlInit()
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
        temp = nvidia_smi.nvmlDeviceGetTemperature(handle, nvidia_smi.NVML_TEMPERATURE_GPU)
        nvidia_smi.nvmlShutdown()
        return temp
    except ImportError:
        return None

def main():
    try:
        while True:
            cpu_temp = get_cpu_temp()
            gpu_temp = get_gpu_temp()
            if cpu_temp:
                print(f"CPU Temperature: {cpu_temp}°C", end='\t')
            else:
                print("CPU Temperature: N/A", end='\t')
            if gpu_temp is not None:
                print(f"GPU Temperature: {gpu_temp}°C")
            else:
                print("GPU Temperature: N/A")
            time.sleep(5)  # Update interval in seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
