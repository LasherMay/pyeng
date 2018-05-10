In [1]: VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

In [2]: VLANS = list(set(VLANS))

In [3]: VLANS.sort
Out[3]: <function list.sort>

In [4]: VLANS.sort()

In [5]: VLANS
Out[5]: [1, 2, 3, 4, 10, 20, 30, 100]
