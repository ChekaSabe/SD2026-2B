import time

def ciclo():
    cnt = 0
    print("Iniciando Ciclo...")
    while True:
        try:
            print(f"{cnt}: Ciclo en ejecución...")
            cnt += 1
            time.sleep(1)
        except keyboardInterrupt:
            print("Ciclo intermedio por el usuario.")
            break
if __name__ == "__main__":
    ciclo()