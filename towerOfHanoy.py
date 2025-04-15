class TowerOfHanoi:
    def __init__(self, num_disks):  # Constructeur
        self.num_disks = num_disks

    def move_disk(self, from_rod, to_rod):  # Afficher le mouvement
        print(f"Move disk from {from_rod} to {to_rod}")

    def solve(self, n, source, target, auxiliary):  # Résolution récursive
        if n == 1:
            self.move_disk(source, target)
        else:
            self.solve(n - 1, source, auxiliary, target)
            self.move_disk(source, target)
            self.solve(n - 1, auxiliary, target, source)

    def play(self):  # Lancer la résolution
        print(f"Solving Tower of Hanoi with {self.num_disks} disks:")
        self.solve(self.num_disks, 'A', 'C', 'B')

if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))   # Demander le nombre de disques
    tower_of_hanoi = TowerOfHanoi(num_disks)                # Créer une instance de TowerOfHanoi
    tower_of_hanoi.play()                                   # Lancer la résolution