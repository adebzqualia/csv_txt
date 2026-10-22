import base64
from pathlib import Path


def decode_csv(txt_path: str, csv_path: str) -> None:
    """Décode un fichier Base64 pour restaurer le CSV original.

    :param txt_path: Chemin du fichier TXT encodé.
    :param csv_path: Chemin du fichier CSV restauré.
    :raises ValueError: Si les données Base64 sont invalides.
    """
    encoded = Path(txt_path).read_text(encoding="ascii")

    data = base64.b64decode(encoded, validate=True)

    Path(csv_path).write_bytes(data)

    print(f"CSV restauré avec succès : {csv_path}")


if __name__ == "__main__":
    decode_csv(
        txt_path="encoded.txt",
        csv_path="restored.csv",
    )
