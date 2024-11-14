import random

def get_computer_choice():
    choices = ["Taş", "Kağıt", "Makas"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Seçiminizi yapın (Taş, Kağıt, Makas): ")
    while user_input not in ["Taş", "Kağıt", "Makas"]:
        user_input = input("Geçersiz seçim. Lütfen Taş, Kağıt veya Makas seçin: ")
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == "Taş" and computer_choice == "Makas") or \
         (user_choice == "Kağıt" and computer_choice == "Taş") or \
         (user_choice == "Makas" and computer_choice == "Kağıt"):
        return "Tebrikler, kazandınız!"
    else:
        return "Bilgisayar kazandı!"

def play_game():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Bilgisayarın seçimi: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
