from config.settings import check_settings, OUTPUT_DIR
from prompt_generator import generate_prompt
from image_generator import generate_image_with_ark
from utils.file_utils import save_json, save_image, generate_filename


def main():
    check_settings()

    user_input = input("请输入你的图像需求：").strip()
    if not user_input:
        print("输入不能为空。")
        return

    try:
        # 第一步：DeepSeek 生成结构化 prompt
        result = generate_prompt(user_input)

        print("\n生成结果：")
        print("-" * 50)
        print("main_prompt:")
        print(result.get("main_prompt", ""))

        print("\nnegative_prompt:")
        print(result.get("negative_prompt", ""))

        print("\nstyle:")
        print(result.get("style", ""))

        print("\naspect_ratio:")
        print(result.get("aspect_ratio", ""))

        print("\nchinese_summary:")
        print(result.get("chinese_summary", ""))

        # 保存 prompt 结果
        json_filename = generate_filename(prefix="prompt_result", ext=".json")
        json_path = save_json(result, OUTPUT_DIR, json_filename)
        print(f"\nPrompt 结果已保存到: {json_path}")

        # 第二步：拼接出图 prompt
        main_prompt = result.get("main_prompt", "").strip()
        negative_prompt = result.get("negative_prompt", "").strip()

        final_image_prompt = main_prompt
        if negative_prompt:
            final_image_prompt += f"\n\nNegative prompt: {negative_prompt}"

        print("\n正在调用火山方舟生成图片...")

        # 兼容模型返回像 "16:9" 或 "16:9 (landscape)" 这种格式
        aspect_ratio = result.get("aspect_ratio", "1:1").strip()
        if ":" in aspect_ratio:
            aspect_ratio = aspect_ratio.split()[0]
        else:
            aspect_ratio = "1:1"

        image_bytes = generate_image_with_ark(final_image_prompt, aspect_ratio)

        image_filename = generate_filename(
            prefix="generated_image", ext=".png")
        image_path = save_image(image_bytes, OUTPUT_DIR, image_filename)

        print(f"图片已保存到: {image_path}")

    except Exception as e:
        print(f"\n运行出错: {e}")


if __name__ == "__main__":
    main()
