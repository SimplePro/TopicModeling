# TopicModeling

#### 문서의 분야를 예측하는 모듈
``` python
>>> from topic_module import get_topic
>>> get_topic(sentence="""1. Python is an interpreted, high-level Object and general-purpose programming language.
                          2. Python's design philosophy emphasizes code readability with its notable use of significant indentation.
                          3. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.Python is dynamically-typed and garbage-collected.
                          4. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming.
                          5. Python is often described as a "batteries included" language due to its comprehensive standard library.Guido van Rossum began working on Python in the late 1980's, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.1.
                          6. Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.
                          7. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.
                          8. Python consistently ranks as one of the most popular programming languages.""")

[['Computer Science', 23.096446700507613], ['Math', 15.736040609137056], ['Science', 15.48223350253807], ['Music', 11.421319796954315], ['Art', 8.375634517766498], ['Social', 8.121827411167512], ['Economy', 7.614213197969544], ['Sports', 5.0761421319796955], ['Physics', 5.0761421319796955]]
```
