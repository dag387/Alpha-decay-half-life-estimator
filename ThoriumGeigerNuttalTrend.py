import numpy as np
import matplotlib.pyplot as plt
"""
Th-233 -> Ra-229 + a
m_parent_u = 233.041577
m_daughter_u = 229.034957
A = 233
Z=90
Q= 3.7418118146359842
Result = 5.306869109603225e+19

Th-232 -> Ra-228 + a
m_parent_u = 232.038051
m_daughter_u = 228.0310686
A = 232
Z=90
Q=4.0793852778237865
Result = 3.4945291696776708e+16

Th-231-> Ra-227 + a
m_parent_u = 231.036299
m_daughter_u = 227.029171
A = 231
Z=90
Q=4.215010819348139
Result = 2443854336964133.5

Th-230 -> Ra-226 + a
m_parent_u = 230.033128
m_daughter_u = 226.025403
A = 230
Z=90
Q=4.771112799240785
Result = 140138580253.2264

Th-229 -> Ra-225 + a
m_parent_u = 229.031755
m_daughter_u = 225.023604
A = 229
Z=90
Q=5.167929287429065
Result = 370504402.33279663

Th-228 -> Ra-224 + a
m_parent_u = 228.0287397
m_daughter_u = 224.0202104
A = 228
Z=90
Q= 5.5203135068603695
Result = 3382854.11948945

Th-227 -> Ra-223 + a
m_parent_u = 227.0277025
m_daughter_u = 223.018501
A = 227
Z=90
Q= 6.146463843403478
Result = 2275.7029460343992

Th-226 -> Ra-222 + a
m_parent_u = 226.024904
m_daughter_u = 222.015353
A = 226
Z=90
Q=6.472021032625404
Result = 81.53516113748832
"""
Qlist = (3.7418118146359842,
         4.0793852778237865,
         4.215010819348139,
         4.771112799240785,
         5.167929287429065,
         5.5203135068603695,
         6.146463843403478,
         6.472021032625404
         )
tlist = (5.306869109603225e+19,
        3.4945291696776708e+16,
        2443854336964133.5,
        140138580253.2264,
        370504402.33279663,
        3382854.11948945,
        2275.7029460343992,
        81.53516113748832
       )

arr = np.array(tlist, dtype='float32')
newtlist = np.log10(tlist)

fig, ax = plt.subplots()

ax.scatter(Qlist[0], newtlist[0], color='blue')
ax.annotate('Th-233', xy=(Qlist[0], newtlist[0]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[1], newtlist[1], color='blue')
ax.annotate('Th-232', xy=(Qlist[1], newtlist[1]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[2], newtlist[2], color='blue')
ax.annotate('Th-231', xy=(Qlist[2], newtlist[2]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[3], newtlist[3], color='blue')
ax.annotate('Th-230', xy=(Qlist[3], newtlist[3]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[4], newtlist[4], color='blue')
ax.annotate('Th-229', xy=(Qlist[4], newtlist[4]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[5], newtlist[5], color='blue')
ax.annotate('Th-228', xy=(Qlist[5], newtlist[5]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[6], newtlist[6], color='blue')
ax.annotate('Th-227', xy=(Qlist[6], newtlist[6]), xytext=(0, 10), textcoords='offset points', ha='center')

ax.scatter(Qlist[7], newtlist[7], color='blue')
ax.annotate('Th-226', xy=(Qlist[7], newtlist[7]), xytext=(0, 10), textcoords='offset points', ha='center')
ax.set_title("Geiger-Nuttal trend in Thorium isotopes")
ax.set_xlabel("Q (MeV)")
ax.set_ylabel("log(t)")

plt.show()
