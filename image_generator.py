import base64
from openai import OpenAI
from config.settings import ARK_API_KEY, ARK_BASE_URL, ARK_IMAGE_MODEL


def choose_image_size(aspect_ratio: str = "1:1") -> str:
    """
    根据比例返回 Seedream 可接受的尺寸
    这些尺寸满足较高像素要求，适合 5.0 模型
    """
    ratio_map = {
        "1:1": "2048x2048",
        "4:3": "2304x1728",
        "3:4": "1728x2304",
        "16:9": "2560x1440",
        "9:16": "1440x2560",
        "3:2": "2496x1664",
        "2:3": "1664x2496",
        "21:9": "3136x1344",
    }
    return ratio_map.get(aspect_ratio, "2048x2048")


def generate_image_with_ark(prompt: str, aspect_ratio: str = "1:1") -> bytes:
    """
    使用火山方舟 Seedream 生成图片
    """
    if not ARK_API_KEY:
        raise ValueError("ARK_API_KEY 未设置，请检查 .env")

    image_size = choose_image_size(aspect_ratio)

    print("\n调用火山方舟模型生成图片...")
    print("使用模型:", ARK_IMAGE_MODEL)
    print("使用尺寸:", image_size)

    client = OpenAI(
        api_key=ARK_API_KEY,
        base_url=ARK_BASE_URL,
    )

    result = client.images.generate(
        model=ARK_IMAGE_MODEL,
        prompt=prompt,
        size=image_size,
        response_format="b64_json",
    )

    if not result.data:
        raise RuntimeError("火山方舟未返回图片数据")

    image_base64 = result.data[0].b64_json
    return base64.b64decode(image_base64)
