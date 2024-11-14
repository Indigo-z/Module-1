

class WordsFinder:
    def __init__(self, *filenames):
        self.file_name= list(filenames)

    def get_all_words(self):
        all_words = {}
        for filename in self.file_name:
            with open(filename, 'r', encoding='utf-8') as file:
                text_ = file.read().lower()
                marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for mark in marks:
                    text_ = text_.replace(mark, '')

                word = text_.split()
                all_words[filename] = word

        return all_words
    def find(self, word):
        word = word.lower()
        dict_ = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word== words[i]:
                    dict_[name] = words.index(word) + 1
        return dict_

    def count(self, word):
        word = word.lower()
        dict_ = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word== words[i]:
                    dict_[name] = words.count(word)
        return dict_




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего