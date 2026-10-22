import base64
from pathlib import Path


def encode_csv(csv_path: str, txt_path: str) -> None:
    """Encode un fichier CSV en Base64.

    :param csv_path: Chemin du fichier CSV original.
    :param txt_path: Chemin du fichier TXT de sortie.
    """
    data = Path(csv_path).read_bytes()

    encoded = base64.b64encode(data).decode("ascii")

    Path(txt_path).write_text(encoded, encoding="ascii")

    print(f"CSV encodé avec succès : {txt_path}")


if __name__ == "__main__":
    encode_csv(
        csv_path="original.csv",
        txt_path="encoded.txt",
    )
