def printf(format, **args):
    pass
    name = "Test App"
    mode = MODE_GUI
    uint8_a = 5
    uint8_b = 6 # banan
    uint8_c = 0
class lv_objs:
    pass
class funcs:
    def uint8_sum(uint8_a, uint8_b):
        printf("ahoj: %d + %d\n", uint8_a, uint8_b)
        return uint8_a + uint8_b
    def void_print_globals():
        printf("%d %d %d\n", uint8_a, uint8_b, uint8_c)
class ints:
    def irq_short_button():
        printf("vysledek: %d", funcs.uint8_sum(uint8_a, uint8_b))
