## Задача. 
### Игра крестики - нолики
------
bot 
---
1. принимает список адресов с пустыми ячейками после перемешивания. На первом ходу берёт пустую ячейку и ставит item

2. Далее берёт список адресов тех ячеек, где содержится bot_item и от этой ячейки проверяет соседние ячейки, чтобы поставить item.

    2.1 Логика бота не идеальная, можно было просто использовать случайные ячейки, на игре было бы то же самое, но я пытался сделать боту ии.
---
game 
---
3. init_items Выбор пользователю x или 0, и назначение боту item.

4. de_coder_bot_msg принимает адрес ячейки от бота, и возвращает цифру.

5. check_cell проверяет занята ли ячейка.

6. check_winner проверяет условие для победы

7. check_tie проверяет условие для ничьи
