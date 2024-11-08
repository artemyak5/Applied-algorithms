# example.py

from lup_decomposition import Matrix, lup_decomposition, lup_solve

def main():
    # Вхідні дані (матриця A і вектор b)
    A_data = [
        [2, 3, 1, 5, 1, 2],
        [4, 1, 3, 1, 2, 3],
        [3, 4, 2, 3, 1, 4],
        [1, 2, 5, 2, 3, 1],
        [5, 1, 2, 4, 2, 3],
        [2, 3, 4, 1, 5, 2]
    ]
    b = [10, 15, 20, 12, 18, 14]

    # Створюємо об'єкт матриці
    A = Matrix(A_data)

    # Виконуємо LUP-розклад
    L, U, P = lup_decomposition(A.data)

    # Розв'язуємо систему
    x = lup_solve(L, U, P, b)

    # Виводимо розв'язок
    print("Знайдений розв'язок x:")
    for i, xi in enumerate(x, 1):
        print(f"x_{i} = {xi:.4f}")

    # Перевірка
    Ax = A * x
    print("\nПеревірка (Ax):")
    for i, (bi_calc, bi_orig) in enumerate(zip(Ax, b), 1):
        print(f"Рівняння {i}: Ax = {bi_calc:.4f}, b = {bi_orig}")


main()
