import time
import random

# Fungsi untuk melakukan Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    end_time = time.time()
    return arr, end_time - start_time

# Fungsi untuk melakukan Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    return arr, end_time - start_time

# Fungsi untuk menampilkan 5 iterasi pertama dan terakhir
def show_iterations(arr):
    print("5 Iterasi Pertama:")
    for i in range(5):
        print(arr[i], end=" ")
    print("\n")

    print("5 Iterasi Terakhir:")
    n = len(arr)
    for i in range(n - 5, n):
        print(arr[i], end=" ")
    print("\n")

# Fungsi untuk menampilkan array sebelum dan sesudah pengurutan
def show_before_after(arr, sorted_arr):
    print("Sebelum pengurutan:", arr)
    print("Setelah pengurutan:", sorted_arr)
    print("\n")

# Fungsi untuk melakukan analisis algoritma
def analyze_algorithm():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    print("list:")
    print(arr)
    print("\n")

    while True:
        print("Pilihan pengurutan:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        choice = input("Masukkan pilihan Anda (1/2): ")

        if choice == '1':
            print("Bubble Sort\n")
            sorted_arr, bubble_time = bubble_sort(arr.copy())
            show_before_after(arr, sorted_arr)
            print("Waktu komputasi Bubble Sort:", bubble_time, "detik")
            print("Hasil Iterasi Bubble Sort:")
            show_iterations(sorted_arr)

            # Analisis algoritma Bubble Sort
            print("Analisis Algoritma Bubble Sort:")
            n = len(arr)
            worst_case = list(range(n, 0, -1))
            best_case = list(range(n))
            avg_case = random.sample(range(n), n)
            print("Worst Case:")
            _, worst_case_time = bubble_sort(worst_case.copy())
            print("Waktu komputasi:", worst_case_time, "detik")
            print("Best Case:")
            _, best_case_time = bubble_sort(best_case.copy())
            print("Waktu komputasi:", best_case_time, "detik")
            print("Average Case:")
            _, avg_case_time = bubble_sort(avg_case.copy())
            print("Waktu komputasi:", avg_case_time, "detik")

            break
        elif choice == '2':
            print("Insertion Sort\n")
            sorted_arr, insertion_time = insertion_sort(arr.copy())
            show_before_after(arr, sorted_arr)
            print("Waktu komputasi Insertion Sort:", insertion_time, "detik")
            print("Hasil Iterasi Insertion Sort:")
            show_iterations(sorted_arr)

            # Analisis algoritma Insertion Sort
            print("Analisis Algoritma Insertion Sort:")
            n = len(arr)
            worst_case = list(range(n, 0, -1))
            best_case = list(range(n))
            avg_case = random.sample(range(n), n)
            print("Worst Case:")
            _, worst_case_time = insertion_sort(worst_case.copy())
            print("Waktu komputasi:", worst_case_time, "detik")
            print("Best Case:")
            _, best_case_time = insertion_sort(best_case.copy())
            print("Waktu komputasi:", best_case_time, "detik")
            print("Average Case:")
            _, avg_case_time = insertion_sort(avg_case.copy())
            print("Waktu komputasi:", avg_case_time, "detik")

            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
analyze_algorithm()