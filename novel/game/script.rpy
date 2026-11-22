# Сценарий игры распологается в этом файле.

default all_score = 0
default vlad_score = 0
default ev_score = 0
default maks_score = 0
default grig_score = 0

define e = Character("Владимир Иванович", color="#1d1c1c")
define ee = Character("Евгений Георгиевич", color="#384473")
define eee = Character("Максим Дмитриевич", color="#23873e")
default dif = 0
default player_name = "Игрок"
define you = Character("[player_name]", color="#c61313")
define grig = Character("Григорий Яковлевич", color="#20d0d0")
define company_rep = Character("Представитель компании", color="#73ef15")
define schoolboy = Character("Школьник", color="#ff009d")
define research_lead = Character("Руководитель исследования", color="#0400eb")


# Игра начинается здесь.

label start:

   
    menu:
        "Выберите уровень сложности миниигр."
        "Лёгкий.":
            $ dif = 1
        "Средний":
            $ dif = 2
        "Сложный":
            $ dif = 3

    
    "..."

    scene black with Dissolve(3)
    python:
        
        player_name = renpy.input("Введите ваше имя:", default="Алексей", length=20)
        player_name = player_name.strip()

        
        if not player_name:
            player_name = "Игрок"
    "Кажется, ещё недавно я поступал на прикладную математику, толком не представляя, чем хочу заниматься после университета. "
    "За бакалавриат успел привыкнуть к бесконечным лекциям, дедлайнам и даже находил время на жизнь."
    "Математика всегда давалась мне легче многих других вещей."
    "В магистратуре я решил углубиться в теорию вероятностей и математическую статистику. "
    "Постепенно интересы вышли за рамки чистой математики: диплом я посвятил статистическому анализу факторов, определяющих спрос на товары повседневного потребления."
    "Сейчас я заканчиваю магистратуру." 
    "До защиты осталось меньше месяца." 
    "А вот с планами на будущее всё куда менее определённо." 
    "И это начинает слегка давить."

    scene koridor with Dissolve(2)
    "Первая пара. Современные методы статистики..."
    scene lecauditory with Dissolve(2)
    "Прохлада утренней лекционной и спокойный голос Владимира Ивановича постепенно возвращают меня к привычному ритму."
    "В аудитории — сонные студенты, которые пытаются осознать очередной ворох информации. Получается, конечно, далеко не у всех."

    show vladimir with dissolve:
        xalign 0.5 yalign 1.2

    e "— Коллеги, советую подружиться со статистикой. "
    e "В умелых руках этот инструмент позволяет делать открытия."
    e "В неумелых — превращается в оружие софиста."
    e "Разница иногда в одном неверно выбранном критерии."

    "Несколько человек усмехаются. Владимир Иванович продолжает, почти не отвлекаясь на реакцию."
    "Наконец лекция заканчивается, поэтому я подхожу к преподавателю."

    you "— Владимир Иванович, как вам мой черновик?"

    "Он быстро пробегает глазами по страницам."

    e "— Расчёты чистые, с выборкой порядок. Экономическую часть комментировать не буду — не мой профиль. Но математическая основа нормальная."

    "Отложив записи для прошедшей лекции, Владимир Иванович достаёт стопку исписанной бумаги."

    e "— Кстати, завтра буду проверять студенческие работы. Одному муторно."
    e "Если будет час-полтора — загляни. Руку набьёшь. "
    e "Только не обещай, если не уверен, что придёшь."

    you "Нет, всё нормально, у меня будет свободное время."

    "Попрощавшись с Владимиром Ивановичем, я отправляюсь на вторую пару."

    scene koridor with Fade(1.5, 1.0, 1.5)

    "Вот и вторая пара. Методы оптимизации."

    scene lecauditory with Fade (1.5, 1.0, 1.5)

    show evgeniy with dissolve
    "На лекциях Евгения Георгиевича всегда немного другая атмосфера."
    "Утончённый стиль, дорогие часы и периодические взгляды в телефон выдают человека, у которого наука — далеко не единственный интерес."
    "Сегодня разбираем задачу оптимального распределения ресурсов. Вроде бы всё знакомо: ограничения, целевая функция. Но Евгений Георгиевич смотрит на неё прежде всего с прикладной стороны."
    "После пары он окликает меня:"

    ee "— [player_name], на минуту. Я помню вашу дипломную. Есть у меня одно исследование на смежную тему. Возьмите, посмотрите."
    ee  "Там есть пара любопытных мест… и пара сомнительных. Будет полезно понять, где именно сомнительных."

    "Он передаёт несколько распечатанных страниц, кивает и покидает аудиторию."

    scene compauditory with Fade (1.5, 1.0, 1.5)

    "Вот и третья пара. Самая сложная и самая интересная - Методы машинного обучения."
    "Хотя у Максима Дмитриевича и тяжело, но у него всегда стопроцентная посещаемость."

    show maksim with dissolve

    "Его занятия наполнены вопросами к аудитории, лёгкими шутками и постоянным взаимодействием."
    "Сегодня — применение алгоритмов машинного обучения к реальным данным."
    "После звонка часть студентов остаётся с вопросами. Я тоже хотел уточнить кое-что, но, взглянув на часы, понимаю: автобус ждать не будет."

    menu:
        "Что же сделать? Спросить и опоздать на автобус или бежать?"

        "Остаться и спросить":
            jump question
        "Бежать на автобус":
            jump bus




    
    return

label question:

    "И всё же я решил остаться."
    you "Максим Дмитриевич, можно уточнить один момент насчёт выбора признаков?"
    eee "Конечно. В таких задачах важно не только качество на обучающей выборке. Посмотрите, насколько устойчиво ведёт себя модель на новых данных."
    you "То есть хорошая точность сама по себе ещё ничего не гарантирует?"
    eee "Именно. Особенно если есть утечка данных или переобучение."
    "Короткий разговор оказался полезнее, чем я ожидал. Правда, когда я наконец вышел из корпуса, автобус уже скрылся за поворотом."
    $ maks_score += 1
    scene black with Fade(1.5, 1.0, 0.0)

    "Несмотря на все попытки, всё же опоздал на автобус."

    jump rq

label bus:

    scene black with Fade(1.5, 1.0, 0.0)
    "Решил не оставаться, а сразу бежать на автобус"

    jump rq

label rq:
    scene room with Fade(1.5, 1.0, 1.5)
    "День выдался насыщенным. Три пары, несколько разговоров и теперь ещё две дополнительные работы."
    " Кажется, свободное время на этой неделе окончательно отменяется."

    scene black with fade 
    scene room with Fade(1.5, 1.0, 1.5)

    "Суббота. Наконец-то можно не торопиться в университет с самого утра."
    "На столе лежат конспекты, рядом — недочитанная работа Евгения Георгиевича."

    menu:
        "С чего начать?"
        "Изучить работу Евгения Георгиевича":
            "Решаю начать с тех бумаг, которые мне передал Евгений Георгиевич."
            jump day2_evg_start
        "Помочь Владимиру Ивановичу":
            "Сначала решаю зайти в университет и помочь Владимиру Ивановичу."
            jump day2_vlad_start


    jump card_play

label day2_evg_start:
    "Утром я устраиваюсь за столом и открываю распечатки Евгения Георгиевича."
    "Работа оказалась интереснее, чем я ожидал. В ней рассматривается прогнозирование спроса на отдельные группы товаров."
    "Некоторые методы знакомы, другие приходится перечитывать по нескольку раз. Отдельные решения вызывают вопросы, но пока не хватает контекста, чтобы уверенно судить о них."
    "К вечеру решаю занести материалы обратно в университет и заодно уточнить пару моментов."
    "Заодно зайду помочь Владимиру Ивановичу."

    jump day2_vlad

