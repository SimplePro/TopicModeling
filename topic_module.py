import pandas as pd
from nltk.tokenize import word_tokenize
from nltk import pos_tag


topic_modeling_df = pd.read_csv("./topic_modeling.csv")
topic_modeling_df.drop("Unnamed: 0", axis=1, inplace=True)


def get_topic(sentence):
    topic_count = {"Computer Science": 0, "Social": 0, "Science": 0, "Math": 0, "Sports": 0, "Art": 0, "Music": 0,
                   "Economy": 0, "Physics": 0, "Person": 0}

    topics = topic_count.keys()

    # sentence 에서 명사만 추출
    words = [i[0] for i in pos_tag(word_tokenize(sentence)) if i[1] in ["NN", "NNP"]]

    # 각 명사들이 어떤 분야에 해당하는지 카운트
    for word in words:
        topic_word = topic_modeling_df[topic_modeling_df["word"] == word].to_numpy()

        for topic in topics:
            topic_count[topic] += len([i for i in topic_word if i[1] == topic])

    # 분야별로 카운트가 높은 순으로 정렬한다.
    topic = sorted(map(list, topic_count.items()), key=lambda x: x[1], reverse=True)
    sum_count = sum([i[1] for i in topic])

    # 카운트를 퍼센테이지로 변환한다.
    for i in range(len(topic)):
        topic[i][1] = (topic[i][1] / sum_count) * 100

    return topic


if __name__ == '__main__':
    print(get_topic(sentence="""1. Python is an interpreted, high-level Object and general-purpose programming language.
                                2. Python's design philosophy emphasizes code readability with its notable use of significant indentation.
                                3. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.Python is dynamically-typed and garbage-collected.
                                4. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming.
                                5. Python is often described as a "batteries included" language due to its comprehensive standard library.Guido van Rossum began working on Python in the late 1980's, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.1.
                                6. Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.
                                7. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.
                                8. Python consistently ranks as one of the most popular programming languages."""))
