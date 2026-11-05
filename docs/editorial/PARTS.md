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

## Остальные переработанные темы (52 карточки)

Части пересобраны по тем же правилам. Содержание слайдов на этом шаге не менялось, кроме четырёх карточек с рядами слов-маркеров (см. ниже). Поэтому в картах ниже каждый пункт отмечен «сохранено» и показано, в какую часть он попал. Цели частей — в UNITS.md; они собраны из уже проверенных целей прежних частей.

### Темы без деления

Все слайды одного уровня и одного навыка, поэтому тема — одна часть. «Ошибки», «Примеры фраз» и «Диалог» стали её последними шагами.

| Тема | Часть | Уровень | Слайды | Было частей |
|---|---|---|---|---|
| Алфавит (alphabet) | `intro_alphabet_names` «Английский алфавит» | Intro | 0, 1, 2, 3 | 2 |
| Правила чтения (readingrules) | `intro_reading_vowels` «Как читать слова» | Intro | 0, 1, 2, 3 | 4 |
| Рассказать о себе (aboutme) | `a1_aboutme_basics` «Рассказ о себе» | A1 | 0, 1, 2, 3 | 3 |
| Сравнение as … as (asas) | `a2_asas_core` «As … as: как» | A2 | 0, 1 | 2 |
| Степени сравнения (comparisons) | `a2_comparisons_degrees` «Taller, more, the best» | A2 | 0, 1, 2, 3, 4, 5 | 5 |
| Как пройти (directions) | `a1_directions_ask` «Как пройти?» | A1 | 0, 1, 2, 3, 4 | 4 |
| В кафе и ресторане (restaurant) | `a1_restaurant_arrive` «В ресторане» | A1 | 0, 1, 2, 3, 4, 5 | 5 |
| Коллокации (collocations) | `a2_colloc_intro` «Слова парами» | A2 | 0, 1, 2, 3, 4, 5 | 5 |
| Идиомы (idioms) | `b1_idioms_intro` «Идиомы» | B1 | 0, 1, 2, 3, 4 | 4 |
| Сильные прилагательные (strongadjectives) | `a2_strongadj_words` «Вместо very» | A2 | 0, 1, 2, 3, 4 | 4 |
| There was / There were (therewaswere) | `a1_therewas_core` «There was, there were» | A1 | 0, 1, 2 | 3 |
| Would like (wouldlike) | `a1_wouldlike_core` «I'd like, would you like» | A1 | 0, 1, 2 | 3 |
| Few / Little (fewlittle) | `a2_fewlittle_core` «Few, little, a few» | A2 | 0, 1, 2 | 3 |
| Артикли: обобщение (genericarticles) | `b1_generic_kinds` «Артикль в обобщениях» | B1 | 0, 1, 2, 3 | 4 |
| There will be (therewillbe) | `a2_therewillbe_core` «There will be» | A2 | 0, 1 | 2 |

### Темы с делением

Делятся по уровню. Внутри уровня — только если этап самостоятельный и на него ссылаются другие темы: be и Present Simple, числа 1–20, большие и порядковые, -ed / неправильные / did в Past Simple.

В таблице: слайд → часть. Отметки: **с** — сохранено; **и** — исправлено на этом шаге (ряд слов-маркеров превращён в подсказку с границами правила, или исправлен цвет).

#### Артикли (articles) — было частей: 6, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_article_introduction` «Артикль a / an» | A1 | 0 a / an, the или ничего, 1 a / an: какой-то один | a1_nouns_core | a1_article_reference, a1_jobs_names |
| `a1_article_reference` «The или без артикля» | A1 | 2 the: тот самый, 3 Когда артикль не нужен, 4 Сводка по артиклям | a1_article_introduction | a2_pronouns_reflexive, a2_comparisons_degrees, a2_nature_words, b1_generic_kinds |
| `a2_article_special` «The best, the school» | A2 | 5 The best, the first, 6 School или the school | a2_comparisons_degrees | — |

Карта: 0 «a / an, the или ничего» → `a1_article_introduction` (с); 1 «a / an: какой-то один» → `a1_article_introduction` (с); 2 «the: тот самый» → `a1_article_reference` (с); 3 «Когда артикль не нужен» → `a1_article_reference` (с); 4 «Сводка по артиклям» → `a1_article_reference` (с); 5 «The best, the first» → `a2_article_special` (с); 6 «School или the school» → `a2_article_special` (с).

#### Present Simple (presentsimp) — было частей: 4, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_be_core` «Кто я и где я» | A1 | 3 Am, is, are | — | a1_simple_routines, a1_pronouns_personal, a1_cont_core, a1_greetings_hello |
| `a1_simple_routines` «Факты и привычки» | A1 | 0 Факты и привычки, 2 He, she, it: глагол + s | a1_be_core | a1_simple_questions, a2_prep_verbs, a1_aboutme_basics, a2_cont_vs_simple |
| `a1_simple_questions` «Don't, doesn't, do you…?» | A1 | 1 Отрицание и вопрос, 4 Частые ошибки | a1_simple_routines | a1_questions_yesno, a2_havegot_vs_have, a2_so_neither, a1_past_forms |