label day2_vlad_start:

    scene kabinet with Dissolve(1.0)
    show vladimir with dissolve

    e "А, пришёл. Отлично. Вот здесь как раз нужно проверить расчёты и отметить спорные места."
    "Проверка оказалась не такой уж сложной, но довольно однообразной. Несколько часов ушло на сверку расчётов и поиск мелких неточностей."
    e "Хорошо поработали. Главное — не просто отмечать ошибку, а понимать, откуда она появилась."
    "Кажется, Владимир Иванович остался доволен. По крайней мере, теперь у меня есть представление, сколько времени уходит на подобную работу."
    "Закончив работу, я прощаюсь с Владимиром Ивановичем, и покидаю его кабинет."

    scene black with Dissolve(1.0)
    scene koridor with fade

    "В коридоре неподалёку от кафедры кто-то оживлённо разговаривает с сотрудником. Мужчина держит распечатки и, кажется, куда-то торопится."

    grig "Да, я понимаю, что сроки уже поджимают. Но если оставить это утверждение в таком виде, рецензент совершенно справедливо задаст вопрос."

    "Он замечает меня."

    show grigoriy with dissolve:
        xalign 0.5, yalign 1.1

    grig "А, здравствуйте. Вы ведь учитесь в магистратуре у Владимира Ивановича?"
    you "Да."
    grig "Кажется, я видел вашу фамилию в списке дипломных. Прикладная математика, статистика? Хорошее сочетание."
    grig "Хотя подозреваю, вам уже успели объяснить, что сочетать можно далеко не всё."

    "Он слегка улыбается и уходит, не дожидаясь ответа."
    hide grigoriy with fade
    "Кажется, это был Григорий Яковлевич — преподаватель, о котором мне уже доводилось слышать."

    jump day2_ev

label day2_ev:

    scene black with fade
    scene room with fade

    "Вернувшись домой, я устраиваюсь за столом и открываю распечатки Евгения Георгиевича."
    "Работа оказалась интереснее, чем я ожидал. В ней рассматривается прогнозирование спроса на отдельные группы товаров."
    "Некоторые методы знакомы, другие приходится перечитывать по нескольку раз. Отдельные решения вызывают вопросы, но пока не хватает контекста, чтобы уверенно судить о них."

    jump day2_final

label day2_vlad:
    scene kabinet with Dissolve(1.0)
    show vladimir with dissolve

    e "А, пришёл. Отлично. Вот здесь как раз нужно проверить расчёты и отметить спорные места."
    "Проверка оказалась не такой уж сложной, но довольно однообразной. Несколько часов ушло на сверку расчётов и поиск мелких неточностей."
    e "Хорошо поработали. Главное — не просто отмечать ошибку, а понимать, откуда она появилась."
    "Кажется, Владимир Иванович остался доволен. По крайней мере, теперь у меня есть представление, сколько времени уходит на подобную работу."
    "Закончив работу, я прощаюсь с Владимиром Ивановичем, и покидаю его кабинет."

    scene black with Dissolve(1.0)
    scene koridor with fade

    "В коридоре неподалёку от кафедры кто-то оживлённо разговаривает с сотрудником. Мужчина держит распечатки и, кажется, куда-то торопится."

    grig "Да, я понимаю, что сроки уже поджимают. Но если оставить это утверждение в таком виде, рецензент совершенно справедливо задаст вопрос."

    "Он замечает меня."

    show grigoriy with dissolve:
        xalign 0.5, yalign 1.1

    grig "А, здравствуйте. Вы ведь учитесь в магистратуре у Владимира Ивановича?"
    you "Да."
    grig "Кажется, я видел вашу фамилию в списке дипломных. Прикладная математика, статистика? Хорошее сочетание."
    grig "Хотя подозреваю, вам уже успели объяснить, что сочетать можно далеко не всё."

    "Он слегка улыбается и уходит, не дожидаясь ответа."
    hide grigoriy with fade
    "Кажется, это был Григорий Яковлевич — преподаватель, о котором мне уже доводилось слышать."

    jump day2_final

label day2_final:

    scene black with fade
    scene room with fade

    "Изрядно устав, я ложусь в кровать..."

    scene black with Dissolve(1.0)

    "Воскресенье проходит незаметно... Завтра уже понедельник... Снова университет..."

    jump day3



label day3:
    scene room with fade
    "Понедельник... Собираюсь и иду в университет."

    scene black with fade

    "Пары проходят быстро. Сегодня их две... После обеда случайно натыкаюсь на Владимира Ивановича."

    scene koridor with fade
    show vladimir with dissolve
    e "Добрый день. Насколько я помню, тебе не хватает последних баллов для красного диплома. "
    "Я осторожно киваю, и он достаёт несколько листов."
    e "Тогда реши вот эту задачку. Ничего сверхъестественного, но хотелось бы получить аккуратный результат."
    e "Нужно сравнить показатели двух групп и понять, насколько различия между ними вообще заслуживают внимания."
    e "Только без фанатизма — я уже видел, как люди находят «значимость» там, где её нет."

    jump static
    
init python:
    import random

    
    STUDIES_DATA = (
        (
            "А",
            "Исследование А (Мороженое и акулы)",
            "Анализ данных за 10 лет показал прямую связь (r = 0,89): в месяцы, когда продажи мороженого растут, резко увеличивается число нападений акул на людей. Вывод: запах мороженого привлекает хищников."
        ),
        (
            "Б",
            "Исследование Б (Бронежилеты и ранения)",
            "После введения новых кевларовых касок в армии число солдат, попадающих в госпитали с ранениями головы, выросло на 40%. Вывод: новые каски делают солдат более уязвимыми."
        ),
        (
            "В",
            "Исследование В (Монетки и экстрасенс)",
            "Участник эксперимента подбросил монетку 10 раз, и 9 раз выпал орёл. Вероятность такого исхода меньше 1%. Вывод: испытуемый обладает телекинезом."
        ),
        (
            "Г",
            "Исследование Г (Витамины и долголетие)",
            "Опрос 5000 человек показал, что люди, ежедневно принимающие дорогие мультивитамины, живут в среднем на 6 лет дольше. Вывод: эти витамины продлевают жизнь."
        ),
    )

    EXPLANATIONS_DATA = (
        (
            "1",
            "Объяснение 1 (Ложная корреляция)",
            "Два события связаны через третью, скрытую переменную (жаркую погоду летом), но не влияют друг на друга напрямую."
        ),
        (
            "2",
            "Объяснение 2 (Ошибка выжившего)",
            "В статистику попали только те, кто остался в живых благодаря защите. Раньше такие люди погибали на месте и не доезжали до врачей."
        ),
        (
            "3",
            "Объяснение 3 (Малая выборка)",
            "На короткой дистанции случайные отклонения неизбежны. Чтобы делать выводы, нужны сотни или тысячи повторений."
        ),
        (
            "4",
            "Объяснение 4 (Неучтённые факторы)",
            "Не учтён образ жизни: дорогие добавки покупают богатые люди, у которых лучше питание, медицина и меньше стресса."
        ),
    )

    CORRECT_PAIRS = {
        "А": "1",
        "Б": "2",
        "В": "3",
        "Г": "4",
    }

    PAIR_COLORS = ("#3b5998", "#8b5a2b", "#6a3d9a", "#2e7d82")

    class StatAnalysisGame(object):
        def __init__(self):
            self.reset_game()

        def reset_game(self):
            self.selected_left = None
            self.selected_right = None
            self.user_links = {}
            self.checked = False
            self.result_text = ""
            self.result_color = "#69f0ae"

            self.left_cards = []
            for s_id, title, body in STUDIES_DATA:
                self.left_cards.append({"id": s_id, "title": title, "body": body})

            shuffled = list(EXPLANATIONS_DATA)
            random.shuffle(shuffled)
            self.right_cards = []
            for e_id, title, body in shuffled:
                self.right_cards.append({"id": e_id, "title": title, "body": body})

        def on_card_click(self, side, item_id):
            if self.checked:
                return

            if side == "left":
                if item_id in self.user_links:
                    del self.user_links[item_id]
                self.selected_left = None if self.selected_left == item_id else item_id
            else:
                linked_s = None
                for s, e in self.user_links.items():
                    if e == item_id:
                        linked_s = s
                        break
                if linked_s is not None:
                    del self.user_links[linked_s]
                self.selected_right = None if self.selected_right == item_id else item_id

            if self.selected_left and self.selected_right:
                self.user_links[self.selected_left] = self.selected_right
                self.selected_left = None
                self.selected_right = None

            renpy.restart_interaction()

        def get_card_style(self, side, item_id):
            if self.checked:
                for s_id, e_id in self.user_links.items():
                    if (side == "left" and s_id == item_id) or (side == "right" and e_id == item_id):
                        if CORRECT_PAIRS[s_id] == e_id:
                            return {
                                "bg": "#1e5631",
                                "border": "#4caf50",
                                "badge": u"✔ Верно! ({0} — {1})".format(s_id, e_id),
                                "badge_fg": "#c8f7c5",
                            }
                        return {
                            "bg": "#6e1e1e",
                            "border": "#f44336",
                            "badge": u"✘ Ошибка! (верно: {0} — {1})".format(s_id, CORRECT_PAIRS[s_id]),
                            "badge_fg": "#ffcdd2",
                        }
                return {"bg": "#2d2d2d", "border": "#555555", "badge": u"Не выбрано", "badge_fg": "#888888"}

            for idx, (s_id, e_id) in enumerate(self.user_links.items()):
                if (side == "left" and s_id == item_id) or (side == "right" and e_id == item_id):
                    color = PAIR_COLORS[idx % len(PAIR_COLORS)]
                    if side == "left":
                        badge = u"Связано с Объяснением {0}".format(e_id)
                    else:
                        badge = u"Связано с Исследованием {0}".format(s_id)
                    return {"bg": color, "border": "#ffffff", "badge": badge, "badge_fg": "#ffffff"}

            if side == "left" and item_id == self.selected_left:
                return {
                    "bg": "#444444",
                    "border": "#ffd700",
                    "badge": u"Выбрано (нажмите на карточку справа)",
                    "badge_fg": "#ffd700",
                }
            if side == "right" and item_id == self.selected_right:
                return {
                    "bg": "#444444",
                    "border": "#ffd700",
                    "badge": u"Выбрано (нажмите на карточку слева)",
                    "badge_fg": "#ffd700",
                }

            return {"bg": "#2d2d2d", "border": "#555555", "badge": u"Не выбрано", "badge_fg": "#888888"}

        def check_answers(self):
            if len(self.user_links) < 4:
                self.result_text = u"Сначала соедините все 4 карточки!"
                self.result_color = "#ff6b6b"
                renpy.restart_interaction()
                return

            errors = 0
            for s_id, e_id in self.user_links.items():
                if CORRECT_PAIRS[s_id] != e_id:
                    errors += 1

            if errors >= 2:
                self.result_color = "#ff6b6b"
                self.result_text = u"Ошибок: {0} из 4.\n— Что-то ты сегодня варёный. Много напортачил, но ладно — на практике обучился, считай.".format(errors)
            else:
                self.result_color = "#69f0ae"
                self.result_text = u"Ошибок: {0} из 4.\n— Молодец. Как и ожидал, справился нормально. Спасибо, что помог.".format(errors)
                self.checked = True
                store.vlad_score += 1  # <-- Используем store. перед именем переменной
            renpy.restart_interaction()

    
    stat_game = StatAnalysisGame()


