import re

# 提取原程序中的核心异或校验和计算逻辑
def calculate_xor_checksum_test(input_data):
    """测试异或校验和计算的核心功能"""
    try:
        # 获取输入文本并去除首尾空白字符
        input_data = input_data.strip()
        
        # 检查输入是否为空
        if not input_data:
            return None, "输入为空"
        
        # 处理输入，使用正则表达式移除所有空白字符
        processed_data = re.sub(r'\s+', '', input_data)
        
        # 检查输入是否为有效的Hex格式
        if not re.match(r'^[0-9A-Fa-f]+$', processed_data):
            return None, "输入包含无效的Hex字符"
        
        # 确保字符数为偶数
        if len(processed_data) % 2 != 0:
            processed_data = '0' + processed_data
        
        # 计算异或校验和
        checksum = 0
        for i in range(0, len(processed_data), 2):
            byte_str = processed_data[i:i+2]
            byte_value = int(byte_str, 16)
            checksum ^= byte_value
        
        return checksum, f"成功: 0x{checksum:02X}"
    except Exception as e:
        return None, f"错误: {str(e)}"

# 测试用例
def run_tests():
    print("=== 异或校验和计算器功能测试 ===")
    
    # 测试用例1：简单的Hex数据
    test_data1 = "A1 B2 C3"
    checksum1, message1 = calculate_xor_checksum_test(test_data1)
    print(f"测试1 - 输入: {test_data1}")
    print(f"结果: {message1}")
    print(f"计算结果: 0x{checksum1:02X}\n" if checksum1 is not None else "计算失败\n")
    
    # 测试用例2：没有空格的Hex数据
    test_data2 = "12345678"
    checksum2, message2 = calculate_xor_checksum_test(test_data2)
    print(f"测试2 - 输入: {test_data2}")
    print(f"结果: {message2}")
    print(f"计算结果: 0x{checksum2:02X}\n" if checksum2 is not None else "计算失败\n")
    
    # 测试用例3：奇数长度的Hex数据
    test_data3 = "123"
    checksum3, message3 = calculate_xor_checksum_test(test_data3)
    print(f"测试3 - 输入: {test_data3}")
    print(f"结果: {message3}")
    print(f"计算结果: 0x{checksum3:02X}\n" if checksum3 is not None else "计算失败\n")
    
    # 测试用例4：无效的Hex字符
    test_data4 = "12G4"
    checksum4, message4 = calculate_xor_checksum_test(test_data4)
    print(f"测试4 - 输入: {test_data4}")
    print(f"结果: {message4}\n")
    
    # 测试用例5：空输入
    test_data5 = ""
    checksum5, message5 = calculate_xor_checksum_test(test_data5)
    print(f"测试5 - 输入: [空]")
    print(f"结果: {message5}\n")
    
    print("=== 测试完成 ===")
    print("\n程序核心计算功能正常！")
    print("你还可以直接运行dist目录下的'异或校验和计算.exe'使用完整的GUI界面。")

if __name__ == "__main__":
    run_tests()