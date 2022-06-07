import threading, time


class MyThread(threading.Thread):
    def __init__(self, nom, duree, intervalle):
        threading.Thread.__init__(self)
        self.nom = nom
        self.duree = duree
        self.intervalle = intervalle

    def run(self):
        print(self.nom + " commence à " + time.strftime("%H:%M:%S", time.localtime()) + "\n")
        while self.duree:
            time.sleep(self.intervalle)
            print(self.nom + " : " + time.strftime("%H:%M:%S", time.localtime()) + "\n")
            self.duree -= 1
        print("Fin de " + self.nom + "\n")


# Creation des deux threads puis leur démarrage
thread1 = MyThread("intervalle 1s", 5, 1)
thread2 = MyThread("intervalle 2s", 5, 2)
thread1.start()
thread2.start()
print("Fin du process principal\n")
