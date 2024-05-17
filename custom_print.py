# Enhances the print and input with different color/styles
class CustomPrint:
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    PURPLE = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def error(self, message: str):
        print(f"{self.RED}{message}{self.RESET}")

    def success(self, message: str):
        print(f"{self.GREEN}{message}{self.RESET}")

    def info(self, message: str):
        print(f"{self.BLUE}{message}{self.RESET}")

    def warning(self, message: str):
        print(f"{self.YELLOW}{message}{self.RESET}")

    def option_list(self, message: str):
        print(f"{self.PURPLE}{message}{self.RESET}")

    def header(self, message: str, color: str = PURPLE):
        print(f"{color}{self.BOLD}{message}{self.RESET}")

    # The input has to be returned so it can be converted to int in case a number is passed in the str
    def input(self, message: str):
        return input(f"{self.YELLOW}{message}{self.RESET}")
