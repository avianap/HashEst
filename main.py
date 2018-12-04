from hashest import hashest
from hashest import get_words

string_dict = {0: "Who was the first king of Poland?", 1: "Who was the first ruler of Poland?", 2: "Who was the last pharaoh of Egypt?", 3:"Who are you?"}
print(string_dict)

j = hashest.jaccard_maker(string_dict)
occur_dict = j.string_dict_to_occur_dict()
jac_df = j.direct_jaccard(occur_dict)
print(jac_df)
jac_est_df = j.permute_jaccard(occur_dict, permutations = 100)
print(jac_est_df)

