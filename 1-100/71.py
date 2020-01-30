class Solution:
    def simplifyPath(self, path: str) -> str:
        # 连续的/化成一个
        i = 1
        while i < len(path):
            if path[i] == '/' and path[i - 1] == '/':
                path = path[:i] + path[i+1:]
            else:
                i += 1
        # 去除最后的/
        if len(path) > 1 and path[-1] == '/':
            path = path[:-1]
        # 重新组合，删除"."，".."和前面的同归于尽 
        paths = path[1:].split('/')
        i = 0
        while i < len(paths):
            if i < 0:
                i = 0
            elif paths[i] == '.':
                del paths[i]
            elif paths[i] == ".." and i == 0:
                del paths[i]
            elif paths[i] == "..":
                del paths[i]
                del paths[i - 1]
                i -= 1
            else:
                i += 1
        return '/' + '/'.join(paths)