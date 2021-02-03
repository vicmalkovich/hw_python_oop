import datetime as dt
print('_____________________________')
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    

    def add_record(self, some_record):
        # some_record.date = dt.datetime.strptime(some_record.date, self.date_format)
        self.records.append(some_record)

    def get_today_stats(self):
        stats = 0
        now_date = dt.datetime.now()

        for item in self.records:
            if item.date.date() == now_date.date():
                stats = stats + item.amount
        return stats

    def get_week_stats(self):
        stats = 0     
        now_date = dt.datetime.now()
        last_week = dt.datetime.now() - dt.timedelta(days=7)
     
        for item in self.records:
    
            if item.date.date() >= last_week.date():
                stats = stats + item.amount
        return stats


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        

    USD_RATE = 60.0
    EURO_RATE = 70.0
    

    def get_today_cash_remained(self, currency):
        today_stats = cash_сalculator.get_today_stats()
        limit_money = self.limit

        if currency == 'usd':
           currency = 'USD'
           limit_money = self.limit / CashCalculator.USD_RATE
           today_stats = today_stats / CashCalculator.USD_RATE
        if currency == 'eur':
           currency = 'Euro' 
           limit_money = self.limit / CashCalculator.EURO_RATE
           today_stats = today_stats / CashCalculator.EURO_RATE
        if currency == 'rub':
            currency = 'руб'

        if today_stats == limit_money:
            return 'Денег нет, держись'
        if today_stats < limit_money:
            return f'На сегодня осталось {round(limit_money - today_stats, 2)} {currency}'
        if today_stats > limit_money:
            return f'Денег нет, держись: твой долг - {round(limit_money - today_stats, 2)} {currency}'

    
class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)     

    def get_calories_remained(self):
        today_stats = calories_calculator.get_today_stats()
        if today_stats < self.limit :
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - today_stats} кКал», если лимит {self.limit} не достигнут'
        else:
            return 'Хватит есть!'
 


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        else: 
            self.date = dt.datetime.now()
            

# для CashCalculator 
r1 = Record(amount=100, comment="Безудержный шопинг", date="02.02.2021")
r2 = Record(amount=1500, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=900, comment="Катание на такси", date="29.01.2021")
r4 = Record(amount=100, comment="К чаю", date="02.02.2021")
r5 = Record(amount=50, comment="Транспорт", date="03.02.2021")
r9 = Record(amount=50, comment="Транспорт")

# для CaloriesCalculator
r6 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r7 = Record(amount=84, comment="Йогурт.", date="01.02.2021")
r8 = Record(amount=1140, comment="Баночка чипсов.", date="02.01.2021")

cash_сalculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(2500)
cash_сalculator.add_record(r1)
cash_сalculator.add_record(r2)
cash_сalculator.add_record(r3)
cash_сalculator.add_record(r4)
cash_сalculator.add_record(r5)
cash_сalculator.add_record(r9)
calories_calculator.add_record(r6)
calories_calculator.add_record(r7)
calories_calculator.add_record(r8)

print(calories_calculator.get_calories_remained())

print(cash_сalculator.get_today_cash_remained('rub'))
print(cash_сalculator.get_today_cash_remained('usd'))
print(cash_сalculator.get_today_cash_remained('eur'))


print(f'На сегодня потрачено {cash_сalculator.get_today_stats()} руб.')
print(cash_сalculator.get_week_stats())
print(cash_сalculator.get_today_stats())
