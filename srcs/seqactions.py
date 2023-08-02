from collections import defaultdict

class SequenceActions:
    @staticmethod
    def alignment(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
        rows, cols = len(seq1) + 1, len(seq2) + 1
        matrix = [[0] * cols for _ in range(rows)]

        # Initialize the gaps
        for i in range(rows):
            matrix[i][0] = i * gap_penalty
        for j in range(cols):
            matrix[0][j] = j * gap_penalty

        # Fill the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                match = matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
                delete = matrix[i-1][j] + gap_penalty
                insert = matrix[i][j-1] + gap_penalty
                matrix[i][j] = max(match, delete, insert)

        # Traceback to get the alignment
        align1, align2 = '', ''
        i, j = rows - 1, cols - 1
        while i > 0 and j > 0:
            if seq1[i-1] == seq2[j-1]:
                align1 += seq1[i-1]
                align2 += seq2[j-1]
                i -= 1
                j -= 1
            elif matrix[i][j-1] > matrix[i-1][j]:
                align1 += '-'
                align2 += seq2[j-1]
                j -= 1
            else:
                align1 += seq1[i-1]
                align2 += '-'
                i -= 1

        return align1[::-1], align2[::-1]

    @staticmethod
    def split_into_kmers(sequence, k):
        return [sequence[i:i+k] for i in range(0, len(sequence) - k + 1)]

    @staticmethod
    def generate_all_kmers(s):
        def _generate_kmers(s, k):
            return [s[i:i+k] for i in range(len(s) - k + 1)]

        result = []
        for k in range(1, len(s) + 1):
            result.extend(_generate_kmers(s, k))
        return list(set(result))