# Учебные части: описание и карты содержания

Документ по стандарту «Уточнение требований к содержанию и разделению карточек». Для каждой темы здесь записано, нужно ли её делить, и если нужно — описание каждой части и карта: где теперь каждый смысловой пункт исходной карточки.

Части задаются в `tree/curriculum.json` (id, level, title, slices, prerequisites, reviewed). Цель части дублируется в UNITS.md: в схеме для неё пока нет поля (см. COMPONENTS.md, раздел «Поддержка частей в интерфейсе»).

## Правила деления, по которым пересобраны части

1. **Делим только по необходимости.** Тема, у которой все слайды одного уровня и один навык, остаётся одной частью. Слайды внутри части остаются отдельными шагами проверки: приложение проверяет каждый слайд своими заданиями.
2. **Граница уровня — главная причина деления.** То, что нужно на более высоком уровне, выносится в отдельную часть с этим уровнем. Начальная часть получает ссылку на неё, а не сами тонкости.
3. **Отдельный навык того же уровня** выделяется в часть, только если на него ссылаются другие темы как на предпосылку или им пользуются независимо от остальной карточки.
4. **«Частые ошибки», «Примеры фраз», «Диалог» — не самостоятельные части.** Они входят в ту часть, материал которой закрепляют. Раньше они были отдельными частями «…: проверка» и «… в речи»: такая часть не имела собственного объяснения и была обрывком карточки.
5. **ID при объединении.** Объединённая часть сохраняет ID той части, на которую чаще ссылаются. Удалённые ID перенаправлены во всех предпосылках (MIGRATIONS.md, M-018). Прогресс хранится по шагам route#slide с редакцией, поэтому объединение не теряет и не засчитывает лишнего.

## Показательная тема 1 — простая: There is / There are (cards_thereisare, ред. 2)

**Делить не нужно.** Все три слайда — уровень A1 и один навык: сообщить о наличии. Было три части (`a1_there_core`, `a1_there_questions`, `a1_there_review`), стала одна.

| Часть | Уровень | Слайды | Учебная цель | Предпосылки | Дальше |
|---|---|---|---|---|---|
| `a1_there_core` «There is, there are» | A1 | 0, 1, 2 | Сообщить, что где-то есть предмет или предметы, построить отрицание и вопрос без do, отличить there is от it is | `a1_nouns_core` | There was / were (`a1_therewas_core`), There will be (`a2_therewillbe_core`) |

Проверка по стандарту:
- **Объяснение.** Слайд 0 начинается с ситуации: сообщить, что где-то что-то есть. Затем идёт форма. Есть границы правила:
  - перечисление (there is a desk and two chairs / there are…);
  - some не выбирает глагол;
  - there is или it is;
  - «в вопросах всегда any» — неверное правило.
- **Функции примеров:**
  - знакомство — «Живые примеры»;
  - изменение формы — перевод с русского, утверждение → отрицание → вопрос;
  - сравнение близких смыслов — there is или it is, вода или бутылки с водой;
  - типичная ошибка — слайд 2;
  - новая ситуация — a new reading room → the reading room is on the second floor.
- **Содержание не менялось.** Оно уже соответствует стандарту, поэтому редакция не повышалась.

## Показательная тема 2 — с разделением по уровням: Present Perfect (cards_presentperf, ред. 2)

**Делить нужно.** Карточка смешивала:
- A2 — результат, опыт, форма, V3, «время названо — Past Simple»;
- B1 — длительность с since/for, незаконченный период (today, this morning), вопросы с when, американский вариант.

Было шесть частей по одной на слайд. Стало две. В конец карточки добавлены слайды 6 и 7: так B1-часть идёт после всей A2-части и в обычной читалке.

| Часть | Уровень | Слайды | Учебная цель | Предпосылки | Дальше |
|---|---|---|---|---|---|
| `a2_perfect_meaning` «Present Perfect: результат» | A2 | 0–5 | Сказать о результате к сейчас и об опыте, построить отрицание, вопрос и краткий ответ, выбрать Past Simple, когда названо время | `a1_past_irregular`, `a1_past_forms` | `b1_perfect_time`; Already, yet, still (`a2_alreadyyet_meaning`) |
| `b1_perfect_time` «Present Perfect: период» | B1 | 6, 7 | Выбрать время по периоду, сообщить новость и перейти к подробностям, сказать, сколько длится состояние | `a2_perfect_meaning` | Present Perfect Continuous |

**Часть A2** — основные объяснения и примеры:
- результат и опыт на ситуации с ключами;
- have или has, отрицание, вопрос и краткие ответы;
- just, already, yet, ever, never по смыслу и месту в предложении;
- V3, been или gone;
- вопрос об опыте → ответ с подробностями в Past Simple.

