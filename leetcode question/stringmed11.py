class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(openp,closep,comb):
            if openp==closep and openp+closep==n*2:
                res.append(comb[:])
            if openp<n:
                dfs(openp+1,closep,comb+'(')
            if closep<openp:
                dfs(openp,closep+1,comb+')')
        dfs(0,0,"")
        return res
        