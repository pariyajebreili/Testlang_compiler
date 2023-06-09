import subprocess
from my_utils.colorprints import ColorPrints
import os 


class RunTSVM(object):

    def run(self):        
        return_code = subprocess.run([os.path.join(os.getcwd(), "", "tsvm", "tsvm.exe"), "./generated_IR.out"]).returncode
        if return_code == 0:
            ColorPrints.print_in_purple(f"execution ended with return code: {return_code}")
        else:
            ColorPrints.print_in_red(f"execution ended with return code: {return_code}")            

        
