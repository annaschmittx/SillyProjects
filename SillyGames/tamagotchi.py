import random
import time

class tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0 - 100, 0 = cheio, 100 = com fome
        self.happiness = 50  # 0 - 100, 0 = triste, 100 = feliz
        self.energy = 50  # 0 - 100, 0 = cansado, 100 = cheio de energia

    def feed(self):
        print(f"\nVocê alimentou {self.name}!")
        self.hunger = max(0, self.hunger - 20)
        print(f"{self.name} tá menos esfomeado. Fomeômetro: {self.hunger}/100")

    def play(self):
        if self.energy <= 10:
            print(f"\n{self.name} tá muito cansadinho. Tenta fazer ele tirar uma soneca :).")
        else:
            print(f"\nVocê brincou com {self.name}!")
            self.happiness = min(100, self.happiness + 15)
            self.hunger = min(100, self.hunger + 10)  # brincar faz o tamagotchi ficar com fome
            self.energy = max(0, self.energy - 15)  # brincar também cansa
            print(f"{self.name} ficou feliz! Felizômetro: {self.happiness}/100")

    def sleep(self):
        print(f"\n{self.name} tá nanando! Zzz...")
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} acordou! Energiômetro: {self.energy}/100")

    def check_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Fome: {self.hunger}/100")
        print(f"Felicidade: {self.happiness}/100")
        print(f"Energia: {self.energy}/100")

    def complain(self):
        complaints = []
        if self.hunger >= 80:
            complaints.append(f"{self.name} tá morrendo de fome, coitado... Alimenta ele!")
        if self.happiness <= 20:
            complaints.append(f"{self.name} tá mais xoxo que chuchu Brinca com ele!")
        if self.energy <= 20:
            complaints.append(f"{self.name} tá cansadinho, coitado. Bota ele pra nanar!")
        if complaints:
            print("\n".join(complaints))
        else:
            print(f"{self.name} tá deiz :D")

    def random_event(self):
        events = ['fome', 'brincar', 'cansado']
        event = random.choice(events)
        if event == 'fome':
            print(f"\n{self.name} te bizoia com os olhos assim O.o ele parece com fome.")
        elif event == 'briincar':
            print(f"\n{self.name} tá mais doido que pinto ciscando, quer brincar!")
        elif event == 'cansado':
            print(f"\n{self.name} parece estar com soniinho...")

def main():
    pet_name = input("Qual o nome do teu bichinho? ")
    pet = tamagotchi(pet_name)

    while True:
        print("\n--- O que tu quer fazer agora? ---")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Botar pra nanar")
        print("4. Checar o Status")
        print("5. Sair :C")

        choice = input("Escolha tua opção: ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.check_status()
        elif choice == '5':
            print(f"Tchauzinho! {pet.name} vai ficar com saudade! <3")
            break
        else:
            print("Ixi maria, não entendi... Tenta de novo!")

        pet.complain()

        # Random events happening after every action
        if random.randint(1, 4) == 1:
            pet.random_event()

        time.sleep(1)  # Add a slight delay to simulate time passing

if __name__ == "__main__":
    main()
