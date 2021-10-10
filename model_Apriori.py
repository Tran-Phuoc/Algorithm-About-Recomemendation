import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules

class Apriori:
    def __init__(self,url,min_Support):
        self.url = url
        self.min_Support = min_Support
        self.basket_User = self.xuLy_Data()
        self.rules_book = self.model_Apriori()
    def one_hot_encode(self,x):
        if  x>=1:
            return 1
        else:
            return 0

    def xuLy_Data(self):
        data = pd.read_csv(self.url)

        data['Name'] = data['Name'].str.strip()
        data['ID'] = data['ID'].astype('int')

        basket_User = (data.groupby(['ID', 'Name'])['ID']
                       .sum().unstack().reset_index().fillna(0)
                       .set_index('ID'))

        basket_encoded = basket_User.applymap(self.one_hot_encode)
        basket_User = basket_encoded
        return basket_User

    def model_Apriori(self):
        frq_items = apriori(self.basket_User, min_support = self.min_Support, use_colnames = True)
        rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
        rules = rules.sort_values(['confidence','lift'], ascending =[False,False])

        rules_book = rules[['antecedents','consequents','support','confidence','lift']]
        rules_book['length'] = rules_book.loc[:,'antecedents'].apply(lambda x:len(x))

        rules_book.index = range(len(rules_book))
        return rules_book

    def rules(self,lst):
        rules_book = self.rules_book
        n=len(lst)
        result = set()
        while (n!=-1):
          data = rules_book[rules_book.length==n]
          if n==0:
            data = rules_book[rules_book.length>0]
            for i in range(len(data)):
              temp = list(data.consequents[i])
              result.add(str(temp[0]))
            break
          data.index = range(len(data))
          for i in range(len(data)):
            if any([1 if lst_temp in list(data.antecedents[i]) else 0 for lst_temp in lst]):
              temp = list(data.consequents[i])
              result.add(str(temp[0]))
          n-=1
        result = result - set(lst)
        result = list(result)
        return result
