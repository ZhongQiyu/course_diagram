
# 项目简介 | Project Overview

这是一个多模态对话系统与异常检测的综合项目，涵盖了 NLP、GAN、RL、代理系统等技术。主要关注日语和中文语言模型的创新，目标是为学术会议（如 EMNLP、COLING、IJCAI、ICME）提交论文。

This is a comprehensive project combining multimodal dialogue systems and anomaly detection, covering technologies such as NLP, GAN, RL, and agent systems. The focus is on innovations in Japanese and Chinese language models, aiming to submit papers to academic conferences like EMNLP, COLING, IJCAI, and ICME.

---

## 数据准备与改进建议 | Data Preparation and Improvement Suggestions

### 1. 数据分布评估 | Data Distribution Evaluation
虽然进行了噪声清洗和数据增强，但仍存在标签不均衡的问题，建议使用标签平衡策略。
Although noise cleaning and data augmentation were performed, the label imbalance issue remains. It is recommended to use label-balancing strategies.

### 2. 标签一致性 | Label Consistency
增加一致性检查步骤，确保人工标注与原始数据的一致性。
Introduce consistency check steps to ensure manual annotations align with the original data.

---

## 相关文献总结 | Literature Review

### a. EmoLLM 工作概述 | EmoLLM Overview
EmoLLM 利用多模态情感数据提高语言模型的情感理解能力。
EmoLLM leverages multimodal emotional data to improve language model emotional understanding.

### b. CPsyCoun 框架概述 | CPsyCoun Framework Overview
CPsyCoun 是为中文心理咨询对话设计的多轮对话生成框架。
CPsyCoun is a multi-turn dialogue generation framework designed for Chinese psychological counseling conversations.

### c. EVA 论文摘要 | EVA Paper Abstract
EVA 是一个大型中文开放领域对话系统，通过数据清洗与 Transformer 架构实现高效对话生成。
EVA is a large-scale Chinese open-domain dialogue system that uses data cleaning and Transformer architecture to generate efficient dialogues.

---

## QLora 数据格式示例 | QLora Data Format Example

```json
{
    "episode": 1,
    "scene": "学校",
    "dialogue": [
        {
            "turn": 1,
            "speaker": "A",
            "text": "今日はどうしたの？",
            "timestamp": "00:01:23",
            "context": "A进入教室，看到B看起来有些不开心。",
            "emotion": "concerned"
        },
        {
            "turn": 2,
            "speaker": "B",
            "text": "ちょっと疲れたんだ。",
            "timestamp": "00:01:30",
            "context": "A刚问了B。",
            "emotion": "tired"
        }
    ]
}
```

---

## 视频转文本任务设置 | Video-to-Text Task Setup

```json
{
    "scene_id": "episode1_scene10",
    "timestamp_start": "00:10:23",
    "timestamp_end": "00:15:45",
    "dialogue": [
        {
            "speaker": "角色A",
            "role_info": {
                "personality": "乐观开朗",
                "background": "来自东京的大学生"
            },
            "text": "今日はいい天気ですね。",
            "timestamp": "00:10:23"
        },
        {
            "speaker": "角色B",
            "role_info": {
                "personality": "认真严格",
                "background": "高校教师"
            },
            "text": "そうですね、でも私は今日は家で仕事があります。",
            "timestamp": "00:10:35"
        },
        {
            "speaker": "角色A",
            "role_info": {
                "personality": "乐观开朗",
                "background": "来自东京的大学生"
            },
            "text": "それは残念です。",
            "timestamp": "00:10:50"
        }
    ]
}
```

---

## Anomaly Detection Pipeline

### 1. 数据分析 | Data Analysis
加载多变量时间序列数据，使用 Matplotlib 或 Seaborn 进行可视化分析。
Load multivariate time series data and perform visual analysis using Matplotlib or Seaborn.

### 2. 数据增强与模型 | Data Augmentation and Model
- **数据增强**: 使用随机掩码扩展输入空间。
- **生成器与判别器**: 使用基于 Transformer 的自编码器和 GAN 进行模式重建。
- **对比学习**: 强化对比学习以提升模型泛化能力。

- **Data Augmentation**: Use random masks to extend the input space.
- **Generator & Discriminator**: Use a Transformer-based autoencoder and GAN for pattern reconstruction.
- **Contrastive Learning**: Apply contrastive learning to enhance model generalization.

### 3. 异常检测模型扩展 | Anomaly Detection Model Extensions
- **PCA**, **One-Class SVM**, **Isolation Forest**, **DBSCAN** 等模型的扩展和实验。
Extend models like PCA, One-Class SVM, Isolation Forest, and DBSCAN for anomaly detection.

### 4. 实证分析 | Empirical Analysis
对不同模型进行 F1 Score、时间、AUC 分析。
Analyze models based on F1 Score, Time, and AUC.

---

## 实时互动与多模态体验示例 | Real-Time Interaction and Multimodal Experience Examples

### 1. BLACKPINK 实时互动平台 | BLACKPINK Real-Time Interaction Platforms
通过 NLP 与实时视频处理技术开发明星互动平台。
Develop platforms for celebrity interaction using NLP and real-time video processing technologies.

### 2. 内容创作与社交媒体 | Content Creation and Social Media
创建短视频编辑和内容推荐工具，帮助优化社交媒体上的内容发布。
Create short video editing and content recommendation tools to optimize content publishing on social media.

### 3. 虚拟偶像与元宇宙游戏 | Virtual Idols and Metaverse Games
开发虚拟偶像互动平台或沉浸式游戏环境，带来全新互动体验。
Develop virtual idol interaction platforms or immersive game environments to bring new interaction experiences.

---

## 配置 Jan.AI Token | Configure Jan.AI Token

1. 注册 Jan.AI 平台并获取 API token。
2. 设置 token 为环境变量：
   ```bash
   export JANAI_TOKEN=your_token_here
   ```
3. 在 `config.py` 中配置：
   ```python
   JANAI_TOKEN = os.getenv("JANAI_TOKEN")
   ```

---

## 未来工作与项目优化 | Future Work and Project Optimization

1. 探索数据增强方法以提升模型的泛化能力。
2. 继续完善多模态对话系统，优化不同语言模型的对话生成效果。

1. Explore data augmentation methods to improve model generalization.
2. Continue improving the multimodal dialogue system, optimizing dialogue generation for different language models.
