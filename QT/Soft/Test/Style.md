以下是一些常用的 Qt 样式属性，适用于 QSS 文件中的控件样式设置：

### 通用样式属性

1. **background-color**: 设置背景颜色。
2. **background-image**: 设置背景图片。
3. **color**: 设置文本颜色。
4. **font-size**: 设置字体大小。
5. **font-family**: 设置字体类型。
6. **border**: 设置边框样式（如 `border: 1px solid black;`）。
7. **border-radius**: 设置边框圆角。
8. **padding**: 设置内边距。
9. **margin**: 设置外边距。
10. **opacity**: 设置透明度（0-1之间的值）。

### 控件特定样式

* **QPushButton**:
    
    * `border: none;`: 移除边框。
    * `padding: 5px;`: 设置按钮内边距。
* **QLineEdit**:
    
    * `background-color`: 设置输入框背景。
    * `border: 1px solid gray;`: 设置边框样式。
* **QComboBox**:
    
    * `QComboBox::drop-down`: 自定义下拉箭头样式。
* **QSlider**:
    
    * `QSlider::handle`: 自定义滑块样式。
* **QProgressBar**:
    
    * `QProgressBar::chunk`: 设置进度条的填充样式。
* **QLabel**:
    
    * `text-align`: 设置文本对齐方式。

### 状态样式

* : 鼠标悬停时的样式。
* : 被按下时的样式。
* : 被选中时的样式。

### 示例

```css
QPushButton {
    background-color: #0078d7; /* 默认背景色 */
    color: white;              /* 默认文字颜色 */
}

QPushButton:hover {
    background-color: #0056a3; /* 悬停时的背景色 */
}

QPushButton:pressed {
    background-color: #003f7f; /* 按下时的背景色 */
}

QPushButton:disabled {
    background-color: #cccccc; /* 禁用状态的背景色 */
    color: #666666;            /* 禁用状态的文字颜色 */
}

```