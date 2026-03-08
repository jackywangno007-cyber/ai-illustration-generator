# 🎨 AI 图像生成工具（AI Illustration Generator）

一个基于 **Python + 多模型 AI Pipeline** 的图像生成项目。
该项目可以将用户的自然语言描述转换为高质量图像，实现从 **文本 → Prompt → 图像生成** 的完整 AI 工作流。

本项目结合了 **大语言模型（DeepSeek）** 和 **图像生成模型（Doubao Seedream）**，用于展示如何构建一个完整的 AI 应用。

---

# ✨ 项目功能

* 🧠 使用 **DeepSeek LLM** 自动生成高质量 Prompt
* 🎨 使用 **Doubao Seedream** 生成高分辨率图像
* 📝 自动生成结构化 Prompt（JSON）
* 📐 自动适配图像比例（aspect ratio）
* 💾 自动保存 Prompt 和生成图像
* 🔐 使用 `.env` 管理 API Key

---

# 🧠 系统架构

```text
用户输入（中文描述）
        ↓
DeepSeek LLM
（Prompt Engineering）
        ↓
结构化 Prompt
(main_prompt / negative_prompt / style)
        ↓
Doubao Seedream 图像生成模型
        ↓
生成高分辨率图片
```

---

# 📂 项目结构

```text
ai-illustration-generator
│
├── config
│   └── settings.py            # 项目配置
│
├── prompts
│   └── prompt_examples.md     # Prompt 示例
│
├── utils
│   └── file_utils.py          # 文件处理工具
│
├── outputs_example            # 示例输出图片
│
├── app.py                     # 主程序入口
├── image_generator.py         # 图像生成模块
├── prompt_generator.py        # Prompt生成模块
├── prompt_builder.py          # Prompt构建逻辑
│
├── requirements.txt           # 项目依赖
├── README.md
├── .env.example               # 环境变量示例
└── .gitignore
```

---

# ⚙️ 安装方法

## 1 克隆项目

```bash
git clone https://github.com/jackywangno007-cyber/ai-illustration-generator.git
cd ai-illustration-generator
```

---

## 2 创建虚拟环境

```bash
python -m venv venv
```

Windows 激活：

```bash
venv\Scripts\activate
```

---

## 3 安装依赖

```bash
pip install -r requirements.txt
```

---

# 🔑 环境变量配置

复制 `.env.example` 并创建 `.env`

```text
DEEPSEEK_API_KEY=your_deepseek_api_key

ARK_API_KEY=your_ark_api_key
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3

ARK_IMAGE_MODEL=doubao-seedream-5-0-260128
```

---

# ▶️ 运行项目

```bash
python app.py
```

输入示例：

```text
画一张兰州黄河铁桥的照片
```

程序运行后会自动完成以下流程：

1. 生成结构化 Prompt
2. 调用图像生成模型
3. 输出高分辨率图片
4. 保存 Prompt JSON 和生成图片

---

# 🖼 示例生成图片

示例生成图像：

![示例图片](outputs_example/example_bridge.png)

---

# 🧩 技术栈

* Python
* DeepSeek API
* Doubao Seedream 图像生成模型
* Prompt Engineering
* REST API 集成

---

# 📖 项目学习目标

本项目主要用于实践：

* LLM Prompt Engineering
* 多模型 AI Pipeline 架构
* AI 图像生成 API 集成
* Python AI 应用开发

---

# 🚀 未来改进方向

后续可以扩展：

* Web UI（Streamlit / Gradio）
* 批量生成图片
* Prompt 风格模板（动漫 / 水彩 / 写实）
* 图片浏览界面
* 多图生成

---

# 👨‍💻 作者

**Jacky Wang**

GitHub：
https://github.com/jackywangno007-cyber
