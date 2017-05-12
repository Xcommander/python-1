# struct test，把字节转换成数据，以及数据转换成字节。
# >把数据转换成二进制字节，<是把二进制数据转换成数据
import os
import struct


def struct_test():
    path = os.getcwd()
    print(path)
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == ".bmp":
            with open(file, "rb") as f:
                b = f.read(30)
                x = struct.unpack("<ccIIIIIIHH", b)
                if x[0] == b'B' and x[1] == b'M':
                    print("大小为%s * %s,颜色数为%s" % (x[6], x[7], x[9]))

    pass


import hashlib


def hashlib_test():
    md5 = hashlib.md5()
    md5.update("I'am xulinchao".encode("utf-8"))
    md5.update("I'am yansuwan".encode("utf-8"))
    print(md5.hexdigest())
    pass


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
db_src = {
    "michael": "123456",
    "bob": "abc999",
    "alice": "alice2008"
}


# 没使用一次hashlib.md5都要重新获取实例
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()


def login(user, password):
    if db[user] == calc_md5(password):
        print("%s 登录成功" % user)
    else:
        print("%s 登录失败" % user)


def start_login():
    for key, value in db_src.items():
        login(key, value)


import itertools


def iterator_test():
    # naturals=itertools.count(1)
    # natuals=itertools.cycle("ABC")
    natuals = itertools.repeat("1", 4)
    for i in natuals:
        print(i)

    for i in itertools.chain("ABC", "234"):
        print(i)

    for i, j in itertools.groupby("QQQQCCFF"):
        print(i, list(j))
    # 截取takewihile
    for i in itertools.takewhile(lambda x: x <= 10, itertools.count(1)):
        print(i)

    pass


from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query info about %s" % self.name)


@contextmanager
def create_query(name):
    print("start")
    q = Query(name)
    yield q
    print("end")


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("<%s>" % name)


# contextmanager是用来实现上下文的。
# 没有实现上下文，可以通过closing
# 没有
from contextlib import closing
from urllib.request import urlopen


def closing_test():
    with closing(urlopen(url="https://www.python.org")) as page:
        for i in page:
            print(i)


# prase xml with SAX

from xml.parsers.expat import ParserCreate


class DefaultSaxHander(object):
    def start_element(self, name, attrs):
        print("sax:start_element:%s,attrs:%s" % (name, str(attrs)))

    def end_element(self, name):
        print("sax:end_element: %s" % name)

    def char_data(self, text):
        print("sax:char_data:%s" % text)


def parese_xml():
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''
    print(xml)
    handler = DefaultSaxHander()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    for i in parser.Parse(xml):
        print(i)


# weather sax
class WeatherSaxHandler(object):
    def __init__(self):
        self.weather = {}
        self.size = 2

    def StartElement(self, name, attrs):
        if name == "yweather:location":
            for key, value in attrs.items():
                if key == "city":
                    self.weather["city"] = value
                elif key == "country":
                    self.weather["country"] = value
        elif name == "yweather:forecast":
            self.size -= 1
            if self.size == 1:
                today_weather = {}
                today_weather["text"] = attrs.get("text")
                for key, value in attrs.items():
                    if key == "low":
                        today_weather["low"] = value
                    elif key == "high":
                        today_weather["high"] = value
                self.weather["today"] = today_weather
            elif self.size == 0:
                tomorrow_weather = {}
                tomorrow_weather["text"] = attrs.get("text")
                for key, value in attrs.items():
                    if key == "low":
                        tomorrow_weather["low"] = value
                    elif key == "high":
                        tomorrow_weather["high"] = value
                self.weather["tomorrow"] = tomorrow_weather


def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.StartElement
    parser.Parse(xml)
    print(handler.weather)
    pass


# html parse
from html.parser import HTMLParser
from html.entities import name2codepoint

import re


class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.con = {}
        self.all = []
        self.tag = ''
        self.flag=0

    def handle_starttag(self, tag, attrs):
        # print(attrs)
        if len(attrs) >0:
            if tag == "a" and re.match(r"^\/events\/python-events\/\d+\/$", attrs[0][1]):
                self.flag = 1
                self.tag = "title"
            elif tag == "time" and re.match(r'^[\d]{4}\-[\d]{2}-*', attrs[0][1]):
                self.flag = 1
                self.tag = 'time'
            elif tag == 'span' and attrs[0][1] == 'say-no-more':
                self.flag = 1
                self.tag = 'time1'
            elif tag == "span" and attrs[0][1] == "event-location":
                self.flag = 1
                self.tag = 'location'


    def handle_endtag(self, tag):
        # self.flag=0
        pass
        # print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        pass
        # print('<%s/>' % tag)

    def handle_data(self, data):
        if self.tag == "title"and re.match(r'^[0-9A-Za-z]+',data):
            self.con["title"] = data
        elif self.tag == 'time':
            self.con['time'] = data
        elif self.tag == 'time1'  and re.match(r'^ [\d]{4}',data):
            self.con['time'] = self.con["time"]+data
            print(self.con['time'])
        elif self.tag == "location" and re.match(r'^[0-9A-Za-z]+',data) and self.flag==1:
            self.con['location'] = data
            self.all.append(self.con)
            self.con = {}
        pass

    def handle_comment(self, data):
        pass
        # print('<!--', data, '-->')

    def handle_entityref(self, name):
        pass
        # print('&%s;' % name)

    def handle_charref(self, name):
        pass
        # print('&#%s;' % name)


