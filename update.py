import requests
from data_ulis import open_file
import datetime
from pprint import pprint
def get_list_of_N_day_ago(n):
    href='http://ketqua.net/xo-so-mien-bac.php?ngay='
    days=[]
    urls=[]
    now=datetime.datetime.now()
    current_date= now.date()
    current_time = now.time()
    today6pm = now.replace(hour=18, minute=30, second=0, microsecond=0)

    for i in reversed(range(n)):
        day = (now - datetime.timedelta(days=i)).date()
        # days.append(href+ (now - datetime.timedelta(days=i)).strftime("%d-%m-%Y"))
        url=href+ (now - datetime.timedelta(days=i)).strftime("%d-%m-%Y")
        if day<current_date:
            days.append(day.strftime("%d-%m-%Y"))
            urls.append(url)
        elif day==current_date:
            if now > today6pm:
                days.append(day.strftime("%d-%m-%Y"))
                urls.append(url)
                break
            else:
                #update date to write initial col
                break


    return days,urls



def main():
    # get_urls_to_update('./excels/lottery100.xlsx')
    print(get_list_of_N_day_ago(2))


if __name__ == '__main__':
    main()
