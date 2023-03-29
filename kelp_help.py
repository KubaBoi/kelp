class help:
    @staticmethod
    def help():
        """
        # Kelp
        
        This is programming language for KubOS. Used in LilyGo Twatch 2020 v3.
        
        Kelp has syntax of Python and compiler is also written in python 
        because its simplicity and string processing
        
        Comments are ONLY marked with `#` ! 
        
        ## Structure
        
        Every program written in Kelp is group of few Python classes.
        Variables and functions should be always written with its data type.
        
        Example:
        ```python
        class vars:
            uint8_a = 5 # define usigned 8-bit int (char) with name a
            int32_b = -5 # define signed 32-bit int (int) with name b
            
        class functions:
            def uint8_sum(uint8_a, uint8_b):
                # define function sum returning unsigned 8-bit integer
                return uint8_a + uint8_b 
        ```
        
        Types:
        - `config`
            - this is NECESSARY in every program
            - need `name` and `mode` from MODE_GUI or MODE_SHL
        - `vars`
            - global variables
            - need a valid data type and _ at the start of variable
        - `lv_objs`
            - objects for gui
            - need a valid data type and _ at the start of variable
        - `funcs`
            - functions of program
            - need a valid data type and _ at the start of function
            - need return of same type as data type in name
        - `ints`
            - functions of interrupts
            - DOES NOT need a valid data type and _ at the start of function
        
        More help:
            - help.system() - system functions
        """
        print(help.help.__doc__)
        
    @staticmethod
    def system():
        """
        # System
        
        There is some default functions. It is just brief list of all functions.
        Details are in doc of every function.
        
        - print(format: str, **args) - print format and variables into STDIN
        - 
        """
        print(help.system.__doc__)