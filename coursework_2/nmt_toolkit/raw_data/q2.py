from itertools import islice
from collections import defaultdict, OrderedDict
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

def freq_v_length(sims):
  xs = []
  ys = []
  for pair in sims.items():
    ys.append(pair[1])
    c0 = o_counts[pair[0][0]]
    c1 = o_counts[pair[0][1]]
    xs.append(min(c0,c1))
  plt.clf() # clear previous plots (if any)
  plt.xscale('log') #set x axis to log scale. Must do *before* creating plot
  plt.plot(xs, ys, 'k.') # create the scatter plot
  plt.xlabel('Min Freq')
  plt.ylabel('Similarity')
  print("Freq vs Similarity Spearman correlation = {:.2f}".format(spearmanr(xs,ys)[0]))
#  plt.show() #display the set of plots



f = open('train.en', "r")
jp_f = open('train.jp', "r")
dic_en = defaultdict(int)
dic_jp = defaultdict(int)

for line in islice(f,0,10000):
    line = line.rstrip()[:-1]
    dic_en[len(line.split())] += 1

for line in islice(jp_f,0,10000):
    line = line.rstrip()[:-1]
    dic_jp[len(line.split())] += 1


#Fill missing values
for i in dic_en.keys():
    if i not in dic_jp:
        dic_jp[i] = 0;

for i in dic_jp.keys():
    if i not in dic_en:
        dic_en[i] = 0;



#Sort dictionaries
sorted_dic_en = OrderedDict(sorted(dic_en.items(), key=lambda item: float(item[0])))
sorted_dic_jp = OrderedDict(sorted(dic_jp.items(), key=lambda item: float(item[0])))

#Create lists of values
list_en = list(sorted_dic_en.values())
list_jp = list(sorted_dic_jp.values())

#Calculate spearman and pearson correlation
spearman, _ = spearmanr(list_en, list_jp)
pearson, _ = pearsonr(list_en, list_jp)

print ("Spearman " +str(spearman))
print ("Pearson "+str(pearson))
#print ("Japanese Std " +str(np.std(list_jp)))
#print ("English Std " + str(np.std(list_en)))
#print ("Japanese Mean " + str(np.mean(list_jp)))
#print ("English Mean " + str(np.mean(list_en)))
#print ("Japanese Median " + str(np.median(list_jp)))
#print ("English Median " + str(np.median(list_en)))
#Plot scatter
plt.scatter(sorted_dic_jp.values(), sorted_dic_en.values(), color='r')
#
plt.xlabel('jp')
plt.ylabel('en')
#plt.yscale('log')
#plt.xscale('log')
plt.show()

#Plot histogram
X = np.arange(len(dic_en))
ax = plt.subplot(111)
ax.bar(X, sorted_dic_en.values(), width=0.2, color='b', align='center')
ax.bar(X-0.2, sorted_dic_jp.values(), width=0.2, color='r', align='center')
ax.legend(('English','Japanese'))
plt.xticks(X, sorted_dic_en.keys())
plt.xlabel('Sentence Length (words)')
plt.ylabel('Sentence Frequency (counts)')
plt.title("Distribution of sentence lengths in the English and Japanese", fontsize=17)
plt.show()