Карта: 0 «Факты и привычки» → `a1_simple_routines` (с); 1 «Отрицание и вопрос» → `a1_simple_questions` (с); 2 «He, she, it: глагол + s» → `a1_simple_routines` (с); 3 «Am, is, are» → `a1_be_core` (с); 4 «Частые ошибки» → `a1_simple_questions` (с).

#### Местоимения (pronouns) — было частей: 8, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_pronouns_personal` «I, me, my, this, who» | A1 | 0 Какие бывают местоимения, 1 I или me, 2 My или mine, 4 Этот и тот, 5 Who, whose, which | a1_nouns_core, a1_be_core | a2_pronouns_reflexive, b1_pronouns_relative, a1_havegot_core |
| `a2_pronouns_reflexive` «Myself, one, ones» | A2 | 3 Myself: сам, себя, 7 One и ones, 8 Частые ошибки | a1_pronouns_personal, a1_article_reference | — |
| `b1_pronouns_relative` «Слово «который»» | B1 | 6 Слово «который» | a1_pronouns_personal | — |

Карта: 0 «Какие бывают местоимения» → `a1_pronouns_personal` (с); 1 «I или me» → `a1_pronouns_personal` (с); 2 «My или mine» → `a1_pronouns_personal` (с); 3 «Myself: сам, себя» → `a2_pronouns_reflexive` (с); 4 «Этот и тот» → `a1_pronouns_personal` (с); 5 «Who, whose, which» → `a1_pronouns_personal` (с); 6 «Слово «который»» → `b1_pronouns_relative` (с); 7 «One и ones» → `a2_pronouns_reflexive` (с); 8 «Частые ошибки» → `a2_pronouns_reflexive` (с).

#### Предлоги (prepositions) — было частей: 8, стало: 4

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_prep_place` «In, on, at: место, время» | A1 | 0 Где, когда, куда, 1 Место: in, on, at, 2 Под, между, напротив, 3 Время: at, on, in | — | a2_prep_direction, a1_directions_ask, a2_emotions_prep |
| `a2_prep_direction` «Куда: to, into, across» | A2 | 4 Куда: to, into, 5 Частые ошибки | a1_prep_place | — |
| `a2_prep_verbs` «Listen to, good at» | A2 | 6 Глагол + предлог, 7 Good at, afraid of | a1_simple_routines | b1_prep_nouns |
| `b1_prep_nouns` «Reason for, rise in» | B1 | 8 Reason for, rise in | a2_prep_verbs | — |

Карта: 0 «Где, когда, куда» → `a1_prep_place` (с); 1 «Место: in, on, at» → `a1_prep_place` (с); 2 «Под, между, напротив» → `a1_prep_place` (с); 3 «Время: at, on, in» → `a1_prep_place` (с); 4 «Куда: to, into» → `a2_prep_direction` (с); 5 «Частые ошибки» → `a2_prep_direction` (с); 6 «Глагол + предлог» → `a2_prep_verbs` (с); 7 «Good at, afraid of» → `a2_prep_verbs` (с); 8 «Reason for, rise in» → `b1_prep_nouns` (с).

#### Present Continuous (presentcont) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_cont_core` «Что происходит сейчас» | A1 | 0 Что идёт сейчас, 1 Отрицание и вопрос, 2 Как добавить -ing | a1_be_core | a2_cont_vs_simple, a2_clothes_verbs, a2_pastcont_core |
| `a2_cont_vs_simple` «Сейчас или обычно» | A2 | 3 Глаголы без -ing, 4 Сейчас или обычно, 5 Частые ошибки | a1_cont_core, a1_simple_routines | — |

Карта: 0 «Что идёт сейчас» → `a1_cont_core` (и); 1 «Отрицание и вопрос» → `a1_cont_core` (с); 2 «Как добавить -ing» → `a1_cont_core` (с); 3 «Глаголы без -ing» → `a2_cont_vs_simple` (с); 4 «Сейчас или обычно» → `a2_cont_vs_simple` (с); 5 «Частые ошибки» → `a2_cont_vs_simple` (с).

#### Вопросы (questions) — было частей: 7, стало: 4

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_questions_yesno` «Вопросы: do, what, or» | A1 | 0 Какие бывают вопросы, 1 Вопрос «да или нет», 2 What, where, why, 4 Вопрос с выбором | a1_simple_questions | a2_questions_subject, a2_imperative_polite, a1_study_words |
| `a2_questions_subject` «Who called? — без do» | A2 | 3 Вопрос без do | a1_questions_yesno | a2_questions_tags |
| `a2_questions_tags` «Хвостики: don't you?» | A2 | 5 Хвостики: don't you?, 7 Частые ошибки | a2_questions_subject | b1_questions_tags_special |
| `b1_questions_tags_special` «Aren't I, shall we» | B1 | 6 Особые хвостики | a2_questions_tags | — |

Карта: 0 «Какие бывают вопросы» → `a1_questions_yesno` (с); 1 «Вопрос «да или нет»» → `a1_questions_yesno` (с); 2 «What, where, why» → `a1_questions_yesno` (с); 3 «Вопрос без do» → `a2_questions_subject` (с); 4 «Вопрос с выбором» → `a1_questions_yesno` (с); 5 «Хвостики: don't you?» → `a2_questions_tags` (с); 6 «Особые хвостики» → `b1_questions_tags_special` (с); 7 «Частые ошибки» → `a2_questions_tags` (с).

#### Some, any, no, every (determinants) — было частей: 6, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_det_some_any` «Some и any» | A1 | 0 Some, any, no, every, 1 Some или any | a1_nouns_core | a2_det_many_much |
| `a2_det_many_much` «None, every, much» | A2 | 2 No, none и not any, 3 Somebody, anything, 4 Every, each и all, 5 Many, much и a lot of, 6 Сводка и ошибки | a1_det_some_any, a2_nouns_special | a2_fewlittle_core |

