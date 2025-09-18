# 导入必要的模块
import tkinter as tk                  # 导入tkinter库，用于创建GUI界面
from tkinter import ttk, messagebox   # 导入ttk模块（提供更现代的UI组件）和messagebox模块（用于显示消息对话框）
import re                             # 导入正则表达式模块，用于处理文本输入

class XORChecksumCalculator:
    """异或校验和计算器类"""
    
    def __init__(self, root):
        """构造函数，初始化GUI界面"""
        # 保存根窗口引用
        self.root = root
        # 设置窗口标题
        self.root.title("异或校验和计算器")
        # 设置窗口初始大小
        self.root.geometry("600x300")
        # 设置窗口可调整大小
        self.root.resizable(True, True)
        # 设置窗口最小尺寸，确保所有UI元素都能显示
        self.root.minsize(400, 300)
        
        # 设置中文字体支持
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("SimHei", 10))   # 设置标签字体
        self.style.configure("TButton", font=("SimHei", 10))  # 设置按钮字体
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # 配置根窗口的行列权重
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # 配置主框架的列和行的权重，使它们能够扩展
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)  # 输入框区域
        main_frame.grid_rowconfigure(1, weight=0)  # 按钮区域
        main_frame.grid_rowconfigure(2, weight=0)  # 结果区域
        
        # 初始化数据类型切换变量，默认为十六进制模式
        self.input_mode = tk.StringVar()
        self.input_mode.set("hex")  # hex 或 string
        
        # 创建输入部分
        input_frame = ttk.LabelFrame(main_frame, text="Hex数据输入", padding="10")
        input_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_rowconfigure(0, weight=1)
        
        # 创建多行文本输入框，用于输入Hex数据（不设置固定高度，让它随窗口调整）
        self.input_text = tk.Text(input_frame, font=("Courier New", 10))
        self.input_text.grid(row=0, column=0, sticky="nsew")
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(input_frame, command=self.input_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.input_text.config(yscrollcommand=scrollbar.set)
        
        # 创建按钮部分
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        button_frame.grid_columnconfigure(0, weight=1)
        
        # 在按钮框架内部使用pack布局是允许的，因为它是一个独立的容器
        # 创建计算按钮，点击时调用calculate_xor_checksum方法
        self.calculate_button = ttk.Button(button_frame, text="计算异或校验和", command=self.calculate_xor_checksum)
        self.calculate_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 创建清除按钮，点击时调用clear_input方法
        self.clear_button = ttk.Button(button_frame, text="清除", command=self.clear_input)
        self.clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 创建数据类型切换按钮，点击时调用toggle_input_mode方法
        self.mode_button = ttk.Button(button_frame, text="切换为字符串模式", command=self.toggle_input_mode)
        self.mode_button.pack(side=tk.LEFT)
        
        # 创建结果部分
        result_frame = ttk.LabelFrame(main_frame, text="计算结果", padding="10")
        result_frame.grid(row=2, column=0, sticky="nsew")
        result_frame.grid_columnconfigure(0, weight=1)
        
        # 创建字符串变量，用于存储和更新结果
        self.result_var = tk.StringVar()
        # 创建结果显示文本框（只读模式）
        self.result_entry = ttk.Entry(result_frame, textvariable=self.result_var, font=("Courier New", 10), state="readonly")
        self.result_entry.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        
        # 创建复制按钮，点击时调用copy_result方法
        self.copy_button = ttk.Button(result_frame, text="复制结果", command=self.copy_result)
        self.copy_button.grid(row=0, column=1, padx=(5, 0))
        
        # 添加状态栏，用于显示程序状态信息
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        # 使用grid布局代替pack，避免与主框架的grid布局冲突
        self.root.grid_rowconfigure(1, weight=0)
        status_bar.grid(row=1, column=0, sticky="ew")
        
    def toggle_input_mode(self):
        """切换输入模式（十六进制/字符串）"""
        if self.input_mode.get() == "hex":
            self.input_mode.set("string")
            self.mode_button.config(text="切换为十六进制模式")
            # 更新输入框标题
            parent = self.input_text.nametowidget(self.input_text.winfo_parent())
            parent.config(text="字符串输入")
            self.status_var.set("已切换到字符串输入模式")
        else:
            self.input_mode.set("hex")
            self.mode_button.config(text="切换为字符串模式")
            # 更新输入框标题
            parent = self.input_text.nametowidget(self.input_text.winfo_parent())
            parent.config(text="Hex数据输入")
            self.status_var.set("已切换到十六进制输入模式")
            
    def calculate_xor_checksum(self):
        """计算异或校验和的核心方法，同时格式化输入内容"""
        try:
            # 获取输入文本并去除首尾空白字符
            input_data = self.input_text.get("1.0", tk.END).strip()
            
            # 检查输入是否为空
            if not input_data:
                messagebox.showwarning("警告", "请输入" + ("Hex数据" if self.input_mode.get() == "hex" else "字符串"))
                return
            
            # 根据输入模式处理数据
            if self.input_mode.get() == "hex":
                # 处理输入，使用正则表达式移除所有空白字符（包括空格、制表符等）
                processed_data = re.sub(r'\s+', '', input_data)
                
                # 检查输入是否为有效的Hex格式（只能包含0-9, A-F, a-f）
                if not re.match(r'^[0-9A-Fa-f]+$', processed_data):
                    messagebox.showerror("错误", "输入包含无效的Hex字符")
                    return
                
                # 确保字符数为偶数（Hex数据通常是成对出现的）
                if len(processed_data) % 2 != 0:
                    processed_data = '0' + processed_data  # 在前面补0
                
                # 格式化输入内容：每两个字节之间添加一个空格
                formatted_data = ' '.join([processed_data[i:i+2] for i in range(0, len(processed_data), 2)])
                
                # 更新输入框显示格式化后的内容
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", formatted_data)
            else:
                # 字符串模式：将字符串转换为十六进制
                # 保存原始字符串
                original_string = input_data
                # 将字符串转换为字节，再转换为十六进制字符串
                try:
                    # 假设使用UTF-8编码转换字符串
                    byte_data = original_string.encode('utf-8')
                    # 转换为十六进制字符串
                    processed_data = ''.join([f"{b:02X}" for b in byte_data])
                    
                    # 格式化十六进制显示：每两个字符（一个字节）之间添加空格
                    formatted_hex = ' '.join([processed_data[i:i+2] for i in range(0, len(processed_data), 2)])
                    
                    # 更新输入框显示原始字符串和转换后的十六进制
                    self.input_text.delete("1.0", tk.END)
                    self.input_text.insert("1.0", f"原始字符串: {original_string}\n\n转换为Hex: {formatted_hex}")
                except Exception as e:
                    messagebox.showerror("错误", f"字符串转换为Hex时出错: {str(e)}")
                    return
                
            # 计算异或校验和的核心逻辑
            checksum = 0
            # 每次取两个字符（一个字节）进行处理
            for i in range(0, len(processed_data), 2):
                byte_str = processed_data[i:i+2]  # 获取一个字节的Hex字符串
                byte_value = int(byte_str, 16)    # 转换为十进制数值
                checksum ^= byte_value            # 与当前校验和进行异或运算
            
            # 显示计算结果，格式为十六进制（0x前缀，两位数字）
            self.result_var.set(f"0x{checksum:02X}")
            # 更新状态栏信息
            mode_text = "十六进制" if self.input_mode.get() == "hex" else "字符串（UTF-8编码）"
            self.status_var.set(f"成功计算{mode_text}异或校验和: 0x{checksum:02X}")
            
        # 捕获并处理所有可能出现的异常
        except Exception as e:
            messagebox.showerror("错误", f"计算过程中发生错误: {str(e)}")
            self.status_var.set("计算失败")
    
    def clear_input(self):
        """清除输入文本和结果的方法"""
        self.input_text.delete("1.0", tk.END)  # 清空输入文本框
        self.result_var.set("")                # 清空结果文本框
        self.status_var.set("已清除")           # 更新状态栏信息
    
    def copy_result(self):
        """复制计算结果到剪贴板的方法"""
        result = self.result_var.get()  # 获取当前计算结果
        
        # 检查是否有结果可复制
        if result:
            self.root.clipboard_clear()          # 清空剪贴板
            self.root.clipboard_append(result)   # 将结果复制到剪贴板
            self.status_var.set("结果已复制到剪贴板")  # 更新状态栏信息
        else:
            messagebox.showinfo("提示", "没有可复制的结果")  # 提示用户没有结果可复制

# 程序入口点
if __name__ == "__main__":
    root = tk.Tk()                       # 创建根窗口对象
    app = XORChecksumCalculator(root)    # 创建并初始化异或校验和计算器应用实例
    root.mainloop()                      # 启动Tkinter主事件循环，显示窗口并处理用户交互