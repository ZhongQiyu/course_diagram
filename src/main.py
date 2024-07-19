# main.py

import argparse
from pdf_extractor import PDFTextExtractor, KnowledgeGraphBuilder

# 主程序
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='从PDF文件提取文本并构建知识图谱')
    parser.add_argument('pdf_files', nargs='+', help='PDF文件路径列表')
    args = parser.parse_args()

    # 定义知识点模式
    knowledge_patterns = [
        {'regex': r'贝叶斯决策理论', 'parent': '模式识别', 'child': '贝叶斯决策理论'},
        {'regex': r'贝叶斯公式', 'parent': '贝叶斯决策理论', 'child': '贝叶斯公式'},
        {'regex': r'先验概率', 'parent': '贝叶斯决策理论', 'child': '先验概率'},
        {'regex': r'后验概率', 'parent': '贝叶斯决策理论', 'child': '后验概率'},
        {'regex': r'最大后验估计', 'parent': '贝叶斯决策理论', 'child': '最大后验估计'},
        {'regex': r'最小错误率决策', 'parent': '贝叶斯决策理论', 'child': '最小错误率决策'},
        {'regex': r'最小风险决策', 'parent': '贝叶斯决策理论', 'child': '最小风险决策'},
        {'regex': r'概率密度函数估计', 'parent': '模式识别', 'child': '概率密度函数估计'},
        {'regex': r'参数估计', 'parent': '概率密度函数估计', 'child': '参数估计'},
        {'regex': r'矩估计', 'parent': '参数估计', 'child': '矩估计'},
        {'regex': r'最大似然估计', 'parent': '参数估计', 'child': '最大似然估计'},
        {'regex': r'贝叶斯估计', 'parent': '参数估计', 'child': '贝叶斯估计'},
        {'regex': r'非参数估计', 'parent': '概率密度函数估计', 'child': '非参数估计'},
        {'regex': r'Parzen窗法', 'parent': '非参数估计', 'child': 'Parzen窗法'},
        {'regex': r'k-近邻法', 'parent': '非参数估计', 'child': 'k-近邻法'},
        {'regex': r'特征选择和变换', 'parent': '模式识别', 'child': '特征选择和变换'},
        {'regex': r'特征提取', 'parent': '特征选择和变换', 'child': '特征提取'},
        {'regex': r'降维', 'parent': '特征提取', 'child': '降维'},
        {'regex': r'特征选择', 'parent': '特征选择和变换', 'child': '特征选择'},
        {'regex': r'维数灾难', 'parent': '特征选择', 'child': '维数灾难'},
        {'regex': r'聚类分析', 'parent': '模式识别', 'child': '聚类分析'},
        {'regex': r'K-均值算法', 'parent': '聚类分析', 'child': 'K-均值算法'},
        {'regex': r'层次聚类', 'parent': '聚类分析', 'child': '层次聚类'},
        {'regex': r'相似性测度', 'parent': '聚类分析', 'child': '相似性测度'}
    ]

    # 创建PDFTextExtractor实例并提取文本
    extractor = PDFTextExtractor(args.pdf_files)
    extractor.extract_text_from_pdfs()
    cleaned_text = extractor.get_cleaned_text()

    # 打印部分清理后的文本内容以供检查
    print(cleaned_text[:2000])  # 这里只打印前2000个字符以供检查

    # 创建KnowledgeGraphBuilder实例并构建知识图谱
    kg_builder = KnowledgeGraphBuilder(cleaned_text, knowledge_patterns)
    kg_builder.extract_knowledge_points()
    G = kg_builder.build_graph()
    kg_builder.draw_graph(G)
