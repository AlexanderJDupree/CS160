# closing_total = 0.0
# days = 0
# month_averages = []
# month_opens_closes = []
# month_highs_lows = []
# months_open_diff = []
# months_high_diff = []
# current_month = 1


    # for line in file:
    #     month = int(line['Date'].split('/')[0])
    #     if current_month == month:
    #         days += 1
    #         closing_total += float(line['Adj Close'])
    #         month_opens_closes.append([float(line['Open']), float(line['Close'])])
    #         month_highs_lows.append([float(line['High']), float(line['Low'])])
    #     else:
    #         month_averages.append(closing_total / days)
    #         months_open_diff.append(
    #             min([i[0] for i in month_opens_closes])
    #             - max([i[1] for i in month_opens_closes]))
    #         months_high_diff.append(
    #             min([i[0] for i in month_highs_lows])
    #             - max([i[1] for i in month_highs_lows]))
    #         closing_total = float(line['Adj Close'])
    #         month_opens_closes = []
    #         month_highs_lows = []
    #         days = 1
    #         current_month += 1

# month_averages.append(closing_total / days)
# months_open_diff.append(
#                 min([i[0] for i in month_opens_closes])
#                 - max([i[1] for i in month_opens_closes]))
# months_high_diff.append(
#                 min([i[0] for i in month_highs_lows])
#                 - max([i[1] for i in month_highs_lows]))

# print(month_averages)
# print(months_open_diff)
# print(months_high_diff)
