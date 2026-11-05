"""Icons for the second and later parts of cards (units in tree/curriculum.json)."""
from neon import *

W = 17
ICONS = {}


def icon(key, comment, *strokes):
    ICONS[key] = (comment, [(d, w) for d, w in strokes])


def T(s, y=300, scale=1.0, x=256):
    return (text(s, x, y, scale, center=True), W)


def fit(s, maxw=300, maxscale=1.3):
    return min(maxscale, maxw / max(text_width(s), 1))


def word(s, y=300, maxw=300, maxscale=1.3):
    return T(s, y, fit(s, maxw, maxscale))


# pluralnouns
icon('a2_nouns_special', 'Часть «Knives, jeans, news»: джинсы — всегда во множественном',
     ('M168,110 L344,110 L372,404 L292,404 L256,206 L220,404 L140,404 Z M168,150 L344,150', 19))
icon('b2_nouns_rare', 'Часть «Редкие формы: crises»: cactus → cacti', word('cacti', 300))
# articles
icon('a1_article_reference', 'Часть «The или без артикля»: the — тот самый',
     word('the', 250, 260), (circle(256, 352, 26), 15), ('M150,352 L206,352 M306,352 L362,352', 15))
icon('a2_article_special', 'Часть «The best, the school»: the best — звезда',
     word('the', 380, 240), ('M256,84 L272,126 L318,128 L282,154 L294,198 L256,172 L218,198 L230,154 L194,128 L240,126 Z', 15))
# presentsimp
icon('a1_simple_routines', 'Часть «Факты и привычки»: повторяется — he works',
     (arc(256, 256, 140, -60, 250), 19), (arrowhead(326, 135, 30, 34), 19), word('-s', 300, 160))
icon('a1_simple_questions', "Часть «Don't, doesn't, do you…?»", (bubble(96, 118, 416, 352), 19), T('do?', 284, 0.9))
# pronouns
icon('a2_pronouns_reflexive', 'Часть «Myself, one, ones»: зеркало — сам себя',
     ('M256,92 Q352,92 352,220 Q352,348 256,348 Q160,348 160,220 Q160,92 256,92 Z M256,348 L256,412 M196,412 L316,412', 19), T('me', 246, 0.62))
icon('b1_pronouns_relative', 'Часть «Слово «который»»: which указывает назад',
     word('which', 220, 300), ('M370,270 Q370,380 256,380 Q150,380 142,300', 17), (arrowhead(142, 296, -95, 28), 17))
# prepositions
icon('a2_prep_direction', 'Часть «Куда: to, into, across»: стрелка внутрь', (rrect(250, 140, 420, 372, 30), 19),
     ('M84,256 L320,256', 19), (arrowhead(322, 256, 0, 34), 19))
icon('a2_prep_verbs', 'Часть «Listen to, good at»: listen to', ('M140,300 L140,250 A116,116 0 0,1 372,250 L372,300', 19),
     (rrect(112, 286, 168, 392, 22) + ' ' + rrect(344, 286, 400, 392, 22), 17), T('to', 372, 0.62))
icon('b1_prep_nouns', 'Часть «Reason for, rise in»: рост — rise in', ('M100,360 L190,280 L250,320 L380,170', 19),
     (arrowhead(382, 168, -50, 34), 19), T('in', 410, 0.66, 330))
# presentcont
icon('a2_cont_vs_simple', 'Часть «Сейчас или обычно»: -ing или -s', T('-s', 300, 0.8, 158), ('M256,150 L256,370', 15), T('ing', 300, 0.6, 362))
# questions
icon('a2_questions_subject', 'Часть «Who called? — без do»', word('who?', 300, 300))
icon('a2_questions_tags', "Часть «Хвостики: don't you?»: вопрос-хвостик",
     ('M160,150 L330,150 L410,256 L330,362 L160,362 Q120,362 120,322 L120,190 Q120,150 160,150 Z', 19), (circle(345, 256, 13), 15), T('?', 318, 1.1, 236))
icon('b1_questions_tags_special', "Часть «Aren't I, shall we»", word('shall?', 300, 320))
# determinants
icon('a2_det_many_much', 'Часть «None, every, much»: сколько — much', word('much', 290, 320),
     ('M150,370 L150,370.5 M206,370 L206,370.5 M256,370 L256,370.5 M306,370 L306,370.5', 26))