Карта: 0 «Some, any, no, every» → `a1_det_some_any` (с); 1 «Some или any» → `a1_det_some_any` (с); 2 «No, none и not any» → `a2_det_many_much` (с); 3 «Somebody, anything» → `a2_det_many_much` (с); 4 «Every, each и all» → `a2_det_many_much` (с); 5 «Many, much и a lot of» → `a2_det_many_much` (с); 6 «Сводка и ошибки» → `a2_det_many_much` (с).

#### Повелительное наклонение (imperative) — было частей: 3, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_imperative_core` «Просьбы и команды» | A1 | 0 Просьбы и команды, 2 Частые ошибки | — | a2_imperative_polite, a1_directions_ask, a2_food_cooking, a2_tech_verbs |
| `a2_imperative_polite` «Как попросить вежливо» | A2 | 1 Как сказать вежливо | a1_imperative_core, a1_questions_yesno | — |

Карта: 0 «Просьбы и команды» → `a1_imperative_core` (с); 1 «Как сказать вежливо» → `a2_imperative_polite` (с); 2 «Частые ошибки» → `a1_imperative_core` (с).

#### Have got (havegot) — было частей: 3, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_havegot_core` «I've got, have you got?» | A1 | 0 Have got: у меня есть | a1_pronouns_personal | a2_havegot_vs_have, a1_appearance_looks, a1_body_parts |
| `a2_havegot_vs_have` «Have got или have» | A2 | 1 Have got или have, 2 Частые ошибки | a1_havegot_core, a1_simple_questions | b1_uk_us_grammar |

Карта: 0 «Have got: у меня есть» → `a1_havegot_core` (с); 1 «Have got или have» → `a2_havegot_vs_have` (с); 2 «Частые ошибки» → `a2_havegot_vs_have` (с).

#### Both, either, neither (botheither) — было частей: 4, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_both_either` «Both, either, neither» | A2 | 0 Оба, любой, ни один | a1_nouns_core | b1_both_pairs |
| `a2_so_neither` «So do I, Neither do I» | A2 | 2 Я тоже: So do I | a1_simple_questions | b1_both_pairs |
| `b1_both_pairs` «Both … and, either … or» | B1 | 1 Пары: both … and, 3 Частые ошибки | a2_both_either, a2_so_neither | — |

Карта: 0 «Оба, любой, ни один» → `a2_both_either` (с); 1 «Пары: both … and» → `b1_both_pairs` (с); 2 «Я тоже: So do I» → `a2_so_neither` (с); 3 «Частые ошибки» → `b1_both_pairs` (с).

#### Приветствия и small talk (greetings) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_greetings_hello` «Привет и знакомство» | A1 | 0 Привет и пока, 1 Знакомство, 3 Примеры фраз, 4 Диалог на работе, 5 Частые ошибки | a1_be_core | a2_greetings_smalltalk, a1_shopping_choose, a1_restaurant_arrive |
| `a2_greetings_smalltalk` «Small talk» | A2 | 2 Small talk | a1_greetings_hello | — |

Карта: 0 «Привет и пока» → `a1_greetings_hello` (с); 1 «Знакомство» → `a1_greetings_hello` (с); 2 «Small talk» → `a2_greetings_smalltalk` (с); 3 «Примеры фраз» → `a1_greetings_hello` (с); 4 «Диалог на работе» → `a1_greetings_hello` (с); 5 «Частые ошибки» → `a1_greetings_hello` (с).

#### Семья и отношения (family) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_family_core` «Семья» | A1 | 0 Самые близкие, 3 Примеры фраз, 4 Диалог о семье, 5 Частые ошибки | — | a2_family_inlaws |
| `a2_family_inlaws` «Родня и отношения» | A2 | 1 Родня по браку, 2 Отношения | a1_family_core | — |

Карта: 0 «Самые близкие» → `a1_family_core` (с); 1 «Родня по браку» → `a2_family_inlaws` (с); 2 «Отношения» → `a2_family_inlaws` (с); 3 «Примеры фраз» → `a1_family_core` (с); 4 «Диалог о семье» → `a1_family_core` (с); 5 «Частые ошибки» → `a1_family_core` (с).

