# Импортируем необходимые библиотеки.
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Инициализируем словари, в дальнейшем использующийся для получения данных по ключам из других файлов.
flight_data = {}
calculations_data = {}

# Функция, загружающая данные из других файлов.
def load_data() -> None:
    load_flight_data()
    load_calculations_data()


# Функция, загружающая данные всего полета из другого файла.
def load_flight_data() -> None:
    global flight_data
    with open("flight_data.json", "r") as file:
        flight_data = json.load(file)


# Функция, загружающая данные математической модели из другого файла.
def load_calculations_data() -> None:
    global calculations_data
    with open("calculations_data.json", "r") as file:
        calculations_data = json.load(file)


# Функция, выводящая на экран сравнение графиков траектории всего полета математической модели и данных полета.
def show_flight_graphic() -> None:
    plt.subplot(1, 1, 1)
    plt.plot(flight_data["x_start"], flight_data["y_start"], label="KSP")
    plt.plot(calculations_data["x_start"], calculations_data["y_start"], label="MAT")
    plt.title("OXY")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(fontsize=9)
    plt.show()


# Функция, выводящая на экран сравнение графиков зависимости скорости от времени математической модели и данных полета.
def show_speed_graphic() -> None:
    plt.subplot(1, 1, 1)
    plt.plot(calculations_data["t"], calculations_data["v"], label="MAT")
    plt.plot(flight_data["t"], flight_data["v"], label="KSP")
    plt.title("График зависимости скорости от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Скорость, м/с")
    plt.legend(fontsize=9)
    plt.show()

# Функция, выводящая на экран сравнение графиков зависимости траты топлива от времени математической модели и данных полета.
def show_fuel_graphic() -> None:
    plt.subplot(1, 1, 1)
    plt.plot(calculations_data["t"],  calculations_data["fuel_consumption"], label="KSP")
    plt.plot(flight_data["t"], flight_data["fuel_consumption"], label="MAT")
    plt.title("График зависимости траты топлива от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Трата топлива")
    plt.legend(fontsize=9)
    plt.show()


# Точка входа в программу.
def main() -> None:
    load_data()
    show_flight_graphic()
    show_speed_graphic()
    show_fuel_graphic()


if __name__ == "__main__":
    main()

