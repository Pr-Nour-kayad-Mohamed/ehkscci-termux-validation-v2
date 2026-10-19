import matplotlib.pyplot as plt
times=[661,175,86.1,69.4,23.9]
labels=['V3.0','V3.1','V3.2','V3.3','V3.4']
plt.figure()
plt.bar(labels,times)
plt.yscale('log')
plt.savefig('speedup.png')
print('saved')