#### Числа (numbers) — было частей: 6, стало: 4

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_numbers_1_20` «Числа от 1 до 20» | A1 | 1 Числа от 1 до 20 | — | a1_numbers_big, a1_numbers_ordinal |
| `a1_numbers_big` «Десятки, сотни, тысячи» | A1 | 2 Десятки, сотни, тысячи | a1_numbers_1_20 | a2_numbers_dates, a1_time_clock, a2_measures |
| `a1_numbers_ordinal` «Первый, второй, третий» | A1 | 0 Сколько и какой по счёту, 3 First, second, third | a1_numbers_1_20 | a2_numbers_dates, a1_time_clock, a1_home_rooms |
| `a2_numbers_dates` «Даты, дроби, проценты» | A2 | 4 Даты и годы, 5 Частые ошибки, 6 Дроби и проценты | a1_numbers_ordinal, a1_numbers_big | — |

Карта: 0 «Сколько и какой по счёту» → `a1_numbers_ordinal` (с); 1 «Числа от 1 до 20» → `a1_numbers_1_20` (с); 2 «Десятки, сотни, тысячи» → `a1_numbers_big` (с); 3 «First, second, third» → `a1_numbers_ordinal` (с); 4 «Даты и годы» → `a2_numbers_dates` (с); 5 «Частые ошибки» → `a2_numbers_dates` (с); 6 «Дроби и проценты» → `a2_numbers_dates` (с).

#### Past Simple (pastsimp) — было частей: 5, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_past_meaning` «Что случилось: -ed» | A1 | 0 Что случилось, 2 Окончание -ed | a1_simple_routines | a1_past_irregular, a2_modals_can, a1_therewas_core, a2_pastcont_core |
| `a1_past_irregular` «Неправильные глаголы» | A1 | 3 Глаголы: -ed и went | a1_past_meaning | a1_past_forms, b1_pastcont_interrupt |
| `a1_past_forms` «Did и didn't» | A1 | 1 Отрицание и вопрос, 4 Частые ошибки | a1_simple_questions, a1_past_irregular | a2_study_verbs, b1_uk_us_grammar, a2_usedto_core, a2_perfect_meaning |

Карта: 0 «Что случилось» → `a1_past_meaning` (и); 1 «Отрицание и вопрос» → `a1_past_forms` (с); 2 «Окончание -ed» → `a1_past_meaning` (с); 3 «Глаголы: -ed и went» → `a1_past_irregular` (с); 4 «Частые ошибки» → `a1_past_forms` (с).

#### Модальные глаголы (modalverbs) — было частей: 7, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_modals_can` «Can, could, may, might» | A2 | 0 Могу, надо, можно, 1 Can и could, 2 May и might | a1_simple_questions, a1_past_meaning | a2_modals_must |
| `a2_modals_must` «Must, have to, should» | A2 | 3 Must и have to, 4 Советы: should, 6 Частые ошибки | a2_modals_can | b1_modals_past |
| `b1_modals_past` «Must have, should have» | B1 | 5 Must have done | a2_modals_must | — |

Карта: 0 «Могу, надо, можно» → `a2_modals_can` (с); 1 «Can и could» → `a2_modals_can` (с); 2 «May и might» → `a2_modals_can` (с); 3 «Must и have to» → `a2_modals_must` (с); 4 «Советы: should» → `a2_modals_must` (с); 5 «Must have done» → `b1_modals_past` (с); 6 «Частые ошибки» → `a2_modals_must` (с).

#### Время, деньги, меры (timemoney) — было частей: 6, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_time_clock` «Время, даты и цены» | A1 | 0 Который час, 1 Даты и годы, 2 Как читать цены, 4 Примеры фраз, 5 Диалог на рынке, 6 Частые ошибки | a1_numbers_ordinal, a1_numbers_big | a1_shopping_choose, a1_restaurant_arrive |
| `a2_measures` «Мили, футы, фунты» | A2 | 3 Мили, футы, фунты | a1_numbers_big | — |

Карта: 0 «Который час» → `a1_time_clock` (с); 1 «Даты и годы» → `a1_time_clock` (с); 2 «Как читать цены» → `a1_time_clock` (с); 3 «Мили, футы, фунты» → `a2_measures` (с); 4 «Примеры фраз» → `a1_time_clock` (с); 5 «Диалог на рынке» → `a1_time_clock` (с); 6 «Частые ошибки» → `a1_time_clock` (с).

#### Порядок слов (wordorder) — было частей: 6, стало: 3

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_wordorder_svo` «Кто → делает → что» | A1 | 0 Основная схема | a1_be_core | a2_wordorder_frequency, b1_wordorder_adjectives |
| `a2_wordorder_frequency` «Always, also, как, где» | A2 | 1 Always, never: где стоят, 2 Как, где, когда, 4 Also, only, enough, 5 Частые ошибки | a1_wordorder_svo, a1_simple_routines | — |
| `b1_wordorder_adjectives` «Big, old, red: порядок» | B1 | 3 Big, old, red: порядок | a1_wordorder_svo | — |

Карта: 0 «Основная схема» → `a1_wordorder_svo` (с); 1 «Always, never: где стоят» → `a2_wordorder_frequency` (с); 2 «Как, где, когда» → `a2_wordorder_frequency` (с); 3 «Big, old, red: порядок» → `b1_wordorder_adjectives` (с); 4 «Also, only, enough» → `a2_wordorder_frequency` (с); 5 «Частые ошибки» → `a2_wordorder_frequency` (с).

#### В магазине (shopping) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_shopping_choose` «В магазине» | A1 | 0 Выбрать и примерить, 1 Как заплатить, 3 Примеры фраз, 4 Диалог в магазине, 5 Частые ошибки | a1_greetings_hello, a1_time_clock | a2_shopping_return |
| `a2_shopping_return` «Вернуть или обменять» | A2 | 2 Вернуть или обменять | a1_shopping_choose | — |

