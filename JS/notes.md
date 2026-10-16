Python	JavaScript
x = 5	const x = 5;（会被重新赋值的用 let）
def f(a, b):	function f(a, b) { } 或 const f = (a, b) => { }
if a and b or not c:	if (a && b || !c) { }
==	===（永远用三个等号）
None	null（变量未赋值时是 undefined）
for x in arr:	for (const x of arr) { }（注意是 of，不是 in）
for i in range(n):	for (let i = 0; i < n; i++) { }
len(arr)	arr.length
arr.append(x) / arr.pop()	arr.push(x) / arr.pop()
arr.pop(0)	arr.shift()（O(n)，慢）
arr[-1]	arr[arr.length - 1] 或 arr.at(-1)
arr[1:3]	arr.slice(1, 3)
d = {} / d[k] = v	const m = new Map() / m.set(k, v)
k in d / d.get(k, 0)	m.has(k) / m.get(k) ?? 0
set() / s.add(x) / x in s	new Set() / s.add(x) / s.has(x)
sorted(arr)	[...arr].sort((a, b) => a - b)（一定要写比较函数）
[x * 2 for x in arr]	arr.map(x => x * 2)
[x for x in arr if x > 0]	arr.filter(x => x > 0)
sum(arr)	arr.reduce((a, b) => a + b, 0)
f"hi {name}"	`hi ${name}`
float('inf')	Infinity
a // b	Math.floor(a / b)
print(x)	console.log(x)