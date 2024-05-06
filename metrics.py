import clr # the pythonnet module.
import os


# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the reference to the local copy of the DLL
dll_path = os.path.join(current_dir, 'OpenHardwareMonitor/OpenHardwareMonitorLib.dll')
clr.AddReference(dll_path)

# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()
while True:
    for a in range(0, len(c.Hardware[0].Sensors)):
        # print(c.Hardware[0].Sensors[a].Identifier)
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print(c.Hardware[0].Sensors[a].get_Value())
            c.Hardware[0].Update()
