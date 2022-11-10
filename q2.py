import matplotlib.pyplot as plt
import math

p = [0.00024, 0.047, 0.211, 0.422, 0.316]
x = [0, 1, 2, 3, 4]


def prob(x):
    return (
        math.factorial(4)
        / (math.factorial(x) * math.factorial(4 - x))
        * (0.75**x)
        * (0.25 ** (4 - x))
    )


y = [prob(item) for item in x]
print(y)

fig, ax = plt.subplots()
plt.plot(x, y)
plt.xlabel("y")
plt.ylabel("Likelihood for n = 4 and θ = 3/4")
for index in range(len(x)):
    ax.text(x[index], y[index], y[index], size=12)
plt.show()
