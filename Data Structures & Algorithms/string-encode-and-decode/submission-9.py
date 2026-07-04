class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return ''
        if strs==[""]:
            return 'pp'
        return '>.>'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=='':
            return []
        if s=='pp':
            return [""]
        return s.split('>.>')
