class TowerOfHanoi:
    def __init__(self, num_disks):  # Constructeur
        self.num_disks = num_disks
        self.step = 1  # compteur d'étapes

    def move_disk(self, from_rod, to_rod):  # Afficher le mouvement
        print(f"Step {self.step}: Move disk from {from_rod} to {to_rod}")
        self.step += 1

    def solve(self, n, source, target, auxiliary):  # Résolution récursive
        if n == 1:
            self.move_disk(source, target)
        else:
            # 1. Déplacer n-1 disques de source à auxiliaire
            print(f"→ Moving {n-1} disk(s) from {source} to {auxiliary} [using {target} as support]")
            self.solve(n - 1, source, auxiliary, target)

            # 2. Déplacer le disque restant
            self.move_disk(source, target)

            # 3. Déplacer n-1 disques de auxiliaire à destination
            print(f"→ Moving {n-1} disk(s) from {auxiliary} to {target} [using {source} as support]")
            self.solve(n - 1, auxiliary, target, source)

    def play(self):  # Lancer la résolution
        print(f"\n🎯 Solving Tower of Hanoi with {self.num_disks} disks:\n")
        self.solve(self.num_disks, 'A', 'C', 'B')
        print("\n🎉 All disks have been moved successfully!")
        
if __name__ == "__main__":
        num_disks = int(input("Enter the number of disks: "))
        hanoi = TowerOfHanoi(num_disks)
        hanoi.play()
        print("Game Over!")