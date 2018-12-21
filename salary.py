# Kimberly Vo
# kv3nw
# worked with jqn5xk, mtv2mn, ssc6ae, also got help from upperclassman vivian tran with html formatting
import urllib.request
import re

def report(name):
    '''
    takes the name and searches though the URL to find the rank, salary, and title of the person
    :param name: name given by the user to search
    :return: title,rank, and salary ; returns None, 0 , and 0 if it does not exist
    '''
    name = name.lower()
    if ',' in name:
        split_name = name.split(', ')
        name = split_name[1] + '-' + split_name[0]
    elif ' ' in name:
        name = name.replace(' ', '-')
    else:
        name = name

    try:
        url = 'http://cs1110.cs.virginia.edu/files/uva2016/' + name
        read_url = urllib.request.urlopen(url).read().decode('utf-8')
        job = re.compile(r'Job title: ([A-Za-z0-9- &<>;])+<')
        money = re.compile(r'paytype.amount, [0-9]+.[0-9]+')
        rank = re.compile(r'rank</td><td>([0-9]+,*[0-9]*)')
        job_search = job.search(read_url)
        if job_search != None:
            job = job_search.group().strip('<').strip('Job title:')
            if '&amp;' in job:
                job = job.replace('&amp;', '&')
            if '&lt;' in job:
                job = job.replace('&lt;', '<')
            if '&gt;' in job:
                job.replace('&gt;', '>')
        money_search = money.search(read_url)
        if money_search != None:
            money = money_search.group().strip('paytype.amount, ')
            money = float(money)
        rank_search = rank.search(read_url)
        if rank_search != None:
            rank = rank_search.group().strip('(rank rank</td><td>')
            rank = int(rank.replace(',',''))
        if rank_search == None:
            rank = 0
    except:
        job = None
        money = 0
        rank = 0
    full_report = [job, money, rank]
    return full_report
