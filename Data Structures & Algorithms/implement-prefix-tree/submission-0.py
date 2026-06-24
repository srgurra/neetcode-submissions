class PrefixTree:

    def __init__(self):
        
        self.children= {}
        self.isEnd= False


    def insert(self, word: str) -> None:
        root = self
        for ch in word:
            if ch not in root.children:
                root.children[ch]= PrefixTree()
            root= root.children[ch]
        root.isEnd= True

    def search(self, word: str) -> bool:
        root= self
        for ch in word:
            if ch not in root.children:
                return False
            root= root.children[ch]
        return root.isEnd
                
        

    def startsWith(self, prefix: str) -> bool:
        root = self
        for ch in prefix:
            if ch not in root.children:
                return False
            root= root.children[ch]
        return True
        
        