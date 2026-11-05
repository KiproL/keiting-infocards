# Карты миграции материалов

Здесь записывается каждое изменение, которое затрагивает индексы слайдов, состав слайда или привязку заданий к целям. Каждая запись отмечена как совместимая (опубликована) или несовместимая (не публикуется до поддержки в приложении).

Механизм приложения, на который опираются записи (GENERAL-THEORY.md): новая `editorial_revision` карточки сбрасывает оценку памяти FSRS по её целям, но сохраняет исторические попытки. Старое завершение не перепланирует новую редакцию.

## M-001. cards_articles: ред. 2 → 3 — совместимо, опубликовано

Индексы 0–4 сохранены, их темы не изменились. Слайды 5 и 6 добавлены в конец. Ни один старый индекс не исчез и не сдвинулся.

### Слайды

| Старый слайд (ред. 2) | Новый слайд (ред. 3) | Изменение смысла | Подтверждает ли старый результат знание |
|---|---|---|---|
| 0 «a / an, the или ничего» | 0 | сужен: обобщение «a rabbit» убрано (тема — в cards_genericarticles) | да, основы те же |
| 1 «a / an: какой-то один» | 1 | «a water» в кафе и сложные слова вынесены в необязательные блоки | да |
| 2 «the: тот самый» | 2 | превосходная степень и порядковые числа перенесены на слайд 5 | частично: основы the — да, превосходная степень — нужна проверка на слайде 5 |
| 3 «Когда артикль не нужен» | 3 | реки, моря и «the rich» убраны (они в cards_articlesnames и cards_genericarticles); тонкость «the school» — на слайде 6 | частично: «вообще / конкретно» и имена — да; география и the + прилагательное — нужна проверка в своих карточках |
| 4 «Артикли: всё на одной странице» | 4 | только основы; инструменты и спорт — на слайде 6 | да, кроме инструментов |
| — | 5 «The с превосходной степенью» (A2) | новый | нет прежних данных |
| — | 6 «School, bed, bus» (A2) | новый | нет прежних данных |

Опубликованная до этого редакция 0 имела те же 5 слайдов с теми же темами, поэтому карта для перехода 0 → 3 такая же.

### Перепривязка заданий (ID не менялись)

| ID | Было | Стало |
|---|---|---|
| determinants_2_n4, _2_n5, _2_n6, _2_n10, _2_n13; articles_2_m11, _2_m13, _2_m16 | cards_articles#2 | cards_articles#5 |
| determinants_4_3, _4_n8, _4_n9, _9_n12 | cards_articles#4 | cards_articles#6 |
| determinants_3_n7 | cards_articles#3 | cards_articles#2 (переписано: «the sun») |
| determinants_3_n5, articles_3_m23 | cards_articles#3 | cards_articlesnames#0 |
| determinants_3_n6, _3_n13, articles_3_m22 | cards_articles#3 | cards_articlesnames#1 |
| determinants_3_n10, _9_n14 | cards_articles#3 / #4 | cards_genericarticles#1 |
| determinants_3_n11 | cards_articles#3 | cards_genericarticles#2 |

В части заданий изменён текст при сохранении ID: добавлен контекст, заменены дубли. Полный список — в PROGRESS.md.

### Что нужно от приложения

Обязательной доработки нет: изменение укладывается в существующий механизм редакций. Желательно:

1. Не засчитывать исторические попытки перепривязанных заданий новой цели. Прежняя попытка по `determinants_2_n4` относилась к cards_articles#2, а не #5. По описанию TheoryLearningSession результат учитывается по карточке и слайду на момент ответа — это нужно подтвердить.
2. Обновить тестовые ресурсы `test/resources/learning/curriculum.json` и `foundation_cards.json`, если тесты должны совпадать с опубликованным планом. Там остались ред. 2 и прежний состав `a1_article_reference` [2, 3, 4].
3. Временная копия cards_articles ред. 2 в `assets/learning/cards.json` больше не нужна. CardLoader и так возьмёт ред. 3 как более новую. Удаление — по CONTENT-DELIVERY.md.

## M-002. cards_pluralnouns: ред. 2 → 3 — совместимо, опубликовано

Индексы 0–5 сохранены, их темы не изменились. Слайд 6 добавлен в конец. Изменены подписи слайдов 1 («+s, +es и y → ies») и 2 («Слова на -o и -f»). Подпись — только заголовок; цель определяется `route#slide`.

