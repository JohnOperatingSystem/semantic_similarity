import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''
    # Initialize sum of squares
    sum_of_squares = 0.0
    # Add the square of each component
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    # Return the square root of the sum of squares
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    # Compute the dot product of vec1 and vec2
    sum = 0
    for i in vec1:
        if i in vec2:
            sum += vec1[i]*vec2[i]
    # Compute sum of squares for vec1
    vec1sum = 0
    for i in vec1.values():
        vec1sum += i**2
    # Compute sum of squares for vec2
    vec2sum = 0
    for i in vec2.values():
        vec2sum += i**2
    # Return cosine similarity
    return sum/(vec1sum*vec2sum)**0.5


def build_semantic_descriptors(sentences):
    d = {}
    # Loop through each sentence
    for sentence in sentences:
        # Use unique words to avoid double-counting
        unique_words = set(sentence)
        for word in unique_words:
            if word not in d:
                d[word] = {}
            for word2 in unique_words:
                if word2 != word:
                    # Increment co-occurrence count
                    if word2 in d[word]:
                        d[word][word2] += 1
                    else:
                        d[word][word2] = 1
    return d


def build_semantic_descriptors_from_files(filenames):
    actual_L = []
    # Loop through each file
    for i in filenames:
        temp_L = []
        new_file = open(i, "r", encoding = "latin1")
        # Read the file and convert to lowercase
        sentence = new_file.read().lower()
        # Replace punctuation with appropriate spaces or periods
        sentence = sentence.replace("!", ".")
        sentence = sentence.replace("?", ".")
        sentence = sentence.replace(",", " ")
        sentence = sentence.replace("-", " ")
        sentence = sentence.replace("--", " ")
        sentence = sentence.replace(":", " ")
        sentence = sentence.replace(";", " ")
        # Split text into sentences
        temp_L2 = sentence.split(".")
        for j in temp_L2:
            # Split sentence into words
            temp_L.append(j.split())
        actual_L = actual_L + temp_L
    # Build semantic descriptors from the processed sentences
    return build_semantic_descriptors(actual_L)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    # If the word is not in the descriptors, return the first choice
    if word not in semantic_descriptors:
        return choices[0]
    largest_value = 0
    best_word = choices[0]
    word = word.lower()
    vec1 = semantic_descriptors[word]
    # Loop through each choice and compute similarity
    for choice in choices:
        if choice not in semantic_descriptors:
            value = -1
        else:
            vec2 = semantic_descriptors[choice]
            value = similarity_fn(vec1, vec2)
        # Update the best match if similarity is higher
        if value > largest_value:
            largest_value = value
            best_word = choice
    return best_word


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    L = []
    # Read test questions from file
    questions = open(filename, "r", encoding="latin1").read().split("\n")
    count, correct_count = 0, 0
    # Split each line into words
    for line in questions:
        words = line.split(" ")
        L.append(words)
    # Loop through all questions
    for ind1 in range(len(L)):
        word = L[ind1][0]          # Target word
        choices = L[ind1][2:]      # Choices
        # Find the most similar word
        ans = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        # Update counts
        if ans == L[ind1][1]:
            count += 1
        correct_count += 1
    # Return the fraction of correct answers
    return count/correct_count
