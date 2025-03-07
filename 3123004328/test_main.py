import unittest

# 导入待测试的函数
from main import cosine_similarity  # 替换为你的脚本文件名


class TestCosineSimilarity(unittest.TestCase):
    def test_cosine_similarity_identical_texts(self):
        """测试两个完全相同的文本的相似度是否为 1"""
        text1 = "我喜欢用Python编程。Python非常强大！"
        text2 = "我喜欢用Python编程。Python非常强大！"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 1.0)

    def test_cosine_similarity_different_texts(self):
        """测试两个完全不同文本的相似度是否为 0"""
        text1 = "今天天气晴天"
        text2 = "Java是一种很棒的编程语言。"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 0.0)

    def test_cosine_similarity_partial_overlap(self):
        """测试两个部分重叠文本的相似度"""
        text1 = "我喜欢用Python。"
        text2 = "Python是一种很棒的编程语言。"
        similarity = cosine_similarity(text1, text2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)

    def test_cosine_similarity_empty_text(self):
        """测试空文本的相似度是否为 0"""
        text1 = ""
        text2 = "Python是一种很棒的编程语言。"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 0.0)

    def test_cosine_similarity_single_word(self):
        """测试单个词汇的相似度"""
        text1 = "Python"
        text2 = "Python"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 1.0)

    def test_cosine_similarity_numeric_text(self):
        """测试包含数字的文本的相似度"""
        text1 = "Python 3.9 发布了"
        text2 = "Python 3.10 发布了"
        similarity = cosine_similarity(text1, text2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)


if __name__ == "__main__":
    unittest.main()
