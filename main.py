from hashest import hashest
from hashest import get_words

string_dict = {1: "Who was the first king of Poland?", 2: "Who was the first ruler of Poland?", 3: "Who was the last pharaoh of Egypt?"}

j = hashest.jaccard_maker(string_dict)
df = j.string_dict_to_occur_df()
j.direct_jaccard(df)


