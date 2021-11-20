#NVD 태그 분석 latestVulnsArea  >  div > ul > li > div class: col-lg-9
#1. NVD 사이트를 호출하여 등답을 받아온다.
#2. bs4를 이용하여 응답 결과를 html tag 타입으로 파싱한다.
#3. 게시글(li) tag elements 를 lists 로 담는다.
#4. KSTS로 timezone을 설정한다.
#6. 작성된 글이 있다면 Github issue로 등록하여 메일로 알림을 받는다.
#7. 매일 정해진 시각에 자동으로 파이썬 크롤러가 작동되도록 github actions를 만든다.


from urllib.request import urlopen
from bs4 import BeautifulSoup
#from github import GitHub, Issue
import datetime 
from pytz import common_timezones_set, timezone
from dateutil.parser import parse
import os 

res = urlopen('https://nvd.nist.gov/general/nvd-dashboard')
soup = BeautifulSoup(res, 'html.parser')
cve_list = soup.select('#latestVulns > li')


for cve_item in cve_list:
    main_div = cve_item.select('div')[0]
    title = main_div.select_one('strong').get_text()
    cve_score = cve_item.select('div')[1].get_text()
    s_cve_score = cve_score.replace(" " , "")
    content = main_div.get_text().strip()
    print('CVE Title: '+title)
    print('CVE Score: '+s_cve_score)
    print('Content: '+content)
    
'''
KST = timezone('Asia/Seoul')
today = datetime.datetime.now(KST)

def isDateInRange(created_at):
    suffix_KST = '0.000001+09:00'
    created_at = parse(created_at + suffix_KST)
    yesterday = today - datetime.timedelta(1)
    return today > created_at and created_at > yesterday

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
REPO_NAME = 'BaeHyeongYeon/cve_project'
repo = Gihub(GITHUB_TOKEN).get_user().get_repo(REPO_NAME)
if issue_body != '' 
'''



    