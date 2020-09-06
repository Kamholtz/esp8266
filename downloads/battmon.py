from machine import Pin
from machine import ADC

class BatteryMonitor:

    ADC_MAX = 1023
    BATTERY_MAX_V = 4.2
    SOLAR_MAX_V = 6

    def __init__(self):
        self.sela = Pin(3, Pin.OUT)
        self.selb = Pin(10, Pin.OUT)
        self.selc = Pin(9, Pin.OUT)
        self.charge_en = Pin(5, Pin.OUT)
        self.adc = ADC(0)

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
        self.select_battery()
        adc_reading = self.read_adc()

        return adc_reading / BatteryMonitor.ADC_MAX * BatteryMonitor.BATTERY_MAX_V

    def read_solar_voltage(self) -> None:
        """ Battery voltage is between 0 and 4.2 """
        self.select_solar_panel()
        adc_reading = self.read_adc()

        return adc_reading / BatteryMonitor.ADC_MAX * BatteryMonitor.SOLAR_MAX_V