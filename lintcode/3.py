class Solution:
    def strStr(self, source, target):
        # write your code here
        if source == '' and target == '':
            return 0
        if source == None or target == None:
            return -1
        if source != '' and target == '':
            return 0
        if source == target:
            return 0
        # l = len(source)

        # return len(source)-len(target)+1

        # for i in range(l):
        #     if source[i] == target[0]:
        #         return i
        # return -1
        for i in range(len(source)-len(target)+1):
            flag = True
            res = i
            for char in target:
                if char == source[i]:
                    i+=1
                else:
                    flag = False
            if flag:
                return res
        return -1


a = Solution()
b = a.strStr('asdf', 'sb')
print b
"""
      for i in range(len(source)-len(target)+1):
          flag = True
          res = i
          for char in target:
              if char == source[i]:
                  i +=1
              else:
                  flag = False
          if flag:
              return res
      return -1
"""
