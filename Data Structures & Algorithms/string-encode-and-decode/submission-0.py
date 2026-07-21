class Solution:

    messages_db = {}

    def encode(self, strs: List[str]) -> str:
        list_str = str(strs)
        
        self.messages_db[list_str] = strs

        return list_str

    def decode(self, s: str) -> List[str]:
        return self.messages_db[s]
