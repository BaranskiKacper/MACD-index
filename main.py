import jupyterlab
import matplotlib.pyplot as plt
import matplotlib_inline
import pandas as pd
import jupyter

data = pd.read_csv('data.csv', usecols=['Data', 'Zamkniecie'], low_memory=True)
data.plot(x="Data", y="Zamkniecie")


def ema(data, N, i):
    alfa = 2 / (N + 1)
    up = data['Zamkniecie'][i]
    down = 1.0
    power = N
    start = i - N + 1
    end = i
    while start < end:
        up += data['Zamkniecie'][start] * pow(1 - alfa, power)
        down += pow(1 - alfa, power)
        power -= 1
        start += 1
    return up / down


def macd(data):
    macd = []
    for i in range(26, 1001):
            EMA12 = ema(data, 12, i)
            EMA26 = ema(data, 26, i)
            macd.append(EMA12 - EMA26)
    return macd


def signal(data):
    signal = []
    for i in range(9, 1001):
            signal.append(ema(data, 9, i))
    return signal


#data['MACD'] = macd(data)
#data['SIGNAL'] = signal(data)

plt.plot(macd(data), label='MACD', color='red')
plt.plot(signal(data), label='SIGNAL', color='blue')
plt.legend()
plt.show()