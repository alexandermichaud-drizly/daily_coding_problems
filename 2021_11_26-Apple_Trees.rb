def longest_row(orchard)
  trees = orchard.length()
  return orchard if trees < 3

  longest = []  
  
  left_index = 0
  right_index = 1

  bag = {}
  bag[orchard[0]] = 1

  while right_index < trees do
    r = orchard[right_index]
    if !bag[r].nil?
      bag[r] += 1
    elsif bag.keys.length() < 2
      bag[r] = 1 
    else
      current_bag = orchard[left_index..(right_index - 1)]
      apples = current_bag.length()
      longest = current_bag if apples > longest.length()

      until bag.keys.length() == 1 || left_index == right_index do
        l = orchard[left_index]
        bag[l] -= 1
        bag.delete(l) if bag[l] == 0
        left_index += 1
      end
      
      bag[r] = 1
    end
    right_index += 1
    puts bag
  end

  longest
end


test = [2, 1, 2, 3, 3, 1, 3, 5]
puts longest_row(test)