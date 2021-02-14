def longest_substring_length(input, k)
	index = 0 # right side of window
	
	longest = ''
	longest_len = 0
	longest_unique_chars = 0
	
	window = ''
	window_len = 0
	window_unique_chars = 0

	char_hash = {}

	while index < input.length do
		new_char = input[index]
		window += new_char
		prev_count = 0		
		
		if char_hash.has_key? new_char
			prev_count = char_hash[new_char]
			char_hash[new_char] += 1
		else
			char_hash[new_char] = 1
		end
		
		window_len += 1
		window_unique_chars += prev_count == 0 ? 1 : 0

		if window_unique_chars > k 
			while window_unique_chars > k do
				first_char = window.slice!(0)
				window_len -= 1	
				char_hash[first_char] -= 1
				if char_hash[first_char] == 0
					window_unique_chars -= 1
				end
			end
		end
		
		if window_len > longest_len and window_unique_chars >= longest_unique_chars
			longest = window
			longest_len = window_len
			longest_unique_chars = window_unique_chars
		end
		
		index += 1
	end

	return longest
end

puts longest_substring_length('abcba', 2)
puts longest_substring_length('acaab', 2)
puts longest_substring_length('acfafdeeagfb', 4)
