class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        l = len(data)
        while (i < l):
            bin_rep = format(data[i], '#010b')[-8:]

            if '0' not in bin_rep:
                return False
            count = bin_rep.index('0')
            if count == 0:
                i += 1
                continue
                
            if count == 1 or count > 4:
                return False
                
            i += 1
            while count != 1 and i < l:
                bin_rep = format(data[i], '#010b')[-8:]
                if bin_rep[:2] == '10':
                    count -= 1
                    i += 1
                else:
                    return False
            if count > 1:
                return False
        
        return True
