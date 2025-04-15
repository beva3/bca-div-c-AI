class TowerOfHanoi:
    def __init__(self, num_disks):  # Constructeur
        pass

    def move_disk(self, from_rod, to_rod):  # Afficher le mouvement
        pass

    def solve(self, n, source, target, auxiliary):  # Résolution récursive
        pass

    def play(self):  # Lancer la résolution
        pass

if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))   # Demander le nombre de disques
    tower_of_hanoi = TowerOfHanoi(num_disks)                # Créer une instance de TowerOfHanoi
    tower_of_hanoi.play()                                   # Lancer la résolution