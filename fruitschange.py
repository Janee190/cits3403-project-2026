def random_fruit_tag(seed=None):
    import random
    if seed is not None:
        random.seed(seed)
    fruits = [("apple","crisp"), ("banana","soft"), ("orange","juicy")]
    fruit, tag = random.choice(fruits)
    return f"{fruit} - {tag}"