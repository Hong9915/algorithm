def solution(users, emoticons):
    emoticon_percentages = [10, 20, 30, 40]
    n = len(emoticons)
    max_plus_users = 0
    max_sales = 0
    discounts=[]
    def dfs(depth):
        nonlocal max_plus_users, max_sales

        if depth == n:
            plus_users = 0
            total_sales = 0

            for percent, price_limit in users:
                user_total = 0
                for emoticon_price, discount in zip(emoticons, discounts):
                    if discount >= percent:
                        user_total += emoticon_price * (100 - discount) // 100

                if user_total >= price_limit:
                    plus_users += 1
                else:
                    total_sales += user_total

            if plus_users > max_plus_users or (plus_users == max_plus_users and total_sales > max_sales):
                max_plus_users = plus_users
                max_sales = total_sales
            return

        for rate in emoticon_percentages:
            discounts.append(rate)
            dfs(depth + 1)
            discounts.pop()

    dfs(0)

    return [max_plus_users, max_sales]
