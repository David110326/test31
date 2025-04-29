import fitz  # PyMuPDF

# 打开PDF文件
pdf_path = r'C:\Users\Administrator\Desktop\training\\my_test.pdf'
pdf_document = fitz.open(pdf_path)
# 指定保存图片的路径
output_folder = r'C:\Users\Administrator\Desktop\training\\'
name='case_1_'
# 遍历PDF的每一页
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    pix = page.get_pixmap()

    # 保存图片
    image_path = f"{output_folder}{name}page_{page_number + 1}.png"
    pix.save(image_path)

# 关闭PDF文档
pdf_document.close()