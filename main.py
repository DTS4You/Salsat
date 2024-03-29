######################################################
### Main-Program                                   ###
### Projekt: Salsat                                ###
### Version: 1.01                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
#import module_serial
import time


pix_array_01 = [31,34,35,36]
pix_array_02 = [5,6,7,8,9,29]
pix_array_03 = [32,33]
pix_array_04 = [21]
pix_array_05 = [26]
pix_array_06 = [12,13,14,15,16,18,22,23]
pix_array_07 = [27]
pix_array_08 = [10,11,28,30]
pix_array_09 = [2]
pix_array_10 = [35,36]
pix_array_11 = [3]

def blink_func():
    MyWS2812.do_blink()

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    blink_couter = 0
       
    while MySerial.sercon_read_flag():

        if blink_couter > 50:
            blink_couter = 0
            blink_func()
        
        MySerial.sercon_read_line()
        if MySerial.get_ready_flag():       # Zeichenkette empfangen
            #print(MySerial.get_string())
            MyDecode.decode_input(str(MySerial.get_string()))
            #MyDecode.decode_printout()
            if MyDecode.get_valid_flag() == True:
                #print("Valid Command")
                if MyDecode.get_cmd_1() == "do":
                    #print("do")
                    if MyDecode.get_cmd_2() == "all":
                        #print("all")
                        if MyDecode.get_value_1() == 0:
                            #print("off")
                            MyWS2812.do_all_off()
                        if MyDecode.get_value_1() == 1:
                            #print("on")
                            MyWS2812.do_all_on()
                        if MyDecode.get_value_1() == 2:
                            #print("def")
                            MyWS2812.do_all_def()
                    if MyDecode.get_cmd_2() == "obj":
                        #print("obj")
                        #print(MyDecode.get_value_1())
                        #print(segment_map[MyDecode.get_value_1()])
                        if MyDecode.get_value_1() == 1:
                            for i in pix_array_01:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 2:
                            for i in pix_array_02:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 3:
                            for i in pix_array_03:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 4:
                            for i in pix_array_04:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 5:
                            for i in pix_array_05:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 6:
                            for i in pix_array_06:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 7:
                            for i in pix_array_07:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 8:
                            for i in pix_array_08:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 9:
                            for i in pix_array_09:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 10:
                            for i in pix_array_10:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 11:
                            for i in pix_array_11:
                                MyWS2812.set_led_obj(i, MyDecode.get_value_2())
                        
                        #MyWS2812.set_led_obj(MyDecode.get_value_1(), MyDecode.get_value_2())

                if MyDecode.get_cmd_1() == "test":
                    #print("Test")
                    if MyDecode.get_cmd_2() == "led":
                        #print("LED")
                        MyWS2812.test_led(MyDecode.get_value_1(), MyDecode.get_value_2())
                

        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep(0.01)        # 10ms
        
        

        



    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
