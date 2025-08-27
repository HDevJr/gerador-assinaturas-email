from PIL import Image

def ajustar_template_agro(reference_path, target_path, output_path):
    ref = Image.open(reference_path)
    tgt = Image.open(target_path)

    ref_w, ref_h = ref.size
    tgt_w, tgt_h = tgt.size

    escala = ref_w / tgt_w
    new_w = ref_w
    new_h = int(tgt_h * escala)

    resized = tgt.resize((new_w, new_h), resample=Image.LANCZOS)
    resized.save(output_path)
    print(f"Template agro ajustado salvo em: {output_path}")

if __name__ == "__main__":
    ajustar_template_agro(
        reference_path="template-contato-constru.jpg",
        target_path="template-contato-agro.png",
        output_path="template-contato-agro-ajustado.png"
    )
