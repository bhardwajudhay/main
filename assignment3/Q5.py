def f():
	x=42
	def g():
		global x
		x=43
	print("before calling g:",x)
	g()
	print("after calling g:",x)
f()
print("x in main:",x)

# output:
"""before calling g: 42
after calling g: 42
x in main: 43
"""