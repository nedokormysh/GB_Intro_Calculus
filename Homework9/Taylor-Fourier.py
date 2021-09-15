import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize = (10, 6))
plt.axis([-5, 5, -6, 20])

# # n = 50
h = 0.05
# #
x = np.arange (-2, 3, h)
# # # print(x)
# # f = np.exp(x)
# #
# # f_mac = np.array([1])
# #
# # def f_mac(x):
# #   f_mac = np.append((x/np.math.factorial(x)).sum())
# #
# # # while(n != 0):
# # #     f_mac = np.append(f_mac, f_mac[-1] + )
# # #     n -= 1
#
# f_mac = np.array([1])
#
# for x in range(1, 3):
#   for j in range(1, 3):
#     print(f_mac)
#     f_mac = np.append(f_mac,f_mac[-1] + (x ** j) / np.math.factorial(j))
#     print(f_mac)
# # print(f_mac)
#
#
#
# # plt.plot(x, f, marker="x", label="f", ls="", c = 'b')
# plt.plot(x, f_mac, marker="o", ls="", label="g", c = 'r')
# plt.show()
