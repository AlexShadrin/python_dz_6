# add_sale.py
import sys
price = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')
# python add_sale.py 100
# show_sales.py
import sys
nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)
    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())
# python show_sales.py 1 6