screen stat_analysis():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        background "#1e1e1e"
        padding (20, 15)

        vbox:
            spacing 10

            text "Соотнесите исследования (слева) и объяснения ошибок (справа)":
                size 18
                bold True
                color "#ffffff"
                xalign 0.5

            hbox:
                spacing 30

                vbox:
                    spacing 8

                    for card in stat_game.left_cards:
                        $ st = stat_game.get_card_style("left", card["id"])
                        frame:
                            background st["border"]
                            padding (2, 2)

                            button:
                                background st["bg"]
                                hover_background st["bg"]
                                xysize (560, None)
                                sensitive not stat_game.checked

                                vbox:
                                    spacing 2
                                    text card["title"] size 16 bold True color "#e0e0e0"
                                    text card["body"] size 13 color "#cccccc" xmaximum 540
                                    text st["badge"] size 11 color st["badge_fg"] xalign 1.0

                                action Function(stat_game.on_card_click, "left", card["id"])

                vbox:
                    spacing 8

                    for card in stat_game.right_cards:
                        $ st = stat_game.get_card_style("right", card["id"])
                        frame:
                            background st["border"]
                            padding (2, 2)

                            button:
                                background st["bg"]
                                hover_background st["bg"]
                                xysize (560, None)
                                sensitive not stat_game.checked

                                vbox:
                                    spacing 2
                                    text card["title"] size 16 bold True color "#e0e0e0"
                                    text card["body"] size 13 color "#cccccc" xmaximum 540
                                    text st["badge"] size 11 color st["badge_fg"] xalign 1.0

                                action Function(stat_game.on_card_click, "right", card["id"])

            hbox:
                spacing 15

                textbutton "Проверить ответы":
                    text_size 18
                    text_bold True
                    sensitive not stat_game.checked
                    action Function(stat_game.check_answers)


                
                textbutton "Далее":
                    text_size 18
                    text_bold True
                    action Return()

                if stat_game.result_text:
                    text stat_game.result_text:
                        size 14
                        italic True
                        color stat_game.result_color
                        yalign 0.5


label static:
    scene black
    "Соотнесите исследования (слева) и объяснения ошибок (справа). Сначала кликните карточку слева, затем её пару справа — или наоборот. Когда все 4 пары собраны, нажимайте «Проверить ответы»."
    call screen stat_analysis
        

    e "Вот молодец. Балл заработал."
    you "Спасибо, Владимир Иванович!"
    "Как оказалось, он тоже собирался уходить, но случайно натолкнулся на меня."
    "По дороге домой, мы заходим в небольшое кафе, где часто собираются преподаватели и студенты."

    scene kafe with Dissolve(1.5)
    show vladimir with dissolve

    e "Знаешь, иногда полезно хотя бы на час перестать смотреть на цифры."
    you "Не думал, что услышу это от вас."
    e "Я тоже когда-то был студентом, между прочим."

    "Он достаёт колоду карт."
    e "Ну что, сыграем?"

    "А вокруг нас уже собирается толпа... Но я не из пугливых."
    you "Играем."

    init python:
    # Классические номиналы казиношного Блэкджека (52 карты)
        VALUES = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "J": 10, "Q": 10, "K": 10, "A": 11
        }
        SUITS = ["♠", "♥", "♦", "♣"]

        def create_deck():
            # Создаём стандартную покерную/казиношную колоду на 52 карты
            deck = [f"{rank}{suit}" for rank in VALUES.keys() for suit in SUITS]
            renpy.random.shuffle(deck)
            return deck

        def get_card_value(card):
            rank = card[:-1]
            return VALUES[rank]

        def calc_score(hand):
            total = sum(get_card_value(card) for card in hand)
            aces = sum(1 for card in hand if card.startswith("A"))
            # Гибкий туз: превращается из 11 в 1 при переборе
            while total > 21 and aces > 0:
                total -= 10
                aces -= 1
            return total

        def is_blackjack(hand):
            # Натуральный Блэкджек: ровно 21 очко с первых двух карт (Туз + Десятка/Картинка)
            return len(hand) == 2 and calc_score(hand) == 21

        def draw_card(deck):
            if len(deck) == 0:
                renpy.notify("Шуз пуст! Дилер распечатывает новую колоду на 52 карты.")
                deck.extend(create_deck())
            return deck.pop()

# Переменные состояния игры
default deck =[]
default player_hand =[]
default dealer_hand =[]
default round_num = 1
default max_rounds = 10
default player_wins = 0
default dealer_wins = 0
default draws = 0
default game_result = ""

# Визуальный интерфейс стола
screen blackjack_table(hide_dealer=True):
    add Solid("#0b2e19cc")

    # Верхняя панель
    frame:
        xalign 0.5
        yalign 0.05
        padding (30, 15)
        background Solid("#00000088")
        hbox:
            spacing 40
            text "Раунд: [round_num] / [max_rounds]" size 28 color "#ffd700"
            text "Вы: [player_wins]  |  Владимир Иванович: [dealer_wins]  |  Push (Ничья): [draws]" size 26
            text "В колоде: [len(deck)] / 52" size 26 color "#aaaaaa"

    # Зона дилера
    vbox:
        xalign 0.5
        yalign 0.25
        spacing 15
        text "Дилер: Владимир Иванович" xalign 0.5 size 26 color "#cccccc"
        
        hbox:
            xalign 0.5
            spacing 15
            for i, card in enumerate(dealer_hand):
                if hide_dealer and i == 1:
                    frame:
                        xsize 110 ysize 160
                        background Solid("#8b0000")
                        text "🂠" align (0.5, 0.5) size 60 color "#ffffff"
                else:
                    $ card_color = "#d32f2f" if ("♥" in card or "♦" in card) else "#111111"
                    frame:
                        xsize 110 ysize 160
                        background Solid("#f5f5f5")
                        text "[card]" align (0.5, 0.5) size 36 color card_color bold True

        if hide_dealer:
            $ first_card = dealer_hand[0] if dealer_hand else ""
            $ visible_score = get_card_value(first_card) if first_card else 0
            text "Очки: [visible_score] + ?" xalign 0.5 size 24
        else:
            $ d_score = calc_score(dealer_hand)
            if is_blackjack(dealer_hand):
                text "BLACKJACK! (21)" xalign 0.5 size 26 color "#ffd700" bold True
            else:
                text "Очки: [d_score]" xalign 0.5 size 24 color "#ffd700"

    # Зона игрока
    vbox:
        xalign 0.5
        yalign 0.65
        spacing 15
        $ p_score = calc_score(player_hand)
        if is_blackjack(player_hand):
            text "Ваша рука: BLACKJACK! (21)" xalign 0.5 size 28 color "#ffd700" bold True
        else:
            text "Ваша рука (Очки: [p_score])" xalign 0.5 size 28 color "#ffffff"
        
        hbox:
            xalign 0.5
            spacing 15
            for card in player_hand:
                $ card_color = "#d32f2f" if ("♥" in card or "♦" in card) else "#111111"
                frame:
                    xsize 110 ysize 160
                    background Solid("#ffffff")
                    text "[card]" align (0.5, 0.5) size 36 color card_color bold True

