# Module WS2812 V1.01
import time
import module_neopixel
from module_init import Global_WS2812 as MyGlobal


class LedState:
    def __init__(self):
        self.state = False
        self.blink_state = False

    def set(self, set):
        self.state = set

    def get(self):
        return self.state
    
    def do_blink(self):
        self.blink_state = not self.blink_state

    def get_blink(self):
        return self.blink_state

    def refresh(self):
        self.state = False
        for strips in strip_obj:
            strips.show()


class Ledsegment:

    def __init__(self, neopixel, start, count):
        self.neopixel = neopixel
        self.start = start
        self.stop = self.start + count - 1
        self.count = count
        self.position = 0
        self.run_state = False
        self.blink_state = False
        self.color_on = (0,0,0)
        self.color_default = (0,0,0)
        self.color_off = (0,0,0)
        self.color_blink_on = (0,0,0)
        self.color_blink_off = (0,0,0)
        self.color_show = (0,0,0)
        self.color_value = (0,0,0)

    def set_color_on(self, color_on):
        self.color_on = color_on

    def set_color_def(self, color_default):
        self.color_default = color_default
        
    def set_color_off(self, color_off):
        self.color_off = color_off

    def set_color_value(self, color_value):
        self.color_value = color_value

    def set_color_show(self, color_value):
        self.color_show = color_value

    def set_color_blink_off(self, color_value):
        self.color_blink_off = color_value

    def set_color_blink_on(self, color_value):
        self.color_blink_on = color_value

    def set_pixel(self, pixel_num, color=None):
        if color:
            self.color_value = color
        else:
            self.color_value = self.color_show
        self.neopixel.set_pixel(self.start + pixel_num, self.color_value)

    def show_on(self):
        self.color_show = self.color_on
        self.blink_state = False
        self.set_line()

    def show_def(self):
        self.color_show = self.color_default
        self.blink_state = False
        self.set_line()

    def show_off(self):
        self.color_show = self.color_off
        self.blink_state = False
        self.set_line()

    def show_blink(self):
        self.blink_state = True
        if ledstate.get_blink():
            self.color_show = self.color_blink_on
        else:
            self.color_show = self.color_blink_off
        self.set_line()

    def get_blink_state(self):
        return self.blink_state

    def set_line(self):
        self.neopixel.set_pixel_line(self.start, self.stop, self.color_show)

    def show_stripe(self):
        self.neopixel.show()


