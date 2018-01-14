import urllib.request
import AdvancedHTMLParser
import re
def main():
    try:
        urllist = open('url.txt', 'r', encoding='utf8')
        urls = urllist.readlines()
        for lines in urls:
            the_url=lines.rstrip()
            if '/#!/' in the_url:
                the_url=the_url.replace('/#!/','/')
            html=get_html(the_url)
            get_content(html)
            get_time(html)
            get_nums(html)
    except Exception as err:
        print(err)

def get_html(line):
    try:
        response = urllib.request.urlopen(line)
        htmlStr = response.read()
        htmlString = str(htmlStr, encoding="utf-8")
        return htmlString
    except Exception as err:
        print(err)

def get_content(html):
    try:
        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(html)
        twi_content = parser.getElementsByTagName("title")
        for content in twi_content:
            the_content = content.innerHTML.strip()
            tagnum = len(re.findall("#", the_content))
            atnum=len(re.findall("@", the_content))
            print("Content:",the_content)
            print("Hashtag number:",tagnum)
            print("@ number:",atnum)
    except Exception as err:
        print(err)

def get_time(html):
    try:
        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(html)
        time_part=parser.getElementsByClassName("client-and-actions")
        the_time=time_part.getElementsByClassName("metadata")
        for content in the_time:
            the_content = content.innerHTML.strip()
            time_start_index=the_content.index('<span >')
            time_end_index=the_content.index('</span>')
            time_content=the_content[time_start_index+7:time_end_index]
            print("time:",time_content)
    except Exception as err:
        print(err)

def get_nums(html):
    try:
        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(html)
        retw=parser.getElementsByClassName("ProfileTweet-actionCountForPresentation")
        n=0
        for content in retw:
            n += 1
            if n==2 or n==3:
                retw_num = content.innerHTML.strip()
            elif n==4 or n==5:
                like_num = content.innerHTML.strip()
        print("retweet:" ,retw_num)
        print("like:" ,like_num)
    except Exception as err:
        print(err)

main()