# Существует агрегатор новостей, который собирает новости со всех порталов и формирует ленту. 
# Новости (NewsItem) представляют собой класс из 2 полей, текст новости - поле text (в нашей задаче не важен) и ее источник - source. 
# Например: "Интерфакс", "Эхо Москвы", "Радио Радонеж", список источников заранее неизвестен.

# Для того, чтобы лента новостей не выглядела однообразной — было реализовано правило: 
# не должно быть новостей из одного и того же источника ближе чем через 10 позиций от новости такого же источника.  
# Необходимо проверить, соответствует ли сортировка заданному правилу.
# Ничего считать и выводить не нужно, если на протяжении массива встречается хотя бы одна пара новостей на расстоянии ближе 10 пунктов - падаем.
# Для простоты обрезаем все зависимости, у нас есть тестовый метод, в который приходит лист(массив) источников новостей,
# внутри этого метода и должна происходить проверка.

