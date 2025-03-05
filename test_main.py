import unittest
import os
import jieba
import math
from collections import Counter

# 导入待测试的函数
from main import cosine_similarity


class TestCosineSimilarity(unittest.TestCase):
    def test_cosine_similarity_identical_texts(self):
        """测试两个完全相同的文本的相似度是否为 1"""
        text1 = "我喜欢用Python编程。Python非常强大！"
        text2 = "我喜欢用Python编程。Python非常强大！"
        words1 = jieba.lcut(text1)
        words2 = jieba.lcut(text2)
        similarity = cosine_similarity(words1, words2)
        self.assertEqual(similarity, 1.0)

    def test_cosine_similarity_different_texts(self):
        """测试两个完全不同文本的相似度是否为 0"""
        text1 = "我喜欢用Python编程。"
        text2 = "Java是一种很棒的编程语言。"
        words1 = jieba.lcut(text1)
        words2 = jieba.lcut(text2)
        similarity = cosine_similarity(words1, words2)
        self.assertEqual(similarity, 0.0)

    def test_cosine_similarity_partial_overlap(self):
        """测试两个部分重叠文本的相似度"""
        text1 = "我喜欢用Python编程。"
        text2 = "Python是一种很棒的编程语言。"
        words1 = jieba.lcut(text1)
        words2 = jieba.lcut(text2)
        similarity = cosine_similarity(words1, words2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)

    def test_cosine_similarity_empty_text(self):
        """测试空文本的相似度是否为 0"""
        text1 = ""
        text2 = "Python是一种很棒的编程语言。"
        words1 = jieba.lcut(text1)
        words2 = jieba.lcut(text2)
        similarity = cosine_similarity(words1, words2)
        self.assertEqual(similarity, 0.0)

    def test_cosine_similarity_single_word(self):
        """测试单个词汇的相似度"""
        text1 = "Python"
        text2 = "Python"
        words1 = jieba.lcut(text1)
        words2 = jieba.lcut(text2)
        similarity = cosine_similarity(words1, words2)
        self.assertEqual(similarity, 1.0)

    def test_cosine_similarity_numeric_text(self):
        """测试包含数字的文本的相似度"""
        text1 = "Python 3.9 发布了"
        text2 = "Python 3.10 发布了"
        words1 = jieba.lcut(text1)
        words2 = jieba.lcut(text2)
        similarity = cosine_similarity(words1, words2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)


class TestFileIO(unittest.TestCase):
    def setUp(self):
        """创建测试文件"""
        self.file1 = "test_file1.txt"
        self.file2 = "test_file2.txt"
        self.output_file = "test_output.txt"

        with open(self.file1, "w", encoding="utf-8") as f:
            f.write("我喜欢用Python编程。")
        with open(self.file2, "w", encoding="utf-8") as f:
            f.write("Python是一种很棒的编程语言。")

    def tearDown(self):
        """删除测试文件"""
        if os.path.exists(self.file1):
            os.remove(self.file1)
        if os.path.exists(self.file2):
            os.remove(self.file2)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_file_io(self):
        """测试文件读写功能"""
        from main import main  # 替换为你的脚本文件名

        # 模拟命令行参数
        import sys
        sys.argv = ["main.py", self.file1, self.file2, self.output_file]

        # 运行主函数
        main()

        # 检查输出文件是否存在
        self.assertTrue(os.path.exists(self.output_file))

        # 检查输出文件内容
        with open(self.output_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("相似度", content)


if __name__ == "__main__":
    unittest.main()