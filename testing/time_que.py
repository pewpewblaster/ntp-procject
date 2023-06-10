import threading
import time

# Inicijalizacija objekta Lock
time_lock = threading.Lock()

# Globalna varijabla koja predstavlja trenutno vrijeme
current_time = 0

def update_time(new_time):
    global current_time

    # Zaključavanje
    time_lock.acquire()

    try:
        # Provjera i ažuriranje vremena samo ako je novo vrijeme veće od trenutnog
        if new_time > current_time:
            print("Ažuriranje vremena:", new_time)
            current_time = new_time
        else:
            print("Novo vrijeme je manje od trenutnog. Neće se ažurirati.")
    finally:
        # Otključavanje
        time_lock.release()

def main():
    # Simulacija generiranja ažuriranja vremena iz različitih dretvi
    threads = []
    for i in range(5):
        # Generiranje nasumičnog vremena
        new_time = i * 10

        # Stvaranje threada i dodavanje u listu
        thread = threading.Thread(target=update_time, args=(new_time,))
        threads.append(thread)

    # Pokretanje threadova
    for thread in threads:
        thread.start()

    # Čekanje da se svi threadovi završe
    for thread in threads:
        thread.join()

    # Ispis konačnog vremena
    print("Konačno vrijeme:", current_time)

if __name__ == "__main__":
    main()
