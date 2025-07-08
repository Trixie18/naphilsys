import time
import NTRU2

def benchmark_encrypt_decrypt(input_strings):
    for input_string in input_strings:
        # Measure encryption time
        start_time = time.time()
        enc = NTRU2.encrypt("test", input_string)
        end_time = time.time()
        encryption_time = end_time - start_time

        # Measure decryption time
        start_time = time.time()
        dec = NTRU2.decrypt("test", enc)
        end_time = time.time()
        decryption_time = end_time - start_time

        print(f"Input: {input_string}")
        print(f"Encryption time: {encryption_time:.6f} seconds")
        print(f"Decryption time: {decryption_time:.6f} seconds")
        print()

input_strings = [
    "Jocson, Alliah Ziandra Mamaril",
    "5962860319758416",
    "10/14/2003",
    "ziandrajocson@gmail.com",
    "6353 Bayabas St. Villa Cuana Phase 1, Pinagbuhatan, Pasig City",
    "Female",
    "Unknown",
    "Single",
    "City of Manila"
]

benchmark_encrypt_decrypt(input_strings)