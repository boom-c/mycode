import numpy as np
from typing import List
from text_processor import get_word_frequency


def jaccard_similarity(words1: List[str], words2: List[str]) -> float:

    set_a = set(words1)
    set_b = set(words2)

    # 边界场景：两个空文本（TXT内容为空）
    if not set_a and not set_b:
        return 1.0
    # 一个空文本、一个非空文本
    if not set_a or not set_b:
        return 0.0

    intersection = len(set_a & set_b)  # 交集大小
    union = len(set_a | set_b)  # 并集大小
    return round(intersection / union, 4)


def cosine_similarity(words1: List[str], words2: List[str]) -> float:

    # 获取词频字典
    freq1 = get_word_frequency(words1)
    freq2 = get_word_frequency(words2)

    # 构建统一词库（确保向量维度一致）
    all_words = set(freq1.keys()).union(set(freq2.keys()))
    # 生成词频向量
    vec1 = [freq1.get(word, 0) for word in all_words]
    vec2 = [freq2.get(word, 0) for word in all_words]

    # 转换为numpy数组计算
    np_vec1 = np.array(vec1)
    np_vec2 = np.array(vec2)

    # 计算点积和模长
    dot_product = np.dot(np_vec1, np_vec2)
    norm1 = np.linalg.norm(np_vec1)
    norm2 = np.linalg.norm(np_vec2)

    # 边界场景：零向量（避免除以0）
    if norm1 == 0 or norm2 == 0:
        return 1.0 if (norm1 == 0 and norm2 == 0) else 0.0

    return round(dot_product / (norm1 * norm2), 4)


def calculate_final_repeat_rate(words1: List[str], words2: List[str]) -> float:

    jaccard = jaccard_similarity(words1, words2)
    cosine = cosine_similarity(words1, words2)
    return round((jaccard + cosine) / 2, 4)