from money_tracker_menu import *

def main():
    user_data = Parser.parse_money_tracker_data('money_tracker.txt')
    aggregated_data = AggregatedMoneyTracker(user_data)
    money_tracker = MoneyTracker(aggregated_data)

    menu(money_tracker)

if __name__ == '__main__':
    main()