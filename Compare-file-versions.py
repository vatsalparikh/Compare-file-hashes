"""
Welcome!

You are welcome to take a completely different approach than the
starter code suggests.

Being able to compare version differences is important,
imagine for example that a user has made a change to a file.
That change has been represented in the form of an update SHA256 hash, ie
"7aec47f359bb75b7..."

Now we want to compare the user's new version, to a prior stored version.
The prior version may have a different hash, say "f05e411f0e98d2..."

This clearly indicates a change. Since "7aec47f359bb75b7..." != "f05e411f0e98d2...".
However, in a version we may have many files. See the list below for two tiny examples.
How do we know which file was added? Which relates to which?

One way is to compare the file hashes. Python has some powerful built in
tools to help do this in O ( len(s) ) running time.

After you are done comparing the files, make some formatting adjustments
to pretty print for web.

The lists may not be the same length.

"""

import itertools
import random
import string

# alpha_hash_list = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6",
# 				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0",
# 				   "813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452"]
#
# bravo_hash_list = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6",
# 				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0",
# 				   "caccfde4071a22b06a5c7897c54cfe2d8812a254714882e80c7ff75aac6fa187",
# 				   "485F9D544C6AF6B3E634022E4FB0132DC89A7EA864E6FE5EF8E6227E84AC670E"]

# bravo_hash_list = ["apples" for i in range(10**6)]
# alpha_hash_list = ["pears" for i in range(10**6)]

bravo_hash_list = [''.join(random.choices(string.ascii_uppercase, k=10)) for i in range(10 ** 6)]
alpha_hash_list = [''.join(random.choices(string.ascii_uppercase, k=10)) for i in range(10 ** 6)]

change_type_list = ["added", "unchanged", "removed"]


def compare_file_lists(alpha_hash_list, bravo_hash_list):
    """
    Compare the difference between file lists:

    Return a dictionary with the 3 keys in change_type_list
    and the values being the hashs.

    Example output

    {  'unchanged': {'7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6',
                    'f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0'},
        'added': {'813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452'},
        'removed': {'caccfde4071a22b06a5c7897c54cfe2d8812a254714882e80c7ff75aac6fa187'}
    }


    """
    changes = {}

    ### YOUR CODE HERE

    # defining new set for each change_type
    set_a = set(alpha_hash_list)
    set_b = set(bravo_hash_list)
    set_unchanged = set()
    set_added = set()
    set_removed = set()

    # checking if all elements in the list are same
    if len(set_a) <= 1 and len(set_b) <= 1:
        if (alpha_hash_list[0] == bravo_hash_list[0]):
            set_unchanged.add(alpha_hash_list[0])
            changes['unchanged'] = set_unchanged
            changes['added'] = set_added
            changes['removed'] = set_removed
        else:
            set_added.add(alpha_hash_list[0])
            set_removed.add(bravo_hash_list[0])
            changes['unchanged'] = set_unchanged
            changes['added'] = set_added
            changes['removed'] = set_removed
    # checking if all elements in the list are different
    elif len(set_a) <= len(alpha_hash_list) and len(set_b) <= len(bravo_hash_list) and len(set_a) == len(set_b):
        if len(set_a.intersection(set_b)) == 0:
            changes['unchanged'] = set_unchanged
            changes['added'] = set_a
            changes['removed'] = set_b
    # iterating over alpha and bravo lists simultaneously while also taking into consideration the longer list
    else:
        set_unchanged = set_a.intersection(set_b)
        set_added = set_a.difference(set_b)
        set_removed = set_b.difference(set_a)
        changes['unchanged'] = set_unchanged
        changes['added'] = set_added
        changes['removed'] = set_removed

    return changes


def add_change_type_flags_into_one_list(changes, change_type_list):
    """
    Convert differences into single list for easier front end consumption

    Arguments:
        changes, dict from compare_file_lists()
        change_type_list, list of strings

    Returns:
        list of dicts
            each dict has key/value pairs of:
                'hash' : hash_value,
                'change_type' : change_string
            ie. {'hash': '813c9c630a770b91a...',
                'change_type': 'added'}
    """
    new_list_with_flags = []

    ### YOUR CODE HERE

    for type in changes:
        set = changes.get(type)
        # handling change_type_key is None case
        if set is not None:
            for value in set:
                dict = {}
                dict['hash'] = value
                dict['change_type'] = type
                new_list_with_flags.append(dict)

    ### TODO NOTE
    # Handle if a change_type_key is None, ie there are no 'added" files

    return new_list_with_flags


def main(alpha_hash_list, bravo_hash_list, change_type_list):
    """
    Runs comparison and combination, prints out results
    """
    changes = compare_file_lists(alpha_hash_list, bravo_hash_list)

    combined_list = add_change_type_flags_into_one_list(changes, change_type_list)

    for item in combined_list:
        print(item)

    """
    Example output

    {'hash': '813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452', 'change_type': 'added'}
    {'hash': '7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6', 'change_type': 'unchanged'}
    {'hash': 'f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0', 'change_type': 'unchanged'}
    {'hash': 'caccfde4071a22b06a5c7897c54cfe2d8812a254714882e80c7ff75aac6fa187', 'change_type': 'removed'}

    """


main(alpha_hash_list, bravo_hash_list, change_type_list)