| Старый слайд | Новый | Изменение смысла | Подтверждает ли старый результат знание |
|---|---|---|---|
| 0 «Один и много» | 0 | сужен до числа и is/are, this/these; задания на особые формы ушли на свои слайды | частично: is/are — да; старые задания слайда 0 проверяли и другие правила |
| 1 «+s или +es» | 1 | добавлено правило y → ies со слайда 2 | да для +s/+es; y → ies — нужна проверка |
| 2 «Слова на -o, -y и -f» | 2 | убраны -y и редкие исключения | да для -o/-f |
| 3 «Особые формы» | 3 | латинские формы и ox ушли на слайд 6 | да для частых форм |
| 4, 5 | 4, 5 | уточнены; police — в необязательный блок | да |
| — | 6 «Редкие формы» (B1) | новый | нет прежних данных |

Перепривязка заданий:

| ID | Было | Стало |
|---|---|---|
| pluralnouns_0_0, _0_n1, _0_5, _0_n12 | #0 | #1 |
| pluralnouns_0_n13 | #0 | #2 |
| pluralnouns_0_1, _0_n2, _0_4, _0_n3, _0_n9, _0_n11 | #0 | #3 |
| pluralnouns_0_2, _0_n14, _0_n8, _0_3 | #0 | #4 |
| pluralnouns_2_n2, _2_n3, _2_n4, _2_n7, _2_n12, _2_n14, foundation_pluralnouns_2_0_v1 | #2 | #1 |
| pluralnouns_3_n11, _3_n12, _3_n13, _3_n14 | #3 | #6 |
| pluralnouns_0_n4, _0_n5, _5_n3, _5_n4, _5_n7, _5_n8 | cards_pluralnouns#0 / #5 | cards_presentsimp#2 |

Учебная часть a1_nouns_variants изменила состав с [2, 3, 4, 5] на [3], ID сохранён. Части черновые и ещё не подключены к маршруту, поэтому прогресса по ним нет.

## M-003. cards_presentsimp: ред. 1 → 2 — совместимо, опубликовано

Все 5 индексов и темы сохранены, слайды не добавлялись. Слайд 0 сужен: сравнение с Present Continuous перенесено в необязательный блок, результаты по основам слайда 0 остаются свидетельством.

Перепривязка заданий: `presentsimp_0_4` перенесено с #0 на #1 (отрицание). Шесть заданий пришли из cards_pluralnouns (см. M-002).

Часть a1_simple_routines изменила состав с [0, 1, 2, 4] на [0, 2]; добавлены a1_simple_questions [1] и a1_simple_review [4].

### Что нужно от приложения для M-002 и M-003

То же, что в M-001: попытки по перепривязанным заданиям не засчитывать их новым целям; обновить тестовые копии плана и карточек. В тестовом `foundation_cards.json` и `assets/learning/cards.json` остались pluralnouns ред. 2 и presentsimp ред. 1. CardLoader возьмёт опубликованные редакции как более новые.

## M-004. cards_articlesadv: дублирование — ПРЕДЛОЖЕНИЕ, не выполнено

cards_articlesadv почти полностью повторяет две другие карточки: его слайды 1–3 совпадают с cards_genericarticles 0–2, а слайды 4–5 — с cards_articlesnames 1–2. Один и тот же материал получает две независимые цели, и прохождение одной не учитывает другую.

Варианты (нужно решение пользователя и разработчика приложения):

- **А. Оставить маршрут и превратить карточку в обзорно-проверочную.** «Трудные случаи» на смешанных заданиях, без повтора теории. Совместимо, если сохранить число слайдов, но меняет смысл слайдов 1–5. Нужна повторная проверка, а карта соответствия старого прогресса — как в M-001.
- **Б. Вывести карточку из маршрута курса.** Оставить в справочнике, не включать в учебные части. Совместимо. Старый прогресс по articlesadv можно учитывать как свидетельство по соответствующим слайдам двух других карточек — для этого нужна поддержка приложения.

До решения карточка не изменяется.

## M-005. Партия 3: alphabet 0 → 1, readingrules 0 → 1, thereisare 1 → 2 — совместимо, опубликовано

У всех трёх карточек сохранены индексы и темы слайдов, новых слайдов нет. Старые результаты по слайдам остаются свидетельством той же темы. Повторная проверка нужна только из-за механизма редакций.

Перепривязка заданий: `thereisare_0_3`, `thereisare_0_4`, `thereisare_0_5` перенесены с cards_thereisare#0 на #1 (вопрос и отрицание).

В alphabet 25 заданий сохранили ID, но получили новый текст: прежний текст проверял копирование буквы. Исторические попытки по этим ID относятся к старому содержанию и не должны подтверждать знание названий букв. При смене редакции карточки приложение это уже учитывает.

Выполнять миграцию со стороны приложения не нужно.

## M-006. Партия 4 — совместимо, опубликовано

Ни у одной карточки не сдвинулся и не исчез существующий индекс.

