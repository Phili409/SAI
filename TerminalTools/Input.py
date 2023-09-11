import sys, time, threading, cursor, msvcrt

class Input:
    def __init__(self):
        self.StopBlinking = False
        self.Current = ""

    def BlinkingDot(self):
        while not self.StopBlinking:
            # Display current input along with the dots
            sys.stdout.write('\r' + self.Current + '.' * (26 - len(self.Current)))
            sys.stdout.flush()
            time.sleep(0.5)
            # Clear the dots without going to a new line
            sys.stdout.write('\r' + ' ' * (len(self.Current) + 26) + '\r' + self.Current)
            sys.stdout.flush()
            time.sleep(0.5)

    def CustomInput(self, prompt):
        print(prompt, end="", flush=True)
        while True:
            ch = msvcrt.getch().decode('utf-8', 'ignore')
            if ch == '\r':  # Enter key pressed
                print()
                return self.Current
            elif ch == '\b':  # Backspace key pressed
                if self.Current:
                    print(ch + ' ' + ch, end="", flush=True)
                    self.Current = self.Current[:-1]
            else:  
                print(ch, end="", flush=True)
                self.Current += ch

    def GetInput(self):
        sys.stdout.write('\033[1B\r')  # Move down one line and return to the beginning
        sys.stdout.flush()
        result = self.CustomInput("Pick Something: ")
        self.StopBlinking = True
        return result

    def Return(self):
        cursor.hide()
        thread = threading.Thread(target=self.BlinkingDot)
        thread.start()
        user_input = self.GetInput()
        sys.stdout.write('\033[1A\r                 \r')  # Move up one line and clear it
        sys.stdout.flush()
        cursor.show()
        return user_input

# Example usage:
inputter = Input()
result = inputter.Return()
print(f"You entered: {result}")
