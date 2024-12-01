def calcular_agua_peso(peso):
    return peso * 35 / 1000  # 35 ml por kg em litros

def verificar_consumo(consumido, ideal):
    if consumido >= ideal:
        return "Parabéns! Você atingiu sua meta de consumo diário de água."
    else:
        return f"Você precisa beber mais {ideal - consumido:.2f} litros hoje."

if __name__ == "__main__":
    peso = float(input("Digite seu peso (kg): "))
    ideal = calcular_agua_peso(peso)
    print(f"Sua meta diária de consumo de água é: {ideal:.2f} litros.")

    consumido = float(input("Digite a quantidade de água consumida hoje (litros): "))
    print(verificar_consumo(consumido, ideal))