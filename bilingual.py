dictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
english_list = ["merry", "christmas", "and", "happy", "new", "year"]


def translate(obj, any_list):
    i = 0
    final_list = []
    for key, value in obj.items():
        if key == any_list[i]:
            final_list.append(value)
            i += 1
    print(final_list)


translate(dictionary, english_list)
