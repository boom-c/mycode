import jieba
import string
from typing import List

# 基础停用词表（过滤无意义词汇，提升查重准确性）
STOP_WORDS = {"的", "是", "在", "我", "要", "去", "今天", "晚上", "和", "及", "与", "了", "就", "也", "很",
              "非常"}


def process_txt_content(content: str) -> List[str]:

    # 1. 去除中英文标点符号（TXT文本常见干扰项）
    punctuation = string.punctuation + "，。、；：？！（）【】《》""''"
    translator = str.maketrans("", "", punctuation)
    clean_content = content.translate(translator).strip()

    # 2. 中文分词（精确模式，适配中文论文场景）
    words = jieba.lcut(clean_content)

    # 3. 过滤停用词和空字符串
    valid_words = [word for word in words if word.strip() and word not in STOP_WORDS]

    return valid_words


def get_word_frequency(words: List[str]) -> dict:

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq