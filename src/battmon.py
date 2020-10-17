from machine import Pin
from machine import ADC

class BatteryMonitor:

    ADC_MAX = 1023
    BATTERY_MAX_V = 4.2
    SOLAR_MAX_V = 6

    def __init__(self):
        self.sela = Pin(4, Pin.OUT)
        self.selb = Pin(5, Pin.OUT)
        self.selc = Pin(14, Pin.OUT)
        self.charge_en = Pin(12, Pin.OUT)
        self.adc = ADC(0)

    def connect_solar_panel(self) -> None:
        self.charge_en.off()

    def disconnect_solar_panel(self) -> None:
        self.charge_en.on()

    def select_solar_panel(self) -> None:
        self.sela.off()
        self.selb.off()
        self.selc.off()

    def select_battery(self) -> None:
        self.sela.on()
        self.selb.off()
        self.selc.off()

    def read_adc(self) -> float:
        return self.adc.read()

    def read_battery_voltage(self) -> None:
        """ Battery voltage is between 0 and 4.2 """
        self.disconnect_solar_panel()
        self.select_battery()
        adc_reading = self.read_adc()
        volt = adc_reading / BatteryMonitor.ADC_MAX * BatteryMonitor.BATTERY_MAX_V * 1.122

        print("Battery ADC: " + str(adc_reading))
        print("Battery Voltage: " + str(volt))
        self.connect_solar_panel()
        return volt

    def read_solar_voltage(self) -> None:
        """ Battery voltage is between 0 and 4.2 """
        self.disconnect_solar_panel()
        self.select_solar_panel()
        adc_reading = self.read_adc()
        volt = adc_reading / BatteryMonitor.ADC_MAX * BatteryMonitor.SOLAR_MAX_V * 1.037

        print("Solar ADC: " + str(adc_reading))
        print("Solar Voltage: " + str(volt))
        self.connect_solar_panel()
        return volt