import os
from PIL import Image, ImageDraw
from ttf_opensans import OPENSANS_BOLD, opensans

def testar_posicoes(template_path, nome, cargo, tel1, tel2=None):
    img = Image.open(template_path).convert("RGBA")
    draw = ImageDraw.Draw(img)

    font_name = OPENSANS_BOLD.imagefont(size=24)
    font_cargo = OPENSANS_BOLD.imagefont(size=18)
    font_tel_bold = OPENSANS_BOLD.imagefont(size=16)
    font_tel_regular = opensans(font_weight=400).imagefont(size=18)

    # Alexander do Nascimento
    # pos_nome = (49, 130)
    # pos_cargo = (157, 170)

    # Gefferson Margreiter
    # pos_nome = (77, 130)
    # pos_cargo = (120, 170)

    # Ildo Voidaleski
    # pos_nome = (117, 130)
    # pos_cargo = (96, 170)

    # Laryssa Siqueira
    # pos_nome = (105, 130)
    # pos_cargo = (83, 170)

    # Luis Picoloto
    pos_nome = (125, 130)
    pos_cargo = (110, 170)

    # Oscar Cruz
    # pos_nome = (135, 130)
    # pos_cargo = (90, 170)

    # Paulo Ricardo
    # pos_nome = (120, 130)
    # pos_cargo = (150, 170)

    draw.text(pos_nome, nome, font=font_name, fill="#0b493c")
    draw.text(pos_cargo, cargo, font=font_cargo, fill="#36466a")

    def draw_telefone(txt, base_pos):
        if not txt.startswith("("):
            return
        parts = txt.split(")")
        ddd = parts[0] + ")"
        numero = parts[1].strip() if len(parts) > 1 else ""
        w_ddd = draw.textbbox((0, 0), ddd, font=font_tel_regular)[2]
        draw.text(base_pos, ddd, font=font_tel_regular, fill="#294b42")
        draw.text((base_pos[0] + w_ddd + 2, base_pos[1]), numero, font=font_tel_bold, fill="#294b42")

    if tel1:
        # Alexander do Nascimento
        # draw_telefone(tel1.strip(), (145, 207))

        # Gefferson Margreiter
        # draw_telefone(tel1.strip(), (148, 207))

        # Ildo Voidaleski
        # draw_telefone(tel1.strip(), (150, 207))

        # Laryssa Siqueira
        # draw_telefone(tel1.strip(), (150, 207))

        # Luiz Picoloto
        draw_telefone(tel1.strip(), (141, 207))

        # Oscar Cruz
        # draw_telefone(tel1.strip(), (146, 207))

        # Paulo Ricardo
        # draw_telefone(tel1.strip(), (141, 207))
    if tel2:
        # Alexander do Nascimento
        # draw_telefone(tel2.strip(), (137, 237))

        # Gefferson Margreiter
        # draw_telefone(tel2.strip(), (141, 237))

        # Ildo Voidaleski
        # draw_telefone(tel2.strip(), (143, 237))

        # Laryssa Siqueira
        # draw_telefone(tel2.strip(), (143, 237))

        # Luiz Picoloto
        draw_telefone(tel2.strip(), (136, 237))

        # Oscar Cruz
        # draw_telefone(tel2.strip(), (139, 237))

        # Paulo Ricardo
        # draw_telefone(tel2.strip(), (134, 237))

    img.show()

if __name__ == "__main__":
    testar_posicoes(
        template_path="template-contato-treze.png",
        nome="Luiz Picoloto",
        cargo="Gerente de Vendas",
        tel1="(49) 3566-9800",
        tel2="(49) 9 9803-4632"
    )
