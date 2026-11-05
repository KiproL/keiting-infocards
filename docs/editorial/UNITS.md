# Учебные части и их цели

Цель каждой части из `tree/curriculum.json`. Пока для неё нет поля в схеме, цели записаны здесь, как требует задание. Уровень — редакторская разметка по содержанию, лексике и сложности заданий, а не официальная сертификация CEFR. Все части пока `reviewed=false`.

| ID | Уровень | Карточка и слайды | Учебная цель | Предпосылки |
|---|---|---|---|---|
| intro_alphabet_names | Intro | alphabet 0, 1 | Называть английские буквы и узнавать их на слух | — |
| intro_alphabet_dictation | Intro | alphabet 2, 3 | Продиктовать и записать по буквам имя, e-mail и номер; различать пары E и I, G и J | intro_alphabet_names |
| intro_reading_vowels | Intro | readingrules 0 | Читать гласную по типу слога: открытый (name) и закрытый (man) | intro_alphabet_names |
| intro_reading_r | Intro | readingrules 1 | Читать сочетания гласной с r: car, bird, more | intro_reading_vowels |
| intro_reading_consonants | Intro | readingrules 2 | Читать c и g перед e, i, y и перед другими буквами | intro_alphabet_names |
| intro_reading_review | Intro | readingrules 3 | Не читать английские слова по буквам, как русские | intro_reading_vowels, intro_reading_r, intro_reading_consonants |
| a1_nouns_core | A1 | pluralnouns 0, 1 | Образовать множественное число с +s, +es, y → ies и согласовать is/are, this/these | — |
| a1_article_introduction | A1 | articles 0, 1 | Назвать один исчисляемый предмет с a/an по звуку следующего слова; не ставить два определителя | a1_nouns_core |
| a1_be_core | A1 | presentsimp 3 | Говорить о себе и других с am/is/are: возраст, место, профессия, состояние; вопрос и отрицание без do | — |
| a1_simple_routines | A1 | presentsimp 0, 2 | Описывать привычки, факты и расписание; ставить -s/-es/-ies с he/she/it | a1_be_core |
| a1_simple_questions | A1 | presentsimp 1 | Строить отрицание и вопрос с do/does, глагол после них — в начальной форме; краткие ответы | a1_simple_routines |
| a1_simple_review | A1 | presentsimp 4 | Исправлять частые ошибки: he play, does he plays, I am play, he have | a1_simple_questions |
| a1_nouns_variants | A1 | pluralnouns 3 | Употреблять частые особые формы: men, women, children, people, feet, teeth, sheep, fish | a1_nouns_core |
| a2_nouns_spelling | A2 | pluralnouns 2 | Писать формы слов на -o и -f/-fe, проверяя исключения по словарю | a1_nouns_core |
| a2_nouns_uncountable | A2 | pluralnouns 4 | Считать неисчисляемое через единицу; trousers и scissors с are; news и физика с is | a1_nouns_core |
| a2_nouns_review | A2 | pluralnouns 5 | Найти и исправить ошибки числа и согласования в смешанных примерах | a1_nouns_variants, a2_nouns_spelling, a2_nouns_uncountable |
| b1_nouns_rare | B1 | pluralnouns 6 | Узнавать редкие формы множественного числа (crises, criteria, roofs) и пары с разным смыслом (fishes, persons, peoples) | a1_nouns_variants, a2_nouns_spelling |
| a1_article_reference | A1 | articles 2 | Выбрать the, когда собеседник понимает, какой именно предмет: уже назван, виден, единственный в ситуации, уточнён | a1_article_introduction |
| a1_article_zero | A1 | articles 3 | Говорить о многих предметах и веществах вообще без артикля; имена, языки, приёмы пищи без артикля | a1_article_introduction |
| a1_article_choice | A1 | articles 4 | Выбрать a/an, the или нулевой артикль для одного слова в разных ситуациях | a1_article_reference, a1_article_zero |
| a2_article_superlative | A2 | articles 5 | Ставить the с превосходной степенью и порядковыми числами; my вместо the | a1_article_reference, a2_comparisons_degrees |
| a2_article_institutions | A2 | articles 6 | Различать дело (go to school, by bus) и конкретное место (the school, on the bus) | a1_article_zero |
| a1_there_core | A1 | thereisare 0 | Сказать, что где есть: there is с одним предметом и неисчисляемым, there are — с несколькими | a1_nouns_core |
| a1_there_questions | A1 | thereisare 1 | Спросить Is there…? / Are there…?, ответить кратко и построить отрицание с any или no | a1_there_core |
| a1_there_review | A1 | thereisare 2 | Не путать there is и it is, is и are в одном задании без подсказки | a1_there_questions |
| a1_pronouns_personal | A1 | pronouns 0, 1 | Выбрать местоимение-подлежащее (I, he) или дополнение (me, him) по месту в предложении | — |
| a1_pronouns_possessive | A1 | pronouns 2 | Различать my перед существительным и mine вместо него; its и it's | a1_pronouns_personal |
| a1_pronouns_demonstrative | A1 | pronouns 4 | Выбрать this / that / these / those по числу и расстоянию | a1_nouns_core |
| a1_pronouns_questions | A1 | pronouns 5 | Задать вопрос с who, whose, what, which; отличать whose от who's | a1_be_core |
| a2_pronouns_reflexive | A2 | pronouns 3 | Употреблять myself, yourself… когда действие направлено на себя и не ставить их после глаголов без -ся | a1_pronouns_personal |
| a2_pronouns_one | A2 | pronouns 7 | Заменять повторяемое существительное на one / ones | a1_article_reference, a1_pronouns_demonstrative |
| a2_pronouns_review | A2 | pronouns 8 | Выбрать нужное местоимение в смешанных заданиях; me and him, it's / its | a1_pronouns_possessive, a2_pronouns_reflexive |
| b1_pronouns_relative | B1 | pronouns 6 | Связать части предложения словами who, which, that, whose, where | a1_pronouns_personal |
| a1_prep_place | A1 | prepositions 0, 1 | Выбрать in, on, at для места: в чём-то, на поверхности, в точке | — |
| a1_prep_position | A1 | prepositions 2 | Описать положение: under, between, opposite, next to, behind | a1_prep_place |
| a1_prep_time | A1 | prepositions 3 | Выбрать at, on, in для времени: час, день и дата, месяц и год | a1_prep_place |
| a2_prep_direction | A2 | prepositions 4 | Показать направление: to, into, out of, across, through; go home без to | a1_prep_position |
| a2_prep_review | A2 | prepositions 5 | Не ставить русские предлоги вместо английских: in Moscow, at home, to home → home | a1_prep_time, a2_prep_direction |
| a2_prep_verbs | A2 | prepositions 6 | Употреблять глаголы с постоянным предлогом: wait for, listen to, depend on | a1_simple_routines |
| a2_prep_adjectives | A2 | prepositions 7 | Употреблять прилагательные с постоянным предлогом: good at, afraid of, interested in | a1_be_core |
| b1_prep_nouns | B1 | prepositions 8 | Употреблять существительные с предлогом: reason for, increase in, solution to | a2_prep_verbs |
| a1_aboutme_basics | A1 | aboutme 0 | Назвать имя, откуда ты, где живёшь и чем занимаешься | a1_be_core |
| a1_aboutme_interests | A1 | aboutme 1 | Рассказать об интересах с like, love, enjoy + -ing и be into | a1_simple_routines |
| a1_aboutme_story | A1 | aboutme 2, 3 | Связно рассказать о себе в пяти фразах и не делать типичных ошибок (I am from…, I like…) | a1_aboutme_basics, a1_aboutme_interests |
| a1_cont_core | A1 | presentcont 0, 1 | Сказать, что происходит сейчас: am / is / are + -ing в утверждении, отрицании и вопросе | a1_be_core |
| a1_cont_spelling | A1 | presentcont 2 | Правильно писать -ing: making, running, lying | a1_cont_core |
| a2_cont_states | A2 | presentcont 3 | Не ставить в Continuous глаголы состояния (know, like, want) в основном значении | a1_cont_core, a1_simple_routines |
| a2_cont_vs_simple | A2 | presentcont 4 | Выбрать Continuous (сейчас, временно) или Simple (обычно, всегда) по смыслу | a1_cont_core, a1_simple_routines |
| a2_cont_review | A2 | presentcont 5 | Находить и исправлять ошибки Continuous: пропуск am/is/are, лишнее -ing | a1_cont_spelling, a2_cont_states |
| a2_comparisons_degrees | A2 | comparisons 0, 1 | Образовать сравнительную и превосходную степень коротких прилагательных (-er, -est) | a1_article_reference |
| a2_comparisons_long | A2 | comparisons 2 | Образовать степени длинных прилагательных с more / the most | a2_comparisons_degrees |
| a2_comparisons_irregular | A2 | comparisons 3 | Употреблять особые формы: good, better, the best; bad, worse, the worst; farther / further | a2_comparisons_degrees |
| a2_comparisons_than | A2 | comparisons 4 | Сравнивать с than и as … as; не смешивать more и -er | a2_comparisons_degrees |
| a2_comparisons_review | A2 | comparisons 5 | Сравнивать наречиями (faster, more carefully) и ставить the там, где он нужен | a2_comparisons_long, a2_comparisons_irregular, a2_comparisons_than |
| a2_asas_core | A2 | asas 0 | Сказать «такой же, как» и «не такой, как»: as … as, not as … as, twice as … as | a2_comparisons_than |
| a2_asas_review | A2 | asas 1 | Исправлять ошибки: as taller as, so tall as в утверждении | a2_asas_core |
| a1_questions_yesno | A1 | questions 0, 1 | Задать вопрос «да или нет» с do / does, be или can и кратко ответить | a1_simple_questions |
| a1_questions_wh | A1 | questions 2 | Задать вопрос с what, where, when, why, how: вопросительное слово + вспомогательный глагол | a1_questions_yesno |
| a1_questions_choice | A1 | questions 4 | Задать вопрос с выбором (tea or coffee?) и ответить вариантом | a1_questions_yesno |
| a2_questions_subject | A2 | questions 3 | Спросить о подлежащем без do: Who called? What happened? | a1_questions_wh |
| a2_questions_tags | A2 | questions 5 | Добавить хвостик: утверждение — отрицательный хвостик и наоборот | a1_questions_yesno |
| b1_questions_tags_special | B1 | questions 6 | Употреблять особые хвостики: aren't I, shall we, will you | a2_questions_tags |
| a2_questions_review | A2 | questions 7 | Исправлять ошибки в вопросах: Do you can…, What means…, лишний do | a1_questions_wh, a2_questions_subject, a2_questions_tags |
| a1_det_some_any | A1 | determinants 0, 1 | Выбрать some в утверждении и предложении, any — в отрицании и вопросе | a1_nouns_core |
| a2_det_negation | A2 | determinants 2 | Сказать «нет ни одного»: no, none, not any без двойного отрицания | a1_det_some_any |
| a2_det_compounds | A2 | determinants 3 | Употреблять somebody, anything, nowhere и их пары по тем же правилам, что some / any | a2_det_negation |
| a2_det_every_each | A2 | determinants 4 | Различать every, each и all; глагол после every в единственном числе | a1_nouns_core |
| a2_det_many_much | A2 | determinants 5 | Выбрать many или much по исчисляемости; a lot of — для обоих | a2_nouns_uncountable |
| a2_det_review | A2 | determinants 6 | Выбрать слово количества в смешанных заданиях | a2_det_compounds, a2_det_every_each, a2_det_many_much |
| a1_imperative_core | A1 | imperative 0 | Попросить, предложить и запретить: глагол без you, Don't + глагол, Let's + глагол | — |
| a2_imperative_polite | A2 | imperative 1 | Смягчить просьбу (please, could you…?) и понимать, где прямая форма нормальна | a1_imperative_core, a1_questions_yesno |
| a1_imperative_review | A1 | imperative 2 | Исправлять ошибки: Not be late, Don't to, Let's don't | a1_imperative_core |
| a1_havegot_core | A1 | havegot 0 | Сказать, что у тебя есть, с have got / has got; построить отрицание и вопрос | a1_pronouns_personal |
| a2_havegot_vs_have | A2 | havegot 1 | Выбрать have got или have: только «иметь», только настоящее; I got — «получил» | a1_havegot_core, a1_simple_questions |
| a2_havegot_review | A2 | havegot 2 | Исправлять ошибки: Do you have got, have got в прошлом и с действием | a2_havegot_vs_have |
| a2_both_either | A2 | botheither 0 | Выбрать both, either, neither для двух предметов; all, any, none — для трёх и больше | a1_nouns_core |
| b1_both_pairs | B1 | botheither 1 | Связывать два варианта: both … and, either … or, neither … nor — с одним отрицанием | a2_both_either |
| a2_so_neither | A2 | botheither 2 | Ответить «я тоже» на утверждение (So do I) и на отрицание (Neither do I) с нужным вспомогательным | a1_simple_questions |
| b1_both_review | B1 | botheither 3 | Исправлять ошибки: the both, двойное отрицание с neither, Me too на отрицание | b1_both_pairs, a2_so_neither |
| a1_greetings_hello | A1 | greetings 0 | Поздороваться и попрощаться в подходящем регистре и ответить на How are you? | — |
| a1_greetings_meet | A1 | greetings 1 | Представиться, представить другого и ответить на Nice to meet you | a1_greetings_hello, a1_be_core |
| a2_greetings_smalltalk | A2 | greetings 2 | Начать, поддержать и закончить лёгкий разговор на безопасную тему | a1_greetings_meet |
| a1_greetings_phrases | A1 | greetings 3, 4 | Понимать и употреблять фразы приветствия в связном диалоге | a1_greetings_meet |
| a1_greetings_review | A1 | greetings 5 | Не говорить кальками: Normal, Good night при встрече, What is your work? | a1_greetings_meet |
| a1_family_core | A1 | family 0 | Назвать близких родственников; cousin, siblings, parents и relatives | — |
| a2_family_inlaws | A2 | family 1 | Назвать родню по браку (-in-law) и через отчима или мачеху (step-) | a1_family_core |
| a2_family_relationships | A2 | family 2 | Рассказать об отношениях: get married, get on with, take after, grow up | a1_family_core |
| a1_family_phrases | A1 | family 3, 4 | Рассказать о своей семье связно, в диалоге | a1_family_core |
| a1_family_review | A1 | family 5 | Исправлять ошибки: married with, two childs, brother вместо cousin | a1_family_core |
| a1_numbers_1_20 | A1 | numbers 1 | Называть и писать числа 1–20; различать на слух thirteen и thirty | — |
| a1_numbers_big | A1 | numbers 2 | Называть десятки, сотни и тысячи: forty, two hundred без -s, hundreds of | a1_numbers_1_20 |
| a1_numbers_ordinal | A1 | numbers 0, 3 | Различать количественные и порядковые числа и образовывать порядковые: first, fifth, twelfth | a1_numbers_1_20 |
| a2_numbers_dates | A2 | numbers 4 | Читать даты, годы, дроби и проценты | a1_numbers_ordinal, a1_numbers_big |
| a2_numbers_fractions | A2 | numbers 6 | Читать дроби (a half, a third, three quarters), проценты и простые действия | a1_numbers_ordinal |
| a2_numbers_review | A2 | numbers 5 | Исправлять ошибки в написании и чтении чисел: fourty, nineth, 21th | a2_numbers_dates, a2_numbers_fractions |
| a1_past_meaning | A1 | pastsimp 0 | Понимать, когда нужен Past Simple: закончилось, есть время в прошлом (yesterday, ago, last) | a1_simple_routines |
| a1_past_forms | A1 | pastsimp 1 | Строить отрицание и вопрос с did и начальной формой; was / were без did | a1_past_meaning, a1_simple_questions |
| a1_past_ed | A1 | pastsimp 2 | Писать и произносить -ed: stopped, studied; три звука /t/, /d/, /ɪd/ | a1_past_meaning |
| a1_past_irregular | A1 | pastsimp 3 | Узнавать и употреблять частые неправильные глаголы: went, saw, had, took | a1_past_ed |
| a1_past_review | A1 | pastsimp 4 | Исправлять ошибки: did went, was go, have seen yesterday | a1_past_forms, a1_past_irregular |
| a2_modals_rules | A2 | modalverbs 0 | Соблюдать общие правила модальных: начальная форма без to, без -s, вопрос без do | a1_simple_questions |
| a2_modals_can | A2 | modalverbs 1 | Говорить об умении и возможности с can, could, be able to; could и was able to в прошлом | a2_modals_rules, a1_past_meaning |
| a2_modals_may | A2 | modalverbs 2 | Спрашивать разрешение и говорить о возможности с may и might | a2_modals_rules |
| a2_modals_must | A2 | modalverbs 3 | Различать must, have to, mustn't и don't have to; had to в прошлом | a2_modals_rules |
| a2_modals_advice | A2 | modalverbs 4 | Давать совет и предупреждение: should, ought to, had better; предлагать с shall | a2_modals_rules |
| b1_modals_past | B1 | modalverbs 5 | Делать вывод и жалеть о прошлом: must have, can't have, should have done | a2_modals_must, a2_modals_may |
| a2_modals_review | A2 | modalverbs 6 | Исправлять ошибки: can swims, must to go, will can | a2_modals_can, a2_modals_must, a2_modals_advice |
| a1_time_clock | A1 | timemoney 0 | Назвать время словами (past, to, half, quarter) и цифрами | a1_numbers_1_20 |
| a1_time_dates | A1 | timemoney 1 | Выбрать on, in, at для даты, месяца, времени; читать годы | a1_time_clock, a1_numbers_ordinal |
| a1_money_prices | A1 | timemoney 2 | Читать цены и спрашивать о них: How much is / are; much money | a1_numbers_big |
| a2_measures | A2 | timemoney 3 | Понимать имперские меры: дюймы, футы, мили, фунты | a1_numbers_big |
| a1_timemoney_phrases | A1 | timemoney 4, 5 | Понимать и употреблять фразы о времени и деньгах в диалоге на рынке | a1_time_clock, a1_money_prices |
| a1_timemoney_review | A1 | timemoney 6 | Исправлять ошибки: half past eight вместо 7:30, a five minutes walk, five dollar | a1_timemoney_phrases |
| a1_wordorder_svo | A1 | wordorder 0 | Строить предложение по схеме «кто — делает — что»; не пропускать подлежащее (It's cold) | a1_be_core |
| a2_wordorder_frequency | A2 | wordorder 1 | Ставить always, often, never перед обычным глаголом, после be и вспомогательного | a1_wordorder_svo, a1_simple_routines |
| a2_wordorder_tail | A2 | wordorder 2 | Ставить уточнения в конце по порядку «как — где — когда»; ничего между глаголом и дополнением | a1_wordorder_svo |
| b1_wordorder_adjectives | B1 | wordorder 3 | Ставить несколько прилагательных в обычном порядке: мнение — размер — возраст — цвет — материал | a1_wordorder_svo |
| a2_wordorder_also_enough | A2 | wordorder 4 | Ставить also, only, too, enough на своё место | a2_wordorder_frequency |
| a2_wordorder_review | A2 | wordorder 5 | Исправлять ошибки порядка слов: like very much coffee, go always | a2_wordorder_frequency, a2_wordorder_tail, a2_wordorder_also_enough |
| a1_directions_ask | A1 | directions 0 | Вежливо спросить дорогу: Excuse me, how do I get to…? Is there a … near here? | a1_there_core |
| a1_directions_explain | A1 | directions 1 | Объяснить и понять дорогу: go straight on, turn left, on the corner, opposite | a1_directions_ask, a1_prep_place, a1_imperative_core |
| a1_directions_practice | A1 | directions 2, 3 | Понимать объяснение дороги в связном диалоге | a1_directions_explain |
| a1_directions_review | A1 | directions 4 | Не говорить кальками: say me, turn to left, in the left | a1_directions_practice |
| a1_shopping_choose | A1 | shopping 0 | Попросить размер и цвет, примерить вещь (try on), сказать, подходит ли она (fit / suit) | a1_greetings_phrases |
| a1_shopping_pay | A1 | shopping 1 | Спросить цену и способ оплаты: by card, in cash, receipt, 20% off | a1_shopping_choose, a1_money_prices |
| a2_shopping_return | A2 | shopping 2 | Вернуть или обменять покупку: return, exchange, refund, faulty | a1_shopping_pay |
| a1_shopping_practice | A1 | shopping 3, 4 | Понимать фразы покупателя и продавца в диалоге | a1_shopping_pay |
| a1_shopping_review | A1 | shopping 5 | Исправлять ошибки: How much costs it, measure вместо try on, Give me | a1_shopping_practice |
| a1_restaurant_arrive | A1 | restaurant 0 | Попросить столик и меню, сказать о брони | a1_greetings_phrases |
| a1_restaurant_order | A1 | restaurant 1 | Заказать вежливо: I'd like, I'll have, Can I have…? | a1_restaurant_arrive |
| a1_restaurant_bill | A1 | restaurant 2 | Попросить счёт, заплатить, понять, включено ли обслуживание | a1_restaurant_order, a1_money_prices |
| a1_restaurant_practice | A1 | restaurant 3, 4 | Понимать заказ в диалоге с официантом | a1_restaurant_order |
| a1_restaurant_review | A1 | restaurant 5 | Просить вопросом, а не приказом: Can I have, не Give me / I want | a1_restaurant_practice |
| a1_weather_words | A1 | weather 0 | Говорить о погоде через it: It's sunny, It's raining; sun → sunny | a1_be_core |
| a1_weather_talk | A1 | weather 1 | Спросить о погоде, назвать температуру и прогноз | a1_weather_words |
| a2_nature_words | A2 | weather 2 | Назвать места на природе и не путать the с реками и морями и без the с отдельными горами | a1_weather_words, a1_article_zero |
| a1_weather_practice | A1 | weather 3, 4 | Понимать разговор о погоде | a1_weather_talk |
| a1_weather_review | A1 | weather 5 | Исправлять ошибки: Today is sun, a nice weather, strong rain | a1_weather_practice |
| a1_food_products | A1 | food 0 | Называть продукты и отличать неисчисляемые (bread, rice) от тех, что считают (eggs) | a1_nouns_core |
| a2_food_cooking | A2 | food 1 | Понимать глаголы готовки в рецепте: boil, fry, bake, chop | a1_food_products, a1_imperative_core |
| a1_food_taste_meals | A1 | food 2 | Описать вкус прилагательным (salty, sweet) и сказать have breakfast / lunch / dinner | a1_food_products |
| a1_food_practice | A1 | food 3, 4 | Понимать разговор о еде и холодильнике | a1_food_taste_meals |
| a1_food_review | A1 | food 5 | Исправлять ошибки: a bread, very salt, Russian kitchen, take a lunch | a1_food_practice |
| a1_jobs_names | A1 | jobs 0 | Назвать профессию с a / an: I'm a nurse, he's an engineer | a1_article_introduction |
| a2_jobs_work_job | A2 | jobs 1 | Различать job (место, считаем) и work (работа вообще, без a) | a1_jobs_names, a2_nouns_uncountable |
| a1_jobs_talk | A1 | jobs 2 | Спросить и рассказать о работе: What do you do? I work as / for / at / in | a1_jobs_names, a1_simple_questions |
| a2_jobs_practice | A2 | jobs 3, 4 | Понимать разговор о работе | a1_jobs_talk, a2_jobs_work_job |
| a2_jobs_review | A2 | jobs 5 | Исправлять ошибки: I'm teacher, a lot of works, What is your work? | a2_jobs_practice |
| a1_appearance_looks | A1 | appearance 0 | Описать рост, фигуру, возраст, волосы и лицо; have для волос и глаз | a1_havegot_core |
| a2_appearance_order | A2 | appearance 1 | Ставить прилагательные внешности в обычном порядке: long dark hair | a1_appearance_looks |
| a1_character | A1 | appearance 2 | Назвать черты характера и их противоположности | a1_be_core |
| a2_like_looklike | A2 | appearance 3 | Различать What is she like? (характер), What does she look like? (внешность) и take after | a1_appearance_looks, a1_character, a1_simple_questions |
| a2_appearance_practice | A2 | appearance 4, 5 | Понимать описание человека в диалоге | a2_like_looklike |
| a2_appearance_review | A2 | appearance 6 | Исправлять ошибки: a long hair, How does she look like, He is with blue eyes | a2_appearance_practice, a2_appearance_order |
| a1_body_parts | A1 | body 0 | Называть части тела; arm / hand, leg / foot, finger / toe | a1_nouns_core |
| a1_body_ache | A1 | body 1 | Сказать, что болит: headache, sore throat, my knee hurts | a1_body_parts, a1_havegot_core |
| a2_body_habits | A2 | body 2 | Говорить о здоровых привычках: keep fit, work out, give up, put on weight | a1_body_ache |
| a1_body_practice | A1 | body 3, 4 | Понимать разговор о самочувствии | a1_body_ache |
| a1_body_review | A1 | body 5 | Исправлять ошибки: My head is ill, I have temperature, Be healthy! после чиха | a1_body_practice |
| a1_clothes_words | A1 | clothes 0 | Называть одежду; trousers и jeans — всегда множественное, a pair of | a1_nouns_core |
| a1_clothes_accessories | A1 | clothes 1 | Называть обувь и аксессуары | a1_clothes_words |
| a2_clothes_verbs | A2 | clothes 2 | Различать put on и wear, fit и suit, go with | a1_clothes_words, a1_cont_core |
| a2_clothes_practice | A2 | clothes 3, 4 | Понимать разговор в примерочной | a2_clothes_verbs |
| a2_clothes_review | A2 | clothes 5 | Исправлять ошибки: dressing my coat, goes you, a trouser | a2_clothes_practice |
| a1_home_rooms | A1 | home 0 | Называть комнаты; ground floor и first floor в Британии и США | a1_there_core, a1_numbers_ordinal |
| a1_home_furniture | A1 | home 1 | Называть мебель и технику: wardrobe и cupboard, cooker и plate | a1_home_rooms |
| a2_home_chores | A2 | home 2 | Называть дела по дому: do the cleaning, make the bed, take out the rubbish | a1_home_furniture |
| a1_home_practice | A1 | home 3, 4 | Понимать рассказ о квартире | a1_home_furniture |
| a2_home_review | A2 | home 5 | Исправлять ошибки: the 1 floor, make cleaning, plate вместо cooker | a1_home_practice, a2_home_chores |
| a1_hobbies_ing | A1 | hobbies 0 | Называть хобби формой на -ing; после enjoy — -ing | a1_simple_routines |
| a1_hobbies_play_go_do | A1 | hobbies 1 | Выбрать play, go или do для спорта; the с инструментами | a1_hobbies_ing |
| a2_hobbies_talk | A2 | hobbies 2 | Рассказать о хобби: be into, take up, twice a week | a1_hobbies_play_go_do |
| a1_hobbies_practice | A1 | hobbies 3, 4 | Понимать разговор о планах на выходные | a1_hobbies_play_go_do |
| a2_hobbies_review | A2 | hobbies 5 | Исправлять ошибки: play swimming, do football, the football | a1_hobbies_practice, a2_hobbies_talk |
| a1_emotions_words | A1 | emotions 0 | Назвать чувство через be или feel | a1_be_core |
| a2_emotions_prep | A2 | emotions 1 | Употреблять чувство с нужным предлогом: afraid of, angry with, proud of | a1_emotions_words, a1_prep_place |
| a2_emotions_ed_ing | A2 | emotions 2 | Различать -ed (что чувствую) и -ing (что вызывает): bored / boring | a1_emotions_words |
| a2_emotions_practice | A2 | emotions 3, 4 | Понимать разговор о переживаниях | a2_emotions_prep, a2_emotions_ed_ing |
| a2_emotions_review | A2 | emotions 5 | Исправлять ошибки: I'm boring, afraid from, angry on | a2_emotions_practice |
| a1_study_words | A1 | study 0 | Называть школьные и вузовские слова: subject, mark, lecture | a1_nouns_core |
| a2_study_verbs | A2 | study 1 | Различать take, pass, fail an exam и study / learn | a1_study_words, a1_past_forms |
| a1_study_classroom | A1 | study 2 | Спросить и попросить на занятии: Can I ask…? Could you repeat…? | a1_questions_yesno |
| a2_study_practice | A2 | study 3, 4 | Понимать разговор перед экзаменом | a2_study_verbs, a1_study_classroom |
| a2_study_review | A2 | study 5 | Исправлять ошибки: passed вместо took, I learn at university, made my homework | a2_study_practice |
| a1_tech_words | A1 | technology 0 | Называть устройства и вещи в телефоне и компьютере; laptop, а не notebook | a1_nouns_core |
| a2_tech_verbs | A2 | technology 1 | Различать download и upload; log in, sign up, install | a1_tech_words, a1_imperative_core |
| a2_tech_problems | A2 | technology 2 | Описать неполадку: keeps crashing, won't turn on, is dead | a2_tech_verbs |
| a2_tech_practice | A2 | technology 3, 4 | Понимать разговор о технике | a2_tech_problems |
| a2_tech_review | A2 | technology 5 | Исправлять ошибки: notebook, discharged, download to Instagram | a2_tech_practice |
| a2_uk_us_words | A2 | britishamerican 0 | Узнавать пары бытовых слов: flat / apartment, lift / elevator | — |
| a2_uk_us_spelling | A2 | britishamerican 1 | Узнавать британское и американское написание: colour / color, centre / center | — |
| b1_uk_us_grammar | B1 | britishamerican 2 | Узнавать грамматические различия: have got / have, at / on the weekend, got / gotten | a2_havegot_vs_have, a1_past_forms |
| b1_uk_us_sound | B1 | britishamerican 3 | Узнавать на слух британское и американское произношение: r, t, can't | intro_reading_r |
| b1_uk_us_practice | B1 | britishamerican 4, 5 | Понимать собеседника с другим вариантом английского | a2_uk_us_words, b1_uk_us_grammar |
| a2_colloc_intro | A2 | collocations 0 | Понимать, что такое устойчивое сочетание, и не переводить его по словам | — |
| a2_colloc_verbs | A2 | collocations 1 | Выбрать make, do, take, have, pay для сочетания: make a mistake, take a photo | a2_colloc_intro |
| a2_colloc_adjectives | A2 | collocations 2 | Выбрать прилагательное для сочетания: heavy rain, strong coffee, high price | a2_colloc_intro |
| a2_colloc_practice | A2 | collocations 3, 4 | Употреблять сочетания в связной речи | a2_colloc_verbs, a2_colloc_adjectives |
| a2_colloc_review | A2 | collocations 5 | Исправлять ошибки: did a mistake, make a photo, strong rain | a2_colloc_practice |
| b1_idioms_intro | B1 | idioms 0 | Понимать частые идиомы целиком: a piece of cake, under the weather | — |
| b1_idioms_pairs | B1 | idioms 1 | Сопоставлять английские идиомы с русскими: kill two birds with one stone | b1_idioms_intro |
| b1_idioms_register | B1 | idioms 2 | Не употреблять идиомы в деловом письме и отчёте | b1_idioms_intro |
| b1_idioms_practice | B1 | idioms 3, 4 | Понимать идиомы в разговоре | b1_idioms_pairs, b1_idioms_register |
| a2_strongadj_words | A2 | strongadjectives 0 | Заменять very + обычное прилагательное сильным: huge, exhausted, starving | a1_be_core |
| a2_strongadj_very | A2 | strongadjectives 1 | Ставить very с обычными, absolutely — с сильными, really — с теми и другими | a2_strongadj_words |
| a2_strongadj_practice | A2 | strongadjectives 2, 3 | Употреблять сильные прилагательные в речи | a2_strongadj_very |
| a2_strongadj_review | A2 | strongadjectives 4 | Исправлять ошибки: very huge, absolutely cold, very perfect | a2_strongadj_practice |
| a1_goingto_form | A1 | begoingto 0 | Сказать о плане: am / is / are going to + начальная форма | a1_be_core |
| a2_goingto_will | A2 | begoingto 1 | Выбрать going to (план, примета) или will (решение сейчас, обещание) | a1_goingto_form |
| a2_goingto_review | A2 | begoingto 2 | Исправлять ошибки: I going to, will going to, am going to yesterday | a2_goingto_will |
| a1_therewas_core | A1 | therewaswere 0 | Сказать, что где было: there was с одним, there were с несколькими | a1_there_core, a1_past_meaning |
| a1_therewas_negq | A1 | therewaswere 1 | Спросить Was there…? / Were there…? и ответить; there wasn't / there was no | a1_therewas_core, a1_there_questions |
| a1_therewas_review | A1 | therewaswere 2 | Исправлять ошибки: there was many, It was a party | a1_therewas_negq |
| a1_wouldlike_core | A1 | wouldlike 0 | Вежливо попросить и предложить: I'd like a coffee, I'd like to + глагол | a1_simple_routines |
| a1_wouldlike_questions | A1 | wouldlike 1 | Задать вопрос Would you like…? и ответить Yes, please / I'd love to | a1_wouldlike_core |
| a1_wouldlike_review | A1 | wouldlike 2 | Исправлять ошибки: I want в просьбе, would like go, do you would like | a1_wouldlike_questions |
| a2_fewlittle_core | A2 | fewlittle 0 | Выбрать few или little по исчисляемости и a few / a little по смыслу «немного, но хватает» | a2_det_many_much |
| a2_fewlittle_talk | A2 | fewlittle 1 | В разговоре говорить not many / not much; quite a few — «довольно много» | a2_fewlittle_core |
| a2_fewlittle_review | A2 | fewlittle 2 | Исправлять ошибки: a little friends, few water, only few | a2_fewlittle_talk |
| b1_generic_kinds | B1 | genericarticles 0 | Говорить обо всём виде тремя способами: dogs, a dog, the dog — и выбирать обычный (множественное без артикля) | a1_article_zero |
| b1_generic_groups | B1 | genericarticles 1 | Называть группу людей the + прилагательное с глаголом во множественном числе | a1_article_reference |
| b1_generic_abstract | B1 | genericarticles 2 | Употреблять абстрактные слова без артикля в общем смысле и с the, когда смысл уточнён | a1_article_zero |
| b1_generic_review | B1 | genericarticles 3 | Исправлять ошибки: The life is beautiful, the poors, the rich is | b1_generic_kinds, b1_generic_groups, b1_generic_abstract |
| a2_names_countries | A2 | articlesnames 0 | Не ставить the с городами и большинством стран; ставить с the USA, the UK, the Netherlands | a1_article_zero |
| a2_names_geography | A2 | articlesnames 1 | Ставить the с реками, морями, хребтами, группами островов; без the — отдельная гора, озеро, континент | a2_names_countries |
| b1_names_city | B1 | articlesnames 2 | Не ставить the с улицами, площадями, парками; ставить с отелями, музеями, театрами и названиями с of | a2_names_countries |
| b1_names_review | B1 | articlesnames 3 | Исправлять ошибки: the Moscow, in USA, the Lake Baikal | a2_names_geography, b1_names_city |
| a2_usedto_core | A2 | usedto 0 | Сказать о прошлой привычке или факте с used to; отрицание и вопрос с use | a1_past_forms |
| a2_usedto_review | A2 | usedto 1 | Исправлять ошибки: I use to, used to living, didn't used to | a2_usedto_core |
| b1_usedto_vs_beused | B1 | usedto 2 | Различать used to + глагол (раньше) и be used to + -ing (привык) | a2_usedto_core |
| a2_therewillbe_core | A2 | therewillbe 0 | Сказать, что что-то будет: there will be, there won't be, Will there be…? | a1_there_questions |
| a2_therewillbe_review | A2 | therewillbe 1 | Не пропускать be: There will a party ✗ | a2_therewillbe_core |
| a2_pastcont_core | A2 | pastcont 0 | Сказать, что действие шло в момент прошлого: was / were + -ing; отличать от Past Simple | a1_past_meaning, a1_cont_core |
| a2_pastcont_negq | A2 | pastcont 1 | Строить wasn't / weren't + -ing и вопрос Was / Were…? | a2_pastcont_core |
| a2_pastcont_markers | A2 | pastcont 2 | Узнавать подсказки while, when, at that moment, this time yesterday | a2_pastcont_core |
| a2_pastcont_ing | A2 | pastcont 3 | Правильно писать -ing в Past Continuous | a1_cont_spelling |
| b1_pastcont_interrupt | B1 | pastcont 4 | Сочетать длинное действие (Past Continuous) и прервавшее его короткое (Past Simple) | a2_pastcont_markers, a1_past_irregular |
| a2_pastcont_review | A2 | pastcont 5 | Исправлять ошибки: was read, they was, was knowing | a2_pastcont_negq, a2_pastcont_ing |
| a1_future_will | A1 | futuresimp 0 | Сказать о решении сейчас, обещании, предложении помощи и прогнозе: will + начальная форма | a1_simple_routines |
| a1_future_negq | A1 | futuresimp 1 | Строить won't и вопрос Will you…? без do; краткие ответы | a1_future_will |
| a1_future_contractions | A1 | futuresimp 2 | Употреблять и понимать сокращения I'll, she'll, won't | a1_future_will |
| a2_future_markers | A2 | futuresimp 3 | Узнавать подсказки будущего и мнения; после when и if — настоящее | a1_future_will |
| a2_future_will_goingto | A2 | futuresimp 4 | Выбирать will (решение сейчас, мнение) или going to (план, признаки) | a2_future_markers, a2_goingto_will |
| a2_future_review | A2 | futuresimp 5 | Исправлять ошибки: will to, wills, do you will, will can | a1_future_negq |
| a2_perfect_meaning | A2 | presentperf 0 | Понимать, когда нужен Present Perfect: результат сейчас, опыт, длится до сих пор | a1_past_meaning |
| a2_perfect_negq | A2 | presentperf 1 | Строить haven't / hasn't + V3 и вопрос Have / Has…? | a2_perfect_meaning |
| a2_perfect_markers | A2 | presentperf 2 | Ставить just, already, yet, ever, never; различать since и for | a2_perfect_meaning |
| a2_perfect_v3 | A2 | presentperf 3 | Образовывать V3 правильных и частых неправильных глаголов; been и gone | a1_past_irregular |
| b1_perfect_vs_past | B1 | presentperf 4 | Выбирать Present Perfect (результат, без времени) или Past Simple (указано время) | a2_perfect_markers |
| a2_perfect_review | A2 | presentperf 5 | Исправлять ошибки: have went, have seen yesterday | a2_perfect_negq, a2_perfect_v3 |
| a2_alreadyyet_meaning | A2 | alreadyyet 0 | Различать already, yet, still и just по смыслу | a2_perfect_meaning |
| a2_alreadyyet_position | A2 | alreadyyet 1 | Ставить already, just между have и V3, still перед глаголом, yet в конце | a2_alreadyyet_meaning |
| b1_alreadyyet_nuance | B1 | alreadyyet 2 | Слышать оттенки: still not — досада, already в вопросе — удивление | a2_alreadyyet_position |
| a2_alreadyyet_review | A2 | alreadyyet 3 | Исправлять ошибки: yet в утверждении, just в конце | a2_alreadyyet_position |
| a1_contractions_core | A1 | contractions 0 | Писать и читать сокращения с апострофом: I'm, doesn't, won't | a1_be_core |
| a2_contractions_s_d | A2 | contractions 1 | Понимать 's (is / has / чей) и 'd (would / had) по следующему слову | a1_contractions_core |
| a2_contractions_full | A2 | contractions 2 | Писать полностью в коротком ответе (Yes, I am) и в официальном тексте | a1_contractions_core |
| a2_contractions_review | A2 | contractions 3 | Исправлять ошибки: Yes, I'm; its / it's; willn't | a2_contractions_full |
