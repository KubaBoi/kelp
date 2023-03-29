
class kelp_comp:
    
    # source data lines
    src_dtl = ""
    
    @staticmethod
    def load(path: str):
        with open(path, "r", encoding="utf-8") as f:
            kelp_comp.src_dtl = f.readlines()
            
    @staticmethod
    def compile():
        line = kelp_comp.src_dtl[0]
        while (line)
        
if __name__ == "__main__":
    kelp_comp.load("kelp/testApp.py")