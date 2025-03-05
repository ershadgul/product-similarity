### Product Similarity Detection Algorithm

#### Objective
Identify near-similar or duplicate product listings based on product attributes using **Longest Common Subsequence (LCS)** and **suffix arrays**.

---
### Algorithm Steps

#### 1. **Preprocessing & Normalization**
- Combine important product attributes like `product_title`, `brand`, `department`, `category`, `gender`, and `age_group` into a single **composite_key**.
- Normalize the composite key by:
  - Lowercasing text
  - Removing special characters
  - Stripping extra spaces

**Formula:**
```python
composite_key = preprocess(product_title + brand + department + category + gender + age_group)
```

---
#### 2. **Suffix Array Construction**
Build a suffix array from the composite key to enable faster substring matching.

**Steps:**
- Generate all suffixes from the composite key.
- Sort suffixes lexicographically.

**Output:** List of starting indices of sorted suffixes.

---
#### 3. **Similarity Score Calculation (LCS-Based)**
Use **Longest Common Subsequence (LCS)** to measure the similarity between two product composite keys.

**Formula:**
```python
Similarity = (2 * LCS_Length) / (len(text1) + len(text2))
```
Where:
- `LCS_Length`: Length of the longest common subsequence
- `text1`, `text2`: Preprocessed composite keys

---
#### 4. **Duplicate Detection**
- Iterate through product pairs.
- Calculate similarity score.
- If similarity exceeds the **threshold (0.99)**, mark products as duplicates.

**Output:** List of duplicate product pairs with similarity percentage.

---
#### 5. **Performance Optimizations**
- **Caching** with `lru_cache` to speed up LCS computation.
- Early exit for zero-length strings.
- Pre-sort product lists to avoid redundant checks.


---
### Final Output
- List of similar product pairs with