import config
from utils.color_prints import Colorprints

class CompilerMessages(object):

    def __init__(self):
        self.errors = 0
        self.warnings = 0
        self.messages = []


    def print_messages(self):
        self.messages.sort(key=self.sort_by_lineno)
        for msg in self.messages:
            Colorprints.print_in_black(f"{config.code_file_path}:", end="")
            Colorprints.print_in_cyan(f"{msg['lineno']}: ", end="")
            if "is_warning" in msg:
                Colorprints.print_in_yellow(f"{msg['message']}")
            else:
                Colorprints.print_in_red(f"{msg['message']}")


    def add_message(self, message):
        if not message in self.messages:
            self.messages.append(message)
            if not "is_warning" in message:
                self.errors += 1 
            else:
                message["message"] = "WARNING" + message["message"]
                self.warnings +=1

    def sort_by_lineno(self, msg):
        return msg["lineno"]