Карта: 0 «Выбрать и примерить» → `a1_shopping_choose` (с); 1 «Как заплатить» → `a1_shopping_choose` (с); 2 «Вернуть или обменять» → `a2_shopping_return` (с); 3 «Примеры фраз» → `a1_shopping_choose` (с); 4 «Диалог в магазине» → `a1_shopping_choose` (с); 5 «Частые ошибки» → `a1_shopping_choose` (с).

#### Погода и природа (weather) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_weather_words` «Погода» | A1 | 0 Солнце, дождь, ветер, 1 Как говорить о погоде, 3 Примеры фраз, 4 Диалог о погоде, 5 Частые ошибки | a1_be_core | a2_nature_words |
| `a2_nature_words` «Горы, реки, море» | A2 | 2 Горы, реки, море | a1_weather_words, a1_article_reference | — |

Карта: 0 «Солнце, дождь, ветер» → `a1_weather_words` (с); 1 «Как говорить о погоде» → `a1_weather_words` (с); 2 «Горы, реки, море» → `a2_nature_words` (с); 3 «Примеры фраз» → `a1_weather_words` (с); 4 «Диалог о погоде» → `a1_weather_words` (с); 5 «Частые ошибки» → `a1_weather_words` (с).

#### Еда и напитки (food) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_food_products` «Еда и вкус» | A1 | 0 Продукты, 2 Вкус и приёмы пищи, 3 Примеры фраз, 4 Что в холодильнике, 5 Частые ошибки | a1_nouns_core | a2_food_cooking |
| `a2_food_cooking` «Готовка: boil, fry, bake» | A2 | 1 Как готовить | a1_food_products, a1_imperative_core | — |

Карта: 0 «Продукты» → `a1_food_products` (с); 1 «Как готовить» → `a2_food_cooking` (с); 2 «Вкус и приёмы пищи» → `a1_food_products` (с); 3 «Примеры фраз» → `a1_food_products` (с); 4 «Что в холодильнике» → `a1_food_products` (с); 5 «Частые ошибки» → `a1_food_products` (с).

#### Работа и профессии (jobs) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_jobs_names` «Профессии» | A1 | 0 Профессии, 2 What do you do? | a1_article_introduction, a1_simple_questions | a2_jobs_work_job |
| `a2_jobs_work_job` «Job, work и разговор» | A2 | 1 Job или work, 3 Примеры фраз, 4 Диалог о работе, 5 Частые ошибки | a1_jobs_names, a2_nouns_special | — |

Карта: 0 «Профессии» → `a1_jobs_names` (с); 1 «Job или work» → `a2_jobs_work_job` (с); 2 «What do you do?» → `a1_jobs_names` (с); 3 «Примеры фраз» → `a2_jobs_work_job` (с); 4 «Диалог о работе» → `a2_jobs_work_job` (с); 5 «Частые ошибки» → `a2_jobs_work_job` (с).

#### Внешность и характер (appearance) — было частей: 6, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_appearance_looks` «Внешность и характер» | A1 | 0 Рост, волосы, лицо, 2 Черты характера | a1_havegot_core | a2_appearance_order |
| `a2_appearance_order` «Long dark hair, look like» | A2 | 1 Long dark hair: порядок, 3 Like или look like, 4 Примеры фраз, 5 Диалог о коллеге, 6 Частые ошибки | a1_appearance_looks, a1_simple_questions | — |

Карта: 0 «Рост, волосы, лицо» → `a1_appearance_looks` (с); 1 «Long dark hair: порядок» → `a2_appearance_order` (с); 2 «Черты характера» → `a1_appearance_looks` (с); 3 «Like или look like» → `a2_appearance_order` (с); 4 «Примеры фраз» → `a2_appearance_order` (с); 5 «Диалог о коллеге» → `a2_appearance_order` (с); 6 «Частые ошибки» → `a2_appearance_order` (с).

#### Тело и здоровье (body) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_body_parts` «Тело и что болит» | A1 | 0 Части тела, 1 Что болит, 3 Примеры фраз, 4 Диалог: болит голова, 5 Частые ошибки | a1_havegot_core | a2_body_habits |
| `a2_body_habits` «Здоровые привычки» | A2 | 2 Здоровые привычки | a1_body_parts | — |

Карта: 0 «Части тела» → `a1_body_parts` (с); 1 «Что болит» → `a1_body_parts` (с); 2 «Здоровые привычки» → `a2_body_habits` (с); 3 «Примеры фраз» → `a1_body_parts` (с); 4 «Диалог: болит голова» → `a1_body_parts` (с); 5 «Частые ошибки» → `a1_body_parts` (с).

#### Одежда (clothes) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_clothes_words` «Одежда и обувь» | A1 | 0 Одежда, 1 Обувь и аксессуары | a1_nouns_core | a2_clothes_verbs |
| `a2_clothes_verbs` «Put on, wear, fit» | A2 | 2 Put on, wear, fit, 3 Примеры фраз, 4 Диалог в примерочной, 5 Частые ошибки | a1_clothes_words, a1_cont_core | — |