def setup_ws2812():

    global strip_obj
    global led_obj
    global ledstate
    global mg
    
    mg = MyGlobal
    
    led_obj = []
    strip_obj = []

    ledstate = LedState()
    
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_1, 0, 6, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_2, 1, 7, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_3, 2, 8, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_4, 3, 9, "GRB"))
    
    led_obj.append(Ledsegment(strip_obj[mg.seg_01_strip], mg.seg_01_start, mg.seg_01_count))      #  0 (01) -> LED Position -> # 01 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_02_strip], mg.seg_02_start, mg.seg_02_count))      #  1 (02) -> LED Position -> # 02 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_03_strip], mg.seg_03_start, mg.seg_03_count))      #  2 (03) -> LED Position -> # 03 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_04_strip], mg.seg_04_start, mg.seg_04_count))      #  3 (04) -> LED Position -> # 04 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_05_strip], mg.seg_05_start, mg.seg_05_count))      #  4 (05) -> LED Position -> # 05 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_06_strip], mg.seg_06_start, mg.seg_06_count))      #  5 (06) -> LED Position -> # 06 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_07_strip], mg.seg_07_start, mg.seg_07_count))      #  6 (07) -> LED Position -> # 07 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_08_strip], mg.seg_08_start, mg.seg_08_count))      #  7 (08) -> LED Position -> # 08 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_09_strip], mg.seg_09_start, mg.seg_09_count))      #  8 (09) -> LED Position -> # 09 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_10_strip], mg.seg_10_start, mg.seg_10_count))      #  9 (10) -> LED Position -> # 10 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_11_strip], mg.seg_11_start, mg.seg_11_count))      #  0 (11) -> LED Position -> # 01 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_12_strip], mg.seg_12_start, mg.seg_12_count))      #  1 (12) -> LED Position -> # 02 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_13_strip], mg.seg_13_start, mg.seg_13_count))      #  2 (13) -> LED Position -> # 03 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_14_strip], mg.seg_14_start, mg.seg_14_count))      #  3 (14) -> LED Position -> # 04 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_15_strip], mg.seg_15_start, mg.seg_15_count))      #  4 (15) -> LED Position -> # 05 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_16_strip], mg.seg_16_start, mg.seg_16_count))      #  5 (16) -> LED Position -> # 06 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_17_strip], mg.seg_17_start, mg.seg_17_count))      #  6 (17) -> LED Position -> # 07 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_18_strip], mg.seg_18_start, mg.seg_18_count))      #  7 (18) -> LED Position -> # 08 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_19_strip], mg.seg_19_start, mg.seg_19_count))      #  8 (19) -> LED Position -> # 09 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_20_strip], mg.seg_20_start, mg.seg_20_count))      #  9 (20) -> LED Position -> # 10 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_21_strip], mg.seg_21_start, mg.seg_21_count))      #  0 (21) -> LED Position -> # 01 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_22_strip], mg.seg_22_start, mg.seg_22_count))      #  1 (22) -> LED Position -> # 02 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_23_strip], mg.seg_23_start, mg.seg_23_count))      #  2 (23) -> LED Position -> # 03 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_24_strip], mg.seg_24_start, mg.seg_24_count))      #  3 (24) -> LED Position -> # 04 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_25_strip], mg.seg_25_start, mg.seg_25_count))      #  4 (25) -> LED Position -> # 05 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_26_strip], mg.seg_26_start, mg.seg_26_count))      #  5 (26) -> LED Position -> # 06 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_27_strip], mg.seg_27_start, mg.seg_27_count))      #  6 (27) -> LED Position -> # 07 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_28_strip], mg.seg_28_start, mg.seg_28_count))      #  7 (28) -> LED Position -> # 08 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_29_strip], mg.seg_29_start, mg.seg_29_count))      #  8 (29) -> LED Position -> # 09 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_30_strip], mg.seg_30_start, mg.seg_30_count))      #  9 (30) -> LED Position -> # 10 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_31_strip], mg.seg_31_start, mg.seg_31_count))      #  0 (31) -> LED Position -> # 01 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_32_strip], mg.seg_32_start, mg.seg_32_count))      #  1 (32) -> LED Position -> # 02 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_33_strip], mg.seg_33_start, mg.seg_33_count))      #  2 (33) -> LED Position -> # 03 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_34_strip], mg.seg_34_start, mg.seg_34_count))      #  3 (34) -> LED Position -> # 04 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_35_strip], mg.seg_35_start, mg.seg_35_count))      #  4 (35) -> LED Position -> # 05 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_36_strip], mg.seg_36_start, mg.seg_36_count))      #  5 (36) -> LED Position -> # 06 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_37_strip], mg.seg_37_start, mg.seg_37_count))      #  6 (37) -> LED Position -> # 07 #

    for strips in strip_obj:
        strips.brightness(255)
   
    # Alle Leds auf Vorgabewert -> aus
    for strips in strip_obj:
        strips.set_pixel_line(0, strips.num_leds - 1, mg.color_off)
    for strips in strip_obj:
        strips.show()

    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.set_color_off(mg.color_off)
        leds.set_color_def(mg.color_def)
        leds.set_color_on(mg.color_on)
        leds.set_color_value(mg.color_dot)
        leds.set_color_show(mg.color_dot)
        leds.set_color_blink_off(mg.color_blink_off)
        leds.set_color_blink_on(mg.color_blink_on)
    
    # Blinken aus
    do_all_no_blink()