# Основной сценарий игры
label card_play:
    $ deck = create_deck()
    $ round_num = 1
    $ player_wins = 0
    $ dealer_wins = 0
    $ draws = 0

    "Владимир Иванович распечатывает стандартную колоду на 52 карты и профессионально тасует её."
    "«Играем в классический блэкджек. Десять раздач, отбой в сторону. Дилер стоит на семнадцати»."

    while round_num <= max_rounds:
        $ player_hand = [draw_card(deck), draw_card(deck)]
        $ dealer_hand = [draw_card(deck), draw_card(deck)]

        show screen blackjack_table(hide_dealer=True)

        # Проверка на натуральный Блэкджек с раздачи
        if is_blackjack(player_hand) or is_blackjack(dealer_hand):
            pause 0.5
            show screen blackjack_table(hide_dealer=False)
            
            if is_blackjack(player_hand) and is_blackjack(dealer_hand):
                $ draws += 1
                "У обоих натуральный Блэкджек! Ничья (Push)."
            elif is_blackjack(player_hand):
                $ player_wins += 1
                "Блэкджек с раздачи! Чистая победа в раунде."
            else:
                $ dealer_wins += 1
                "У Владимира Ивановича Блэкджек с раздачи! Вы проиграли раунд."
            jump .next_round

        # Ход игрока
        label .player_turn:
            $ p_score = calc_score(player_hand)

            if p_score > 21:
                show screen blackjack_table(hide_dealer=False)
                $ dealer_wins += 1
                "Перебор ([p_score])! Вы проиграли раздачу."
                jump .next_round
            elif p_score == 21:
                "21 очко! Передаем ход дилеру."
                jump .dealer_turn

            menu:
                "Ещё (Hit)":
                    $ player_hand.append(draw_card(deck))
                    jump .player_turn
                "Хватит (Stand)":
                    jump .dealer_turn

        # Ход дилера
        label .dealer_turn:
            show screen blackjack_table(hide_dealer=False)
            pause 0.6

            while calc_score(dealer_hand) < 17:
                $ dealer_hand.append(draw_card(deck))
                pause 0.5

            $ p_score = calc_score(player_hand)
            $ d_score = calc_score(dealer_hand)

            if d_score > 21:
                $ player_wins += 1
                "У дилера перебор ([d_score])! Вы выиграли раунд."
            elif p_score > d_score:
                $ player_wins += 1
                "Вы победили ([p_score] против [d_score])!"
            elif p_score < d_score:
                $ dealer_wins += 1
                "Дилер забрал раунд ([d_score] против [p_score])."
            else:
                $ draws += 1
                "Ровно! По [p_score] очков — Push (ничья)."

        label .next_round:
            $ round_num += 1

    hide screen blackjack_table

    "Серия из 10 раздач окончена. Счет — Вы: [player_wins], Владимир Иванович: [dealer_wins], Ничьи: [draws]."

    if player_wins > dealer_wins:
        $ game_result = "win"
        "Владимир Иванович складывает карты: «Отличная игра. Ты меня переиграл»."
        $ vlad_score +=1
    elif player_wins < dealer_wins:
        $ game_result = "lose"
        "«Казино всегда в плюсе», — усмехается Владимир Иванович."
        $ vlad_score+=0
    else:
        $ game_result = "draw"
        "«Ничья по итогам десяти раздач. Достойно»."
        $ vlad_score+=0

    jump day3_evening


label day3_evening:
    e "Это была неплохая игра. Увидел силу теории вероятностей?"
    you "Увидел."
    "Студенты вокруг тихо посмеиваются..."

    scene black with fade
    scene room with fade

    "Интересный день... Кто бы мог подумать, что теория вероятностей всегда окружает нас..."

    scene black with fade
    jump day4

label day4:
    scene black with dissolve
    scene lecauditory with fade

    "Вторник. Пара экономики..."
    "После занятий решаю обсудить с Евгением Георгиевичем его исследование."

    show evgeniy with dissolve:
        xalign 0.5 yalign 1.0

    ee "Успели ознакомиться с материалами?"
    you "Да. Особенно заинтересовала часть, где вы рассматриваете прогнозирование спроса. Я как раз сталкивался с похожими задачами."
    ee "Хорошо. В таком случае, возможно, вам будет интересно посмотреть, как подобные методы применяются за пределами университета."
    "Он ненадолго задумывается."
    ee "У меня есть знакомый, руководит аналитическим направлением в одной компании. Они периодически берут молодых специалистов на стажировку. Могу вас познакомить."
    you "А что именно они делают?"
    ee "Разные задачи. Оптимизация процессов, анализ показателей, работа с данными. Ничего экзотического, но математика там вполне пригодится."
    you "Было бы интересно."
    ee "Тогда я передам ему ваши контакты. Думаю, найдётся время встретиться."

    hide evgeniy with dissolve
    jump day4_interview

label day4_interview:
    scene black with Dissolve(1.5)
    "Через некоторое время я оказываюсь в офисе компании."
    "Обстановка заметно отличается от привычных университетских коридоров: открытое пространство, переговорные, несколько сотрудников за компьютерами."
    "Меня встречает знакомый Евгения Георгиевича."

    scene office with Fade(1.5, 1.0, 1.5)
    show companyrep with dissolve:
        xalign 0.5 yalign 1.0
    
    company_rep "Здравствуйте. Евгений Георгиевич немного рассказал о вас. Вы заканчиваете магистратуру по математической статистике?"
    you "Да, сейчас занимаюсь дипломом."
    company_rep "Хорошо. Расскажите немного о своей работе."
    "Я кратко объясняю тему диплома и использованные методы."
    company_rep "Понятно. У нас, кстати, бывают похожие задачи. Только обычно заказчику не так важно, насколько красивую модель вы построили. Ему нужно понимать, что с ней делать."
    "Он открывает ноутбук."
    company_rep "Давайте попробуем небольшую задачу. Представим, что у нас есть ограниченное количество ресурсов и несколько направлений, куда их можно распределить. Нужно найти решение, которое даст наилучший результат."
    
    if dif == 1:
        $ pipe_board.new_game(max_moves=20)
    
    if dif == 2:
        $ pipe_board.new_game(max_moves=15)
    
    if dif == 3:
        $ pipe_board.new_game(max_moves=10)
    "Собери трубу от зелёного входа (слева внизу) к красному выходу (справа вверху). У тебя есть [pipe_board.max_moves] ходов."
    call screen plumber
    jump vodop

