import unittest
import os
import sys
from PyQt5.QtWidgets import QApplication
from diff_tool import DiffTool

class TestDiffTool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 创建QApplication实例
        cls.app = QApplication(sys.argv)
        # 创建DiffTool实例
        cls.diff_tool = DiffTool()
        
    def test_file_loading(self):
        """测试文件加载功能"""
        # 获取测试文件路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sample1_path = os.path.join(current_dir, 'test_files', 'sample1.txt')
        sample2_path = os.path.join(current_dir, 'test_files', 'sample2.txt')
        
        # 确保测试文件存在
        self.assertTrue(os.path.exists(sample1_path), "测试文件1不存在")
        self.assertTrue(os.path.exists(sample2_path), "测试文件2不存在")
        
        # 模拟加载文件1
        with open(sample1_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.diff_tool.file1Content = content
        self.diff_tool.textEdit1.setPlainText(content)
        
        # 模拟加载文件2
        with open(sample2_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.diff_tool.file2Content = content
        self.diff_tool.textEdit2.setPlainText(content)
        
        # 验证文件内容已正确加载
        self.assertNotEqual(self.diff_tool.file1Content, "", "文件1内容未加载")
        self.assertNotEqual(self.diff_tool.file2Content, "", "文件2内容未加载")
    
    def test_diff_comparison(self):
        """测试差异比较功能"""
        # 设置简单的测试文本
        self.diff_tool.file1Content = "Line 1\nLine 2\nLine 3"
        self.diff_tool.file2Content = "Line 1\nModified Line\nLine 3"
        
        # 执行比较
        self.diff_tool.compareDiff()
        
        # 验证比较结果
        self.assertGreater(len(self.diff_tool.diffResults), 0, "未生成差异结果")
        
        # 检查是否有差异行
        has_diff = False
        for line in self.diff_tool.diffResults:
            if line.startswith('- ') or line.startswith('+ '):
                has_diff = True
                break
        
        self.assertTrue(has_diff, "未检测到差异行")

if __name__ == '__main__':
    unittest.main()
