import os
import re
from google import genai

# Khởi tạo Client từ API Key lưu trong GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def call_gemini(prompt):
    system_instruction = (
        "Đóng vai kỹ sư tự động hóa đang làm đồ án Điều khiển hệ thống điện công nghiệp. "
        "Hãy viết nội dung chuyên môn chi tiết cho yêu cầu sau (viết bằng tiếng Việt, giữ nguyên công thức LaTeX): "
    )
    
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"{system_instruction}{prompt}"
    )
    return response.text.strip()

def process_document():
    if not os.path.exists("dan_y.md"):
        print("Không tìm thấy file dan_y.md")
        return

    with open("dan_y.md", "r", encoding="utf-8") as f:
        content = f.read()

    matches = re.findall(r'\[GEMINI:\s*(.*?)\]', content)
    
    for prompt in matches:
        print(f"Đang xử lý prompt: {prompt[:30]}...")
        generated_text = call_gemini(prompt)
        placeholder = f"[GEMINI: {prompt}]"
        content = content.replace(placeholder, generated_text)

    with open("hoan_thien.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Đã tạo xong file hoan_thien.md!")

if __name__ == "__main__":
    process_document()
