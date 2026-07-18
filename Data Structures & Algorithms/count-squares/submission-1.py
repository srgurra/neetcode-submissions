class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.rows = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[(x, y)] += 1
        self.rows[y].append(x)

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        for x2 in self.rows[y]:
            if x2 == x:
                continue

            side = x2 - x

            result += (
                self.counts[(x, y + side)]
                * self.counts[(x2, y + side)]
            )


            result += (
                self.counts[(x, y - side)]
                * self.counts[(x2, y - side)]
            )

        return result
