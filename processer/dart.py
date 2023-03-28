from crawl.common import Common

import xml.etree.ElementTree as ET

class DartProcesser(Common):
    def __init__(self):
        super().__init__()

        self.hot_keyword = "무상증자"
        self.namespaces = {"dc":"http://purl.org/dc/elements/1.1/"}

    def parsing_all_data(self):
        html = self.get_html_by_url(url="https://dart.fss.or.kr/api/todayRSS.xml")

        row_xml = ET.fromstring(html)

        rss = row_xml.find("channel")

        disclosure_data = list()
        for item in rss.findall("item") :
            title = item.find("title").text
            link = item.find("link").text
            category = item.find("category").text
            pubDate = item.find("pubDate").text
            guid = item.find("guid").text
            dc_creator = item.find("dc:creator",self.namespaces).text
            dc_date = item.find("dc:date",self.namespaces).text
            
            disclosure_data.append({
                "title": title,
                "link": link,
                "category": category,
                "pubDate": pubDate,
                "guid": guid,
                "dc_creator": dc_creator,
                "dc_date": dc_date,
            })

        return disclosure_data
    
    def is_in_bonus_issue(self, disclosure_data:list):
        bonus_issue_company_list = list()
        for data in disclosure_data :
            if self.hot_keyword in data["title"]:
                bonus_issue_company_list.append({
                    "dc_creator" : data["dc_creator"],
                    "link" : data["link"],
                })

        return bonus_issue_company_list
