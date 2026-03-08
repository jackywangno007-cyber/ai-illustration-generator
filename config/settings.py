import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"

ARK_API_KEY = os.getenv("ARK_API_KEY")
ARK_BASE_URL = os.getenv(
    "ARK_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3")
ARK_IMAGE_MODEL = os.getenv("ARK_IMAGE_MODEL", "doubao-seedream-5-0-260128")

OUTPUT_DIR = "outputs"


def check_settings():
    if not DEEPSEEK_API_KEY:
        raise ValueError("DEEPSEEK_API_KEY 未设置，请检查 .env 文件")
    if not ARK_API_KEY:
        raise ValueError("ARK_API_KEY 未设置，请检查 .env 文件")

    print("\n===== AI Pipeline Config =====")
    print("DeepSeek Model:", DEEPSEEK_MODEL)
    print("Ark Image Model:", ARK_IMAGE_MODEL)
    print("Ark Base URL:", ARK_BASE_URL)
    print("================================\n")
