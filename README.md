# keiting-infocards — контент приложения Keitling

Здесь лежит всё, что приложение скачивает из интернета: карточки теории, словарь, предложения,
цитаты, тексты, опрос, экзамены, курс «Древа» и адрес сервера ИИ.
Приложение берёт файлы по адресу
`https://raw.githubusercontent.com/KiproL/keiting-infocards/main/<путь к файлу>`
(константа `CONTENT_BASE_URL` в `data/remote/content/ContentPack.kt`).

> ⚠️ **Файлы нельзя переименовывать и переносить в другие папки.** Путь каждого файла записан в коде
> приложения: перенесённый файл приложение просто не найдёт. Менять можно только содержимое.

## Структура

```
keiting-infocards/
├── *pages.json          ← английские карточки теории (231 шт., лежат в корне — так их ищет приложение)
├── cards/               ← список карточек, добавленных с сервера
├── dictionary/          ← английский словарь по уровням
├── sentences/           ← банк предложений для заданий
├── quotes/              ← цитаты дня
├── texts/               ← тексты для режима «Текст»
├── tree/                ← курс «Древо познания»
├── survey/              ← опрос при регистрации
├── exam/                ← экзаменационный лист
├── japanese/            ← всё для японского курса
├── server/              ← адрес сервера ИИ
└── docs/editorial/      ← редакторские отчёты: PROGRESS.md, MIGRATIONS.md
```

| Папка / файл | Что внутри | Где используется в приложении |
|---|---|---|
| `*pages.json` (корень) | карточка теории: `route`, `tenseName` (название), `slides` (слайды). Маршрут `cards_pastsimp` → файл `pastsimppages.json` | `feature/cards/remote/CardRoutes.kt` |
| `cards/index.json` | карточки, которые появляются в приложении без обновления: id, папка (`constructions`, `communication`…), название, уровень (32 шт.) | `feature/cards/remote/CardIndex.kt` |
| `dictionary/words_<уровень>.json` | слова уровня A1–C2: перевод, значения, примеры, связи | `ContentPack.kt` → словарь, «Мои слова», практика |
| `dictionary/phrases_<уровень>.json` | фразы уровня | «Мои фразы», фраза дня, практика |
| `dictionary/forms_<уровень>.json` | формы слов отдельными записями словаря (add → added, go → went) с переводом и примером | режим «Какая форма», карточка слова |
| `sentences/sentences_<уровень>.json` | общий банк предложений A1–C2 с переводом | задания к теории (`DrillEngine`), Кубик, Голос, Блиц |
| `quotes/quotes.json` | цитаты дня с переводом и метками-темами | `QuoteRepository.kt` |
| `texts/texts.json` | тексты 20–80 слов с переводом, словариком и вопросами | режим «Текст» |
| `tree/course.json` | **текущий** курс «Древо познания» 3.0: главы и уроки | `TreeScreen`, `ContentPack.kt` |
| `tree/curriculum.json` | черновой план курса: цели по навыкам (`outcomes`) и учебные части тем (`units`) со ссылками на route, редакцию и слайды. Все части пока `reviewed=false` | `CurriculumRepository`, пакет «Программа Древа» |
| `tree/tree.json` | старый формат Древа (узлы с теорией). Текущее приложение его не читает, но в нём есть тексты, которые ещё нужно сверить (см. `docs/learning/CURRICULUM.md` в Keiting) | — |
| `survey/survey.json` | вопросы опроса при регистрации по 6 уровням | `SurveyRepository.kt` |
| `exam/exams.json` | варианты экзаменационного листа (ОГЭ, ЕГЭ) | `ExamRepository.kt` |
| `japanese/cards/*pages.json` | 68 карточек японского курса (N5–N3, 4–8 слайдов, по образцу английских) (маршрут `cards_ja_hiragana1` → `japanese/cards/hiragana1pages.json`) | `CardRoutes.kt` |
| `japanese/dictionary/words_<уровень>.json` | японские слова N5, N4, N3: запись, чтение каной и ромадзи, перевод, пример | словарь, «Мои слова», «Слово ↔ перевод», слово дня (переводятся в общий формат в `ContentStore`). Поле `sets` — связи как в английском: синонимы, антонимы, однокоренные |
| `japanese/dictionary/phrases_<уровень>.json` | японские фразы N5, N4, N3 (тот же формат, id `phrase_ja_…`) | словарь (вкладка «Фразы»), «Мои фразы», фраза дня |
| `japanese/sentences/sentences_<уровень>.json` | база японских предложений N5, N4, N3 (формат английской + `reading` «кана · ромадзи» и `chunks` — смысловые куски); у каждой — карточка и слайд | режимы «Частицы», «Сборка предложения», задания после слайдов |
| `japanese/quotes/quotes.json` | японские пословицы и цитаты (текст, чтение, перевод) | `QuoteRepository.kt` |
| `server/endpoint.json` | текущий адрес туннеля к Ollama и модель. Обновляется скриптом `tools/server/start-keiting.ps1` из Keiting | `AiEndpointStore.kt` |

