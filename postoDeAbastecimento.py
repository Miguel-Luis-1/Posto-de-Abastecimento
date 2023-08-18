gasolina = 7.199
etanol = 5.419
gnv = 4.259

valorGasolina = 0
valorEtanol = 0
valorGnv = 0
valorTotal = 0

opcao = None

while opcao != 0:
    print("Insira um número para o tipo de abastecimento que deseja:")
    print("0 - Finalizar | 1 - Gasolina | 2 - Etanol | 3 - GNV ")
    opcao = int(input("Opção: "))
    print("---------------------------------------------")

    if opcao == 1:
        qtndGasolina = float(input("Quantos litros de Gasolina você deseja abastecer?"))
        valorGasolina += qtndGasolina * gasolina
        valorTotal += valorGasolina
    elif opcao == 2:
        qtndEtanol = float(input("Quantos litros de Etanol você deseja abastecer?"))
        valorEtanol += qtndEtanol * etanol
        valorTotal += valorEtanol
    elif opcao == 3:
        qtndGnv = float(input("Quantos m³ de GNV você deseja abastecer?"))
        valorGnv += qtndGnv * gnv
        valorTotal += valorGnv

print("---------------------------------------------")
print("Valores totais:")
print(f"Total abastecido de Gasolina: {qtndGasolina} L")
print(f"Valor gasto em Gasolina: R${valorGasolina:.2f}")
print(f"Total abastecido de Etanol: {qtndEtanol} L")
print(f"Valor gasto em Etanol: R${valorEtanol:.2f}")
print(f"Total abastecido de GNV: {qtndGnv} m³")
print(f"Valor gasto em GNV: R${valorGnv:.2f}")
print(f"Valor total: R${valorTotal:.2f}")
