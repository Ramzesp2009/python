class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Створюємо рядки для кожного рівня Zigzag
        rows = [''] * numRows
        current_row = 0
        direction = -1  # 1 для вниз, -1 для вгору

        for char in s:
            rows[current_row] += char
            # Змінюємо напрямок, якщо досягнуто верхнього/нижнього рівня
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction

        # Об'єднуємо всі рядки в один
        return ''.join(rows)


# Перевірка
solution = Solution()
result_string = solution.convert('P', 3)
print(result_string)  # Очікуваний результат: "PAHNAPLSIIGYIR"
