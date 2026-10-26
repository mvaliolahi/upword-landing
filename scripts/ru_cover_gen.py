#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — generate the 91 Russian-course clay-render covers (1344x768 JPG).

Style matches the existing German-course covers (commit 784a637 «clay-render
brand style»): soft matte 3D claymation, muted deep-green studio background,
one small friendly turtle, a topic-relevant scene per lesson, NO text.

Usage:
  python3 ru_cover_gen.py --from 0 --to 3        # range [from, to)
  python3 ru_cover_gen.py --only russian-from-zero,german-style-check
  Idempotent: skips slugs whose JPG already exists (use --force to redo).
Output: blog/covers/<slug>.jpg
"""
import argparse
import os
import subprocess
import sys

ROOT = '/home/z/my-project/repos/upword-landing'
OUT = os.path.join(ROOT, 'blog', 'covers')
TMP = '/home/z/my-project/blogimg/raw'
os.makedirs(OUT, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

STYLE = ('cute 3D claymation render, soft matte clay material, rounded shapes, '
         'muted deep dark-green studio background, soft warm studio lighting, '
         'subtle depth of field, one small friendly green clay turtle, '
         'cozy and playful mood, clean minimal composition, '
         'no text, no letters, high quality, detailed')

# (slug, scene) — 0 = hub, 1..90 = lessons in course order
SPECS = [
    ('russian-course', 'a small clay turtle with a tiny backpack standing at the start of a winding path that leads toward a stylized clay Kremlin tower and Saint Basil cathedral domes in the distance, five little milestone flags along the path'),
    ('russian-from-zero', 'a small clay turtle looking up at a wooden signpost with five blank direction arrows pointing toward a clay city skyline'),
    ('russian-alphabet-friends', 'a curious clay turtle inspecting several big soft clay letter-blocks scattered on the floor with a magnifying glass, the blocks look like playful abstract glyphs'),
    ('russian-alphabet-rest', 'a clay turtle arranging the last few soft clay letter-blocks on a shelf, some blocks have little soft signs on them, warm playful scene'),
    ('russian-vowel-reduction', 'a clay turtle pouring tea from a little teapot; the tea stream is made of tiny shrinking clay beads, a kettle and a cup on a wooden table'),
    ('russian-stress-softness', 'a clay turtle bouncing on a trampoline over soft clay word-pillows, little musical accent marks floating in the air like springy notes'),
    ('russian-greetings', 'two friendly clay characters, a turtle and a hedgehog, greeting each other with a wave and a handshake under a warm street lantern'),
    ('russian-introduce-yourself', 'a proud clay turtle holding a tiny blank ID card and wearing a small graduation scarf, presenting itself'),
    ('russian-eto-pronouns', 'a clay turtle pointing at objects in a cozy room: a little table, a window, a cup, a book, with a soft spotlight on each'),
    ('russian-numbers-100', 'a clay turtle counting shiny clay coins on an abacus, small numbered blocks spread around, a toy phone nearby'),
    ('russian-present-verbs', 'a lively clay turtle doing three activities at once: reading a tiny book, stirring a pot, and typing on a small laptop'),
    ('russian-questions', 'a clay turtle with a big soft question-mark made of clay floating above its head, looking curious, two smaller question marks nearby'),
    ('russian-gender', 'three soft clay boxes of different shapes and pastel colors arranged on a table with a clay turtle sorting little objects into them'),
    ('russian-family-possessives', 'a warm clay family portrait scene: turtle with a baby turtle, family photo frame, little heart decorations'),
    ('russian-days-time', 'a clay turtle next to a big soft clay clock with movable hands and a small calendar with flip pages, morning light'),
    ('russian-phase1-review', 'a happy clay turtle celebrating with confetti, holding a little trophy, a cozy cafe table with two mugs'),
    ('russian-arrival-immigration', 'a clay turtle at a little airport check-in desk, friendly stamp and tiny airplane visible, suitcase beside it'),
    ('russian-transport', 'a clay turtle riding a cute clay metro train, a little bus and a taxi in the background, round friendly vehicles'),
    ('russian-supermarket', 'a clay turtle shopping with a tiny basket: clay bread, milk bottle, cheese wheel and apple on wooden shelves'),
    ('russian-cafe-restaurant', 'a cozy clay cafe table with a steaming teacup, a little menu board, the turtle holding a spoon'),
    ('russian-dormitory', 'a clay turtle sitting on a bunk bed in a cozy dorm room with a small desk lamp, poster, and slippers'),
    ('russian-apartment-rent', 'a clay turtle holding a big key in front of a little apartment building with a for-rent flag, contract scroll nearby'),
    ('russian-university-registration', 'a clay turtle receiving a little student ID card across a university desk, official stamp and register book'),
    ('russian-bank-sim', 'a clay turtle holding a little bank card and a tiny smartphone with a SIM chip, coins stacked beside'),
    ('russian-city-places', 'a clay turtle at a little crossroads with miniature buildings: pharmacy with cross, post office, bank, park tree'),
    ('russian-weather-clothes', 'a clay turtle wearing a knitted scarf and hat in soft snowfall, little mittens, cozy winter scene'),
    ('russian-doctor-pharmacy', 'a caring clay turtle doctor with a tiny stethoscope checking a hedgehog patient, little medicine bottles on a tray'),
    ('russian-emergency', 'a little clay ambulance and a fire truck parked under a green emergency light, clay turtle waving at a dispatcher phone booth'),
    ('russian-shopping-sizes', 'a clay turtle trying on a little jacket in front of a soft mirror, clothes rack with tiny hangers'),
    ('russian-phone-internet', 'a clay turtle holding a smartphone with soft chat bubbles floating up, wifi signal made of clay arcs'),
    ('russian-present-2', 'a clay turtle juggling more activity icons: a paintbrush, a dancing shoe, a microphone, playful motion'),
    ('russian-accusative', 'a clay turtle reading a book while an arrow-shaped clay beam flows toward the book, gift-wrapped box beside'),
    ('russian-prepositional', 'a clay turtle standing inside a little glass diorama of a tiny university building with a location pin above'),
    ('russian-phase2-review', 'a wide clay diorama of a full day: little metro, tiny shop, university door, dorm window, sun and moon together'),
    ('russian-classroom', 'a clay turtle at a school desk with a tiny notebook and pencil, blackboard with abstract shapes, raised hand'),
    ('russian-lecture', 'a clay turtle taking notes at a lecture: a small podium, soft spotlight, floating abstract idea bubbles'),
    ('russian-exams', 'a nervous but determined clay turtle at an exam desk with paper and a big soft five-pointed star badge as a grade'),
    ('russian-library', 'a clay turtle reading under a warm lamp between tall soft bookshelves, stack of books beside'),
    ('russian-student-life', 'clay turtle and friends with a little guitar, cinema tickets and a football, cozy evening scene'),
    ('russian-email-teacher', 'a clay turtle at a laptop writing a formal letter, a soft envelope with a wax seal floating beside'),
    ('russian-office-first-day', 'a clay turtle with a little visitor badge meeting clay colleagues around an office desk, handshake'),
    ('russian-office-daily', 'a clay turtle at a round meeting table with sticky notes, a small whiteboard with abstract charts, coffee mug'),
    ('russian-work-chat', 'a clay turtle peeking at a smartphone with playful chat bubbles and a soft notification bell, office background'),
    ('russian-task-progress', 'a clay turtle moving soft progress bars like clay loaves, checklist with clay checkmarks on a clipboard'),
    ('russian-job-interview', 'a clay turtle in a small tie sitting across an interview table from a friendly clay interviewer, resume scroll'),
    ('russian-salary', 'a clay turtle stacking coin towers on a paycheck scroll, a little calendar with a circled payday, safe in background'),
    ('russian-genitive-1', 'a clay turtle holding an empty cup turned upside down with tiny particles floating away, little «absence» mood'),
    ('russian-genitive-2', 'a clay turtle grouping little clay figures: two apples in one group, five apples in another, counting mat'),
    ('russian-dative', 'a clay turtle handing a heart-shaped cookie to a happy hedgehog, gift bows floating, giving mood'),
    ('russian-instrumental', 'a clay turtle as a tiny chef stirring a pot with a clay spoon, tools hanging on the wall, craft table'),
    ('russian-aspect', 'a clay turtle beside two objects: an hourglass with flowing sand and a completed soft trophy on a pedestal'),
    ('russian-past-tense', 'a clay turtle flipping through a cozy photo album with little framed memories, warm nostalgic light'),
    ('russian-phase3-review', 'a confident clay turtle on a small stage with a microphone, soft spotlight, presentation screen with abstract shapes'),
    ('russian-registration', 'a clay turtle at a little service window receiving a stamped paper with an official round stamp, house keys beside'),
    ('russian-visa', 'a clay turtle holding a little passport with a fresh visa stamp, calendar with a circled renewal date'),
    ('russian-rvp', 'a clay turtle holding a little house-shaped permit card with a ribbon, three-year calendar stack beside'),
    ('russian-vnj', 'a proud clay turtle in front of a cozy little house with deep roots growing beneath it, a permanent key'),
    ('russian-migration-exam', 'a clay turtle at an exam desk with three soft icons: a language book, a history scroll, balanced scales'),
    ('russian-insurance', 'a clay turtle protected under a soft shield umbrella with a little medical cross, clinic in the background'),
    ('russian-inn-selfemployed', 'a clay turtle freelancer at a laptop with a receipt printer spooling a tiny receipt, coins and a percentage pie'),
    ('russian-driving', 'a clay turtle driving a cute round clay car with a little license card, traffic light and road sign'),
    ('russian-official-letters', 'a clay turtle with a quill writing on a formal scroll at an office desk, envelope and seal nearby'),
    ('russian-mfc', 'a clay turtle at a little service-center counter with a ticket machine, number display, and soft waiting chairs'),
    ('russian-renter-rights', 'a clay turtle reviewing a lease scroll with a magnifying glass, keys and a little apartment door'),
    ('russian-everyday-law', 'a calm clay turtle showing documents to a friendly clay police officer figure, balanced scales in between'),
    ('russian-future', 'a clay turtle looking through a telescope toward a sunrise horizon, little calendar pages fluttering forward'),
    ('russian-subjunctive', 'a dreaming clay turtle with a soft dream bubble containing a fantasy clay Saint Petersburg bridge and fireworks'),
    ('russian-imperative', 'a clay turtle with a little megaphone and a friendly pointing gesture, arrow signs around'),
    ('russian-comparatives', 'two clay towers of different heights with a proud turtle on the taller one, balance scale beside'),
    ('russian-ordinals', 'a clay turtle standing on a winners podium with three steps of different heights, little flags'),
    ('russian-big-numbers', 'a clay turtle with big soft coin wheels and banknote stacks, a percentage pie chart made of clay'),
    ('russian-connectors', 'soft clay chain links connecting colorful clay blocks in a row, turtle placing the final link'),
    ('russian-phase4-review', 'a wide clay service-center diorama: queue, counters, screens, the turtle completing the journey with a folder of documents'),
    ('russian-motion-1', 'a clay turtle walking on a path while a little clay bus and metro pass by, arrows on the ground'),
    ('russian-motion-2', 'a clay turtle with little clay arrows arriving at, leaving and entering tiny doorways on a map-like floor'),
    ('russian-aspect-narrative', 'clay turtle telling a story around a little campfire with soft story bubbles above, friends listening'),
    ('russian-cases-review', 'six little soft clay houses in a row, each with a different colored door, turtle walking past them'),
    ('russian-participles', 'a clay turtle hanging a little round sign on a door knob, door slightly closed, cozy hallway'),
    ('russian-adverbs', 'a clay turtle running fast with soft motion lines next to a slow strolling snail, speedometer dial'),
    ('russian-politeness', 'two clay turtles exchanging a gentle bow and a small gift box, soft hearts floating, respectful distance'),
    ('russian-smalltalk', 'two clay friends with tea mugs chatting on a cozy couch, little hockey stick and film reel nearby'),
    ('russian-phone-calls', 'a clay turtle talking on a round old-school phone with soft sound waves, little answering machine'),
    ('russian-opinions', 'two clay turtles at a debate podium with balanced scales between them, thought bubbles with different shapes'),
    ('russian-idioms', 'a playful clay turtle juggling quirky icons: a feather, a tiny cat, a small bag, a piece of coal'),
    ('russian-culture', 'a clay turtle with matryoshka dolls, an odd number of flowers in a vase, a samovar and tea party'),
    ('russian-listening', 'a clay turtle with big headphones and floating music notes, a film clapperboard and soft sound waves'),
    ('russian-reading', 'a clay turtle reading a little newspaper under a book light with a magnifying glass, soft reading nook'),
    ('russian-torfl', 'a clay turtle climbing soft stairs with certificate frames on each level, a big diploma at the top'),
    ('russian-fluency', 'a clay turtle speaking confidently with a microphone, soft ripple waves spreading from it, small speedometer'),
    ('russian-after-course', 'a clay turtle at the edge of a finished path looking toward a new longer road into sunrise, backpack on'),
    ('russian-final-review', 'a graduating clay turtle with a little diploma and graduation cap, confetti, fireworks and friends celebrating'),
]


def gen(slug, scene, force=False):
    jpg = os.path.join(OUT, slug + '.jpg')
    if os.path.exists(jpg) and not force:
        return 'skip'
    png = os.path.join(TMP, slug + '.png')
    prompt = f'{scene}, {STYLE}'
    import time
    for attempt in range(6):
        r = subprocess.run(['z-ai', 'image', '-p', prompt, '-o', png, '-s', '1344x768'],
                           capture_output=True, text=True, timeout=300)
        if os.path.exists(png):
            break
        if '429' in (r.stderr or '') + (r.stdout or ''):
            wait = 150 * (attempt + 1)
            print(f'  429 rate-limited; sleeping {wait}s (attempt {attempt+1}/6)', flush=True)
            time.sleep(wait)
    if not os.path.exists(png):
        print(f'GEN-FAIL {slug}: {(r.stderr or r.stdout)[-160:]}')
        return 'fail'
    from PIL import Image
    im = Image.open(png).convert('RGB')
    if im.size != (1344, 768):
        im = im.resize((1344, 768))
    im.save(jpg, 'JPEG', quality=88)
    os.remove(png)
    return f'ok {os.path.getsize(jpg)//1024}KB'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='frm', type=int, default=0)
    ap.add_argument('--to', dest='to', type=int, default=len(SPECS))
    ap.add_argument('--only', default='')
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()
    only = set(args.only.split(',')) if args.only else None
    done = fails = 0
    for i, (slug, scene) in enumerate(SPECS):
        if not (args.frm <= i < args.to):
            continue
        if only and slug not in only:
            continue
        res = gen(slug, scene, args.force)
        print(f'[{i}] {slug}: {res}')
        if res == 'fail':
            fails += 1
        elif res.startswith('ok'):
            done += 1
    print(f'generated={done} fails={fails}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