Проверка японского контента: `node tools/learning/audit-japanese.mjs ../keiting-infocards` (из репозитория Keiting).

## Как добавить новое

- **Карточку английского** — файл `<имя>pages.json` в корень + маршрут `cards_<имя>` в приложении
  (`feature/cards/data/…List.kt`) или строка в `cards/index.json` (тогда обновлять приложение не нужно).
- **Карточку японского** — файл в `japanese/cards/`.
- **Слова, фразы, предложения** — в файл нужного уровня в `dictionary/` или `sentences/`.
- **Цитату** — в `quotes/quotes.json` (японскую — в `japanese/quotes/quotes.json`).

## Все английские карточки (корень)

| Файл | Название |
|---|---|
| `aboutmepages.json` | Рассказать о себе |
| `activepassivepages.json` | Active & Passive Voice |
| `addressingpages.json` | Обращения и имена |
| `advancedidiomspages.json` | Продвинутые идиомы |
| `advancedpassivepages.json` | Passive: продвинутый уровень |
| `adverbcollocationspages.json` | Коллокации: deeply, highly |
| `advicepages.json` | Как дать совет |
| `advrelativepages.json` | Relative clauses: продвинутый уровень |
| `alphabetpages.json` | Алфавит и диктовка по буквам |
| `alreadyyetpages.json` | Already, yet, still, just |
| `annoyinghabitspages.json` | Always + -ing, will и would для привычек |
| `apologiespages.json` | Извинения, отказы, жалобы |
| `appearancepages.json` | Внешность и характер |
| `articlesadvpages.json` | Артикли: сложные случаи |
| `articlesnamespages.json` | Артикли с названиями |
| `articlespages.json` | Артикли |
| `asaspages.json` | As…as |
| `asifthoughpages.json` | As if / As though |
| `bankpages.json` | В банке |
| `beabletopages.json` | Be able to |
| `beabouttopages.json` | Be about to |
| `becauseofpages.json` | Because of |
| `beduetosetpages.json` | Be due to, be set to, on the verge of |
| `begoingtopages.json` | Be going to |
| `besupposedtopages.json` | Be supposed to |
| `betoinfinitivepages.json` | Be to + infinitive |
| `beusedtopages.json` | Be used to |
| `bodypages.json` | Тело и здоровье |
| `botheitherpages.json` | Both / Either / Neither |
| `britishamericanpages.json` | Британский и американский |
| `businesscollocationspages.json` | Коллокации: работа и бизнес |
| `businessidiomspages.json` | Бизнес-идиомы |
| `butforotherwisepages.json` | But for, otherwise, supposing |
| `bytimeuntilpages.json` | By и until, in time и on time |
| `carpages.json` | Машина: аренда и дорога |
| `citypages.json` | Город и места |
| `clarifyingpages.json` | Если не понял |
| `cleftsentencepages.json` | It is / was … that / who |
| `clothespages.json` | Одежда |
| `collectivenounspages.json` | The police are |
| `collocationspages.json` | Коллокации |
| `comparativesadvpages.json` | Сравнения: the more…, the better |
| `comparisonspages.json` | Comparisons |
| `compoundadjectivespages.json` | Составные прилагательные |
| `compoundnounspages.json` | Составные существительные |
| `concessivepages.json` | Much as, try as I might |
| `conditionalspages.json` | Conditionals |
| `confusingwordspages.json` | Слова-путаницы |
| `congratulationspages.json` | Поздравления и сочувствие |
| `connectedspeechpages.json` | Слитная речь |
| `connectorspages.json` | Connectors |
| `consonantcombospages.json` | Consonant Combos |
| `contractionspages.json` | Сокращённые формы |
| `contrastlinkerspages.json` | Whereas, albeit, notwithstanding |
| `cvpages.json` | Резюме и сопроводительное письмо |
| `deductionpages.json` | Must be, can't be — догадки |
| `descriptionspages.json` | Descriptions |
| `despitepages.json` | Despite / Although |
| `determinantspages.json` | Some, any, no, every |
| `directionspages.json` | Как пройти |
| `discoursemarkerspages.json` | Discourse markers: mind you, admittedly |
| `doctorpages.json` | У врача и в аптеке |
| `donthavetopages.json` | Don't have to |
| `eachotherpages.json` | Each Other |
| `edingadjpages.json` | -ed и -ing |
| `ellipsispages.json` | Ellipsis |
| `emailspages.json` | Письма и сообщения |
| `emergencypages.json` | Экстренные ситуации |
| `emotionspages.json` | Эмоции и чувства |
| `emphasispages.json` | Усиление: the very, at all, whatsoever |
| `emphaticdopages.json` | Emphatic do |
| `endingspages.json` | Окончания -s и -ed |
| `essaylinkerspages.json` | Связки для текста |
| `essaypages.json` | Как писать эссе |
| `falsefriendspages.json` | Ложные друзья |
| `familypages.json` | Семья и отношения |
| `fewlittlepages.json` | Few / Little |
| `fillerspages.json` | Слова-паузы и междометия |
| `foodpages.json` | Еда и напитки |
| `formalinformalpages.json` | Официальные и разговорные слова |
| `formspages.json` | Анкеты и формы |
| `frontingpages.json` | Вынос вперёд: Tired as I was |
| `futurecontpages.json` | Future Continuous |
| `futureinpastpages.json` | Будущее в прошлом: would |
| `futureperfcontpages.json` | Future Perfect Continuous |
| `futureperfpages.json` | Future Perfect |
| `futuresimppages.json` | Future Simple |
| `futurewayspages.json` | Как говорить о будущем |
| `genericarticlespages.json` | Артикли: обобщение |
| `gerundpages.json` | Gerund |
| `getsomeonetodopages.json` | Get someone to do |
| `getusedtopages.json` | Get used to |
| `getverbpages.json` | Глагол get |
| `greetingspages.json` | Приветствия и small talk |
| `hadbetterpages.json` | Had better |
| `hardhardlypages.json` | Hard / hardly, late / lately |
| `hardlywhenpages.json` | Hardly … when |
| `hardsoundspages.json` | Трудные звуки |
| `havegotpages.json` | Have got |
| `havesomethingdonepages.json` | Have something done |
| `havetopages.json` | Have to |
| `hedgingpages.json` | Hedging / Softening |
| `hobbiespages.json` | Хобби и спорт |
| `homepages.json` | Дом и квартира |
| `homophonespages.json` | Омофоны |
| `hotelpages.json` | В отеле |
| `idiomspages.json` | Идиомы |
| `idlovetopages.json` | I'd love to |
| `imperativepages.json` | Повелительное наклонение |
| `indirectquestionspages.json` | Косвенные вопросы |
| `infinitivepages.json` | Инфинитив |
| `inordertopages.json` | In order to |
| `interviewpages.json` | Собеседование |
| `intonationpages.json` | Интонация |
| `inversionpages.json` | Inversion |
| `invitationspages.json` | Приглашения |
| `irregularverbspages.json` | Irregular Verbs |
| `isitokayifpages.json` | Is it okay if |
| `itshightimepages.json` | It's (high) time |
| `itstimepages.json` | It's time to |
| `itsworthpages.json` | It's worth / no use / no point |
| `ittakespages.json` | It takes … to |
| `ittherepages.json` | It или there |
| `jobspages.json` | Работа и профессии |
| `lestforfearpages.json` | Lest, for fear that, so as not to |
| `letsomeonedopages.json` | Let someone do |
| `likelytopages.json` | Be likely / bound to |
| `likeunlikepages.json` | Like / Unlike |
| `makedopages.json` | Make, do, take, have |
| `makesomeonedopages.json` | Make someone do |
| `messagingpages.json` | Сообщения в мессенджерах |
| `mightaswellpages.json` | May / Might as well |
| `mixedconditionalspages.json` | Mixed Conditionals |
| `modalperfectcontpages.json` | Must have been doing |
| `modalperfectpages.json` | Should have / Must have |
| `modalverbspages.json` | Modal Verbs |
| `mustntpages.json` | Must / Mustn't |
| `narrativetensespages.json` | Как рассказывать историю |
| `needtopages.json` | Need to |
| `nominalisationpages.json` | Номинализация |
| `nosoonerthanpages.json` | No sooner … than |
| `notespages.json` | Открытки и записки |
| `numberspages.json` | Numbers |
| `opinionspages.json` | Мнение и спор |
| `participleclausespages.json` | Participle clauses |
| `partitivespages.json` | A piece of, a cup of |
| `passivegetpages.json` | Пассив: get и два дополнения |
| `passivemodalspages.json` | Пассив с модальными |
| `pastcontpages.json` | Past Continuous |
| `pastperfcontpages.json` | Past Perfect Continuous |
| `pastperfpages.json` | Past Perfect |
| `pastsimppages.json` | Past Simple |
| `pharmacypages.json` | Аптека |
| `phonecallspages.json` | По телефону |
| `phrasalbytopicpages.json` | Фразовые глаголы по темам |
| `phrasalverbspages.json` | Phrasal Verbs |
| `pluralnounspages.json` | Plural Nouns |
| `postpages.json` | Почта и доставка |
| `prefixespages.json` | Приставки |
| `prepositionspages.json` | Предлоги: место, время, направление |
| `presentcontpages.json` | Present Continuous |
| `presentforfuturepages.json` | Present for Future |
| `presentperfcontpages.json` | Present Perfect Continuous |
| `presentperfpages.json` | Present Perfect |
| `presentsimppages.json` | Present Simple |
| `pronounspages.json` | Pronouns |
| `pseudocleftpages.json` | Выделение: All I need is… |
| `punctuationadvpages.json` | Пунктуация в эссе |
| `punctuationpages.json` | Пунктуация |
| `quantifierspages.json` | Quantifiers: a great deal, plenty, most |
| `questionspages.json` | Questions |
| `quiteratherpages.json` | Quite, rather, fairly, pretty |
| `readingrulespages.json` | Правила чтения |
| `relativeclausespages.json` | Relative Clauses |
| `rentingpages.json` | Аренда жилья |
| `reportedspeechpages.json` | Reported Speech |
| `reportingpassivepages.json` | Reporting passive |
| `reportingverbspages.json` | Reporting verbs: admit, deny, accuse |
| `requestspages.json` | Вежливые просьбы |
| `restaurantpages.json` | В кафе и ресторане |
| `reviewcomplaintpages.json` | Отзыв и жалоба |
| `sentencestresspages.json` | Ударение во фразе |
| `servicespages.json` | Аренда, парикмахерская, почта |
| `shallpages.json` | Shall I / Shall we |
| `shoppingpages.json` | В магазине |
| `silentletterspages.json` | Немые буквы |
| `sosuchpages.json` | So / Such / Enough |
| `sothatpages.json` | So that |
| `spellingpages.json` | Орфография |
| `storypages.json` | Как написать рассказ |
| `strongadjectivespages.json` | Сильные прилагательные |
| `studypages.json` | Учёба |
| `subjunctiveadvpages.json` | Сослагательное: Were I to… |
| `subjunctivepages.json` | Subjunctive |
| `suffixespages.json` | Суффиксы |
| `suffixsoundspages.json` | Окончания -tion, -ture, -ous, -age |
| `synonymspages.json` | Нюансы синонимов |
| `technologypages.json` | Технологии и интернет |
| `tensechoicepages.json` | Какое время выбрать |
| `textabbreviationspages.json` | Сокращения в переписке |
| `thereisarepages.json` | There is / There are |
| `therewaswerepages.json` | There was / There were |
| `therewillbepages.json` | There will be |
| `thesameaspages.json` | The same as |
| `threepartphrasalpages.json` | Фразовые из трёх частей |
| `ticketspages.json` | Кино, театр, билеты |
| `timeclausespages.json` | When / As soon as |
| `timemoneypages.json` | Время, деньги, меры |
| `tootopages.json` | Too…to |
| `transcriptionpages.json` | Транскрипция |
| `transportpages.json` | Такси и транспорт |
| `travelpages.json` | В аэропорту и в дороге |
| `twoobjectspages.json` | Два дополнения |
| `unlessincasepages.json` | Unless, as long as, provided |
| `usedtopages.json` | Used to |
| `videocallspages.json` | Видеозвонки |
| `vowelcombospages.json` | Vowel Combos |
| `weatherpages.json` | Погода и природа |
| `whatabouthowaboutpages.json` | What about / How about |
| `whetherifpages.json` | Whether или if |
| `whoeverpages.json` | Whoever / Whatever |
| `wishpages.json` | Wish / If only |
| `wordorderpages.json` | Word Order |
| `wordstresspages.json` | Ударение |
| `wordstressshiftpages.json` | Ударение: photograph → photographer |
| `workenglishpages.json` | Английский на работе |
| `wouldhabitspages.json` | Would (прошлые привычки) |
| `wouldlikepages.json` | Would like |
| `wouldpreferpages.json` | Would prefer |
| `wouldratherpages.json` | Would rather |
| `wouldratherpastpages.json` | Would rather + Past |