Карта: 0 «Одежда» → `a1_clothes_words` (с); 1 «Обувь и аксессуары» → `a1_clothes_words` (с); 2 «Put on, wear, fit» → `a2_clothes_verbs` (с); 3 «Примеры фраз» → `a2_clothes_verbs` (с); 4 «Диалог в примерочной» → `a2_clothes_verbs` (с); 5 «Частые ошибки» → `a2_clothes_verbs` (с).

#### Дом и квартира (home) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_home_rooms` «Комнаты и мебель» | A1 | 0 Комнаты и этажи, 1 Мебель и техника, 3 Примеры фраз, 4 Диалог о квартире | a1_there_core, a1_numbers_ordinal | a2_home_chores |
| `a2_home_chores` «Дела по дому» | A2 | 2 Дела по дому, 5 Частые ошибки | a1_home_rooms | — |

Карта: 0 «Комнаты и этажи» → `a1_home_rooms` (с); 1 «Мебель и техника» → `a1_home_rooms` (с); 2 «Дела по дому» → `a2_home_chores` (с); 3 «Примеры фраз» → `a1_home_rooms` (с); 4 «Диалог о квартире» → `a1_home_rooms` (с); 5 «Частые ошибки» → `a2_home_chores` (с).

#### Хобби и спорт (hobbies) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_hobbies_ing` «Хобби: play, go, do» | A1 | 0 Хобби на -ing, 1 Play, go или do, 3 Примеры фраз, 4 Планы на выходные | a1_simple_routines | a2_hobbies_talk |
| `a2_hobbies_talk` «Рассказ о хобби» | A2 | 2 Рассказ о хобби, 5 Частые ошибки | a1_hobbies_ing | — |

Карта: 0 «Хобби на -ing» → `a1_hobbies_ing` (с); 1 «Play, go или do» → `a1_hobbies_ing` (с); 2 «Рассказ о хобби» → `a2_hobbies_talk` (с); 3 «Примеры фраз» → `a1_hobbies_ing` (с); 4 «Планы на выходные» → `a1_hobbies_ing` (с); 5 «Частые ошибки» → `a2_hobbies_talk` (с).

#### Эмоции и чувства (emotions) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_emotions_words` «Как назвать чувство» | A1 | 0 Как назвать чувство | a1_be_core | a2_emotions_prep |
| `a2_emotions_prep` «Afraid of, bored» | A2 | 1 Чувство + предлог, 2 Bored или boring, 3 Примеры фраз, 4 Диалог: экзамен, 5 Частые ошибки | a1_emotions_words, a1_prep_place | — |

Карта: 0 «Как назвать чувство» → `a1_emotions_words` (с); 1 «Чувство + предлог» → `a2_emotions_prep` (с); 2 «Bored или boring» → `a2_emotions_prep` (с); 3 «Примеры фраз» → `a2_emotions_prep` (с); 4 «Диалог: экзамен» → `a2_emotions_prep` (с); 5 «Частые ошибки» → `a2_emotions_prep` (с).

#### Учёба (study) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_study_words` «Учёба и занятие» | A1 | 0 Школа и университет, 2 Фразы на занятии | a1_nouns_core, a1_questions_yesno | a2_study_verbs |
| `a2_study_verbs` «Take или pass» | A2 | 1 Take или pass, 3 Примеры фраз, 4 Перед экзаменом, 5 Частые ошибки | a1_study_words, a1_past_forms | — |

Карта: 0 «Школа и университет» → `a1_study_words` (с); 1 «Take или pass» → `a2_study_verbs` (с); 2 «Фразы на занятии» → `a1_study_words` (с); 3 «Примеры фраз» → `a2_study_verbs` (с); 4 «Перед экзаменом» → `a2_study_verbs` (с); 5 «Частые ошибки» → `a2_study_verbs` (с).

#### Технологии и интернет (technology) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_tech_words` «Телефон и компьютер» | A1 | 0 Телефон и компьютер | a1_nouns_core | a2_tech_verbs |
| `a2_tech_verbs` «Download, crash, fix» | A2 | 1 Download или upload, 2 Если не работает, 3 Примеры фраз, 4 Тормозит ноутбук, 5 Частые ошибки | a1_tech_words, a1_imperative_core | — |

Карта: 0 «Телефон и компьютер» → `a1_tech_words` (с); 1 «Download или upload» → `a2_tech_verbs` (с); 2 «Если не работает» → `a2_tech_verbs` (с); 3 «Примеры фраз» → `a2_tech_verbs` (с); 4 «Тормозит ноутбук» → `a2_tech_verbs` (с); 5 «Частые ошибки» → `a2_tech_verbs` (с).

#### Британский и американский (britishamerican) — было частей: 5, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_uk_us_words` «Flat и apartment» | A2 | 0 Flat и apartment, 1 Colour и color | — | b1_uk_us_grammar |
| `b1_uk_us_grammar` «UK и US: грамматика» | B1 | 2 Грамматика и даты, 3 Произношение, 4 Примеры фраз, 5 Диалог: аптека | a2_havegot_vs_have, a1_past_forms, intro_reading_vowels, a2_uk_us_words | — |

