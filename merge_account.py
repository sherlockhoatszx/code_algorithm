'''首先构造email_to_ids'email_to_ids':{'email1':[0,2],'email2':[2]}
然后用union_find把相联通的列表下表更新他对应的老大哥
step3,把每个联通图用老大哥的id 作key和邮件list作value,构建id_to_email_set
step4,然后将老大哥的下表对应到人名,遍历添加merged_accounts中'''
class UnionFind:

    def initialize(self,n):
        self.father ={}

        for i in range(n):
            self.father[i] = i

    def find(self,user_id):
        path = []
        while user_id != self.father[user_id]:
            path.append(user_id)
            user_id = self.father[user_id]

        for u in path:
            self.father[u] = user_id

        return user_id

    def union(self,id1,id2):
        self.father[self.find(id1)] = self.find(id2)




import pdb
class Solution(UnionFind):

    def accountsMerge(self,accounts):
        pdb.set_trace()
        self.initialize(len(accounts))
        email_to_ids = self.get_email_to_ids(accounts)

        # union
        for email, ids in email_to_ids.items():
            root_id = ids[0]
            for id in ids[1:]:
                self.union(id, root_id)

        id_to_email_set = self.get_id_to_email_set(accounts)

        merged_accounts = []
        for user_id, email_set in id_to_email_set.items():
            merged_accounts.append([
                accounts[user_id][0],
                *sorted(email_set),
            ])
        return merged_accounts


    def get_email_to_ids(self,accounts):
        email_to_ids = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_ids[email] = email_to_ids.get(email, [])
                email_to_ids[email].append(i)
        return email_to_ids


    def get_id_to_email_set(self,accounts):
        id_to_email_set = {}
        for user_id, account in enumerate(accounts):
            root_user_id = self.find(user_id)
            email_set = id_to_email_set.get(root_user_id, set())
            for email in account[1:]:
                email_set.add(email)
            id_to_email_set[root_user_id] = email_set
        return id_to_email_set

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John",
"johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

sl = Solution()
print(sl.accountsMerge(accounts))
