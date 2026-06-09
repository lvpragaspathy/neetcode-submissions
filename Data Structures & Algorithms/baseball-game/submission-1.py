class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = 0
        record = []

        for i in range(len(operations)):
            if operations[i] == '+':
                record.append(record[-1] + record[-2])
                output += record[-1]
            elif operations[i] == 'C':
                x = record.pop(-1)
                output -= x
            elif operations[i] == 'D':
                record.append(record[-1] * 2)
                output += record[-1]
            else:
                record.append(int(operations[i]))
                output += record[-1]

        return output
