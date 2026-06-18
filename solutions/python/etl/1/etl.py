def transform(legacy_data):
    new = dict()
    for key, value in legacy_data.items():
        for letter in value:
            new[letter.lower()] = key
    return new
