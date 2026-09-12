# -*- coding: utf-8 -*-
"""Generate branded RPE Quick Guide PDFs (EN / ES / FR) using the website palette."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Segoe", os.path.join(FONT_DIR, "segoeui.ttf")))
pdfmetrics.registerFont(TTFont("Segoe-Bold", os.path.join(FONT_DIR, "segoeuib.ttf")))
pdfmetrics.registerFont(TTFont("Segoe-Semibold", os.path.join(FONT_DIR, "seguisb.ttf")))
pdfmetrics.registerFont(TTFont("Segoe-Italic", os.path.join(FONT_DIR, "segoeuii.ttf")))

W, H = letter  # 612 x 792

CONTENT = {
    "en": {
        "title": "Rate the whole ride.",
        "subtitle": "Not the hardest moment. Not how it ended.",
        "intro1": "Your RPE tells Alpine how much training to give you next. Inflate it and your plan gets softer than",
        "intro2": "it should. Two habits quietly inflate almost every score:",
        "m1_tag": "MISTAKE 1",
        "m1_title": "The hardest moment",
        "m1_body": ["One climb felt like a 9, so you call the whole", "ride a 9. But the other 80 minutes were a 4."],
        "m1_bold": "Rate the ride, not its peak.",
        "m2_tag": "MISTAKE 2",
        "m2_title": "How it ended",
        "m2_body": ["Easy for 2 hours, harder near the end — rate it", "right after, and the hard finish is all you", "remember."],
        "m2_bold": "Think in sections, then average.",
        "talk_title": "The talk test",
        "talk_rows": [
            ("1–2", "Chatting effortlessly", "#6ee7b7", "#052e16", "#10b981"),
            ("3–4", "Full sentences, easy", "#a7f3d0", "#064e3b", "#059669"),
            ("5–6", "Short sentences, working", "#fde68a", "#451a03", "#d97706"),
            ("7–8", "A few words at a time", "#fed7aa", "#431407", "#ea580c"),
            ("9–10", "Can't speak — minutes only", "#fecaca", "#450a0a", "#dc2626"),
        ],
        "talk_note1": "Nobody holds 9–10 for more than a few minutes. A \"brutal 2-hour ride\" is almost always a 4–6 with one hard moment",
        "talk_note2": "inside it.",
        "ways_title": "TODAY'S RIDE, RATED TWO WAYS",
        "w1_sym": "✘",
        "w1_head": "Right after finishing: RPE 4",
        "w1_body": ["2 hrs easy, then 90 min of building fatigue. The tired", "finish is freshest in memory, so it wins the rating."],
        "w2_sym": "✓",
        "w2_head": "Rated in sections: RPE 2–3",
        "w2_body": ["Easy start (2) averaged with a moderately harder", "finish (4) — not the ride-ending recency spike."],
        "bottom1": "Rate the whole ride, in sections, from memory of how each part felt —",
        "bottom2": "not the peak, and not the ending. Accurate beats impressive, every time.",
        "footer": "Alpine AI Coach — RPE Quick Guide",
    },
    "es": {
        "title": "Valora toda la salida.",
        "subtitle": "No solo el momento más duro. No solo cómo terminó.",
        "intro1": "Tu RPE le indica a Alpine cuánto entrenamiento darte a continuación. Si lo inflas, tu plan queda más suave",
        "intro2": "de lo que debería. Dos hábitos inflan silenciosamente casi todas las valoraciones:",
        "m1_tag": "ERROR 1",
        "m1_title": "El momento más duro",
        "m1_body": ["Una subida se sintió como un 9 y calificas toda la salida", "como un 9. Pero los otros 80 minutos fueron un 4."],
        "m1_bold": "Valora la salida, no su pico.",
        "m2_tag": "ERROR 2",
        "m2_title": "Cómo terminó",
        "m2_body": ["Fácil durante 2 horas, más dura hacia el final: si la valoras", "nada más terminar, el final duro es lo único que recuerdas."],
        "m2_bold": "Piensa por tramos y promedia.",
        "talk_title": "El test del habla",
        "talk_rows": [
            ("1–2", "Charla sin ningún esfuerzo", "#6ee7b7", "#052e16", "#10b981"),
            ("3–4", "Frases completas, fácil", "#a7f3d0", "#064e3b", "#059669"),
            ("5–6", "Frases cortas, trabajando", "#fde68a", "#451a03", "#d97706"),
            ("7–8", "Unas pocas palabras cada vez", "#fed7aa", "#431407", "#ea580c"),
            ("9–10", "No puedes hablar — solo minutos", "#fecaca", "#450a0a", "#dc2626"),
        ],
        "talk_note1": "Nadie mantiene un 9–10 durante más de unos pocos minutos. Una «salida brutal de 2 horas» es casi siempre un 4–6 con",
        "talk_note2": "un momento duro dentro.",
        "ways_title": "LA SALIDA DE HOY, VALORADA DE DOS FORMAS",
        "w1_sym": "✘",
        "w1_head": "Justo al terminar: RPE 4",
        "w1_body": ["2 h fáciles y luego 90 min de fatiga creciente. El final cansado", "está más fresco en la memoria, así que gana la valoración."],
        "w2_sym": "✓",
        "w2_head": "Valorada por tramos: RPE 2–3",
        "w2_body": ["Inicio fácil (2) promediado con un final moderadamente más duro", "(4) — no el pico de recencia del final de la salida."],
        "bottom1": "Valora toda la salida, por tramos, desde el recuerdo de cómo se sintió cada parte —",
        "bottom2": "no el pico y no el final. Ser preciso supera a impresionar, siempre.",
        "footer": "Alpine AI Coach — Guía rápida de RPE",
    },
    "fr": {
        "title": "Évaluez la sortie entière.",
        "subtitle": "Pas le moment le plus dur. Pas la façon dont elle s'est terminée.",
        "intro1": "Votre RPE indique à Alpine la quantité d'entraînement à vous donner ensuite. La gonfler rend votre plan plus",
        "intro2": "facile qu'il ne devrait l'être. Deux habitudes gonflent discrètement presque chaque note :",
        "m1_tag": "ERREUR 1",
        "m1_title": "Le moment le plus dur",
        "m1_body": ["Une montée a semblé valoir 9, et vous notez toute", "la sortie à 9. Pourtant, 80 minutes valaient un 4."],
        "m1_bold": "Notez la sortie, pas son sommet.",
        "m2_tag": "ERREUR 2",
        "m2_title": "La façon dont elle s'est finie",
        "m2_body": ["Facile pendant 2 h, plus dur vers la fin — notée juste après,", "la fin difficile est tout ce dont vous vous souvenez."],
        "m2_bold": "Pensez en sections, puis moyennez.",
        "talk_title": "Le test de conversation",
        "talk_rows": [
            ("1–2", "Conversation sans effort", "#6ee7b7", "#052e16", "#10b981"),
            ("3–4", "Phrases complètes, facile", "#a7f3d0", "#064e3b", "#059669"),
            ("5–6", "Phrases courtes, en effort", "#fde68a", "#451a03", "#d97706"),
            ("7–8", "Quelques mots à la fois", "#fed7aa", "#431407", "#ea580c"),
            ("9–10", "Impossible de parler — quelques minutes", "#fecaca", "#450a0a", "#dc2626"),
        ],
        "talk_note1": "Personne ne tient un 9–10 plus de quelques minutes. Une « sortie brutale de 2 heures » est presque toujours un 4–6",
        "talk_note2": "avec un moment dur à l'intérieur.",
        "ways_title": "LA SORTIE DU JOUR, NOTÉE DE DEUX FAÇONS",
        "w1_sym": "✘",
        "w1_head": "Juste après l'arrivée : RPE 4",
        "w1_body": ["2 h faciles, puis 90 min de fatigue croissante. La fin fatiguée", "est la plus fraîche en mémoire, donc elle gagne la note."],
        "w2_sym": "✓",
        "w2_head": "Notée par sections : RPE 2–3",
        "w2_body": ["Début facile (2) moyenné avec une fin modérément plus dure (4)", "— pas le pic de récence de la fin de sortie."],
        "bottom1": "Notez la sortie entière, par sections, d'après le souvenir de chaque partie —",
        "bottom2": "pas le sommet, ni la fin. La justesse bat l'impression, à chaque fois.",
        "footer": "Alpine AI Coach — Guide rapide RPE",
    },
}


def hexcol(value):
    return colors.HexColor(value)


def draw_pdf(path, t):
    c = canvas.Canvas(path, pagesize=letter)

    # Page background
    c.setFillColor(hexcol("#050d1f"))
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Header band
    c.setFillColor(hexcol("#0a1628"))
    c.rect(0, H - 125, W, 125, fill=1, stroke=0)
    c.setStrokeColor(hexcol("#1a2d4a"))
    c.setLineWidth(1)
    c.line(0, H - 125, W, H - 125)
    c.setStrokeColor(hexcol("#38bdf8"))
    c.setLineWidth(2)
    c.line(48, H - 125, 180, H - 125)

    # Logo
    if os.path.exists("logo.png"):
        c.drawImage("logo.png", 48, H - 105, width=68, height=68, mask="auto", preserveAspectRatio=True)

    tx = 130
    c.setFillColor(hexcol("#38bdf8"))
    c.setFont("Segoe-Bold", 9)
    c.drawString(tx, H - 52, "ALPINE AI COACH")

    c.setFillColor(hexcol("#f0f8ff"))
    c.setFont("Segoe-Bold", 20)
    c.drawString(tx, H - 76, t["title"])

    c.setFillColor(hexcol("#38bdf8"))
    c.setFont("Segoe-Italic", 10.5)
    c.drawString(tx, H - 94, t["subtitle"])

    # Intro
    c.setFillColor(hexcol("#94b8d4"))
    c.setFont("Segoe", 9.5)
    c.drawString(48, H - 144, t["intro1"])
    c.drawString(48, H - 158, t["intro2"])

    # --- Mistake cards ---
    card_w, card_h = 248, 104
    card_y = H - 276

    def mistake_card(x, tag, title, body, bold, accent):
        c.setFillColor(hexcol("#0a1628"))
        c.roundRect(x, card_y, card_w, card_h, 6, fill=1, stroke=0)
        c.setStrokeColor(hexcol("#1a2d4a"))
        c.setLineWidth(1)
        c.roundRect(x, card_y, card_w, card_h, 6, fill=0, stroke=1)
        c.setFillColor(hexcol("#0f1e35"))
        c.rect(x, card_y + card_h - 26, card_w, 26, fill=1, stroke=0)
        c.setStrokeColor(hexcol(accent))
        c.setLineWidth(2)
        c.line(x, card_y + card_h, x + card_w, card_y + card_h)
        c.setFillColor(hexcol(accent))
        c.setFont("Segoe-Bold", 7.5)
        c.drawString(x + 10, card_y + card_h - 17, tag)
        tag_w = pdfmetrics.stringWidth(tag, "Segoe-Bold", 7.5)
        c.setFillColor(hexcol("#f0f8ff"))
        c.setFont("Segoe-Bold", 10.5)
        c.drawString(x + 18 + tag_w, card_y + card_h - 18, title)
        c.setFillColor(hexcol("#94b8d4"))
        c.setFont("Segoe", 8.8)
        for i, line in enumerate(body):
            c.drawString(x + 10, card_y + 54 - i * 14, line)
        c.setFillColor(hexcol("#38bdf8"))
        c.setFont("Segoe-Bold", 9)
        c.drawString(x + 10, card_y + 14, bold)

    mistake_card(48, t["m1_tag"], t["m1_title"], t["m1_body"], t["m1_bold"], "#ef4444")
    mistake_card(48 + card_w + 20, t["m2_tag"], t["m2_title"], t["m2_body"], t["m2_bold"], "#f59e0b")

    # --- Talk test ---
    tt_y = card_y - 28
    c.setFillColor(hexcol("#f0f8ff"))
    c.setFont("Segoe-Bold", 13)
    c.drawString(48, tt_y, t["talk_title"])
    c.setStrokeColor(hexcol("#1a2d4a"))
    c.setLineWidth(1)
    c.line(48, tt_y - 6, 564, tt_y - 6)

    row_y = tt_y - 30
    row_h = 24
    table_w = 516
    for i, (rpe, desc, txt_col, badge_bg, badge_border) in enumerate(t["talk_rows"]):
        cur_y = row_y - i * (row_h + 3)
        c.setFillColor(hexcol("#0a1628"))
        c.roundRect(48, cur_y, table_w, row_h, 4, fill=1, stroke=0)
        c.setStrokeColor(hexcol("#1a2d4a"))
        c.setLineWidth(1)
        c.roundRect(48, cur_y, table_w, row_h, 4, fill=0, stroke=1)
        c.setFillColor(hexcol(badge_bg))
        c.roundRect(52, cur_y + 3, 46, row_h - 6, 3, fill=1, stroke=0)
        c.setStrokeColor(hexcol(badge_border))
        c.roundRect(52, cur_y + 3, 46, row_h - 6, 3, fill=0, stroke=1)
        c.setFillColor(hexcol(txt_col))
        c.setFont("Segoe-Bold", 10)
        c.drawCentredString(52 + 23, cur_y + 7, rpe)
        c.setFillColor(hexcol("#f0f8ff"))
        c.setFont("Segoe-Semibold", 9.5)
        c.drawString(112, cur_y + 7, desc)

    note_y = row_y - len(t["talk_rows"]) * (row_h + 3) - 10
    c.setFillColor(hexcol("#7dd3fc"))
    c.setFont("Segoe-Italic", 8.5)
    c.drawString(48, note_y, t["talk_note1"])
    c.drawString(48, note_y - 12, t["talk_note2"])

    # --- Two ways panel ---
    rated_y = note_y - 44
    c.setFillColor(hexcol("#0f1e35"))
    c.roundRect(48, rated_y - 74, table_w, 96, 6, fill=1, stroke=0)
    c.setStrokeColor(hexcol("#243d5e"))
    c.setLineWidth(1)
    c.roundRect(48, rated_y - 74, table_w, 96, 6, fill=0, stroke=1)
    c.setFillColor(hexcol("#0a1628"))
    c.rect(48, rated_y - 2, table_w, 24, fill=1, stroke=0)
    c.setStrokeColor(hexcol("#38bdf8"))
    c.setLineWidth(2)
    c.line(48, rated_y + 22, 48 + table_w, rated_y + 22)
    c.setFillColor(hexcol("#38bdf8"))
    c.setFont("Segoe-Bold", 8.5)
    c.drawString(60, rated_y + 6, t["ways_title"])

    c.setStrokeColor(hexcol("#1a2d4a"))
    c.setLineWidth(1)
    c.line(48 + table_w / 2, rated_y - 2, 48 + table_w / 2, rated_y - 74)

    c.setStrokeColor(hexcol("#ef4444"))
    c.setLineWidth(2)
    c.line(60, rated_y - 22, 66, rated_y - 14)
    c.line(66, rated_y - 22, 60, rated_y - 14)
    c.setFillColor(hexcol("#ef4444"))
    c.setFont("Segoe-Bold", 9.5)
    c.drawString(76, rated_y - 18, t["w1_head"])
    c.setFillColor(hexcol("#94b8d4"))
    c.setFont("Segoe", 8.2)
    c.drawString(60, rated_y - 36, t["w1_body"][0])
    c.drawString(60, rated_y - 48, t["w1_body"][1])

    x2 = 48 + table_w / 2 + 14
    c.setStrokeColor(hexcol("#34d399"))
    c.setLineWidth(2)
    c.line(x2, rated_y - 18, x2 + 3, rated_y - 21)
    c.line(x2 + 3, rated_y - 21, x2 + 8, rated_y - 13)
    c.setFillColor(hexcol("#34d399"))
    c.setFont("Segoe-Bold", 9.5)
    c.drawString(x2 + 16, rated_y - 18, t["w2_head"])
    c.setFillColor(hexcol("#94b8d4"))
    c.setFont("Segoe", 8.2)
    c.drawString(x2, rated_y - 36, t["w2_body"][0])
    c.drawString(x2, rated_y - 48, t["w2_body"][1])

    # --- Bottom takeaway ---
    hero_y = rated_y - 150
    c.setFillColor(hexcol("#0a1628"))
    c.roundRect(48, hero_y, table_w, 64, 8, fill=1, stroke=0)
    c.setStrokeColor(hexcol("#38bdf8"))
    c.setLineWidth(1.5)
    c.roundRect(48, hero_y, table_w, 64, 8, fill=0, stroke=1)
    c.setFillColor(hexcol("#38bdf8"))
    c.rect(48, hero_y, 4, 64, fill=1, stroke=0)

    c.setFillColor(hexcol("#f0f8ff"))
    c.setFont("Segoe-Bold", 10.5)
    c.drawString(64, hero_y + 38, t["bottom1"])
    c.setFillColor(hexcol("#7dd3fc"))
    c.setFont("Segoe-Bold", 10.5)
    c.drawString(64, hero_y + 20, t["bottom2"])

    # --- Footer ---
    c.setStrokeColor(hexcol("#1a2d4a"))
    c.setLineWidth(1)
    c.line(48, 42, 48 + table_w, 42)
    c.setFillColor(hexcol("#3a5878"))
    c.setFont("Segoe", 8)
    c.drawString(48, 28, t["footer"])
    c.drawRightString(48 + table_w, 28, "https://alpineai-webapp-production.up.railway.app/")

    c.save()
    print("Generated", path)


if __name__ == "__main__":
    draw_pdf("rpe-education-guide.pdf", CONTENT["en"])
    draw_pdf(os.path.join("es", "rpe-education-guide.pdf"), CONTENT["es"])
    draw_pdf(os.path.join("fr", "rpe-education-guide.pdf"), CONTENT["fr"])
