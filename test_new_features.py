import tkinter as tk
from tkinter import messagebox
import sys
import os

# 添加数据类型切换功能的测试
def test_data_type_switching():
    """测试异或校验和计算器的数据类型切换功能"""
    print("=== 异或校验和计算器新功能测试 ===")
    print("[功能介绍]")
    print("1. 已添加数据类型切换功能，支持十六进制和字符串两种输入模式")
    print("2. 通过点击\"切换为字符串模式\"按钮可以切换输入类型")
    print("3. 在字符串模式下，输入的字符串会自动转换为UTF-8编码的十六进制数据再计算")
    print("4. 切换模式时，输入框标题和按钮文本会相应更新")
    print("5. 计算结果会显示当前使用的输入模式")
    
    print("\n[测试用例建议]")
    print("1. 十六进制模式测试:")
    print("   - 输入: A1 B2 C3")
    print("   - 预期输出: 0xD0")
    print("   - 输入会自动格式化为每两个字符一组，用空格分隔")
    
    print("\n2. 字符串模式测试:")
    print("   - 输入: Hello世界")
    print("   - 预期处理: 自动转换为UTF-8编码的十六进制数据(48 65 6C 6C 6F E4 B8 96 E7 95 8C)")
    print("   - 输入框会显示原始字符串和转换后的十六进制值")
    
    print("\n[注意事项]")
    print("- 请确保您的Python环境已安装tkinter库")
    print("- 字符串模式使用UTF-8编码进行转换")
    print("- 状态栏会显示当前的输入模式和计算状态")
    
    # 提示用户运行主程序进行测试
    print("\n=== 测试完成 ===")
    print("\n请运行 xor_checksum_calculator.py 来体验新功能！")
    print("或者您可以重新打包程序为可执行文件，命令如下：")
    print("  pyinstaller --onefile --windowed --icon=xor3.ico xor_checksum_calculator.py")
    
    # 创建一个简单的对话框提示用户
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo("功能已更新", 
        "异或校验和计算器已添加数据类型切换功能！\n\n" +
        "1. 点击\"切换为字符串模式\"按钮可以在两种模式间切换\n" +
        "2. 在字符串模式下，输入的字符串会自动转换为UTF-8编码的十六进制数据\n" +
        "3. 输入框标题会随模式变化而更新\n\n" +
        "请运行主程序体验新功能！")
    root.destroy()

if __name__ == "__main__":
    test_data_type_switching()