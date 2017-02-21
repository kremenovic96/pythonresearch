# input your code here!
def word_count_distribution(text):
    word_counts = count_words_fast(text)
    count_distribution = {}
    keys = word_counts.keys()
    sum = 0
    for i in keys:
        for j in keys:
            if word_counts[i] == word_counts[j]:
                sum += 1
               # print(sum)
        count_distribution[word_counts[i]] = sum
        sum = 0
       # print(count_distribution)
    return count_distribution

distribution = word_count_distribution(text)    
# input your code here!
def more_frequent(distribution):
    dic = {}
    keys = distribution.keys()
    frac = 0
    for i in keys:
        for j in keys:
            if distribution[j] > distribution[i]:
                frac += 1
        dic[i] = frac / len(distribution)
    return dic    
            
    

more_frequent(distribution)

hamlets = pd.DataFrame(columns=("language", "distribution"))
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text)
                hamlets.loc[title_num] = language, distribution
                title_num += 1

