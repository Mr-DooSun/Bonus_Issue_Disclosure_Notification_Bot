from apscheduler.schedulers.background import BackgroundScheduler

from processer.dart import DartProcesser

class DartScheduler():
    def __init__(self):
        self.dart_parser = DartProcesser()

        self.init_data = self.dart_parser.parsing_all_data() 

    def loop(self):
        self.disclosure_data = self.dart_parser.parsing_all_data()

        bonus_issue_data = self.dart_parser.is_in_bonus_issue(disclosure_data = self.disclosure_data)
        if len(bonus_issue_data) > 0 :
            for data in bonus_issue_data :
                print(f"[{data['dc_creator']}] : 무상증자 알림 -> <참고> {data['link']}")
        else :
            print("무상증자 알림 없음")

    def run(self):
        dart_schedule = BackgroundScheduler(timezone='Asia/Seoul')
        dart_schedule.add_job(self.loop,'interval', seconds=1, id='dart')
        dart_schedule.start()