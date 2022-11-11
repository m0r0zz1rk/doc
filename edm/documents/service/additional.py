from transliterate import translit, get_available_language_codes


def CreateTagRequisite(name: str) -> str:
    """Генерация тэга на основе полученного имени"""
    return translit(name, reversed=True)