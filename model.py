import numpy as np
from numpy import log as ln
from numpy import cos as cos
from numpy import sqrt
from numpy import radians as convert
import time
import math
from progress.bar import IncrementalBar
from progress.bar import Bar
import random


g = 9.8  # ускорение свободного падения
x = 0
y = 0
mu = 0.7  # коэффициент трения
m = 18000  # масса самолета
Cd = 0.5  # коэффициент аэродинамического сопротивления
S = 25  # площадь поперечного сечения самолета
v = 0  # скорость самолета
p = 1.2  # плотность воздуха
a = 0  # ускорение самолета
t = 0  # затраченное время
f_tyagi = 186390  # сила тяги самолета
Cl = 1.8  # коэффициент подъемной силы
h = 800  # высота поъема
Sp = 750  # длина пути
nu = 0.3  # кпд
q = 780  # аэродинамическое топливо


def N(m, g):
    return m * g


def sila_tr(mu, m, g):
    return mu * N(m, g)


def sila_sopr(Cd, S, p, v):
    return 1 / 2 * Cd * S * p * v**2


def spid(v, a, t):
    return v + a * t


def a_gorizont(m):
    return (f_tyagi - sila_tr(mu, m, g) - sila_sopr(Cd, S, p, v)) / m


def F_pd(Cl, S, p, v):
    return 1 / 2 * Cl * S * p * v**2


def ay(m, g):

    return (F_pd(Cl, S, p, v) - m * g) / m


def potenshil_energy(m, g, h):
    return m * g * h


def cinetic_energy(m, v):
    return m * v**2 / 2


def save_energy():
    return potenshil_energy(m, g, h) + cinetic_energy(m, v)


def change_cinetic_potensial_energy(m, v, g):
    return m * v * a_gorizont(
        f_tyagi, sila_tr(mu, m, g), sila_sopr(Cd, S, p, v), m
    ) + m * g * ay(m, g)


def work_sila_sopr_air(S):
    S * sila_sopr(Cd, S, p, v)


def summ_all_sil_sopr(S):
    return S * work_sila_sopr(mu, N(m, g), Cd, S, p, v)


def work_sila_sopr(mu, N, Cd, S, p, v, Sp):
    return (mu * N + 1 / 2 * Cd * S * p * v**2) * Sp


def energy_toplivo(mt, q):
    return mt * q


def consumption_toplivo(nu, q):
    return summ_all_sil_sopr(S) / (nu * q)


def work_sopr_razgon(Sp):
    change_cinetic_potensial_energy(m, v, g) + Sp * work_sila_sopr(
        mu, N, Cd, S, p, v, Sp
    )


def change_kinetic_energy(m, vk, v):
    return m * (vk**2 - v**2) / 2


def work_sopr_vzlet(Sp):
    change_cinetic_potensial_energy(m, v, g) + Sp * work_sila_sopr(
        mu, N, Cd, S, p, v, Sp
    )


def work_sopr_kreis(Sp):
    return Sp * work_sila_sopr(mu, N, Cd, S, p, v, Sp)


print("=========================")
print("-------------------------")
print("Взлет (Этап I/II) закончен! Данные:")
print("-------------------------")
print(f"Масса самолета: {m} (кг)")
print(f"Скорость: {v} (м/с)")
print(f"Ускорение: {ay} (м^2/с)")
print(f"Ускорение: {ax} (м^2/с)")
print(f"Сопротивление: {D} (Н)")
print("=========================")


# --- 2 Этап (Конфиг) ---
# Параметры ракеты ( ПОДСТАВИТЬ ЗНАЧЕНИЯ
F = 510000  # Тяга ракеты (Н)
seconds = [0, 10, 15, 20, 25, 30]
air_speed = 2500  # м/с
# Запускаем симмуляцию взлета
po_massive = [0.05, 0.035, 0.025, 0.013, 0.0072, 0.0065]
current = 0
for second in seconds:
    D = (po_massive[current], air_speed, Cd, A)
    a = (F, D, m)
    # print("a->",a,"D->",D)
    current_rocket_speed = (V0, a, second)
    air_speed += 80 * current
    print(f"Текущая скорость самолета: {current_rocket_speed } (м/с)")
    print(f"Координата по х: {D}")
    print(f"Координата по y: {D}")
    print(f"Топливо{consumption_toplivo(nu, q)}")
    current += 1

print("=========================")
print("-------------------------")
print("Взлет (Этап II/II) закончен! Данные:")
print("-------------------------")
print(f"Масса самолета в начале:{a_gorizont(m)} (кг)")
print(f"Масса самолета после посадки: {m} (кг)")
print(f"Скорость: {current_rocket_speed} (м/с)")
print(f"Ускорение: {a_gorizont(m)} (м^2/с)")
print(f"Сопротивление: {sila_sopr(Cd, S, p, v)} (Н)")
print("=========================")

print("-------------------------")
print("Симмуляция успешно завершена!")
print("-------------------------")
