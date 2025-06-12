import sys
import difflib
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, 
                            QPushButton, QVBoxLayout, QHBoxLayout, 
                            QWidget, QFileDialog, QLabel, QSplitter,
                            QShortcut, QToolBar, QAction, QStatusBar)
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QKeySequence, QIcon
from PyQt5.QtCore import Qt, QSize

class DiffTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('文本差异比较工具')
        self.setGeometry(100, 100, 1200, 800)
        
        # 创建主窗口部件
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        
        # 创建布局
        mainLayout = QVBoxLayout()
        fileSelectionLayout = QHBoxLayout()
        
        # 创建工具栏
        toolbar = QToolBar("主工具栏")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        # 添加工具栏按钮
        openFile1Action = QAction("打开文件1", self)
        openFile1Action.triggered.connect(lambda: self.openFile(1))
        toolbar.addAction(openFile1Action)
        
        openFile2Action = QAction("打开文件2", self)
        openFile2Action.triggered.connect(lambda: self.openFile(2))
        toolbar.addAction(openFile2Action)
        
        toolbar.addSeparator()
        
        compareAction = QAction("比较差异", self)
        compareAction.triggered.connect(self.compareDiff)
        toolbar.addAction(compareAction)
        
        nextDiffAction = QAction("下一个差异", self)
        nextDiffAction.triggered.connect(self.nextDiff)
        toolbar.addAction(nextDiffAction)
        
        prevDiffAction = QAction("上一个差异", self)
        prevDiffAction.triggered.connect(self.prevDiff)
        toolbar.addAction(prevDiffAction)
        
        # 文件选择按钮
        self.file1Button = QPushButton('选择文件1')
        self.file2Button = QPushButton('选择文件2')
        self.file1Label = QLabel('未选择文件')
        self.file2Label = QLabel('未选择文件')
        
        fileSelectionLayout.addWidget(self.file1Button)
        fileSelectionLayout.addWidget(self.file1Label)
        fileSelectionLayout.addWidget(self.file2Button)
        fileSelectionLayout.addWidget(self.file2Label)
        
        # 创建分割器
        splitter = QSplitter(Qt.Horizontal)
        
        # 文本编辑区
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()
        self.textEdit1.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit2.setLineWrapMode(QTextEdit.NoWrap)
        
        # 设置等宽字体
        font = QFont("Courier New", 10)
        self.textEdit1.setFont(font)
        self.textEdit2.setFont(font)
        
        # 添加到分割器
        splitter.addWidget(self.textEdit1)
        splitter.addWidget(self.textEdit2)
        
        # 比较按钮
        self.compareButton = QPushButton('比较差异')
        
        # 添加布局
        mainLayout.addLayout(fileSelectionLayout)
        mainLayout.addWidget(splitter)
        mainLayout.addWidget(self.compareButton)
        mainWidget.setLayout(mainLayout)
        
        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('准备就绪')
        
        # 连接信号和槽
        self.file1Button.clicked.connect(lambda: self.openFile(1))
        self.file2Button.clicked.connect(lambda: self.openFile(2))
        self.compareButton.clicked.connect(self.compareDiff)
        
        # 添加快捷键
        QShortcut(QKeySequence("Ctrl+O"), self, lambda: self.openFile(1))
        QShortcut(QKeySequence("Ctrl+P"), self, lambda: self.openFile(2))
        QShortcut(QKeySequence("Ctrl+D"), self, self.compareDiff)
        QShortcut(QKeySequence("F3"), self, self.nextDiff)
        QShortcut(QKeySequence("Shift+F3"), self, self.prevDiff)
        
        self.file1Content = ""
        self.file2Content = ""
        self.diffResults = []
        self.currentDiffIndex = -1
        
    def openFile(self, fileNum):
        fileName, _ = QFileDialog.getOpenFileName(self, f"选择文件 {fileNum}", "", "文本文件 (*.txt);;所有文件 (*)")
        
        if fileName:
            try:
                with open(fileName, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if fileNum == 1:
                    self.file1Content = content
                    self.textEdit1.setPlainText(content)
                    self.file1Label.setText(fileName.split('/')[-1])
                    self.statusBar.showMessage(f'已加载文件1: {fileName}')
                else:
                    self.file2Content = content
                    self.textEdit2.setPlainText(content)
                    self.file2Label.setText(fileName.split('/')[-1])
                    self.statusBar.showMessage(f'已加载文件2: {fileName}')
            except Exception as e:
                self.statusBar.showMessage(f"打开文件时出错: {e}")
    
    def compareDiff(self):
        if not self.file1Content or not self.file2Content:
            self.statusBar.showMessage('请先选择两个文件')
            return
            
        # 清除之前的格式
        self.textEdit1.setPlainText(self.file1Content)
        self.textEdit2.setPlainText(self.file2Content)
        
        # 获取文本行
        text1_lines = self.file1Content.splitlines()
        text2_lines = self.file2Content.splitlines()
        
        # 使用difflib比较差异
        d = difflib.Differ()
        self.diffResults = list(d.compare(text1_lines, text2_lines))
        
        # 高亮显示差异
        cursor1 = self.textEdit1.textCursor()
        cursor2 = self.textEdit2.textCursor()
        
        format_add = QTextCharFormat()
        format_add.setBackground(QColor(144, 238, 144))  # 浅绿色
        
        format_delete = QTextCharFormat()
        format_delete.setBackground(QColor(255, 182, 193))  # 浅红色
        
        format_change = QTextCharFormat()
        format_change.setBackground(QColor(255, 255, 153))  # 浅黄色
        
        line_idx1 = 0
        line_idx2 = 0
        
        diff_count = 0
        
        for line in self.diffResults:
            if line.startswith('  '):  # 相同行
                line_idx1 += 1
                line_idx2 += 1
            elif line.startswith('- '):  # 在文件1中但不在文件2中
                cursor1.setPosition(self.textEdit1.document().findBlockByLineNumber(line_idx1).position())
                cursor1.movePosition(cursor1.EndOfBlock, cursor1.KeepAnchor)
                cursor1.setCharFormat(format_delete)
                line_idx1 += 1
                diff_count += 1
            elif line.startswith('+ '):  # 在文件2中但不在文件1中
                cursor2.setPosition(self.textEdit2.document().findBlockByLineNumber(line_idx2).position())
                cursor2.movePosition(cursor2.EndOfBlock, cursor2.KeepAnchor)
                cursor2.setCharFormat(format_add)
                line_idx2 += 1
                diff_count += 1
            elif line.startswith('? '):  # 指示变化的位置
                continue
        
        self.statusBar.showMessage(f'比较完成，发现 {diff_count} 处差异')
        self.currentDiffIndex = -1
    
    def nextDiff(self):
        if not self.diffResults:
            return
            
        line_idx1 = 0
        line_idx2 = 0
        
        # 找到下一个差异
        found = False
        for i, line in enumerate(self.diffResults):
            if i <= self.currentDiffIndex:
                if line.startswith('  '):  # 相同行
                    line_idx1 += 1
                    line_idx2 += 1
                elif line.startswith('- '):  # 在文件1中但不在文件2中
                    line_idx1 += 1
                elif line.startswith('+ '):  # 在文件2中但不在文件1中
                    line_idx2 += 1
                continue
                
            if line.startswith('- '):  # 在文件1中但不在文件2中
                # 滚动到差异位置
                block = self.textEdit1.document().findBlockByLineNumber(line_idx1)
                cursor = self.textEdit1.textCursor()
                cursor.setPosition(block.position())
                self.textEdit1.setTextCursor(cursor)
                self.textEdit1.ensureCursorVisible()
                line_idx1 += 1
                found = True
                self.currentDiffIndex = i
                break
            elif line.startswith('+ '):  # 在文件2中但不在文件1中
                # 滚动到差异位置
                block = self.textEdit2.document().findBlockByLineNumber(line_idx2)
                cursor = self.textEdit2.textCursor()
                cursor.setPosition(block.position())
                self.textEdit2.setTextCursor(cursor)
                self.textEdit2.ensureCursorVisible()
                line_idx2 += 1
                found = True
                self.currentDiffIndex = i
                break
            elif line.startswith('  '):  # 相同行
                line_idx1 += 1
                line_idx2 += 1
        
        if not found:
            self.currentDiffIndex = -1
            self.statusBar.showMessage('已到达最后一个差异')
    
    def prevDiff(self):
        if not self.diffResults:
            return
            
        # 从当前位置向前查找差异
        prev_diff_indices = []
        line_idx1 = 0
        line_idx2 = 0
        
        for i, line in enumerate(self.diffResults):
            if i >= self.currentDiffIndex and self.currentDiffIndex != -1:
                break
                
            if line.startswith('- ') or line.startswith('+ '):
                prev_diff_indices.append((i, line_idx1 if line.startswith('- ') else line_idx2))
                
            if line.startswith('  '):  # 相同行
                line_idx1 += 1
                line_idx2 += 1
            elif line.startswith('- '):  # 在文件1中但不在文件2中
                line_idx1 += 1
            elif line.startswith('+ '):  # 在文件2中但不在文件1中
                line_idx2 += 1
        
        if prev_diff_indices:
            last_diff = prev_diff_indices[-1]
            self.currentDiffIndex = last_diff[0]
            
            if self.diffResults[last_diff[0]].startswith('- '):
                block = self.textEdit1.document().findBlockByLineNumber(last_diff[1])
                cursor = self.textEdit1.textCursor()
                cursor.setPosition(block.position())
                self.textEdit1.setTextCursor(cursor)
                self.textEdit1.ensureCursorVisible()
            else:
                block = self.textEdit2.document().findBlockByLineNumber(last_diff[1])
                cursor = self.textEdit2.textCursor()
                cursor.setPosition(block.position())
                self.textEdit2.setTextCursor(cursor)
                self.textEdit2.ensureCursorVisible()
        else:
            self.statusBar.showMessage('已到达第一个差异')

def main():
    app = QApplication(sys.argv)
    ex = DiffTool()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
