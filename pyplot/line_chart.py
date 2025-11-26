import matplotlib.pyplot as plt


x=[1,2,3]
y=[1,2,3]
plt.plot(x,y,label="first line", color="k")
plt.bar(x,y,label="first line", color="k")


x2=[6,5,8]
y2=[6,5,8]
plt.plot(x2,y2,label="second line")

plt.bar(x2,y2,label="second line")

plt.xlabel("speed")
plt.ylabel("time")
plt.title("what is this")
plt.legend()

plt.show()