# imperative
icon('a2_imperative_polite', 'Часть «Как попросить вежливо»: please', word('please', 280, 330), ('M190,360 Q256,404 322,360', 15))
# havegot
icon('a2_havegot_vs_have', 'Часть «Have got или have»', T('have', 220, 0.78), T('got', 360, 0.78), ('M150,268 L362,268', 15))
# botheither
icon('a2_so_neither', 'Часть «So do I, Neither do I»: я тоже',
     (bubble(80, 120, 290, 290) + ' ' + bubble(222, 222, 432, 392, tail='right'), 17),
     (line((140, 206), (176, 240), (234, 170)) + ' ' + line((282, 308), (318, 342), (376, 272)), 17))
icon('b1_both_pairs', 'Часть «Both … and, either … or»: оба вместе', (circle(196, 256, 110) + ' ' + circle(316, 256, 110), 19))
# greetings
icon('a2_greetings_smalltalk', 'Часть «Small talk»: разговор о погоде', (bubble(96, 118, 416, 352), 19), (circle(256, 236, 40), 17),
     ('M256,160 L256,172 M256,300 L256,312 M180,236 L192,236 M320,236 L332,236 M202,182 L211,191 M301,281 L310,290 M310,182 L301,191 M211,281 L202,290', 15))
# family
icon('a2_family_inlaws', 'Часть «Родня и отношения»: кольца', (circle(206, 286, 92) + ' ' + circle(318, 286, 92), 19),
     ('M318,194 L298,166 L318,140 L338,166 Z', 15))
# numbers
icon('a1_numbers_big', 'Часть «Десятки, сотни, тысячи»', word('1000', 310, 320))
icon('a1_numbers_ordinal', 'Часть «Первый, второй, третий»: пьедестал',
     ('M96,400 L96,300 L192,300 L192,236 L320,236 L320,330 L416,330 L416,400 Z', 19), T('1', 206, 0.8))
icon('a2_numbers_dates', 'Часть «Даты, дроби, проценты»', T('%', 330, 1.7))
# pastsimp
icon('a1_past_irregular', 'Часть «Неправильные глаголы»: went', word('went', 300, 320))
icon('a1_past_forms', "Часть «Did и didn't»", word('did?', 300, 300))
# modalverbs
icon('a2_modals_must', 'Часть «Must, have to, should»: обязательно', ('M256,108 L416,388 L96,388 Z', 19),
     ('M256,206 L256,300', 19), ('M256,346 L256,346.5', 26))
icon('b1_modals_past', 'Часть «Must have, should have»: о прошлом', word('have', 340, 280),
     (arc(256, 210, 96, 200, 340), 17), (arrowhead(166, 176, 110, 30), 17))
# beableto
icon('b1_beableto_past', 'Часть «Could или was able to»: сумел — кубок',
     ('M172,110 L340,110 L340,200 Q340,290 256,290 Q172,290 172,200 Z M256,290 L256,350 M196,400 L316,400 L300,350 L212,350 Z', 19),
     ('M172,140 Q110,140 116,192 Q122,236 176,236 M340,140 Q402,140 396,192 Q390,236 336,236', 15))
# infinitive
icon('b1_infinitive_patterns', 'Часть «Happy to, want you to»', word('you to', 300, 330))
icon('b2_infinitive_forms', 'Часть «To have done, to be done»: уже сделано', T('to', 250, 1.1, 200),
     (line((316, 250), (352, 292), (428, 186)), 19), ('M120,350 L392,350', 15))
# gerund
icon('b1_gerund_noun', 'Часть «Герундий как понятие»: -ing — это предмет', (rrect(96, 150, 416, 362, 36), 19), T('ing', 290, 0.9))
icon('b1_ing_to_meaning', 'Часть «Stop doing, stop to do»: знак стоп',
     ('M206,96 L306,96 L376,166 L376,266 L306,336 L206,336 L136,266 L136,166 Z', 19), T('ing', 252, 0.62), ('M256,336 L256,416', 19))
# timemoney
icon('a2_measures', 'Часть «Мили, футы, фунты»: линейка', (rrect(84, 196, 428, 316, 20), 19),
     ('M132,196 L132,252 M180,196 L180,232 M228,196 L228,252 M276,196 L276,232 M324,196 L324,252 M372,196 L372,232', 15))
# wordorder
icon('a2_wordorder_frequency', 'Часть «Always, also, как, где»', word('always', 300, 340))
icon('b1_wordorder_adjectives', 'Часть «Big, old, red: порядок»: по размеру',
     (rrect(84, 196, 212, 324, 26) + ' ' + rrect(240, 222, 336, 318, 22) + ' ' + rrect(364, 246, 428, 310, 18), 19), ('M100,380 L412,380', 15),
     (arrowhead(414, 380, 0, 26), 15))
