from hashest import hashest
from hashest import get_words

string_dict = {1: "Who was the first king of Poland?", 2: "Who was the first ruler of Poland?", 3: "Who was the last pharaoh of Egypt?"}

j = hashest.jaccard_maker(string_dict)
occur_df = j.string_dict_to_occur_df()
print(occur_df)
jac_df = j.direct_jaccard(occur_df)
print(jac_df)


