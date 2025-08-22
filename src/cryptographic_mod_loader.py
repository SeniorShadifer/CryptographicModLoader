import os

import sh_mod_loader.mod_loader


class DecryptionException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RandomBytesGenerationFunction:
    def generate_random_bytes(self, length: int | None = None) -> bytes:
        return bytes()


class HashFunction:
    def hash(self, data: bytes) -> bytes:
        return bytes()


class PasswordDeriveFunction:
    def derive(
        self, password: bytes, salt: bytes, iterations: int = 150_000, length: int = 32
    ) -> bytes:
        return bytes()


class Key:
    def __init__(self, encoded_key: bytes | None = None):
        pass

    def encode(self) -> bytes:
        return bytes()

    def decode(self, encoded_key: bytes):
        pass


class SymmetricKey(Key):
    pass


class SymmetricAlgorythm:
    key_can_be_random_bytes: bool = True
    key_length: int = 32

    support_aad: bool = False

    def encrypt(
        self, key: SymmetricKey, data: bytes, aad: bytes | None = None
    ) -> bytes:
        return bytes()

    def decrypt(
        self, key: SymmetricKey, encrypted_data: bytes, aad: bytes | None = None
    ) -> bytes:
        return bytes()


class PublicKey(Key):
    pass


class PrivateKey(Key):
    pass


class AssymetricAlgorythm:
    def encrypt(self, pk: PublicKey, data: bytes) -> bytes:
        return bytes()

    def decrypt(self, sk: PrivateKey, encrypted_data: bytes) -> bytes:
        return bytes()

    def generate_key_pair(
        self, length: int | None = None
    ) -> tuple[PrivateKey, PublicKey]:
        return (PrivateKey(), PublicKey())


class AssymetricIncapsulationAlgorythm:
    def generate_and_incapsulate_key(
        self,
        length: int | None = None,
    ) -> tuple[bytes, bytes]:
        return (bytes(), bytes())

    def encapsulate_key(self, pk: PublicKey, key: bytes) -> bytes:
        return bytes()

    def decapsulate_key(self, sk: PrivateKey, incapsulated_key: bytes) -> bytes:
        return bytes()

    def generate_key_pair(
        self, length: int | None = None
    ) -> tuple[PrivateKey, PublicKey]:
        return (PrivateKey(), PublicKey())


class CryptographicModLoader(sh_mod_loader.mod_loader.ModLoader):
    symmetric_algorythms: dict[str, SymmetricAlgorythm] = {}
    assymetric_algorythms: dict[str, AssymetricAlgorythm] = {}
    assymetric_incapsulation_algorythms: dict[str, AssymetricIncapsulationAlgorythm] = (
        {}
    )

    random_bytes_generation_function: dict[str, RandomBytesGenerationFunction] = {}
    hash_functions: dict[str, HashFunction] = {}
    password_derive_functions: dict[str, PasswordDeriveFunction] = {}

    def load_symmetric_algorythm(self, path: str):
        if not os.path.exists(f"{path}/symmetric_algorythm.py"):
            return

    def __init__(self):
        super().__init__()

        self.processors |= {"symmetric_algorythms": self.load_symmetric_algorythm}