# shopping
icon('a2_shopping_return', 'Часть «Вернуть или обменять»: сумка и возврат',
     ('M132,196 L380,196 L404,400 L108,400 Z M192,196 Q192,120 256,120 Q320,120 320,196', 19),
     ('M300,300 Q300,250 250,250 L200,250', 17), (arrowhead(198, 250, 180, 28), 17))
# weather
icon('a2_nature_words', 'Часть «Горы, реки, море»', ('M84,330 L196,170 L262,262 L316,196 L428,330', 19),
     ('M84,390 Q128,360 172,390 Q216,420 260,390 Q304,360 348,390 Q392,420 428,396', 15))
# food
icon('a2_food_cooking', 'Часть «Готовка: boil, fry, bake»: сковорода', (circle(220, 300, 104), 19), ('M324,300 L430,300', 21),
     ('M180,150 Q160,124 180,98 M230,150 Q210,124 230,98 M280,150 Q260,124 280,98', 15))
# jobs
icon('a2_jobs_work_job', 'Часть «Job, work и разговор»: портфель', (rrect(96, 182, 416, 390, 32), 19),
     ('M206,182 L206,140 Q206,124 222,124 L290,124 Q306,124 306,140 L306,182 M96,262 L416,262 M256,250 L256,280', 17))
# appearance
icon('a2_appearance_order', 'Часть «Long dark hair, look like»: похож на',
     (circle(150, 230, 64) + ' ' + circle(362, 230, 64), 19), ('M100,380 Q100,310 150,310 Q200,310 200,380 M312,380 Q312,310 362,310 Q412,310 412,380', 17),
     ('M232,236 L280,236 M232,268 L280,268', 15))
# body
icon('a2_body_habits', 'Часть «Здоровые привычки»: сердце и пульс',
     ('M256,396 Q100,296 100,196 Q100,124 172,124 Q226,124 256,176 Q286,124 340,124 Q412,124 412,196 Q412,296 256,396 Z', 19),
     ('M150,250 L210,250 L236,206 L270,300 L296,250 L362,250', 15))
# clothes
icon('a2_clothes_verbs', 'Часть «Put on, wear, fit»: футболка',
     ('M196,110 Q256,160 316,110 L420,166 L384,236 L346,218 L346,404 L166,404 L166,218 L128,236 L92,166 Z', 19))
# home
icon('a2_home_chores', 'Часть «Дела по дому»: ведро', ('M146,206 L366,206 L340,404 L172,404 Z', 19), ('M156,206 Q156,110 256,110 Q356,110 356,206', 15),
     (circle(250, 152, 14) + ' ' + circle(306, 130, 10), 13))
# hobbies
icon('a2_hobbies_talk', 'Часть «Рассказ о хобби»: о музыке', (bubble(96, 118, 416, 352), 19),
     ('M236,300 L236,180 L316,164 L316,284', 17), (circle(214, 300, 22) + ' ' + circle(294, 284, 22), 15))
# emotions
icon('a2_emotions_prep', 'Часть «Afraid of, bored»: скучно', (circle(256, 256, 140), 19),
     ('M206,226 L206,226.5 M306,226 L306,226.5', 28), ('M196,316 L316,316', 17))
# study
icon('a2_study_verbs', 'Часть «Take или pass»: сдал экзамен', (rrect(132, 96, 380, 416, 26), 19),
     ('M182,166 L330,166 M182,216 L330,216 M182,266 L262,266', 15), (line((210, 342), (246, 376), (314, 300)), 19))
# technology
icon('a2_tech_verbs', 'Часть «Download, crash, fix»: скачать', ('M256,96 L256,300', 19), (arrowhead(256, 302, 90, 44), 19),
     ('M110,300 L110,396 L402,396 L402,300', 19))
# britishamerican
icon('b1_uk_us_grammar', 'Часть «UK и US: грамматика»', T('UK', 220, 0.72, 170), ('M226,410 L290,104', 15), T('US', 400, 0.72, 344))
# begoingto
icon('a2_goingto_will', 'Часть «Going to или will»: развилка', ('M256,410 L256,270 Q256,220 196,190 L140,160 M256,270 Q256,220 316,190 L372,160', 19),
     (arrowhead(136, 158, 207, 34) + ' ' + arrowhead(376, 158, -27, 34), 19))