**Часть A2** — ограничения и ошибки:
- закончившееся время (yesterday, ago) — Past Simple;
- маркер — подсказка, а не правило;
- ошибки: have went, do you have finished, I have seen him yesterday.

**Часть B1** — основные объяснения и примеры:
- период ещё идёт или закончился;
- this morning в зависимости от времени суток;
- сначала новость, потом подробности;
- вопрос с when;
- закончившаяся жизнь;
- never с закончившимся периодом;
- «живу пять лет» → I've lived here for five years;
- since или for, живу или жил, ago.

**Часть B1** — ограничения и ошибки:
- американский Past Simple с just, already, yet — вариант, а не ошибка;
- live и work допускают и Continuous, know — только Simple;
- ошибки: When have you arrived?, I live here for five years, since five years, I've moved here two years ago.

### Карта содержания

| Исходный пункт | Где теперь | Отметка |
|---|---|---|
| Определение «действие в прошлом, важно сейчас» (сл. 0) | A2, сл. 0 | исправлено: начинается с ситуации, затем смысл |
| Формула, have или has (сл. 0) | A2, сл. 0 | сохранено |
| Ряд маркеров verbGrid (сл. 0) | — | удалено как повтор: маркеры объясняются по смыслу на сл. 2 |
| «Три случая»: результат, опыт (сл. 0) | A2, сл. 0 «Результат и опыт» | сохранено |
| «Три случая»: началось и длится (сл. 0) | B1, сл. 7 | перенесено и раскрыто: перевод с русского, since или for, живу или жил |
| Утверждение, отрицание, вопрос, сокращения (сл. 1) | A2, сл. 1 | сохранено; вступление исправлено: говорило о другом |
| — | A2, сл. 1 | дополнено: краткие ответы, ошибки с do и does |
| Таблица маркеров just … never (сл. 2) | A2, сл. 2 | сохранено; дополнено местом в предложении |
| Маркеры since, for и правило since или for (сл. 2) | B1, сл. 7 | перенесено |
| «Маркер подсказывает время» (сл. 2) | A2, сл. 2 | исправлено: подсказка, а не правило; решает смысл |
| Правильные и неправильные V3, been или gone (сл. 3) | A2, сл. 3 | сохранено |
| Сравнение с Past Simple, пары примеров (сл. 4) | A2, сл. 4 | сохранено |
| «Если just, already… — обычно Present Perfect» (сл. 4) | A2, сл. 4 | исправлено: список слов закончившегося времени и ссылка на тонкости |
| Американский вариант с just, already, yet (сл. 4) | B1, сл. 6 | перенесено, уточнено: вариант, а не ошибка |
| Совет «Как запомнить» (сл. 4) | — | удалено как повтор вступления |
| — | A2, сл. 4 | дополнено: диалог «опыт → подробности» |
| — | B1, сл. 6 | дополнено: today, so far, this morning; новость и подробности; when; закончившаяся жизнь; never с закончившимся периодом |
| Частые ошибки (сл. 5) | A2, сл. 5 | сохранено; ошибки уровня B1 — на сл. 6 и 7 |
| Цвет: Past Simple был красным, как ошибка | сл. 4 | исправлено: красный только для ошибок и отрицания |

Задания перепривязаны по цели слайда, ID не менялись (M-018). Добавлено 8 заданий на слайды 6 и 7. Одно задание V3 переписано: оно проверяло форму на примере длительности.

### Источники

- British Council LearnEnglish: [Present perfect (B1–B2)](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/present-perfect) — уровень B1 для длительности и незаконченного периода.
- British Council LearnEnglish: [Present perfect (справочник)](https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/present-perfect) — закончившееся и незаконченное время.
- British Council LearnEnglish: [Talking about the past](https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/talking-about-past) — today, this morning, this week.
- British Council LearnEnglish: [British English and American English](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/british-english-american-english) — Past Simple с already, just, yet.
- British Council LearnEnglish: [Present perfect simple and continuous](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/present-perfect-simple-continuous) — for, since, how long с состояниями.
- Oxford Learner's Dictionaries: [present perfect simple and past simple](https://www.oxfordlearnersdictionaries.com/grammar/online-grammar/present-perfect-simple-and-past-simple) — вопрос об опыте, потом подробности в Past Simple.

## Показательная тема 3 — с существенными исключениями: множественное число (cards_pluralnouns, ред. 4)

**Делить нужно.** Без исключений тему не понять. Но частые и редкие исключения нужны на разных уровнях:
- men, children, people — A1;
- potatoes, knives, jeans, news — A2;
- crises, criteria, fishes — лексика B2 и выше; например, criterion в Oxford Learner's Dictionaries отмечено как B2.

