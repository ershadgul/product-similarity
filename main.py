
# Get your data
products = [{
  'sku': 'test1',
  'product_title': 'Response CL Shoes',
  'brand': 'adidas',
  'department': 'shoes',
  'category': 'sneakers',
  'gender': 'male',
  'age_group': 'adult'
}]

import re
from functools import lru_cache

# Step 1: Preprocessing - Normalize & Combine Attributes
def preprocess(text):
    if not text:  
        return ""
    text = text.lower().strip()  
    text = re.sub(r'[^a-z0-9 ]', '', text)  
    return text

def generate_composite_key(product):
    fields = [
        product.get("product_title", "") or "",
        product.get("brand", "") or "",
        product.get("department", "") or "",
        product.get("category", "") or "",
        product.get("gender", "") or "",
        product.get("age_group", "") or "",
    ]
    return preprocess(" ".join(fields))

# Apply preprocessing
for product in products:
    product["composite_key"] = generate_composite_key(product)


def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()  
    return [suffix[1] for suffix in suffixes]

for product in products:
    product["suffix_array"] = build_suffix_array(product["composite_key"])


@lru_cache(None)
def lcs(s1_tuple, s2_tuple):
    if not s1_tuple or not s2_tuple:
        return 0
    if s1_tuple[-1] == s2_tuple[-1]:
        return 1 + lcs(s1_tuple[:-1], s2_tuple[:-1])
    return max(lcs(s1_tuple[:-1], s2_tuple), lcs(s1_tuple, s2_tuple[:-1]))

def compute_similarity(text1, text2):
    if not text1 or not text2:  
        return 0.0

    lcs_length = lcs(tuple(text1), tuple(text2))  
    denominator = len(text1) + len(text2)
    
    if denominator == 0:
        return 0.0

    similarity_score = (2 * lcs_length) / denominator
    return similarity_score

# Step 4: Detect Near-similars
duplicates = []
threshold = 0.99  # 99% similarity threshold

for i in range(len(products)):
    for j in range(i + 1, len(products)):
        text1, text2 = products[i]["composite_key"], products[j]["composite_key"]
        similarity = compute_similarity(text1, text2)
        
        if similarity > threshold:
            duplicates.append((products[i]["parent_zsku"], products[j]["parent_zsku"], similarity))


print("\n **Detected Similar/Duplicate Listings**\n")
for dup in duplicates:
    print(f" Product {dup[0]} and Product {dup[1]} are {dup[2]*100:.2f}% similar")
