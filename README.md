# Semantic Similarity Project

This project builds semantic descriptors from text to determine word similarity using vector-based representations. It includes functions to process text, compute similarity, and evaluate the model on test questions.

## Main Functions

- `norm(vec)`: Returns the Euclidean norm of a vector represented as a dictionary.  
- `cosine_similarity(vec1, vec2)`: Computes cosine similarity between two vectors.  
- `build_semantic_descriptors(sentences)`: Creates semantic descriptors from a list of sentences.  
- `build_semantic_descriptors_from_files(filenames)`: Reads files, processes text, and builds semantic descriptors.  
- `most_similar_word(word, choices, semantic_descriptors, similarity_fn)`: Returns the word from choices most similar to the target word.  
- `run_similarity_test(filename, semantic_descriptors, similarity_fn)`: Evaluates semantic descriptors against a test file and returns the fraction of correct answers.

## Usage

```python
# Build descriptors from text files
descriptors = build_semantic_descriptors_from_files(["sample.txt"])

# Test similarity
result = run_similarity_test("test.txt", descriptors, cosine_similarity)
print("Accuracy:", result)