| Карточка | Редакция | Слайды |
|---|---|---|
| cards_prepositions | 1 → 2 | добавлены 6, 7, 8 (зависимые предлоги) |
| cards_pronouns | 0 → 1 | состав прежний, 9 |
| cards_aboutme | 1 → 2 | состав прежний, 4 |
| cards_asas | 1 → 2 | состав прежний, 2 |
| cards_presentcont | 1 → 2 | состав прежний, 6 |
| cards_comparisons | 1 → 2 | состав прежний, 6 |
| cards_questions | 0 → 1 | состав прежний, 8 |
| cards_determinants | 0 → 1 | состав прежний, 7 |

### Перепривязка заданий (ID не менялись)

**cards_prepositions.** Задания о зависимых предлогах переведены со слайдов, где их тема не объясняется:

| Было | Стало |
|---|---|
| #0, #2, #5 — глагол + предлог (depend on, wait for, enter) | #6 |
| #0, #1, #5 — прилагательное + предлог (good at, afraid of, proud of, married to) | #7 |
| #3, #5 — существительное + предлог (reason for, increase in) | #8 |

Полный список — в `sentences/*.json` по полю `slide`. Старые результаты этих заданий относились к слайдам места и времени, а проверяли другое. Их нельзя считать свидетельством ни для старой, ни для новой цели.

**cards_pronouns:** 17 заданий со слайда 0 переведены на слайды 2–7 по теме.

**cards_questions:** 11 заданий со слайда 0 переведены на слайды 1, 2, 3 и 5.

**cards_presentcont:** `presentcont_0_4`, `presentcont_0_5` — с #0 на #1.

**В другие карточки:**

| Задания | Было | Стало |
|---|---|---|
| `aboutme_0_n14`, `aboutme_3_n4`, `aboutme_3_n9`, `aboutme_3_n13` | cards_aboutme | cards_presentperf#2 |
| `aboutme_2_n10` | cards_aboutme | cards_presentperfcont#2 |
| `comparisons_4_n6`, `comparisons_4_n7`, `comparisons_4_n8` | cards_comparisons | cards_comparativesadv#2 |

### Что нужно от приложения

То же, что в M-001: не засчитывать исторические попытки перепривязанных заданий их новым целям. Обновить тестовые копии prepositions, presentcont, comparisons, aboutme и asas в `assets/learning/cards.json`: опубликованные редакции новее, и CardLoader возьмёт их сам.

## M-007. Партия 5 — совместимо, опубликовано

У всех восьми карточек сохранены индексы и темы слайдов, новых слайдов нет: imperative, havegot, botheither, greetings, family, numbers, pastsimp, modalverbs (все 0 → 1).

Перепривязка заданий (ID не менялись):

| Задания | Было | Стало |
|---|---|---|
| `greetings_3_n0` … `greetings_3_n14` | #3 | #5 (ошибки) |
| `family_3_n0` … `family_3_n14` | #3 | #5 (ошибки) |
| `pastsimp_0_2`, `pastsimp_0_3` | #0 | #1 |

В botheither у шести заданий (`botheither_1_0` … `botheither_1_5`) убран второй пропуск, ответ прежний.

Выполнять миграцию со стороны приложения не нужно; правило о перепривязанных заданиях — как в M-001.

## M-008. Партия 6 — совместимо, опубликовано

У всех восьми карточек сохранены индексы и темы слайдов, новых слайдов нет: timemoney, wordorder, directions, shopping, restaurant, weather, food, jobs (все 0 → 1).

Перепривязка заданий (ID не менялись):

| Задания | Было | Стало |
|---|---|---|
| `timemoney_4_n0` … `timemoney_4_n14` | #4 | #6 (ошибки) |
| `directions_2_n0` … `directions_2_n14` | #2 | #4 (ошибки) |
| `shopping_3_n0` … `shopping_3_n14` | #3 | #5 (ошибки) |
| `restaurant_3_n0` … `restaurant_3_n14` | #3 | #5 (ошибки) |
| `weather_3_n0` … `weather_3_n14` | #3 | #5 (ошибки) |
| `food_3_*`, кроме `food_3_n4`, `food_3_n5`, `food_3_n13` | #3 | #5 (ошибки) |
| `jobs_3_n0` … `jobs_3_n14` | #3 | #5 (ошибки) |

Новые задания получили ID вида `<карточка>_r1_<слайд>_<n>`.

В `wordorder_0_0`, `0_1`, `0_3`, `0_4` пропуск расширен с глагола до «глагол + дополнение». Поля конструктора `words`, `ruShort` и `hint` не менялись. Поле `base` удалено у `0_1` и `0_4`: подсказка формы глагола к новому пропуску не подходит.

Выполнять миграцию со стороны приложения не нужно. Правило о перепривязанных заданиях — как в M-001.

## M-009. Названия слайдов, карточек и частей — совместимо, опубликовано

