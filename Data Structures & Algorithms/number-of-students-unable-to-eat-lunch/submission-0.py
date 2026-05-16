class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        i = 0
        zeros = 0
        ones = 0
        hungry = 0

        for student in students:
            if student == 0:
                zeros += 1
            else:
                ones += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if zeros == 0:
                    break
                zeros -= 1
            elif sandwich == 1:
                if ones == 0:
                    break
                ones -= 1
            
        hungry = zeros + ones

        return (hungry)