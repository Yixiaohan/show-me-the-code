Python Workbooks - One Program One Day
==

*(Translated from the [Chinese Version](https://github.com/illuz/show-me-the-code/blob/master/README.md). :smile:)*

#### Description:

- Workbooks for Python, the problems is also apply for other problems.
- [Click the link and you can see the codes for each problems. Welcome to `Pull Request` your codes to the repository. If you have new problems you can paste it here by Gist or Blog.](https://github.com/Show-Me-the-Code/python)
- These workbooks are collected from the Internet by @史江歌 (shijiangge@gmail.com, QQ:499065469) and translated by @illuz (iilluzen@gmail.com).

> Talk is cheap. Show me the code.--Linus Torvalds

----------
 
**# 0000:**
Add a red number to right upper right corner to your profile photo in twitter of facebook, similar to the unread message prompt of somebody.
Like this:

![photo](http://i.imgur.com/sg2dkuY.png?1)


**# 0001:**
As Apple Store App independent developer, you will engage in limited-time promotion. So you should **generate activation codes** (or coupon) for your app. Using Python to generate 200 activation codes (or coupon).


**# 0002:**
Store the activation codes generated in #0001 to **MySQL** relational database.


**# 0003:**
Store the activation codes generated in #0001 to **Redis** non-relational database.


**# 0004:**
Count the number of appeared words in a text file.


**# 0005:**
You have a folder with a lot of photos. Now put them into a size no larger than the size of the iPhone5 resolution.


**# 0006:**
You have a folder full of your txt diaries written last month. Now find out **the key word** (the most important words) of every diary.


**# 0007:**
There is a folder with a lot of your programs. Statistics about how many lines of codes you wrote. Count the blank lines and comments separately.


**# 0008:**
Find out the **body text** in a HTML file.


**# 0009:**
Find out the **links** in a HTML file.


**# 0010:**
Using Python generate **Letters CAPTCHA image** like follow picture.

![CAPTCHA](http://i.imgur.com/aVhbegV.jpg)

- Materials: [Generate A Random Letter in Python](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python) 


**# 0011:**
You have a sensitive words text file 'filtered_words.txt', the content inside is the following. When people input a sensitive word, print `Freedom`, otherwise print out `Human Rights`.
*(The following contains some Chinese words, you can change them into other words as you like)*

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
    jiangge
    illuz


**# 0012:**
Use the 'filtered_words.txt' in #0011. When people input a sensitive word, replace the it into `*`. For example: `I love you.` will turn into `I **** you.`


**# 0013:**
Write a Python program to crawl pictures from [this website :-)](http://tieba.baidu.com/p/2166231880).

- [Reference code](http://www.v2ex.com/t/61686 "Reference code")


**# 0014:**
Plain text file 'student.txt' contains student information, which the content (including braces) are as follows:
*(You can change the Chinese Name as you like)*

    {
        "1":["张三",150,120,100],
        "2":["李四",90,99,95],
        "3":["王五",60,66,68]
    }

Put these content into 'student.xls'. As shown below:

![student.xls](http://i.imgur.com/nPDlpme.jpg)

- Materials: [Reading Parsing Excel XlS Files with Python](http://stackoverflow.com/questions/2942889/reading-parsing-excel-xls-files-with-python)


**# 0015:**
Plain text file 'city.txt' contains city information, which the content (including braces) are as follows:

    {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }

Put these content into 'student.xls' like #0014. As shown below:

![city.xls](http://i.imgur.com/rOHbUzg.png)


**# 0016:**
Plain text file 'numbers.txt' contains city information, which the content (including braces) are as follows:

    [
        [1, 82, 65535], 
        [20, 90, 13],
        [26, 809, 1024]
    ]

Put these content into 'student.xls' like #0014. As shown below:

![numbers.xls](http://i.imgur.com/iuz0Pbv.png)


**# 0017:**
Put the content of 'student.xls' generated in #0014 to XML file 'student.xml'. As shown below:

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <students>
    <!-- 
        学生信息表
        "id" : [名字, 数学, 语文, 英文]
    -->
    {
        "1" : ["张三", 150, 120, 100],
        "2" : ["李四", 90, 99, 95],
        "3" : ["王五", 60, 66, 68]
    }
    </students>
    </root>


**# 0018:**
Put the content of 'city.xls' generated in #0015 to XML file 'city.xml'. As shown below:

    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <citys>
    <!-- 
        城市信息
    -->
    {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }
    </citys>
    </root>

**# 0019:**
Put the content of 'numbers.xls' generated in #0015 to XML file 'numbers.xml'. As shown below:

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <numbers>
    <!-- 
        数字信息
    -->
    
    [
        [1, 82, 65535],
        [20, 90, 13],
        [26, 809, 1024]
    ]
    
    </numbers>
    </root>

**# 0020:**
Statistics 'Call_detail.xls' file using Python.
(I will translate the xls and upload latter.)


**# 0021:**
Generally, logging in a website or APP require a username and pasword. How to encrypt the password before stored? Please use Python to encrypt the password.

- Materials 1: [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)

- Materials 2: [Hashing Strings with Python](http://www.pythoncentral.io/hashing-strings-with-python/)

- Materials 3: [Python's safest method to store and retrieve passwords from a database](http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)


**# 0022:**
iPhone 6 and 6+ is already listed on sale. Check if your code can be reuse on them.


**# 0023:**
Write a web guestbook application using python web framwork. Like shown below.


- Materials 1: [Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)
- Materials 2: [14 Minimal Web Frameworks for Python](http://codecondo.com/14-minimal-web-frameworks-for-python/)

![Reference](http://i.imgur.com/VIyCZ0i.jpg)


**# 0024:**
Make a web todolist application using python web framework. Like shown below.

![SpringSide TodoList](http://i.imgur.com/NEf7zHp.jpg)