init python:
    import random
    from collections import deque
    import pygame_sdl2 as pygame

    
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    OPPOSITE = {0: 2, 1: 3, 2: 0, 3: 1}

    
    PIPE_SHAPES = {
        'I': (0, 2),        
        'L': (0, 1),        
        'T': (0, 1, 2),     
        '+': (0, 1, 2, 3),  
    }

    class PipeBoard(renpy.Displayable):

        def __init__(self, size=5, cell=90, max_moves=25):
            super(PipeBoard, self).__init__()
            self.size = size
            self.cell = cell
            self.width = size * cell
            self.height = size * cell
            self.max_moves = max_moves
            self.new_game(max_moves)

        def new_game(self, max_moves=None):
            if max_moves is not None:
                self.max_moves = max_moves
            self.moves = 0
            self.won = False
            self.lost = False
            self.generate_solvable_grid()
            self.update_water()
            renpy.redraw(self, 0)
            renpy.restart_interaction()

        def generate_solvable_grid(self):
            
            while True:
                path = [(self.size - 1, 0)]
                visited = set(path)
                while path[-1] != (0, self.size - 1):
                    r, c = path[-1]
                    neighbors = []
                    for dr, dc in DIRS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size and (nr, nc) not in visited:
                            neighbors.append((nr, nc))
                    if not neighbors:
                        break
                    nxt = random.choice(neighbors)
                    path.append(nxt)
                    visited.add(nxt)
                if path[-1] == (0, self.size - 1):
                    break

            
            required = dict((cell, set()) for cell in path)
            required[(self.size - 1, 0)].add(3)
            required[(0, self.size - 1)].add(1)

            for i in range(len(path) - 1):
                r1, c1 = path[i]
                r2, c2 = path[i + 1]
                dr, dc = r2 - r1, c2 - c1
                d = DIRS.index((dr, dc))
                required[(r1, c1)].add(d)
                required[(r2, c2)].add(OPPOSITE[d])

            
            self.grid = [[None] * self.size for _ in range(self.size)]
            for r in range(self.size):
                for c in range(self.size):
                    if (r, c) in required:
                        req = required[(r, c)]
                        valid_shapes = []
                        for shape, base_dirs in PIPE_SHAPES.items():
                            for rot in range(4):
                                rotated = set((d + rot) % 4 for d in base_dirs)
                                if req.issubset(rotated):
                                    valid_shapes.append(shape)
                                    break
                        shape = random.choice(valid_shapes)
                    else:
                        shape = random.choice(['I', 'L', 'T'])

                    rot = random.randint(0, 3)
                    self.grid[r][c] = {'shape': shape, 'rot': rot, 'water': False}

        def get_openings(self, r, c):
            cell = self.grid[r][c]
            base = PIPE_SHAPES[cell['shape']]
            return set((d + cell['rot']) % 4 for d in base)

        def update_water(self):
            
            for r in range(self.size):
                for c in range(self.size):
                    self.grid[r][c]['water'] = False

            
            start_r, start_c = self.size - 1, 0
            if 3 in self.get_openings(start_r, start_c):
                queue = deque([(start_r, start_c)])
                self.grid[start_r][start_c]['water'] = True

                while queue:
                    r, c = queue.popleft()
                    for d in self.get_openings(r, c):
                        dr, dc = DIRS[d]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size:
                            if not self.grid[nr][nc]['water'] and OPPOSITE[d] in self.get_openings(nr, nc):
                                self.grid[nr][nc]['water'] = True
                                queue.append((nr, nc))

            
            end_r, end_c = 0, self.size - 1
            if self.grid[end_r][end_c]['water'] and 1 in self.get_openings(end_r, end_c):
                self.won = True

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            surface = render.canvas().get_surface()
            self.draw(surface)
            return render

        def event(self, ev, x, y, st):
            
            if self.won or self.lost:
                return

            if ev.type == pygame.MOUSEBUTTONDOWN and getattr(ev, 'button', 0) == 1:
                c = int(x // self.cell)
                r = int(y // self.cell)
                if 0 <= r < self.size and 0 <= c < self.size:
                    cell = self.grid[r][c]
                    cell['rot'] = (cell['rot'] + 1) % 4
                    self.moves += 1

                    
                    try:
                        if renpy.loadable("click.ogg"):
                            renpy.play("click.ogg")
                    except Exception:
                        pass

                    self.update_water()

                    
                    if not self.won and self.moves >= self.max_moves:
                        self.lost = True

                    renpy.redraw(self, 0)
                    renpy.restart_interaction()

        def draw(self, surface):
            cs = self.cell
            half = cs // 2

            surface.fill((43, 43, 43))

            for r in range(self.size):
                for c in range(self.size):
                    x1, y1 = c * cs, r * cs
                    cx, cy = x1 + half, y1 + half

                    
                    bg_color = (56, 56, 56)
                    if r == self.size - 1 and c == 0:
                        bg_color = (46, 74, 62)    
                    elif r == 0 and c == self.size - 1:
                        bg_color = (74, 46, 46)    

                    pygame.draw.rect(surface, bg_color, (x1 + 2, y1 + 2, cs - 4, cs - 4), 0)
                    pygame.draw.rect(surface, (85, 85, 85), (x1 + 2, y1 + 2, cs - 4, cs - 4), 2)

                    
                    if r == self.size - 1 and c == 0:
                        pygame.draw.line(surface, (0, 191, 255), (x1, cy), (x1 + 12, cy), 18)
                    if r == 0 and c == self.size - 1:
                        pygame.draw.line(surface, (255, 85, 85), (x1 + cs - 12, cy), (x1 + cs, cy), 18)

                    
                    pipe_color = (0, 191, 255) if self.grid[r][c]['water'] else (153, 153, 153)
                    openings = self.get_openings(r, c)

                    
                    for d in openings:
                        dr, dc = DIRS[d]
                        ex = cx + dc * half
                        ey = cy + dr * half
                        pygame.draw.line(surface, pipe_color, (cx, cy), (ex, ey), 16)
                        pygame.draw.circle(surface, pipe_color, (int(ex), int(ey)), 8)

                    
                    pygame.draw.circle(surface, pipe_color, (cx, cy), 10)
                    pygame.draw.circle(surface, (34, 34, 34), (cx, cy), 10, 2)

        def visit(self):
            return []

    pipe_board = PipeBoard(max_moves=25)



screen plumber():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        background "#1a1a1a"
        padding (15, 15)

        vbox:
            spacing 10

            hbox:
                xfill True

                
                $ moves_color = "#ff5555" if (pipe_board.max_moves - pipe_board.moves) <= 5 else "#eeeeee"
                text "Ходы: [pipe_board.moves] / [pipe_board.max_moves]" size 24 color moves_color

                textbutton "Новая игра":
                    xalign 1.0
                    text_size 20
                    action Function(pipe_board.new_game)

            add pipe_board

    
    if pipe_board.won:
        $ ev_score+=2
        frame:
            xalign 0.5
            yalign 0.5
            background "#000000"
            padding (30, 20)

            vbox:
                spacing 15

                text "Победа!" size 36 color "#ffd700" xalign 0.5
                text "Вода дошла до цели за [pipe_board.moves] ходов!" size 24 color "#eeeeee"
                

                hbox:
                    spacing 20
                    xalign 0.5

                    textbutton "Продолжить":
                        action Return(True)

                    
    
    elif pipe_board.lost:
        $ ev_score+=0
        frame:
            xalign 0.5
            yalign 0.5
            background "#000000"
            padding (30, 20)

            vbox:
                spacing 15

                text "Ходы закончились!" size 36 color "#ff5555" xalign 0.5
                text "Вы не успели собрать трубопровод за [pipe_board.max_moves] ходов." size 22 color "#eeeeee" xalign 0.5
                

                hbox:
                    spacing 20
                    xalign 0.5

                    textbutton "Попробовать снова":
                        action Function(pipe_board.new_game)


label vodop:
    scene office
    
    

    show companyrep with dissolve
    "После выполнения задачи представитель компании некоторое время изучает получившийся результат."
    company_rep "Неплохо. Но обратите внимание: оптимальное решение зависит от того, что именно мы считаем эффективностью."
    you "То есть можно получить несколько правильных ответов?"
    company_rep "Можно получить несколько разумных решений. Вопрос в том, какое из них лучше подходит под конкретную задачу."
    company_rep "Для локальной маршрутизации хорошо работают алгоритмы на графах, а если нужно прогнозировать плотность потока на всей магистрали — подключают макроскопические модели или методы машинного обучения."
    company_rep "Выбор инструмента всегда диктуется масштабом задачи."

    "Собеседование заканчивается коротким разговором о возможной стажировке."
    "По дороге домой я ловлю себя на мысли, что использование математических знаний в коммерческих целях устроено совсем иначе, чем университетские исследования."
    "Здесь гораздо чаще приходится объяснять, зачем вообще нужны твои расчёты."

    scene room with fade
    "Завтра тоже будет сложно. Максим Дмитриевич просил помочь с проведением занятия для школьников..."
    "Но думаю, что справлюсь. "
    scene black with fade

    jump day5

label day5:
    scene room with fade
    "Будильник звенит в 7 утра... Мда, давно я не был в школе..."
    "Срочно собираюсь и бегу на автобус..."

    scene school with Fade(1.5, 1.0, 1.5)
    "Максим Дмитриевич раскладывает материалы."
    eee "Я подготовил небольшой план. Но не обязательно строго ему следовать. Главное, чтобы ребята поняли саму идею."
    "Он передаёт мне лист с заданием."
    eee "Попробуй объяснить вот этот пример. Посмотрим, как пойдёт."

    "Аудитория постепенно заполняется школьниками. Некоторые активно переговариваются, другие внимательно рассматривают доску."
    "Максим Дмитриевич представляет меня и предлагает начать объяснение."
    "Сначала всё идёт довольно гладко. Я разбираю пример, показываю основные переходы, отвечаю на пару вопросов."
    "Но постепенно доска заполняется, количество формул увеличивается, а память учеников заканчивается."
    "И вот один из перегруженных информацией школьников поднимает руку."

    schoolboy "Вопрос не по теме… как запомнить все эти формулы и преобразования?"
    "Кажется, придётся объяснить иначе."

    jump memo

init python:
    import random

    
    MEMO_PAIRS = (
        (u"E=1.5*kT",              u"полтора KоTа"),
        (u"F=pgV",                 u"B PоЖУ"),
        (u"P=pgh",                 u"РоЖА-АШ"),
        (u"u=(3kT/m)**0.5",        u"три КоТа на Мясо"),
        (u"Fa=BIL*sin(a)",         u"Ампер БИЛ сына"),
        (u"T=2π*(m/k)",                 u"ПиТца с МаКом"),
        (u"T=2π*(l/g)",              u"ПиТца в ЛуЖе"),
        (u"e=2,718281828",   u"2,7ЛевТолстойЛевТолстой"),
    )

    PAIRS_COUNT = len(MEMO_PAIRS)   
    GRID_COLS = 4
    GRID_ROWS = 4
    MISMATCH_DELAY = 1.0            # сколько секунд открыта пара несовпавших карточек

    class MemoGame(object):
        def __init__(self):
            self.new_game()

        def new_game(self):
            
            deck = []
            for p, (formula, joke) in enumerate(MEMO_PAIRS):
                deck.append({"pair": p, "side": 0, "text": formula})
                deck.append({"pair": p, "side": 1, "text": joke})
            random.shuffle(deck)

            self.cards = []
            for item in deck:
                item["flipped"] = False
                item["matched"] = False
                self.cards.append(item)

            self.first = None       
            self.mismatch = None    
            self.locked = False     
            self.moves = 0
            self.matched_pairs = 0
            self.won = False

        def open_card(self, idx):
            if self.locked or self.won:
                return
            card = self.cards[idx]
            if card["matched"] or card["flipped"]:
                return

            card["flipped"] = True

            if self.first is None:
                
                self.first = idx
            else:
                self.moves += 1
                other = self.cards[self.first]
                if other["pair"] == card["pair"] and other["side"] != card["side"]:
                    
                    other["matched"] = True
                    card["matched"] = True
                    self.matched_pairs += 1
                    self.first = None
                    if self.matched_pairs == PAIRS_COUNT:
                        self.won = True
                else:
                    
                    self.mismatch = (self.first, idx)
                    self.first = None
                    self.locked = True

            renpy.restart_interaction()

        def hide_mismatch(self):
            
            if self.mismatch is not None:
                for i in self.mismatch:
                    self.cards[i]["flipped"] = False
                self.mismatch = None
            self.locked = False
            renpy.restart_interaction()

    memo_game = MemoGame()


screen memo():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        background "#1e1e1e"
        padding (20, 15)

        vbox:
            spacing 10

            hbox:
                xfill True

                text "Ходы: [memo_game.moves]   Найдено пар: [memo_game.matched_pairs] из 8":
                    size 20
                    color "#eeeeee"

                textbutton "Новая игра":
                    xalign 1.0
                    text_size 18
                    action Function(memo_game.new_game)

            
            grid GRID_COLS GRID_ROWS:
                spacing 10

                for idx in range(len(memo_game.cards)):
                    $ card = memo_game.cards[idx]

                    if card["matched"] or card["flipped"]:
                        
                        if card["side"] == 0:
                            
                            button:
                                xysize (280, 150)
                                background "#3a3a3a"
                                hover_background "#3a3a3a"
                                sensitive False

                                text card["text"]:
                                    size 26
                                    color "#69f0ae"
                                    font "DejaVuSans.ttf"
                                    text_align 0.5
                                    xalign 0.5
                                    yalign 0.5
                        else:
                            
                            button:
                                xysize (280, 150)
                                background "#3a3a3a"
                                hover_background "#3a3a3a"
                                sensitive False

                                text card["text"]:
                                    size 18
                                    color "#ffd54f"
                                    text_align 0.5
                                    xalign 0.5
                                    yalign 0.5
                                    xmaximum 260
                    else:
                        
                        button:
                            xysize (280, 150)
                            background "#2d2d2d"
                            hover_background "#444444"

                            text "?":
                                size 40
                                bold True
                                color "#555555"
                                xalign 0.5
                                yalign 0.5

                            action Function(memo_game.open_card, idx)

            
            if memo_game.locked:
                timer MISMATCH_DELAY action Function(memo_game.hide_mismatch)

    
    
    if memo_game.won:
        $ maks_score+=2
        frame:
            xalign 0.5
            yalign 0.5
            background "#000000"
            padding (30, 20)

            vbox:
                spacing 15

                text "Все пары найдены!":
                    size 32
                    bold True
                    color "#ffd700"
                    xalign 0.5

                text "Ходов: [memo_game.moves]":
                    size 22
                    color "#eeeeee"
                    xalign 0.5

                hbox:
                    spacing 20
                    xalign 0.5

                    

                    textbutton "Далее":
                        text_size 20
                        action Return(True)

label memo:
    scene black
    "Найди все 8 пар: каждая физическая формула соединяется со своей шуточной расшифровкой. Открывай по две карточки за ход."
    call screen memo

    scene koridor with fade
    show maksim with dissolve
    "После занятия Максим Дмитриевич догоняет меня в коридоре."
    eee "Ну что, как ощущения?"
    you "Не так просто, как казалось сначала."
    eee "А ты думал, достаточно знать предмет?"
    you "Видимо, нет."
    eee "Знать тему и уметь объяснить её другому человеку — всё-таки разные вещи. Но получилось неплохо."

    "Я собираю материалы и выхожу из аудитории. Школьники ещё какое-то время обсуждают задания в коридоре."
    "Неожиданно приятное ощущение — видеть, что кому-то действительно удалось что-то понять благодаря твоему объяснению."

    hide maksim with dissolve
    scene black with Dissolve(1.5)
    scene room with fade

    "Вечером я заглядываю в наш студенческий чат."
    "С удивлением для себя узнаю, что завтра пару вместо Максима Дмитриевича проведёт Григорий Яковлевич..."
    you "Это определённо будет интересно."
    "С такими мыслями я ложусь спать..."
    scene black with fade
    jump day6

label day6:
    scene compauditory with fade
    "Удивительно, но сегодня аудитория полна, как никогда..."
    "Григорий Яковлевич ведёт лекцию непринуждённо, легко и быстро..."
    "Однако тем не менее, всё абсолютно понятно."
    "Воистину удивительный человек."
    "После занятия я решаю подойти к нему."
    show grigoriy with dissolve
    you "Здравствуйте."
    grig "А, здравствуйте. Мы ведь уже встречались?"
    you "Да, в коридоре на прошлой неделе."
    grig "Верно. Вы ведь занимаетесь статистикой?"
    you "Да, магистратура по теории вероятностей и математической статистике."
    grig "Хорошо. А с доказательствами как?"
    you "По-разному. Зависит от того, что доказывать."
    "Он слегка улыбается."
    grig "Справедливо. Посмотрите-ка сюда."

    "Григорий Яковлевич поворачивает ко мне лист."
    grig "Здесь есть небольшое рассуждение. Мне интересно, дорешаете ли вы его."

    jump math

label math:
    
    screen math_puzzle():
        frame:
            xalign 0.5
            yalign 0.15
            padding (30, 20)
            background "#000000cc" 
        
            vbox:
                spacing 10
                text "Решите систему уравнений:" bold True size 28
                text "⎧ Va + VIb = LV" size 26
                text "⎩ XVa + XXb = CL" size 26
            
                null height 10 # Небольшой отступ
            
                text "Расшифровка:" bold True size 24
                text "• I = 1   • V = 5   • X = 10" size 22
                text "• XX = 20 • L = 50  • C = 100" size 22

    
    label math_game:
        
        $ correct_a = 20.0
        $ correct_b = -7.5

        
        show screen math_puzzle

        while True:
        
            $ user_a = renpy.input("Введите значение a:", allow="0123456789.-,").strip().replace(",", ".")
            $ user_b = renpy.input("Введите значение b:", allow="0123456789.-,").strip().replace(",", ".")

            python:
                try:
                    a = float(user_a)
                    b = float(user_b)
                    
                    if abs(a - correct_a) < 1e-5 and abs(b - correct_b) < 1e-5:
                        result = "win"
                    else:
                        result = "wrong"
                except ValueError:
                    result = "error"

            
            if result == "win":
                $ grig_score+=1
                hide screen math_puzzle # Прячем условие задачи
                "Верно! Отличная работа! (a = 20, b = -7.5)"
                jump day6_con # Возвращаемся обратно в основной сюжет

            elif result == "wrong":
                "Неверно. Попробуйте еще раз!"

            elif result == "error":
                "Ошибка: пожалуйста, введите корректные числа (например, 10 или -2.5)."

label day6_con:
    "Когда мы заканчиваем, Григорий Яковлевич забирает лист."
    show grigoriy with dissolve

    grig "Я рад, что вы смогли устоять под натиском моих нестандартных записей. Редкое достижение."
    "Он собирает бумаги."
    grig "Многие приходят в математику за возможностью применять её к чему-то. Это вполне разумно. Но иногда интересно заниматься вопросом просто потому, что он существует."
    you "Даже если практической пользы пока не видно?"
    grig "Особенно если её пока не видно. Не всё интересное обязано немедленно приносить пользу."
    "Он смотрит на часы."
    grig "Ладно, не буду вас задерживать. Если заинтересовались — можете как-нибудь заглянуть ещё."

    hide grigoriy with dissolve
    scene black with Dissolve(1.5)

    "Перед сном поток мыслей накрывает голову."
    you "Всё же математика - царица наук. Она везде и всегда."
    "Завтра пятница. Последняя учебная пятница. Как же быстро летит время..."
    jump day7

label day7:
    "Сегодня мне приходит сообщение с предложением помочь в небольшом исследовании."
    "Задача связана с оценкой эффективности дополнительной подготовки студентов."
    "Нужно понять, действительно ли дополнительные занятия помогают улучшить результаты или наблюдаемая разница объясняется другими факторами."
    "Вроде бы ничего особенно сложного. Но сначала нужно правильно организовать само исследование."

    jump experiment









default experiment_score = 0
default experiment_answers = {}
default experiment_result_level = "unknown"



screen experiment_choice(title, prompt, options, selected_text=""):

    modal True
    zorder 100

    add Solid("#101827")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 680
        padding (35, 30)
        background Solid("#202d40")

        vbox:
            spacing 18

            text title:
                size 38
                color "#f2f5fa"
                xalign 0.5

            text prompt:
                size 24
                color "#d5deeb"
                xalign 0.5
                text_align 0.5
                xmaximum 1000

            if selected_text:
                frame:
                    xfill True
                    padding (15, 10)
                    background Solid("#34465e")

                    text "Выбрано: [selected_text]":
                        size 20
                        color "#ffffff"

            null height 8

            grid 2 2:
                xfill True
                yfill True
                spacing 14

                for option_id, option_text in options:
                    button:
                        xfill True
                        yfill True
                        padding (18, 16)
                        background Solid("#354963")
                        hover_background Solid("#4c6686")
                        action Return(option_id)

                        text option_text:
                            size 21
                            color "#ffffff"
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            xmaximum 440

            null height 5

            text "Выберите одну карточку":
                size 17
                color "#aebbd0"
                xalign 0.5


screen experiment_feedback(title, body, continue_text="Продолжить"):

    modal True
    zorder 100

    add Solid("#101827")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        padding (40, 35)
        background Solid("#202d40")

        vbox:
            spacing 22

            text title:
                size 34
                color "#f2f5fa"
                xalign 0.5

            text body:
                size 23
                color "#d5deeb"
                xmaximum 900
                text_align 0.5
                xalign 0.5

            textbutton continue_text:
                xalign 0.5
                text_size 23
                text_color "#ffffff"
                text_hover_color "#b8d7ff"
                action Return()


screen experiment_results_table():

    modal True
    zorder 100

    add Solid("#101827")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1050
        padding (35, 30)
        background Solid("#202d40")

        vbox:
            spacing 18

            text "Результаты условного эксперимента":
                size 34
                color "#f2f5fa"
                xalign 0.5

            text "Средний результат тестирования (баллы из 100)":
                size 21
                color "#d5deeb"
                xalign 0.5

            grid 3 3:
                xfill True
                spacing 10

                text "Показатель" size 21 color "#ffffff"
                text "Доп. занятия" size 21 color "#ffffff" xalign 0.5
                text "Без занятий" size 21 color "#ffffff" xalign 0.5

                text "До эксперимента" size 20 color "#d5deeb"
                text "58" size 22 color "#ffffff" xalign 0.5
                text "65" size 22 color "#ffffff" xalign 0.5

                text "После эксперимента" size 20 color "#d5deeb"
                text "72" size 22 color "#ffffff" xalign 0.5
                text "70" size 22 color "#ffffff" xalign 0.5

            null height 8

            text "Изменение среднего результата:":
                size 22
                color "#ffffff"
                xalign 0.5

            text "Группа дополнительных занятий: +14 баллов\nГруппа без дополнительных занятий: +5 баллов":
                size 23
                color "#b9d9ff"
                xalign 0.5
                text_align 0.5

            text "Важно: группы сформировались по желанию студентов, а не случайным распределением.":
                size 19
                color "#ffcf8a"
                xalign 0.5
                text_align 0.5
                xmaximum 900

            textbutton "Перейти к интерпретации":
                xalign 0.5
                text_size 23
                action Return()




label experiment:

    $ experiment_score = 0
    $ experiment_answers = {}

    scene black with Dissolve(0.7)

    "На экране появляется рабочая область. Передо мной несколько наборов карточек."
    "Нужно собрать план исследования: сформулировать гипотезу, определить группы, выбрать показатели и способ сравнения."
    "После этого откроются результаты эксперимента, которые предстоит интерпретировать."

    

    $ experiment_choice_1 = renpy.call_screen(
        "experiment_choice",
        "Этап 1. Гипотеза",
        "Какую гипотезу мы хотим проверить?",
        [
            ("correct", "Дополнительные занятия повышают средний результат студентов на итоговом тестировании."),
            ("wrong1", "Все студенты, посещающие дополнительные занятия, обязательно сдадут экзамен."),
            ("wrong2", "Студенты с высокими оценками чаще интересуются математикой."),
            ("wrong3", "Дополнительные занятия полезны, потому что преподаватели считают их полезными.")
        ]
    )

    $ experiment_answers["hypothesis"] = experiment_choice_1

    if experiment_choice_1 == "correct":
        $ experiment_score += 1
        "Гипотеза сформулирована проверяемым образом: можно сравнить результаты студентов и оценить эффект дополнительных занятий."
    else:
        "Такая формулировка не позволяет корректно проверить влияние дополнительных занятий."
        "Нам нужна конкретная гипотеза, которую можно проверить на данных."

    

    $ experiment_choice_2 = renpy.call_screen(
        "experiment_choice",
        "Этап 2. Группы",
        "Как лучше сформировать экспериментальную и контрольную группы?",
        [
            ("correct", "Случайным образом распределить студентов: одна группа посещает занятия, другая — нет."),
            ("wrong1", "В экспериментальную группу включить желающих заниматься, в контрольную — всех остальных."),
            ("wrong2", "В экспериментальную группу включить лучших студентов, в контрольную — студентов с низкими оценками."),
            ("wrong3", "Сравнить студентов одного курса с выпускниками другого курса.")
        ]
    )

    $ experiment_answers["groups"] = experiment_choice_2

    if experiment_choice_2 == "correct":
        $ experiment_score += 1
        "Случайное распределение помогает сделать группы сопоставимыми и уменьшить влияние посторонних факторов."
    else:
        "При таком формировании групп они могут изначально отличаться по важным характеристикам."
        "Например, мотивация и начальный уровень знаний способны повлиять на итоговые результаты."

    

    $ experiment_choice_3 = renpy.call_screen(
        "experiment_choice",
        "Этап 3. Показатели",
        "Что следует измерять, чтобы оценить эффект дополнительных занятий?",
        [
            ("correct", "Результаты одинакового тестирования до и после занятий."),
            ("wrong1", "Количество студентов, которым понравились дополнительные занятия."),
            ("wrong2", "Мнение преподавателя о том, насколько хорошо группа усвоила тему."),
            ("wrong3", "Количество часов, проведённых студентами в университете.")
        ]
    )

    $ experiment_answers["indicators"] = experiment_choice_3

    if experiment_choice_3 == "correct":
        $ experiment_score += 1
        "Хороший выбор. Измерения до и после занятий позволяют оценить изменение результатов."
    else:
        "Этот показатель не позволяет напрямую оценить изменение знаний."
        "Нужна единая измеримая метрика, применяемая к обеим группам."

    

    $ experiment_choice_4 = renpy.call_screen(
        "experiment_choice",
        "Этап 4. Сравнение",
        "Какой способ анализа лучше подходит для поставленной задачи?",
        [
            ("correct", "Сравнить изменение результатов до и после занятий в обеих группах."),
            ("wrong1", "Сравнить только итоговые оценки двух групп, не учитывая начальный уровень."),
            ("wrong2", "Выбрать несколько самых высоких оценок и сравнить их."),
            ("wrong3", "Сравнить результаты только тех студентов, которые посещали каждое занятие.")
        ]
    )

    $ experiment_answers["comparison"] = experiment_choice_4

    if experiment_choice_4 == "correct":
        $ experiment_score += 1
        "Верно. Сравнение изменений позволяет учитывать исходный уровень результатов."
    else:
        "Такое сравнение может дать искажённую картину."
        "Важно учитывать не только итоговые результаты, но и то, с какого уровня начинали участники."

    
    if experiment_score == 4:
        $ experiment_result_level = "excellent"
        call screen experiment_feedback(
            "План исследования готов",
            "Все четыре элемента выбраны правильно. Получился последовательный план: проверяемая гипотеза, сопоставимые группы, измеримые показатели и корректный способ сравнения."
        )
    elif experiment_score >= 2:
        $ experiment_result_level = "good"
        call screen experiment_feedback(
            "План исследования готов",
            "Основные элементы выбраны верно, но некоторые решения могут повлиять на достоверность результатов. В реальном исследовании такие детали важно продумывать заранее."
        )
    else:
        $ experiment_result_level = "needs_work"
        call screen experiment_feedback(
            "План исследования готов",
            "В плане есть существенные недочёты. Самое время посмотреть, как они могут повлиять на интерпретацию данных."
        )

    

    "После завершения планирования мне показывают результаты условного исследования."
    call screen experiment_results_table

    "На первый взгляд дополнительные занятия действительно связаны с более заметным улучшением результатов."
    "Но я замечаю одну деталь: группы сформировались по желанию студентов, а не случайным распределением."
    "Возможно, те, кто записался на дополнительные занятия, изначально были более мотивированы или имели другие особенности."

    

    $ experiment_choice_5 = renpy.call_screen(
        "experiment_choice",
        "Этап 5. Интерпретация результатов",
        "Какой вывод можно сделать по представленным данным?",
        [
            ("correct", "Участники дополнительных занятий улучшили результаты сильнее, но нельзя уверенно утверждать, что причиной стали именно занятия."),
            ("wrong1", "Дополнительные занятия доказанно повышают успеваемость каждого студента."),
            ("wrong2", "Дополнительные занятия не имеют никакого эффекта, поскольку группы изначально различались."),
            ("wrong3", "Разница в изменении результатов автоматически доказывает причинно-следственную связь.")
        ]
    )

    $ experiment_answers["interpretation"] = experiment_choice_5

    if experiment_choice_5 == "correct":
        $ experiment_score += 1
        call screen experiment_feedback(
            "Верный вывод",
            "Именно так. Мы наблюдаем различие в изменении результатов, но само по себе оно не доказывает причинный эффект дополнительных занятий. Добровольный выбор участия мог быть связан с мотивацией, подготовкой и другими факторами."
        )
    else:
        call screen experiment_feedback(
            "Не совсем",
            "Данные показывают, что группа дополнительных занятий улучшила результат сильнее. Но участники сами выбирали, посещать занятия или нет. Поэтому группы могли отличаться ещё до начала исследования, и мы не можем однозначно приписать разницу именно занятиям."
        )

    

    if experiment_score == 5:
        $ grig_score+=1
        "Я внимательно проверяю все этапы. Похоже, план исследования получился довольно убедительным."
    elif experiment_score >= 3:
        "Я ещё раз просматриваю свои решения. Некоторые моменты стоило продумать внимательнее, но общая логика исследования теперь понятна."
    else:
        "Я смотрю на собранный план и понимаю, сколько нюансов можно упустить ещё до начала сбора данных."

    you "Результаты получились интересными, хотя не совсем такими, как я ожидал."
    you "Главное, что теперь понятно: даже правильно рассчитанные показатели не спасут исследование, если изначально неправильно поставлен вопрос."

    jump ending

label ending:
    scene room with fade
    "Cуббота..."
    "Последняя неделя пролетела очень быстро."
    "За это время я успел поработать с данными, попробовать себя в прикладной задаче, провести занятие для школьников и даже немного прикоснуться к фундаментальной математике."
    "Сегодня особых планов нет. Нужно закончить несколько оставшихся дел и наконец привести мысли в порядок."
    "На столе лежат конспекты, распечатки и материалы, которые я собирал всю неделю."
    "Странно. Ещё недавно всё это казалось просто очередными университетскими обязанностями."

    "В голове постепенно всплывают прошедшие дни."
    "Владимир Иванович и его бесконечные замечания к статистическим выводам."
    "Евгений Георгиевич, который смотрит на математические модели прежде всего с точки зрения их применения."
    "Максим Дмитриевич, которому, кажется, никогда не надоест объяснять одну и ту же тему."
    "И Григорий Яковлевич, для которого математика существует сама по себе, независимо от того, где и когда её удастся применить."
    "У каждого из них свой подход. И, пожалуй, каждый по-своему прав."

    $ all_score = ev_score+maks_score+grig_score+vlad_score
    if all_score == 8:
        jump harem_root
    elif max(vlad_score, ev_score, grig_score, maks_score) == vlad_score and vlad_score == 2:
        jump vlad_end
    elif max(vlad_score, ev_score, grig_score, maks_score) == maks_score and maks_score == 2:
        jump maks_end
    elif max(vlad_score, ev_score, grig_score, maks_score) == grig_score and grig_score == 2:
        jump grig_end
    elif all_score == 0:
        jump bad_root
    elif max(vlad_score, ev_score, grig_score, maks_score) == ev_score and ev_score == 2:
        jump ev_end



label harem_root:
    "За эту неделю я осознал всю силу математики, поэтому теперь знаю..."
    "Что свяжу свою жизнь со всеми направлениями этой замечательной науки."
    "А помогут мне мои преподаватели!"
    scene black with Dissolve(3.0)
    "КОНЕЦ. ИСТИННАЯ КОНЦОВКА."
    return

label vlad_end:
    "За эту неделю я полностью осознал свою любовь к статитике."
    "Именно поэтому я пойду в аспирантуру к Владимиру Ивановичу!"
    scene black with Dissolve(3.0)
    "КОНЕЦ. КОНЦОВКА ВЛАДИМИРА ИВАНОВИЧА."
    return

label maks_end:
    "За эту неделю я осознал важность массовой обработки данных."
    "Именно поэтому я стану аспирантом на кафедре машинного обучения!"
    scene black with Dissolve(3.0)
    "КОНЕЦ. КОНЦОВКА МАКСИМА ДМИТРИЕВИЧА."
    return

label grig_end:
    "За эту неделю я осознал, насколько ещё не познан мир."
    "Осознал, насколько важна математика."
    "Поэтому направлением поступления я выберу кафедру Григория Яковлевича!"
    scene black with Dissolve(3.0)
    "КОНЕЦ. КОНЦОВКА ГРИГОРИЯ ЯКОВЛЕВИЧА."
    return

label bad_root:
    "Эта неделя показала низкий уровень моих знаний..."
    "Наверное, мне не стоило поступать в технический ВУЗ..."
    scene black with Dissolve(3.0)
    "КОНЕЦ. ПЛОХАЯ КОНЦОВКА."
    return

label ev_end:
    "Эта неделя показала важность использования математики в реальных задач."
    "Поэтому я свяжу свою жизнь с экономикой!"
    scene black with Dissolve(3.0)
    "КОНЕЦ. КОНЦОВКА ЕВГЕНИЯ ГЕОРГИЕВИЧА."
    return