У 30 карточек партий 1–6 изменены названия слайдов (`label`), у 11 карточек — `tenseName`. Индексы слайдов, ID и редакции не менялись: название слайда в приложении служит только заголовком, цель обучения адресуется как `route#индекс`.

Редакцию не повышали. Повышение сбросило бы память FSRS по целям карточки, а смысл слайдов не менялся.

Если какая-то из этих редакций уже вшита в APK, новые названия придут в приложение только с обновлёнными вшитыми данными: загрузчик берёт сетевую копию, только если её редакция выше.

Названия 36 учебных частей в `tree/curriculum.json` укорочены, ID частей прежние.

**Нужно от приложения (рекомендация):** в шапке читалки (`ReaderHeader` → `ScreenHeader`) разрешить заголовку две строки, например параметр `maxLines = 2` или шрифт 20sp для названия слайда. Сейчас там одна строка 24sp, и на экране 360 dp помещается 12–15 букв.

## M-010. Партия 7 — совместимо, опубликовано

У всех восьми карточек сохранены индексы и темы слайдов, новых слайдов нет: appearance, body, clothes, home, hobbies, emotions, study, technology (все 0 → 1).

Перепривязка заданий (ID не менялись):

| Задания | Было | Стало |
|---|---|---|
| `appearance_4_n0` … `appearance_4_n14` | #4 | #6 (ошибки) |
| `body_3_*`, `clothes_3_*`, `home_3_*`, `hobbies_3_*`, `emotions_3_*`, `study_3_*`, `technology_3_*` | #3 | #5 (ошибки) |

Новые задания получили ID вида `<карточка>_r1_<слайд>_<n>`.

Выполнять миграцию со стороны приложения не нужно. Правило о перепривязанных заданиях — как в M-001.

## M-011. Вёрстка правил и таблиц — совместимо, опубликовано

В 12 карточках партий 1–7 изменён текст 50 строк правил, ячеек таблиц и ошибок. Где у правила короткий термин, название и пояснение поменялись местами. Индексы слайдов, ID и редакции не менялись.

Редакцию не повышали: смысл тот же, а повышение сбросило бы память FSRS.

**Рекомендация для приложения.** `RuleLine` отдаёт пояснению справа всю нужную ему ширину, и название слева может сжаться до одной буквы. Надёжнее ограничить пояснение, например `Modifier.weight(1f, fill = false)`. Сейчас это предотвращают только короткие пояснения в данных.

## M-012. Партия 8 — совместимо, опубликовано

У всех восьми карточек сохранены индексы и темы слайдов, новых слайдов нет: britishamerican, collocations, idioms, strongadjectives, begoingto, therewaswere, wouldlike, fewlittle (все 0 → 1).

Перепривязка заданий (ID не менялись):

| Задания | Было | Стало |
|---|---|---|
| `collocations_3_n0` … `collocations_3_n14` | #3 | #5 (ошибки) |
| `strongadjectives_2_n0` … `strongadjectives_2_n14` | #2 | #4 (ошибки) |

Новые задания получили ID вида `<карточка>_r1_<слайд>_<n>`.

Выполнять миграцию со стороны приложения не нужно.

## M-013. Доработка партии 5: редакции 1 → 2 — совместимо, опубликовано

imperative, havegot, botheither, greetings, family, numbers, pastsimp, modalverbs: редакция 2, индексы слайдов прежние.