Карта: 0 «Flat и apartment» → `a2_uk_us_words` (с); 1 «Colour и color» → `a2_uk_us_words` (с); 2 «Грамматика и даты» → `b1_uk_us_grammar` (с); 3 «Произношение» → `b1_uk_us_grammar` (с); 4 «Примеры фраз» → `b1_uk_us_grammar` (с); 5 «Диалог: аптека» → `b1_uk_us_grammar` (с).

#### Be going to (begoingto) — было частей: 3, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_goingto_form` «Планы: going to» | A1 | 0 Планы: going to | a1_be_core | a2_goingto_will |
| `a2_goingto_will` «Going to или will» | A2 | 1 Going to или will, 2 Частые ошибки | a1_goingto_form | a2_future_will_goingto |

Карта: 0 «Планы: going to» → `a1_goingto_form` (с); 1 «Going to или will» → `a2_goingto_will` (с); 2 «Частые ошибки» → `a2_goingto_will` (с).

#### Артикли с названиями (articlesnames) — было частей: 4, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_names_countries` «Страны, реки, горы» | A2 | 0 Страны и города, 1 Реки, моря, горы | a1_article_reference | b1_names_city |
| `b1_names_city` «Названия в городе» | B1 | 2 Названия в городе, 3 Частые ошибки | a2_names_countries | — |

Карта: 0 «Страны и города» → `a2_names_countries` (с); 1 «Реки, моря, горы» → `a2_names_countries` (с); 2 «Названия в городе» → `b1_names_city` (с); 3 «Частые ошибки» → `b1_names_city` (с).

#### Used to (usedto) — было частей: 3, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_usedto_core` «Раньше было, теперь нет» | A2 | 0 Раньше было, теперь нет, 1 Частые ошибки | a1_past_forms | b1_usedto_vs_beused |
| `b1_usedto_vs_beused` «Used to или be used to» | B1 | 2 Used to или be used to | a2_usedto_core | — |

Карта: 0 «Раньше было, теперь нет» → `a2_usedto_core` (с); 1 «Частые ошибки» → `a2_usedto_core` (с); 2 «Used to или be used to» → `b1_usedto_vs_beused` (с).

#### Past Continuous (pastcont) — было частей: 6, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_pastcont_core` «Делал в тот момент» | A2 | 0 Делал в тот момент, 1 Отрицание и вопрос, 2 Подсказки, 3 Как добавить -ing, 5 Частые ошибки | a1_past_meaning, a1_cont_core | b1_pastcont_interrupt |
| `b1_pastcont_interrupt` «Когда что-то случилось» | B1 | 4 Когда что-то случилось | a2_pastcont_core, a1_past_irregular | — |

Карта: 0 «Делал в тот момент» → `a2_pastcont_core` (и); 1 «Отрицание и вопрос» → `a2_pastcont_core` (с); 2 «Подсказки» → `a2_pastcont_core` (и); 3 «Как добавить -ing» → `a2_pastcont_core` (с); 4 «Когда что-то случилось» → `b1_pastcont_interrupt` (и); 5 «Частые ошибки» → `a2_pastcont_core` (с).

#### Future Simple (futuresimp) — было частей: 6, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_future_will` «Will, won't, I'll» | A1 | 0 Решения и прогнозы, 1 Отрицание и вопрос, 2 I'll, won't | a1_simple_routines | a2_future_will_goingto |
| `a2_future_will_goingto` «Will или going to» | A2 | 3 Подсказки, 4 Will или going to, 5 Частые ошибки | a1_future_will, a2_goingto_will | — |

Карта: 0 «Решения и прогнозы» → `a1_future_will` (и); 1 «Отрицание и вопрос» → `a1_future_will` (с); 2 «I'll, won't» → `a1_future_will` (с); 3 «Подсказки» → `a2_future_will_goingto` (и); 4 «Will или going to» → `a2_future_will_goingto` (с); 5 «Частые ошибки» → `a2_future_will_goingto` (с).

#### Already, yet, still, just (alreadyyet) — было частей: 4, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a2_alreadyyet_meaning` «Already, yet, still» | A2 | 0 Already, yet, still, just, 1 Где ставить, 3 Частые ошибки | a2_perfect_meaning | b1_alreadyyet_nuance |
| `b1_alreadyyet_nuance` «Оттенки смысла» | B1 | 2 Оттенки смысла | a2_alreadyyet_meaning | — |

Карта: 0 «Already, yet, still, just» → `a2_alreadyyet_meaning` (с); 1 «Где ставить» → `a2_alreadyyet_meaning` (с); 2 «Оттенки смысла» → `b1_alreadyyet_nuance` (с); 3 «Частые ошибки» → `a2_alreadyyet_meaning` (с).

#### Сокращённые формы (contractions) — было частей: 4, стало: 2

| Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|
| `a1_contractions_core` «I'm, don't, won't» | A1 | 0 I'm, don't, won't | a1_be_core | a2_contractions_s_d |
| `a2_contractions_s_d` «'s, 'd и полная форма» | A2 | 1 's и 'd: два значения, 2 Когда пишут полностью, 3 Частые ошибки | a1_contractions_core | — |

