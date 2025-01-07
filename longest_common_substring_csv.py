# longest_common_substring_csv.py
def longest_common_substring(str1, str2):
    m = [[0] * (1 + len(str2)) for i in range(1 + len(str1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(str1)):
        for y in range(1, 1 + len(str2)):
            if str1[x - 1] == str2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return str1[x_longest - longest: x_longest]

def read_csv(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace('\n', ',').split(',')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python longest_common_substring_csv.py <file1> <file2>")
        sys.exit(1)
    
    file1_fields = read_csv(sys.argv[1])
    file2_fields = read_csv(sys.argv[2])
    
    longest_common = ""
    for field1 in file1_fields:
        for field2 in file2_fields:
            lcs = longest_common_substring(field1, field2)
            if len(lcs) > len(longest_common):
                longest_common = lcs
    
    print("Longest common substring in comma-delimited fields:", longest_common)