У numbers в конец добавлен слайд 6 «Дроби и проценты». На него перепривязаны задания: `numbers_4_n2`, `numbers_4_n3`, `numbers_4_n4`, `numbers_4_n5`, `numbers_4_n10`, `numbers_4_n11`, `numbers_4_n12`, `numbers_4_n14` (#4 → #6). Слайд 4 теперь только «Даты и годы». Новая часть `a2_numbers_fractions`.

Редакция повышена из-за содержательных изменений: память FSRS по целям этих карточек сбросится по обычному правилу приложения, история сохраняется. Других действий от приложения не нужно.

## M-014. Доработка партии 6: редакции 1 → 2 — совместимо, опубликовано

timemoney, wordorder, directions, shopping, restaurant, weather, food, jobs: редакция 2. Индексы слайдов и привязка заданий прежние. Память FSRS по целям сбросится по обычному правилу.

## M-015. Доработка партии 7: редакции 1 → 2 — совместимо, опубликовано

appearance, body, clothes, home, hobbies, emotions, study, technology: редакция 2. Индексы слайдов и привязка заданий прежние.

## M-016. Доработка партии 8: редакции 1 → 2 — совместимо, опубликовано

britishamerican, collocations, idioms, strongadjectives, begoingto, therewaswere, wouldlike, fewlittle: редакция 2. Индексы слайдов и привязка заданий прежние.

## M-017. Партия 9 — совместимо, опубликовано

genericarticles, articlesnames, usedto, therewillbe, pastcont, futuresimp, presentperf, alreadyyet, contractions: редакция 0 → 1. Индексы и темы прежних слайдов сохранены.

У usedto в конец добавлен слайд 2 «Used to или be used to». На него перепривязаны задания `usedto_0_n6`, `usedto_0_5`, `usedto_0_n10`, `usedto_0_n14` (#0 → #2).

В `articlesnames_1_5` второй пропуск убран, ответ прежний. Новые задания получили ID вида `<карточка>_r1_<слайд>_<n>`. Действий от приложения не нужно.

## M-018. Стандарт частей: показательные темы — совместимо, опубликовано

Части пересобраны по правилам из PARTS.md: делим только по уровню или по навыку, на который ссылаются другие темы. «Проверка» и «… в речи» входят в свою часть.

**Части.** Ни один слайд не потерял часть, ни один не попал в две.

| Было | Стало | Слайды новой части |
|---|---|---|
| `a1_there_core`, `a1_there_questions`, `a1_there_review` | `a1_there_core` | thereisare 0, 1, 2 |
| `a2_perfect_meaning`, `a2_perfect_negq`, `a2_perfect_markers`, `a2_perfect_v3`, `b1_perfect_vs_past`, `a2_perfect_review` | `a2_perfect_meaning` (A2) | presentperf 0–5 |
| — (новые слайды) | `b1_perfect_time` (B1) | presentperf 6, 7 |
| `a1_nouns_core`, `a1_nouns_variants` | `a1_nouns_core` | pluralnouns 0, 1, 3 |
| `a2_nouns_spelling`, `a2_nouns_uncountable`, `a2_nouns_review` | `a2_nouns_special` | pluralnouns 2, 4, 5 |
| `b1_nouns_rare` (B1) | `b2_nouns_rare` (B2) | pluralnouns 6 |

**Перенаправленные предпосылки других частей:**
- `a2_det_many_much` и `a2_jobs_work_job`: `a2_nouns_uncountable` → `a2_nouns_special`;
- `a2_therewillbe_core` и `a1_therewas_negq`: `a1_there_questions` → `a1_there_core`.

**Почему это не ломает прогресс.**
- Результаты хранятся по шагам `route#slide` с редакцией (CurriculumResults, CurriculumGraph.checked). Статус части вычисляется из её шагов. Объединение частей ничего не теряет и ничего не засчитывает заранее.
- У новых шагов presentperf#6 и #7 результатов нет.
- Редакции presentperf (1 → 2) и pluralnouns (3 → 4) повышены, поэтому память по их шагам сбросится по обычному правилу.
- Сохранённая незавершённая проверка с удалённым ID части не пройдёт `CourseCheckpoint.permitted`. Экран сообщит, что материалы изменились. Но все части сейчас Draft, поэтому таких проверок быть не может.

**presentperf, редакция 2.**
- В конец добавлены слайды 6 «Закончилось или нет» и 7 «Since, for, how long».
- Слайд 2 больше не объясняет since и for: это перенесено на слайд 7. Цель шага #2 сузилась до just, yet, ever, never.
- Слайд 4 остался A2: «время названо — Past Simple». Американский вариант перенесён на слайд 6.

Перепривязка заданий (ID не менялись):

| Задания | Было | Стало |
|---|---|---|
| `presentperf_2_n6`, `_2_n7`, `_2_n8`, `_2_n9`, `_2_n11`, `_2_n12`; `aboutme_3_n4`, `aboutme_3_n9`, `aboutme_0_n14`, `aboutme_3_n13` | #2 | #7 |
| `presentperf_0_n9` | #0 | #7 |
| `presentperf_4_n8`, `presentperf_4_n12` | #4 | #7 |
| `presentperf_5_n8`, `presentperf_5_n9`, `presentperf_5_n10` | #5 | #7 |
| `presentperf_4_n7`, `presentperf_4_n9` | #4 | #6 |

- `presentperf_3_n8`: предложение заменено на «We have [studied] all the new words.» Ответ прежний.
- Новые задания:
  - `presentperf_r2_6_0` … `presentperf_r2_6_5`;
  - `presentperf_r2_7_0`, `presentperf_r2_7_1`.
- Новый error_pattern `error:presentperf.duration`. Им помечены задания на «длится до сих пор». У всех шаблонов `slides` пересчитаны по заданиям.

**pluralnouns, редакция 4.** Индексы слайдов и привязка заданий прежние. Исправлены три неестественных примера.

Действий от приложения для совместимости не нужно. Поддержка частей в интерфейсе — отдельное предложение в COMPONENTS.md.

## M-019. Стандарт частей: остальные 52 темы — совместимо, опубликовано

Части всех переработанных карточек пересобраны по правилам PARTS.md: было 249 частей, стало 108. Слайды, их индексы и задания не менялись. Каждый прежний ID перенаправлен в часть, которая теперь содержит все его слайды; предпосылки других частей переписаны по этой карте. Прогресс хранится по шагам route#slide, поэтому ничего не теряется и ничего не засчитывается заранее (подробно — M-018).

| Новая часть | Прежние части |
|---|---|
| `a1_article_introduction` (articles) | `a1_article_introduction` |
| `a1_article_reference` (articles) | `a1_article_reference`, `a1_article_zero`, `a1_article_choice` |
| `a2_article_special` (articles) | `a2_article_superlative`, `a2_article_institutions` |
| `a1_be_core` (presentsimp) | `a1_be_core` |
| `a1_simple_routines` (presentsimp) | `a1_simple_routines` |
| `a1_simple_questions` (presentsimp) | `a1_simple_questions`, `a1_simple_review` |
| `intro_alphabet_names` (alphabet) | `intro_alphabet_names`, `intro_alphabet_dictation` |
| `intro_reading_vowels` (readingrules) | `intro_reading_vowels`, `intro_reading_r`, `intro_reading_consonants`, `intro_reading_review` |
| `a1_pronouns_personal` (pronouns) | `a1_pronouns_personal`, `a1_pronouns_possessive`, `a1_pronouns_demonstrative`, `a1_pronouns_questions` |
| `a2_pronouns_reflexive` (pronouns) | `a2_pronouns_reflexive`, `a2_pronouns_one`, `a2_pronouns_review` |
| `b1_pronouns_relative` (pronouns) | `b1_pronouns_relative` |
| `a1_prep_place` (prepositions) | `a1_prep_place`, `a1_prep_position`, `a1_prep_time` |
| `a2_prep_direction` (prepositions) | `a2_prep_direction`, `a2_prep_review` |
| `a2_prep_verbs` (prepositions) | `a2_prep_verbs`, `a2_prep_adjectives` |
| `b1_prep_nouns` (prepositions) | `b1_prep_nouns` |
| `a1_aboutme_basics` (aboutme) | `a1_aboutme_basics`, `a1_aboutme_interests`, `a1_aboutme_story` |
| `a2_asas_core` (asas) | `a2_asas_core`, `a2_asas_review` |
| `a1_cont_core` (presentcont) | `a1_cont_core`, `a1_cont_spelling` |
| `a2_cont_vs_simple` (presentcont) | `a2_cont_states`, `a2_cont_vs_simple`, `a2_cont_review` |
| `a2_comparisons_degrees` (comparisons) | `a2_comparisons_degrees`, `a2_comparisons_long`, `a2_comparisons_irregular`, `a2_comparisons_than`, `a2_comparisons_review` |
| `a1_questions_yesno` (questions) | `a1_questions_yesno`, `a1_questions_wh`, `a1_questions_choice` |
| `a2_questions_subject` (questions) | `a2_questions_subject` |
| `a2_questions_tags` (questions) | `a2_questions_tags`, `a2_questions_review` |
| `b1_questions_tags_special` (questions) | `b1_questions_tags_special` |
| `a1_det_some_any` (determinants) | `a1_det_some_any` |
| `a2_det_many_much` (determinants) | `a2_det_negation`, `a2_det_compounds`, `a2_det_every_each`, `a2_det_many_much`, `a2_det_review` |
| `a1_imperative_core` (imperative) | `a1_imperative_core`, `a1_imperative_review` |
| `a2_imperative_polite` (imperative) | `a2_imperative_polite` |
| `a1_havegot_core` (havegot) | `a1_havegot_core` |
| `a2_havegot_vs_have` (havegot) | `a2_havegot_vs_have`, `a2_havegot_review` |
| `a2_both_either` (botheither) | `a2_both_either` |
| `b1_both_pairs` (botheither) | `b1_both_pairs`, `b1_both_review` |
| `a2_so_neither` (botheither) | `a2_so_neither` |
| `a1_greetings_hello` (greetings) | `a1_greetings_hello`, `a1_greetings_meet`, `a1_greetings_phrases`, `a1_greetings_review` |
| `a2_greetings_smalltalk` (greetings) | `a2_greetings_smalltalk` |
| `a1_family_core` (family) | `a1_family_core`, `a1_family_phrases`, `a1_family_review` |
| `a2_family_inlaws` (family) | `a2_family_inlaws`, `a2_family_relationships` |
| `a1_numbers_1_20` (numbers) | `a1_numbers_1_20` |
| `a1_numbers_big` (numbers) | `a1_numbers_big` |
| `a1_numbers_ordinal` (numbers) | `a1_numbers_ordinal` |
| `a2_numbers_dates` (numbers) | `a2_numbers_dates`, `a2_numbers_fractions`, `a2_numbers_review` |
| `a1_past_meaning` (pastsimp) | `a1_past_meaning`, `a1_past_ed` |
| `a1_past_forms` (pastsimp) | `a1_past_forms`, `a1_past_review` |
| `a1_past_irregular` (pastsimp) | `a1_past_irregular` |
| `a2_modals_can` (modalverbs) | `a2_modals_rules`, `a2_modals_can`, `a2_modals_may` |
| `a2_modals_must` (modalverbs) | `a2_modals_must`, `a2_modals_advice`, `a2_modals_review` |
| `b1_modals_past` (modalverbs) | `b1_modals_past` |
| `a1_time_clock` (timemoney) | `a1_time_clock`, `a1_time_dates`, `a1_money_prices`, `a1_timemoney_phrases`, `a1_timemoney_review` |
| `a2_measures` (timemoney) | `a2_measures` |
| `a1_wordorder_svo` (wordorder) | `a1_wordorder_svo` |
| `a2_wordorder_frequency` (wordorder) | `a2_wordorder_frequency`, `a2_wordorder_tail`, `a2_wordorder_also_enough`, `a2_wordorder_review` |
| `b1_wordorder_adjectives` (wordorder) | `b1_wordorder_adjectives` |
| `a1_directions_ask` (directions) | `a1_directions_ask`, `a1_directions_explain`, `a1_directions_practice`, `a1_directions_review` |
| `a1_shopping_choose` (shopping) | `a1_shopping_choose`, `a1_shopping_pay`, `a1_shopping_practice`, `a1_shopping_review` |
| `a2_shopping_return` (shopping) | `a2_shopping_return` |
| `a1_restaurant_arrive` (restaurant) | `a1_restaurant_arrive`, `a1_restaurant_order`, `a1_restaurant_bill`, `a1_restaurant_practice`, `a1_restaurant_review` |
| `a1_weather_words` (weather) | `a1_weather_words`, `a1_weather_talk`, `a1_weather_practice`, `a1_weather_review` |
| `a2_nature_words` (weather) | `a2_nature_words` |
| `a1_food_products` (food) | `a1_food_products`, `a1_food_taste_meals`, `a1_food_practice`, `a1_food_review` |
| `a2_food_cooking` (food) | `a2_food_cooking` |
| `a1_jobs_names` (jobs) | `a1_jobs_names`, `a1_jobs_talk` |
| `a2_jobs_work_job` (jobs) | `a2_jobs_work_job`, `a2_jobs_practice`, `a2_jobs_review` |
| `a1_appearance_looks` (appearance) | `a1_appearance_looks`, `a1_character` |
| `a2_appearance_order` (appearance) | `a2_appearance_order`, `a2_like_looklike`, `a2_appearance_practice`, `a2_appearance_review` |
| `a1_body_parts` (body) | `a1_body_parts`, `a1_body_ache`, `a1_body_practice`, `a1_body_review` |
| `a2_body_habits` (body) | `a2_body_habits` |
| `a1_clothes_words` (clothes) | `a1_clothes_words`, `a1_clothes_accessories` |
| `a2_clothes_verbs` (clothes) | `a2_clothes_verbs`, `a2_clothes_practice`, `a2_clothes_review` |
| `a1_home_rooms` (home) | `a1_home_rooms`, `a1_home_furniture`, `a1_home_practice` |
| `a2_home_chores` (home) | `a2_home_chores`, `a2_home_review` |
| `a1_hobbies_ing` (hobbies) | `a1_hobbies_ing`, `a1_hobbies_play_go_do`, `a1_hobbies_practice` |
| `a2_hobbies_talk` (hobbies) | `a2_hobbies_talk`, `a2_hobbies_review` |
| `a1_emotions_words` (emotions) | `a1_emotions_words` |
| `a2_emotions_prep` (emotions) | `a2_emotions_prep`, `a2_emotions_ed_ing`, `a2_emotions_practice`, `a2_emotions_review` |
| `a1_study_words` (study) | `a1_study_words`, `a1_study_classroom` |
| `a2_study_verbs` (study) | `a2_study_verbs`, `a2_study_practice`, `a2_study_review` |
| `a1_tech_words` (technology) | `a1_tech_words` |
| `a2_tech_verbs` (technology) | `a2_tech_verbs`, `a2_tech_problems`, `a2_tech_practice`, `a2_tech_review` |
| `a2_uk_us_words` (britishamerican) | `a2_uk_us_words`, `a2_uk_us_spelling` |
| `b1_uk_us_grammar` (britishamerican) | `b1_uk_us_grammar`, `b1_uk_us_sound`, `b1_uk_us_practice` |
| `a2_colloc_intro` (collocations) | `a2_colloc_intro`, `a2_colloc_verbs`, `a2_colloc_adjectives`, `a2_colloc_practice`, `a2_colloc_review` |
| `b1_idioms_intro` (idioms) | `b1_idioms_intro`, `b1_idioms_pairs`, `b1_idioms_register`, `b1_idioms_practice` |
| `a2_strongadj_words` (strongadjectives) | `a2_strongadj_words`, `a2_strongadj_very`, `a2_strongadj_practice`, `a2_strongadj_review` |
| `a1_goingto_form` (begoingto) | `a1_goingto_form` |
| `a2_goingto_will` (begoingto) | `a2_goingto_will`, `a2_goingto_review` |
| `a1_therewas_core` (therewaswere) | `a1_therewas_core`, `a1_therewas_negq`, `a1_therewas_review` |
| `a1_wouldlike_core` (wouldlike) | `a1_wouldlike_core`, `a1_wouldlike_questions`, `a1_wouldlike_review` |
| `a2_fewlittle_core` (fewlittle) | `a2_fewlittle_core`, `a2_fewlittle_talk`, `a2_fewlittle_review` |
| `b1_generic_kinds` (genericarticles) | `b1_generic_kinds`, `b1_generic_groups`, `b1_generic_abstract`, `b1_generic_review` |
| `a2_names_countries` (articlesnames) | `a2_names_countries`, `a2_names_geography` |
| `b1_names_city` (articlesnames) | `b1_names_city`, `b1_names_review` |
| `a2_usedto_core` (usedto) | `a2_usedto_core`, `a2_usedto_review` |
| `b1_usedto_vs_beused` (usedto) | `b1_usedto_vs_beused` |
| `a2_therewillbe_core` (therewillbe) | `a2_therewillbe_core`, `a2_therewillbe_review` |
| `a2_pastcont_core` (pastcont) | `a2_pastcont_core`, `a2_pastcont_negq`, `a2_pastcont_markers`, `a2_pastcont_ing`, `a2_pastcont_review` |
| `b1_pastcont_interrupt` (pastcont) | `b1_pastcont_interrupt` |
| `a1_future_will` (futuresimp) | `a1_future_will`, `a1_future_negq`, `a1_future_contractions` |
| `a2_future_will_goingto` (futuresimp) | `a2_future_markers`, `a2_future_will_goingto`, `a2_future_review` |
| `a2_alreadyyet_meaning` (alreadyyet) | `a2_alreadyyet_meaning`, `a2_alreadyyet_position`, `a2_alreadyyet_review` |
| `b1_alreadyyet_nuance` (alreadyyet) | `b1_alreadyyet_nuance` |
| `a1_contractions_core` (contractions) | `a1_contractions_core` |
| `a2_contractions_s_d` (contractions) | `a2_contractions_s_d`, `a2_contractions_full`, `a2_contractions_review` |

Редакции повышены из-за правки содержания: presentcont 2 → 3, pastsimp 2 → 3, pastcont 1 → 2, futuresimp 1 → 2 (ряды слов-маркеров стали подсказками с границами правила; у pastcont исправлен цвет Past Simple). Память по шагам этих карточек сбросится по обычному правилу. Действий от приложения не нужно.

## M-020. Партия 10 — совместимо, опубликовано

haveto, donthaveto, mustnt, needto, beableto, hadbetter, shall, irregularverbs: редакция 0 → 1. Индексы и темы прежних слайдов сохранены.

**be able to.**
- В конец добавлен слайд 2 «Could или was able to» (B1). Различие could и was able to перенесено туда со слайда 1. Цель шага beableto#1 сузилась до «can или be able to».
- Задание `beableto_1_4` перепривязано: #1 → #2.

**irregularverbs.** Задание `irregularverbs_1_n12` перепривязано: #1 → #3.

**Новые задания:** `beableto_r1_2_0` … `beableto_r1_2_5`.

**Новые части:**
- `a2_haveto_core`;
- `a2_mustnt_core`;
- `a2_donthaveto_core`;
- `a2_needto_core`;
- `a2_beableto_core`;
- `b1_beableto_past`;
- `a2_shall_core`;
- `b1_hadbetter_core`;
- `a2_irregular_forms`.

Действий от приложения не нужно.

## M-021. Партия 11 — совместимо, опубликовано

presentperfcont, pastperf, tooto, sosuch, wouldprefer, wouldrather, presentforfuture, timeclauses: редакция 0 → 1. Индексы, темы слайдов и привязка заданий прежние.

Новые части:
- `b1_ppc_core`;
- `b1_pastperf_core`;
- `a2_tooto_core`;
- `a2_enough` (sosuch 2);
- `b1_so_such` (sosuch 0, 1, 3);
- `b1_wouldprefer_core`;
- `b1_wouldrather_core`;
- `a2_present_future`;
- `b1_timeclauses_core`.

Действий от приложения не нужно.