def html_test():
    parser = MyHtmlParser()
    with urlopen("https://www.python.org/events/python-events/") as f:
        parser.feed(f.read().decode('utf-8'))
        print(parser.all)
    for i in parser.all:
        print('-------会议 ------')
        print(i["title"])





# urilib test
from urllib import request,parse
def get_data():
    with request.urlopen("http://php.weather.sina.com.cn/iframe/index/w_cl.php?code=js&day=0&city=&dfc=1&charset=utf-8") as f:
        print("status",f.status,f.reason)
        for key,value in f.getheaders():
            print(key,value)
        print(f.read().decode('utf-8'))

    pass

def request_test():
    req=request.Request("https://www.baidu.com")
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with urlopen(req) as f:
        print("Status:",f.status,f.reason)
        for key,value in f.getheaders():
            print(key,value)
        # print(f.read().decode('utf-8'))

def post_test():
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    with urlopen(req,data=login_data.encode('utf-8')) as f:
        print("status",f.status,f.reason)
        for key,value in f.getheaders():
            print(key,value)
        print(f.read().decode('utf-8'))

from tkinter import *
import tkinter.messagebox as messagebox
class MyApplication(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or "world"
        messagebox.showinfo("message","hello, %s"%name)


# 解析xml，就注意一点，重写方法，一个是通过外部重写，一个是通过子类重写
data1 = r'''

<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.css" rel="stylesheet" type="text/css" title="default" />
    <link href="/static/stylesheets/mq.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />
    

    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->

    
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">

    
    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Our Events | Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">

    
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Our Events">
    <meta property="og:description" content="The official home of the Python Programming Language">
    
    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">
    
    <meta property="og:url" content="https://www.python.org/events/python-events/">

    <link rel="author" href="/static/humans.txt">

    

    
    <script type="application/ld+json">
     {
       "@context": "http://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>

    
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
    
</head>

<body class="python events default-page">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lt IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p><strong>Notice:</strong> Your browser is <em>ancient</em> and <a href="http://www.ie6countdown.com/">Microsoft agrees</a>. <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience a better web.</p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">

                
                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>

                
                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close
                </a>

                

<ul class="menu" role="tree">
    
    <li class="python-meta ">
        <a href="/" title="The Python Programming Language" >Python</a>
    </li>
    
    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>
    </li>
    
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>
    
    <li class="pypi-meta ">
        <a href="https://pypi.python.org/" title="Python Package Index" >PyPI</a>
    </li>
    
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>
    
    <li class="shop-meta ">
        <a href="/community/" title="Python Community" >Community</a>
    </li>
    
</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>
                </h1>

                <div class="options-bar do-not-print">

                    
                    <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                        <fieldset title="Search Python.org">

                            <span aria-hidden="true" class="icon-search"></span>

                            <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                            <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                            <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                GO
                            </button>

                            
                            <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                        </fieldset>
                    </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                        <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="winkwink-nudgenudge">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger">Socialize</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="http://plus.google.com/+Python"><span aria-hidden="true" class="icon-google-plus"></span>Google+</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="http://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a href="http://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                    <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="account-signin">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                
                                <a href="/accounts/login/" title="Sign Up or Sign In to Python.org">Sign In</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="/accounts/signup/">Sign Up / Register</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="/accounts/login/">Sign In</a></li>
                                </ul>
                                
                            </li>
                        </ul>
                    </div>

                </div><!-- end options-bar -->

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">
                    
                        
<ul class="navigation menu" role="menubar" aria-label="Main Navigation">
  
    
    
    <li id="about" class="tier-1 element-1  " aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="community" class="tier-1 element-4  " aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">
        <a href="/about/success/" title="success-stories" class="">Success Stories</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="events" class="tier-1 element-7  " aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    
    
    
  
</ul>

                    
                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->
                    
    

                </div>

                
                

             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content with-right-sidebar" role="main">

                    
                    

                    

                    
        
        
        <header class="article-header">
            <h3>from the Python Events Calendar</h3>
        </header>
        
        
        <div class="most-recent-events">
            <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
                
                <ul class="list-recent-events menu">
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/465/">PyCon US 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-05-17T00:00:00+00:00">17 May &ndash; 26 May <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Portland, Oregon, USA</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/516/">PyDataBCN 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-05-19T00:00:00+00:00">19 May &ndash; 22 May <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Barcelona, Spain</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/505/">PyConWEB 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-05-27T00:00:00+00:00">27 May &ndash; 29 May <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Munich, Germany</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/523/">PyCon Taiwan 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-06-06T00:00:00+00:00">06 June &ndash; 12 June <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Academia Sinica, 128 Academia Road, Section 2, Nankang, Taipei 11529, Taiwan</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/513/">PyCon CZ 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-06-09T00:00:00+00:00">09 June &ndash; 12 June <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Prague, Czechia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/509/">PyParis 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-06-12T00:00:00+00:00">12 June &ndash; 14 June <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Paris, France</span>
                            
                        </p>
                    </li>
                
                </ul>
            </div>

            
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/463/">GeoPython 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-05-08T00:00:00+00:00">08 May &ndash; 11 May <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">Basel, Switzerland</span>
                        
                    </p>
                </li>
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/501/">PyDays Vienna 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-05-05T00:00:00+00:00">05 May &ndash; 07 May <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">FH Technikum Wien, Höchstädtplatz 6, 1200 Vienna, Austria</span>
                        
                    </p>
                </li>
                
            </ul>
            
        </div>


                </section>

                
                

                
    <aside class="right-sidebar" role="secondary">
        <div class="sidebar-widget subscribe-widget">
            <h2 class="widget-title">Python Event Subscriptions</h2>
            <p>Subscribe to Python Event Calendars:</p>
            <ul class="menu">
                
                
                <li><a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"><span aria-hidden="true" class="icon-ical"></span>Events in iCal format</a></li>
                
            </ul>
            <h2 class="widget-title">Python Events Calendars</h2>

<br/>

<p>For Python events near you, please have a look at the <a href="http://lmorillas.github.io/python_events/"><b>Python events map</b></a>.</p>

<p>The Python events calendars are maintained by the <a href="https://wiki.python.org/moin/PythonEventsCalendar#Python_Calendar_Team">events calendar team</a>.</p>

<p>Please see the <a href="https://wiki.python.org/moin/PythonEventsCalendar">events calendar project page</a> for details on how to <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event">submit events</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Available_Calendars">subscribe to the calendars</a>, get <a href="https://twitter.com/PythonEvents">Twitter feeds</a> or embed them.</p>

<p>Thank you.</p>


	    </div>
        
        
        
        
        
    </aside>



            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">

                    
                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>

                    

<ul class="sitemap navigation menu do-not-print" role="tree" id="container">
    
    <li class="tier-1 element-1">
        <a href="/about/" >About</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-2">
        <a href="/downloads/" >Downloads</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-3">
        <a href="/doc/" >Documentation</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-4">
        <a href="/community/" >Community</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-5">
        <a href="/about/success/" title="success-stories">Success Stories</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">News</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-7">
        <a href="/events/" >Events</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-8">
        <a href="/dev/" >Contributing</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="http://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
    
</ul>

        
    </li>
    
</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>
                    

                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">
                    
                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright &copy;2001-2017.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->

    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>

    <script type="text/javascript" src="/static/js/main-min.js" charset="utf-8"></script>
    

    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.js" charset="utf-8"></script>
    
    
    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.js" charset="utf-8"></script>
    
    
    <![endif]-->

    

    
    

</body>
</html>

'''
if __name__ == '__main__':
    # with create_query("BOb") as f:
    #     f.query()

        # with tag("hi"):
        #     print("Hello")
        #     print("Hi")

        # closing_test()
        data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
           <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
               <channel>
                   <title>Yahoo! Weather - Beijing, CN</title>
                   <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
                   <yweather:location city="Beijing" region="" country="China"/>
                   <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
                   <yweather:wind chill="28" direction="180" speed="14.48" />
                   <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
                   <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
                   <item>
                       <geo:lat>39.91</geo:lat>
                       <geo:long>116.39</geo:long>
                       <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
                       <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
                       <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
                       <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
                       <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
                       <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
                       <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
                   </item>
               </channel>
           </rss>
           '''
        # parse_weather(data)
        # d=dict({"aa":2,"bb":4})
        # print(d.get("aa"))
        app=MyApplication()
        app.master.title("Hello,World")
        app.mainloop()
