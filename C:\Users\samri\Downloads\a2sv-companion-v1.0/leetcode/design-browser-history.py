class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        homepage = Node(homepage)
        self.head = homepage
        self.last = self.head
    def visit(self, url: str) -> None:
        new_url = Node(url)
        # curr = self.head
        # while curr and curr.next:
        #     curr = curr.next
        # curr.next = new_url 
        # new_url.prev = curr
        self.last.next = new_url
        new_url.prev = self.last
        self.last = new_url

        # curr = self.head 
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print('end')
    def back(self, steps: int) -> str:
        curr = self.last
        while steps and curr and curr.prev:
            curr = curr.prev
            # print(curr.val)
            steps -= 1
        self.last = curr

        # curr = self.head 
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print('end')
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.last
        while steps and curr and curr.next:
            curr = curr.next 
            # print(curr.val)
            steps -= 1
        self.last = curr

        # curr = self.head 
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print('end')
        return curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)