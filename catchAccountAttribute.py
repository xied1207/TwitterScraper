import urllib.request
import AdvancedHTMLParser
def main():
    try:
        urllist = open('url.txt', 'r', encoding='utf8')
        urls = urllist.readlines()
        for lines in urls:
            tweet_url=lines.rstrip()
            if '/#!/' in tweet_url:
                tweet_url=tweet_url.replace('/#!/','/')
            rv_twurl=tweet_url[::-1]
            end_index=rv_twurl.index('tats/')
            rv_acurl=rv_twurl[end_index+4:]
            account_url=rv_acurl[::-1]
            print("Account url:",account_url)
            html=get_html(account_url)
            get_descr(html)
            get_nums(html)
        urllist.close()
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

def get_descr(html):
    try:
        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(html)
        out_part = parser.getElementsByClassName("ProfileHeaderCard")
        for content in out_part:
            the_content = content.innerHTML.strip()
            des_start_index=the_content.index('<p dir="ltr" class="ProfileHeaderCard-bio u-dir" >')
            des_end_index=the_content.index('</p>')
            acc_descr=the_content[des_start_index+50:des_end_index]
            print("Account Description: ",acc_descr)
    except Exception as err:
        print(err)
def get_nums(html):
    try:
        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(html)
        profile_html=parser.getElementsByClassName("ProfileNav")
        for content in profile_html:
            the_content = content.innerHTML.strip()
            novalue_index = the_content.index('tweets')
            tw_index=the_content.index('following')
            tw_content = the_content[novalue_index:tw_index]
            get_twnum(tw_content)
            fli_index = the_content.index('followers')
            fli_content = the_content[tw_index:fli_index]
            get_flinum(fli_content)
            fle_index = the_content.index('favorites')
            fle_content = the_content[fli_index:fle_index]
            get_flenum(fle_content)
            like_content=the_content[fle_index:]
            get_likenum(like_content)
    except Exception as err:
        print(err)

def get_twnum(html):
    start_index=html.index('title')
    end_index=html.index('Tweets')
    tweet_num=html[start_index+7:end_index]
    print("Account tweets number: ",tweet_num )
def get_flinum(html):
    start_index = html.index('title')
    end_index = html.index('Following')
    fli_num = html[start_index+7:end_index]
    print("Account followings number: " , fli_num)

def get_flenum(html):
    start_index = html.index('title')
    end_index = html.index('Followers')
    fle_num = html[start_index+7:end_index]
    print("Account followers number: " , fle_num)

def get_likenum(html):
    start_index = html.index('title')
    end_index = html.index('Like')
    like_num = html[start_index+7:end_index]
    print("Account likes number: " , like_num)

main()