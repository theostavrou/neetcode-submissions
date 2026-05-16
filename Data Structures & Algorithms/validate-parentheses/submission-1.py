class Solution:
    def isValid(self, s: str) -> bool:
        
        output =[]
        for bracket in s:
            if bracket == ")":
                if output and output[-1]=="(":
                    output.pop()
                else:
                    return(False)
            elif bracket == "]":
                if output and output[-1]=="[":
                    output.pop()
                else:
                    return(False)
            elif bracket == "}":
                if output and output[-1] == "{":
                    output.pop()
                else:
                    return (False)
            else:
                output.append(bracket)
        if output == []:
            return(True)
        else:
            return(False)