# dictionary = {
#     "d": {
#         "a": {
#             "d": {"END": True},
#             "y": {"END": True} 
#         },
#         "o": {
#             "END": True,
#             "g": {"END": True}
#         },
#         "u": {
#             "e": {"END": True},
#             "d": {
#                 "END": True, 
#                 "e": {"END": True}
#             }
#         }
#     },
#     "f": {
#         "a": {
#             "n": {"END": True},
#             "i": {
#                 "l": {"END": True},
#                 "n": {
#                     "t": {"END": True}
#                 }
#             }
#         },
#         "u": {
#             "n": {
#                 "END": True,
#                 "d": {
#                     "END": True
#                 }
#             }
#         }
#     }
# }

word_bank = ['dad', 'day', 'do', 'dog', 'due', 'dud', 'dude', 'fan', 'fail', 'faint', 'fun', 'fund']

def dictionary_helper(tree, chars):
    if chars == '':
        tree["END"] = True
        return tree

    leading_char = chars[0]
    
    if leading_char in tree:
        tree[leading_char] = dictionary_helper(tree[leading_char], chars[1:])
    else:
        tree[leading_char] = dictionary_helper({}, chars[1:])

    return tree        

def make_dictionary(words):
    new_dict = {}
    for word in words:
        new_dict = dictionary_helper(new_dict, word)
    return new_dict

def suffix_helper(pre, suffixes):
   output = []
   for suf in suffixes:
      output.append(pre + suf)
   return output

def get_suffixes(tree):
    output = [] 
    for k, v in tree.items():
        if k == "END":
            output.append("")
        else:
            output = output + suffix_helper(k, get_suffixes(v))
    return output
            

def autocomplete(query_string):
    dict_filtered = make_dictionary(word_bank)

    for char in query_string:
        dict_filtered = dict_filtered[char]

    suffixes = get_suffixes(dict_filtered)

    return suffix_helper(query_string, suffixes) 

assert autocomplete('da') == ['dad', 'day']
assert autocomplete('d') == ['dad', 'day', 'do', 'dog', 'due', 'dud', 'dude']
assert autocomplete('fa') == ['fan', 'fail', 'faint']

print(autocomplete(''))
