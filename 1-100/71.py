class Solution:
    def simplifyPath(self, path: str) -> str:
        # 重新组合，删除"."，".."和前面的同归于尽 
        paths = path.split('/')
        i = 0
        while i < len(paths):
            if i < 0:
                i = 0
            elif paths[i] == '':
                del paths[i]
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