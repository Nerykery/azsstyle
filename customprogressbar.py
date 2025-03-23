from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush
from PySide6.QtCore import Qt, QRectF


class CustomProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0  # Значение прогресса (0-100)

    def setValue(self, value):
        """Обновляет значение и перерисовывает виджет"""
        self.value = max(0, min(100, value))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Размеры
        size = min(self.width(), self.height()) - 10
        center_x = self.width() / 2
        center_y = self.height() / 2
        rect = QRectF(center_x - size / 2, center_y - size / 2, size, size)

        # Фон (серый круг)
        painter.setBrush(QBrush(Qt.GlobalColor.lightGray))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(rect)

        # Линии разметки
        pen = QPen(Qt.GlobalColor.darkGray, 2)
        painter.setPen(pen)
        lines = [
            ((center_x, center_y - size / 2), (center_x, center_y - size / 4)),
            ((center_x - size / 4, center_y - size / 2 + 5), (center_x + size / 4, center_y - size / 2 + 5)),
            ((center_x - size / 4, center_y - size / 2 + 12), (center_x + size / 4, center_y - size / 2 + 12)),
            ((center_x + size / 4, center_y - size / 2), (center_x + size / 4, center_y - size / 4)),
            ((center_x - size / 4, center_y - size / 2), (center_x - size / 4, center_y - size / 4)),
            ((center_x + size / 3, center_y - size / 2 + 5), (center_x + size / 3, center_y - size / 3)),
            ((center_x - size / 3, center_y - size / 2 + 5), (center_x - size / 3, center_y - size / 3)),
        ]
        for start, end in lines:
            painter.drawLine(*start, *end)

        # Отрисовка прогресса (черный сектор)
        if self.value > 0:
            painter.setBrush(QBrush(Qt.GlobalColor.black))
            span_angle = int(-360 * (self.value / 100))
            painter.drawPie(rect, 90 * 16, span_angle * 16)
