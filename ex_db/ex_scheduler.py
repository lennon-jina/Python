from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
# pip install --upgrade apscheduler
# 스케줄형 라이브러리
# interval : 특정 주기로 작업
# conn     : 원하는 시간(다양한 시간에 실행 가능)

def test_interval():
    print("interval")
    print(datetime.datetime.now())

def test_cron():
    print("cron =======================")
    print(datetime.datetime.now())
workers = BlockingScheduler()
# 등록
workers.add_job(test_interval, 'interval', seconds=20)  # 20초마다 주기적으로 실행함.
workers.add_job(test_cron, 'cron', hour='15', minute='35')   # 매일 15시 35분마다
# 매월 1일 오전 10시 30분
workers.add_job(test_cron, 'cron', day='1', hour='10', minute='30')
# 월 ~ 금 오후 2시
workers.add_job(test_cron, 'cron', day_of_week='mon-fri', hour='14')
# 수, 금 만 9시에
workers.add_job(test_cron, 'cron', day_of_week='wed,fri', hour='09')
workers.start()

workers.start()