def test_led(stripe, pos):
    do_all_off()
    strip_obj[stripe].set_pixel(pos, (70,70,70))
    ledstate.refresh()

def do_all_on():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_on()
    ledstate.refresh()

def do_all_off():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_off()
    ledstate.refresh()

def do_all_def():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def do_all_no_blink():
    for leds in led_obj:
        leds.blink_state = False

def do_blink():
    ledstate.do_blink()
    for leds in led_obj:
        if leds.get_blink_state():
            leds.show_blink()
        else:
            pass
    
    ledstate.set(True)
    ledstate.refresh()

def do_test_on():
    #print("Test on")
    led_obj[0].show_on()
    led_obj[1].show_on()
    ledstate.set(True)
 
def do_test_off():
    #print("Test off")
    led_obj[0].show_off()
    led_obj[1].show_off()
    ledstate.set(True)

def do_refresh():

    ledstate.refresh()

def do_get_state():

    return ledstate.get()

def set_all_off():                          # Setze Farbwerte in alle LED-Objekte
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_off()
    ledstate.refresh()

def set_all_def():                          # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def set_all_on():                           # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def self_test():                                # Pro Stripe einmal Aus-RGB(25%) -Aus 
    for strips in strip_obj:
        # Alle Aus
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,0))
        strips.show()
        time.sleep(0.3)
        # Alle Rot
        strips.set_pixel_line(0, strips.num_leds - 1, (50,0,0))
        strips.show()
        time.sleep(0.3)
        # Alle Grün
        strips.set_pixel_line(0, strips.num_leds - 1, (0,50,0))
        strips.show()
        time.sleep(0.3)
        # Alle Blau
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,50))
        strips.show()
        time.sleep(0.3)
        # Alle Aus
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,0))
        strips.show()
        time.sleep(0.3)


def do_blink_test():
    loops = 4
    looptime = 0.15
    #print(len(led_obj))
    for x in range(len(led_obj)):
        led_obj[x].show_blink()
        for i in range(loops):
            do_blink()
            time.sleep(looptime)
        led_obj[x].show_off()
        do_refresh()
    

def do_obj_on_off_def_off():
    
    delay_time = 0.3
    for x in range(len(led_obj)):
        led_obj[x].show_on()
        do_refresh()
        time.sleep(delay_time)
        led_obj[x].show_off()
        do_refresh()
        time.sleep(delay_time)
        led_obj[x].show_def()
        do_refresh()
        time.sleep(delay_time)
        led_obj[x].show_off()
        do_refresh()

def do_dot_test():
    delay_time = 0.2
    color_now = (0,10,60)
    for y in range(len(led_obj)):
        for x in range(led_obj[y].count):
            if x > 0:
                led_obj[y].set_pixel(x - 1, (0,0,0))
            led_obj[y].set_pixel(x, color_now)
            do_refresh()
            time.sleep(delay_time)
        led_obj[y].show_off()
        do_refresh()
        time.sleep(delay_time)
        
def set_led_obj(obj,state):
    if state == "off":
        led_obj[obj].show_off()
    if state == "def":
        led_obj[obj].show_def()
    if state == "on":
        led_obj[obj].show_on()
    if state == "blink":
        led_obj[obj].show_blink()
    do_refresh()

# -----------------------------------------------------------------------------

def main():
    
    print("WS2812 -> Setup")
    setup_ws2812()
        
    print("WS2812 -> Run self test")
    self_test()
    
    print("WS2812 -> Test -> LED")
    test_led(0,0)

    #print("WS2812 -> Object Test")
    #do_obj_on_off_def_off()

    #print("WS2812 -> LED-Dot-Test")
    #do_dot_test()

    #print("WS2812 -> Segment-Blink")
    #set_led_obj(0,"blink")
    #for i in range(0,10):
    #    do_blink()
    #    time.sleep(0.5)
    #set_led_obj(0,"def")    
    

    print("WS2812 -> End of Program !!!")

# End

#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
