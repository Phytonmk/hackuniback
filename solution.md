1.

2. K-Tetris.
`C := количество классов`
- Делим заказ на группы по `<= k`.
- Сортируем группы по приоритету `(deadline, amount * average_time)`.
- Храним `C` очередей `equipment e` с приоритетом по ключу `min(e.avaliable_to_start + k * e.poduction_time)`.
- Для каждой группы выбираем вершину минимальное по ключу оборудование `e` из всех очередей.
- Отправляем группу на выполнение на оборудовании `e`. Возвращаем `e` в очередь, изменяя `e.avaliable_to_start += group.size * e.production_time.