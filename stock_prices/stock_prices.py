#!/usr/bin/python

import argparse

'''
[200 90 500 400 900 100]

- find smallest current price
- find max profit so far
- check if smalles price is before largest

'''


def find_max_profit(prices):
        breakpoint()
        curr_min_price_so_far = min(prices[0], prices[1])
        max_profit_so_far = prices[1] - prices[0]
        loops = 0

        for i in range(1, len(prices) - 1):
            loops += 1

            current_price = prices[i]
            if max_profit_so_far < 0 and loops <= 1:
                max_profit_so_far = min(
                    max_profit_so_far, current_price - curr_min_price_so_far)
            else:
                max_profit_so_far = max(
                    max_profit_so_far, current_price - curr_min_price_so_far)
                curr_min_price_so_far = min(
                    curr_min_price_so_far, current_price)
        return max_profit_so_far


find_max_profit([100, 90, 80, 50, 20, 10])

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
