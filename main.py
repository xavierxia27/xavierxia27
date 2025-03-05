import jieba
import math
import argparse
from collections import Counter


# 计算余弦相似度
def cosine_similarity(text1, text2):
    # 统计词频
    counter1 = Counter(text1)
    counter2 = Counter(text2)

    # 获取所有唯一的词汇
    all_words = set(text1).union(set(text2))

    # 将词频转换为向量
    vector1 = [counter1.get(word, 0) for word in all_words]
    vector2 = [counter2.get(word, 0) for word in all_words]

    # 计算点积
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # 计算向量的模
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # 计算余弦相似度
    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # 避免除以零
    else:
        return dot_product / (magnitude1 * magnitude2)


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="论文查重")

    # 添加参数
    parser.add_argument('file1', default="./orig.txt", help='path to the original file')
    parser.add_argument('file2', default="./orig_add.txt", help='path to the modified file')
    parser.add_argument('output_file', default="./res.txt", help='path to the output file')

    # 解析命令行参数
    args = parser.parse_args()

    with open(args.file1, "r", encoding="utf-8") as f1:
        content1 = f1.read()
    with open(args.file2, "r", encoding="utf-8") as f2:
        content2 = f2.read()

    list1 = jieba.lcut(content1)
    list2 = jieba.lcut(content2)
    print(list1)
    print(list2)

    # 计算并输出相似度
    similarity = cosine_similarity(list1, list2)
    print(f"两个文本的余弦相似度: {similarity:.2f}")
    re = f"这两个文本的相似度为{similarity:.2f}"

    # 将结果输进答案文件
    with open(args.output_file, "w", encoding="utf-8") as f3:
        f3.write(re)


if __name__ == "__main__":
    main()

