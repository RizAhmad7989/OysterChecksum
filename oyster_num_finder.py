class OysterNumFinder:

    #0x1 is hexadecimal. so 0x1 = 1, 0x10 = 16, etc
    def checksum(self, number: str) -> int:

        number = int(number)
        return (
            + number * 0x10
            + number // 0x1 * 3
            - number // 0x10 * 3
            + number // 0x100 * 3
            - number // 0x1000 * 3
            + number // 0x10000 * 3
            - number // 0x100000 * 3
            + number // 0x1000000 * 3
            - number // 0x10000000 * 3) % 100
