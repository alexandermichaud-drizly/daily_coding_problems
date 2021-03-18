test_prices = [3,8,7,9,2,5,8,3,5,4,7,12,4,5,3,1]
		
def buy_low_sell_high(p):
		if len(p) == 1:
				return (p, 0)

		temp_a = p[:len(p)//2]
		temp_b = p[len(p)//2:]

		a_recur = buy_low_sell_high(temp_a)
		b_recur = buy_low_sell_high(temp_b)

		a, b, a_profit, b_profit = a_recur[0], b_recur[0], a_recur[1], b_recur[1]

		low_a = None
		high_b = b[-1]

		merged = []
		while len(a) > 0 or len(b) > 0:
				if len(a) == 0:
						merged.append(b.pop(0))
				elif len(b) == 0:
						merged.append(a.pop(0))
				elif a[0] < b[0]:
						if low_a == None:
								low_a = a[0]
						merged.append(a.pop(0))
				else:
						merged.append(b.pop(0))

		profit = 0
		if low_a is not None:
				profit = high_b - low_a

		if a_profit > profit:
				profit = a_profit

		if b_profit > profit:
				profit = b_profit

		return (merged, profit)


print(buy_low_sell_high(test_prices))