# sosuch
icon('b1_so_such', 'Часть «So, such, so … that»: так!', word('so!', 300, 260))
# articlesnames
icon('b1_names_city', 'Часть «Названия в городе»: улица и дома',
     ('M84,400 L428,400 M110,400 L110,220 L190,220 L190,400 M210,400 L210,140 L300,140 L300,400 M320,400 L320,260 L402,260 L402,400', 19),
     ('M236,180 L236,180.5 M274,180 L274,180.5 M236,230 L236,230.5 M274,230 L274,230.5 M136,262 L136,262.5 M164,262 L164,262.5 M346,300 L346,300.5 M376,300 L376,300.5', 22))
# usedto
icon('b1_usedto_vs_beused', 'Часть «Used to или be used to»: привычное кресло',
     ('M150,250 L150,170 Q150,124 196,124 L316,124 Q362,124 362,170 L362,250 M110,250 Q110,220 136,220 Q160,220 160,250 L160,300 L352,300 L352,250 Q352,220 376,220 Q402,220 402,250 L402,346 L110,346 Z M140,346 L140,396 M372,346 L372,396', 17))
# pastcont
icon('b1_pastcont_interrupt', 'Часть «Когда что-то случилось»: процесс и вспышка',
     ('M84,300 Q128,270 172,300 Q216,330 236,312 M300,300 Q340,270 384,300 Q408,316 428,300', 17),
     ('M286,104 L232,236 L282,236 L240,384', 19))
# futuresimp
icon('a2_future_will_goingto', 'Часть «Will или going to»: указатель', ('M256,96 L256,416', 19),
     ('M256,140 L380,140 L416,176 L380,212 L256,212 M256,252 L132,252 L96,288 L132,324 L256,324', 17))
# conditionals
icon('b1_cond_unreal', 'Часть «If: если бы»: мечта-облако',
     ('M150,330 Q90,330 92,276 Q94,224 150,226 Q156,156 226,158 Q270,120 320,158 Q392,150 396,224 Q440,240 424,290 Q410,330 360,330 Z', 19), T('if', 298, 0.8))
icon('b2_cond_wish_linkers', 'Часть «Wish, unless, in case»: на всякий случай — зонт',
     ('M96,256 Q100,116 256,112 Q412,116 416,256 Q376,226 336,256 Q296,226 256,256 Q216,226 176,256 Q136,226 96,256 Z', 19),
     ('M256,256 L256,376 Q256,410 222,410 Q196,410 196,384', 19))
# wish
icon('b2_wish_past', 'Часть «Wish: о прошлом, would»: падающая звезда',
     ('M330,120 L350,172 L404,174 L362,208 L378,262 L330,230 L282,262 L298,208 L256,174 L310,172 Z', 17),
     ('M240,262 L104,398 M276,300 L176,400 M206,236 L120,322', 15))
# presentperf
icon('b1_perfect_time', 'Часть «Present Perfect: период»: с тех пор и до сейчас', ('M84,320 L428,320 M120,280 L120,360', 17),
     ('M120,280 Q256,140 392,280', 19), (arrowhead(394, 282, 50, 30), 19), (circle(400, 320, 18), 15))
# reportedspeech
icon('b1_reported_questions', 'Часть «Пересказ: asked, told to»: вопрос передают дальше', (bubble(84, 104, 300, 274), 17), T('?', 236, 0.9, 192),
     ('M330,190 Q410,200 404,300', 17), (arrowhead(402, 304, 95, 28), 17), (rrect(256, 320, 428, 410, 26), 17))
# activepassive
icon('b2_passive_more', 'Часть «Пассив: given, get, said»: подарок — was given', (rrect(110, 226, 402, 410, 22), 19),
     ('M96,186 L416,186 L416,226 L96,226 Z M256,186 L256,410 M256,186 Q196,100 166,146 Q150,186 256,186 Q316,100 346,146 Q362,186 256,186', 17))
# alreadyyet
icon('b1_alreadyyet_nuance', 'Часть «Оттенки смысла»: регулятор', ('M96,200 L416,200 M96,320 L416,320', 17),
     (circle(196, 200, 30) + ' ' + circle(330, 320, 30), 19))
# contractions
icon('a2_contractions_s_d', "Часть «'s, 'd и полная форма»", T("'d", 320, 1.4))
# besupposedto
icon('b2_be_to', 'Часть «Be to: официально»: объявление — is to', (rrect(120, 96, 392, 416, 26), 19),
     ('M170,160 L342,160 M170,206 L300,206', 15), word('is to', 340, 200))