Карта: 0 «I'm, don't, won't» → `a1_contractions_core` (с); 1 «'s и 'd: два значения» → `a2_contractions_s_d` (с); 2 «Когда пишут полностью» → `a2_contractions_s_d` (с); 3 «Частые ошибки» → `a2_contractions_s_d` (с).


## Партия 10

| Тема | Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|---|
| Have to | `a2_haveto_core` «Have to: приходится» | A2 | 0 Have to: приходится, 1 Do you have to…?, 2 Частые ошибки | a1_simple_questions, a1_past_forms | a2_mustnt_core, a2_needto_core |
| Must / Mustn't | `a2_mustnt_core` «Must и mustn't» | A2 | 0 Must и mustn't, 1 Must I…? без do, 2 Частые ошибки | a2_modals_must, a2_haveto_core | a2_donthaveto_core |
| Don't have to | `a2_donthaveto_core` «Don't have to» | A2 | 0 Не обязательно, 1 Частые ошибки | a2_mustnt_core | — |
| Need to | `a2_needto_core` «Need to: нужно» | A2 | 0 Need to: нужно, 1 Частые ошибки | a2_haveto_core | — |
| Be able to | `a2_beableto_core` «Be able to: смогу» | A2 | 0 Be able to: смогу, 1 Can или be able to | a2_modals_can | b1_beableto_past |
| Be able to | `b1_beableto_past` «Could или was able to» | B1 | 2 Could или was able to | a2_beableto_core, a1_past_irregular | — |
| Shall I / Shall we | `a2_shall_core` «Shall I…? Shall we…?» | A2 | 0 Shall I…? Shall we…?, 1 Shall, will, should | a2_modals_must, a1_questions_yesno | — |
| Had better | `b1_hadbetter_core` «Had better: лучше бы» | B1 | 0 Had better: лучше бы, 1 Частые ошибки | a2_modals_must | — |
| Irregular Verbs | `a2_irregular_forms` «Неправильные глаголы» | A2 | 0–5 | a1_past_irregular | — |

**Делить нужно только be able to.** Различие could и was able to — материал B1: British Council даёт его в уроке «Past ability» уровня B1–B2. Остальные темы — один уровень и один навык.

Карта содержания be able to:

| Исходный пункт | Где теперь | Отметка |
|---|---|---|
| Формы be able to по временам, когда can нельзя (сл. 0) | A2, сл. 0 | сохранено; вступление начинается с ситуации, пример «since age 5» исправлен |
| Сравнение can и be able to (сл. 1) | A2, сл. 1 | сохранено; совет переписан: be able to в настоящем звучит книжно |
| Could или was able to (сл. 1) | B1, сл. 2 | перенесено, дополнено: managed to, couldn't в отрицании, could с see и hear |
| Частые ошибки в скрытом блоке (сл. 1) | A2, сл. 1 | перенесено из скрытого блока на слайд |
| Цитата | — | удалено: не учебное содержание |

## Партия 11

| Тема | Часть | Уровень | Слайды | Предпосылки | Дальше |
|---|---|---|---|---|---|
| Present Perfect Continuous | `b1_ppc_core` «Делаю уже давно» | B1 | 0–5 | b1_perfect_time, a1_cont_core | — |
| Past Perfect | `b1_pastperf_core` «Past Perfect: раньше» | B1 | 0–5 | a2_perfect_meaning, a1_past_forms | — |
| Too … to | `a2_tooto_core` «Too … to: слишком» | A2 | 0, 1, 2 | a2_det_many_much | a2_enough |
| So / Such / Enough | `a2_enough` «Enough: где ставить» | A2 | 2 | a2_tooto_core | b1_so_such |
| So / Such / Enough | `b1_so_such` «So, such, so … that» | B1 | 0, 1, 3 | a2_enough | — |
| Would prefer | `b1_wouldprefer_core` «Would prefer» | B1 | 0, 1 | a1_wouldlike_core | b1_wouldrather_core |
| Would rather | `b1_wouldrather_core` «Would rather» | B1 | 0, 1, 2 | b1_wouldprefer_core | — |
| Present for Future | `a2_present_future` «Будущее настоящим» | A2 | 0, 1 | a1_cont_core, a2_future_will_goingto | — |
| When / As soon as | `b1_timeclauses_core` «When I come: без will» | B1 | 0, 1, 2 | a2_future_will_goingto | — |

**Делить нужно только so / such / enough.** Место enough — материал A2. Усиление so и such и следствие so … that — B1.

Карта содержания so / such / enough:

| Исходный пункт | Где теперь | Отметка |
|---|---|---|
| So и such, so many / much (сл. 0) | B1, сл. 0 | сохранено; вступление начинается с ситуации |
| So … that, such … that, that можно опустить (сл. 1) | B1, сл. 1 | сохранено |
| Место enough (сл. 2) | A2, сл. 2 | сохранено; убран капслок |
| Частые ошибки (сл. 3) | B1, сл. 3 | сохранено; time enough помечено как книжное, а не ошибка |
| Цитата | — | удалено: не учебное содержание |

В читалке слайд 2 (A2) стоит между слайдами B1-части. В курсе порядок задают части; в читалке нужна поддержка границ частей (COMPONENTS.md).
