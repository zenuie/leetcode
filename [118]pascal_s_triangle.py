class Solution:
    def generate(self, numRows):
        base_model = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return base_model
        else:
            self.sum_list(base_model, numRows)

    def sum_list(self, add_list, numRows):
        numRows -= 2
        temp_list = add_list[-1][::1]
        temp = []
        while numRows > 0:
            numRows -= 1
            while len(temp_list) > 1:
                temp.append(temp_list[0] + temp_list[1])
                temp_list.remove(temp_list[0])
            temp.insert(0, 1)
            temp.append(1)
            add_list.append(temp)
            temp_list = add_list[-1][::1]
            temp = []

        return add_list


s = Solution()
s.generate(4)
