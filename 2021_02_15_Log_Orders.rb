class Order_Log
	def initialize()
		@log = []
	end

	def record(order_id)
		@log.push(order_id)
	end

	def get_last(i)
		index = (i + 1) * -1
		return @log[index]
	end
end

new_log = Order_Log.new()

for i in 0..100 do
	new_log.record(i)
end

puts new_log.get_last(0)
puts new_log.get_last(50)
puts new_log.get_last(99)
puts new_log.get_last(100)