Было шесть частей, стало три.

| Часть | Уровень | Слайды | Учебная цель | Предпосылки | Дальше |
|---|---|---|---|---|---|
| `a1_nouns_core` «Один и много» | A1 | 0, 1, 3 | +s, +es, y → ies; men, children, people, teeth, sheep; is / are, this / these | — | `a2_nouns_special`; артикли, some / any |
| `a2_nouns_special` «Knives, jeans, news» | A2 | 2, 4, 5 | -o и -f/-fe; jeans и scissors — мн. ч.; news, advice, information — неисчисляемые; согласование | `a1_nouns_core` | `b2_nouns_rare`; many / much (`a2_det_many_much`) |
| `b2_nouns_rare` «Редкие формы: crises» | B2 | 6 | roofs, oxen, crises, criteria; fish / fishes, people / peoples | `a2_nouns_special` | — |

Ограничения и ошибки по частям:
- **A1.** Ошибки childrens, citys, these book. Местоимение you всегда с are.
- **A2.**
  - Ошибки potatos, knifes, the news are, two informations.
  - A pair of scissors is.
  - Pants в британском и американском.
- **B2.**
  - Не каждое -um → -a (museums).
  - Data is в общем английском, are — в научном.
  - Fishes, persons, peoples — не ошибка, а другой смысл или стиль.

### Карта содержания

| Исходный пункт | Где теперь | Отметка |
|---|---|---|
| Исчисляемое и неисчисляемое, is / are, this / these (сл. 0) | A1, сл. 0 | сохранено |
| -s, -es, -ies, произношение окончания (сл. 1) | A1, сл. 1 | сохранено |
| Частые особые формы men, children, people, sheep (сл. 3) | A1, сл. 3 | сохранено; fishes и persons — ссылка на B2 |
| Слова на -o и -f/-fe (сл. 2) | A2, сл. 2 | сохранено; roofs — ссылка на B2 |
| Только множественное, неисчисляемые, news, науки (сл. 4) | A2, сл. 4 | сохранено; пример «Two pieces of advice are enough» заменён более естественным «Here are two pieces of advice» |
| People и police (сл. 4, дополнительно) | A2, сл. 4 | сохранено |
| Частые ошибки, таблица согласования (сл. 5) | A2, сл. 5 | исправлено: неестественная строка «Two pieces of news are good» заменена парой information / facts; совет переписан тем же способом |
| Team и family: is или are (сл. 5, дополнительно) | A2, сл. 5 | сохранено |
| Редкие -f, oxen, латинские и греческие формы, пары с разным смыслом (сл. 6) | B2, сл. 6 | перенесено в часть B2 (было B1): лексика слайда — уровня B2 и выше |

Удалённых пунктов нет. Все исключения сохранены и распределены по уровням.

### Источники

- British Council LearnEnglish: [Nouns: countable and uncountable (A1–A2)](https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2/nouns-countable-uncountable).
- Oxford Learner's Dictionaries: [criterion](https://www.oxfordlearnersdictionaries.com/definition/english/criterion) — уровень B2, форма criteria.
- Oxford Learner's Dictionaries: [phenomenon](https://www.oxfordlearnersdictionaries.com/definition/english/phenomenon) — форма phenomena.

## Проверка показательных тем

| Проверка | There is | Present Perfect | Множественное число |
|---|---|---|---|
| Блоки | formulas, table, transforms, examples, callout, errors | formulaCard, table, examples, steps, callout, errors, transforms, rules | formulaCard, table, examples, rules, callout, errors, steps |
| Все блоки поддерживаются приложением (CardModels.kt) | да | да | да |
| Вёрстка правил, таблиц, ошибок и переводов на 360 dp (87 строк) | без сжатия | без сжатия | без сжатия |
| Названия слайдов и частей | в 2 строки | в 2 строки, части ≤ 278 px | в 2 строки, части ≤ 278 px |
| Заданий на шаг (нужно ≥ 4 разных) | 18 / 20 / 15 | 20 / 15 / 9 / 15 / 17 / 12 / 8 / 18 | 8 / 31 / 11 / 19 / 22 / 11 / 8 |
| error_patterns пересчитаны по заданиям | да | да, добавлен `duration` | да |
| Дубли, decoys, равные ответу, и выделения (check_card.py) | нет проблем | нет проблем | нет проблем |

Kotlin-генератор упражнений здесь не запускался: в среде нет Android SDK. Готовность заданий проверена по данным:
- число заданий на каждый шаг;
- правило CurriculumDrill.hasEnoughEvidence (≥ 4 разных задания с этого слайда);
- audit-content и audit-curriculum;
- node-тесты.
