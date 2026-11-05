"""Собрать иконки: python3 icons/build.py (из корня репозитория). Пишет icons/<cards|parts>/<id>.xml и .svg и icons/index.json."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from neon import to_xml, to_svg
import designs_cards, designs_parts

idx = {'version': 1, 'note': 'Иконки в стиле res/drawable/icon_cards_*.xml. Для каждой — .xml (векторный ресурс Android) и .svg (то же для загрузки по сети).',
       'cards': {}, 'parts': {}}
for kind, mod in (('cards', designs_cards), ('parts', designs_parts)):
    os.makedirs(f'{HERE}/{kind}', exist_ok=True)
    for k, (comment, st) in mod.ICONS.items():
        open(f'{HERE}/{kind}/{k}.xml', 'w').write(to_xml(st, comment))
        open(f'{HERE}/{kind}/{k}.svg', 'w').write(to_svg(st, 512) + '\n')
        idx[kind][k] = {'xml': f'icons/{kind}/{k}.xml', 'svg': f'icons/{kind}/{k}.svg', 'about': comment}
open(f'{HERE}/index.json', 'w').write(json.dumps(idx, ensure_ascii=False, indent=1) + '\n')
print(len(idx['cards']), 'cards,', len(idx['parts']), 'parts')
