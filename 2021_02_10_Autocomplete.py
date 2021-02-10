dictionary = {
    "d": {
        "a": {
            "d": {"END": True},
            "y": {"END": True} 
        },
        "o": {
            "END": True,
            "g": {"END": True}
        },
        "u": {
            "e": {"END": True},
            "d": {
                "END": True, 
                "e": {"END": True}
            }
        }
    },
    "f": {
        "a": {
            "n": {"END": True},
            "i": {
                "l": {"END": True},
                "n": {
                    "t": {"END": True}
                }
            }
        },
        "u": {
            "n": {
                "END": True,
                "d": {
                    "END": True
                }
            }
        }
    }
}

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
    dict_filtered = dictionary

    for char in query_string:
        dict_filtered = dict_filtered[char]

    suffixes = get_suffixes(dict_filtered)

    return suffix_helper(query_string, suffixes) 

# assert autocomplete('da') == ['dad', 'day']
# assert autocomplete('d') == ['dad', 'day', 'do', 'dog', 'due', 'dud', 'dude']
# assert autocomplete('fa') == ['fan', 'fail', 'faint']

print(autocomplete(''))
