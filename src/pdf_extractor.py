# pdf_extractor.py

import fitz  # PyMuPDF
import re
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

class PDFTextExtractor:
    def __init__(self, pdf_paths):
        self.pdf_paths = pdf_paths
        self.raw_text = ""
        self.cleaned_text = ""
    
    def extract_text_from_pdfs(self):
        for pdf_path in self.pdf_paths:
            self.raw_text += self.extract_text_from_pdf(pdf_path) + "\n"
        self.cleaned_text = self.clean_text(self.raw_text)
    
    def extract_text_from_pdf(self, pdf_path):
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text")
        return text

    def clean_text(self, text):
        # 替换连续的多个换行符和空格为一个空格
        text = ' '.join(text.split())
        # 移除多余的空格和特殊字符
        text = re.sub(r'\s+', ' ', text)
        # 使用正则表达式来分割章节
        segments = re.split(r'华侨大学计算机学院', text)
        return '\n'.join(segments)

    def get_cleaned_text(self):
        return self.cleaned_text

class KnowledgeGraphBuilder:
    def __init__(self, text, knowledge_patterns):
        self.text = text
        self.knowledge_patterns = knowledge_patterns
        self.knowledge_points = []

    def extract_knowledge_points(self):
        for pattern in self.knowledge_patterns:
            matches = re.findall(pattern['regex'], self.text)
            for match in matches:
                parent = pattern['parent']
                child = match if pattern['child'] is None else pattern['child']
                self.knowledge_points.append((parent, child))

    def build_graph(self):
        G = nx.DiGraph()
        for kp in self.knowledge_points:
            G.add_edge(kp[0], kp[1])
        return G

    def draw_graph(self, G):
        # 设置中文字体
        font = FontProperties(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', size=14)
        plt.figure(figsize=(15, 10))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, edge_color='gray', linewidths=1, font_size=12, font_weight='bold', arrows=True, arrowstyle='-|>', arrowsize=20, font_family='sans-serif', fontproperties=font)
        plt.title("知识图谱", fontproperties=font)
        plt.show()
