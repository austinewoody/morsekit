from __future__ import annotations

MORSE_CODE = {
    "A": ".-",     "B": "-...",   "C": "-.-.",   "D": "-..",    "E": ".",
    "F": "..-.",   "G": "--.",    "H": "....",   "I": "..",     "J": ".---",
    "K": "-.-",    "L": ".-..",   "M": "--",     "N": "-.",     "O": "---",
    "P": ".--.",   "Q": "--.-",   "R": ".-.",    "S": "...",    "T": "-",
    "U": "..-",    "V": "...-",   "W": ".--",    "X": "-..-",   "Y": "-.--",
    "Z": "--..",
    "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--",  "4": "....-",
    "5": ".....",  "6": "-....",  "7": "--...",  "8": "---..",  "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.",  "(": "-.--.",  ")": "-.--.-", "&": ".-...",  ":": "---...",
    ";": "-.-.-.", "=": "-...-",  "+": ".-.-.",  "-": "-....-", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-","@": ".--.-."
}

REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}


def encode(text: str, letter_sep: str = " ", word_sep: str = " / ") -> str:
    """
    Convert plain text to Morse code.

    Args:
        text: The input plain text.
        letter_sep: Separator between Morse letters.
        word_sep: Separator between Morse words.

    Returns:
        Encoded Morse code string.

    Raises:
        ValueError: If an unsupported character is found.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    encoded_words = []

    for word in text.upper().split():
        encoded_letters = []
        for char in word:
            if char not in MORSE_CODE:
                raise ValueError(f"Unsupported character: {char}")
            encoded_letters.append(MORSE_CODE[char])
        encoded_words.append(letter_sep.join(encoded_letters))

    return word_sep.join(encoded_words)


def decode(morse_text: str, letter_sep: str = " ", word_sep: str = "/") -> str:
    """
    Convert Morse code to plain text.

    Args:
        morse_text: Morse code string.
        letter_sep: Separator between Morse letters.
        word_sep: Separator between Morse words.

    Returns:
        Decoded plain text string.

    Raises:
        ValueError: If an unsupported Morse token is found.
    """
    if not isinstance(morse_text, str):
        raise TypeError("morse_text must be a string")

    normalized = morse_text.strip()

    if not normalized:
        return ""

    words = [w.strip() for w in normalized.split(word_sep)]
    decoded_words = []

    for word in words:
        if not word:
            continue

        letters = [token for token in word.split(letter_sep) if token]
        decoded_letters = []

        for token in letters:
            if token not in REVERSE_MORSE_CODE:
                raise ValueError(f"Unsupported Morse code: {token}")
            decoded_letters.append(REVERSE_MORSE_CODE[token])

        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)