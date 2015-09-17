#Twitter bot maker

##Description
Twitter bot maker generate Twitter bot without coding. The bot tweets texts provided by you randomly.

##Environment

Python 3.4.3

##Usage

You can get Twitter bot through [web page](https://botmaker.herokuapp.com) or locally with this app. I suggest using web page because you don't have to install `Tweepy` as your local library.

###Use web


Access to [Twitter's developer page](https://apps.twitter.com) and get Twitter's `Consumer key` and `Consumer secret`.   

Prepare tweets text file like [this](https://github.com/Rompei/Twitter-bot-maker/blob/master/example/test.txt)   

```
    Hello, world
    Go
    Python
    Ruby
    C
    C++
    Java
    JavaScript
    ShellScript
    Tokyo
    Australia
    United Status
    Japan
    Kyoto
    Nara
    にゃんぱすー
```

Access to [Web page](https://botmaker.herokuapp.com) and enter Twitter's `Consumer key` and `Consumer srcret` and upload tweets text file.   
I'm sorry, you will take little time to access the site due to Using Heroku.   


###local use


Access to [Twitter's developer page](https://apps.twitter.com) and get Twitter's `Consumer key` and `Consumer secret`.   

Clone this repository to local     

```
    $ git clone git@github.com:Rompei/Twitter-bot-maker.git
```

Prepare tweets text file like [this](https://github.com/Rompei/Twitter-bot-maker/blob/master/example/test.txt)   

```
    Hello, world
    Go
    Python
    Ruby
    C
    C++
    Java
    JavaScript
    ShellScript
    Tokyo
    Australia
    United Status
    Japan
    Kyoto
    Nara
    にゃんぱすー
```

Create a directory you want to generate the bot  

```
    $ mkdir [directory-name]
```
Install [Tweepy](https://github.com/tweepy/tweepy) to use Twitter API.  

If you use `pip` as package controll system, execute the command.  

```
    $ pip install tweepy
```
Execute `python makebot.py [path-to-the-text-file-written-tweets] [path-to-the-directory(created at procedure 3)]`   

Enter `Consumer key` and `Consumer secret`   

Then give permit for this app.   

Back to console and input validation code.   

Files will be generated   

That's it.   

Then, you can upload generated files to your server and set a scheduler. Here is an example with Heroku.   

###Deploy to Heroku


Move to the directory named "bot" generated at procedure 5   

Initialize Git repository   

```
    $ git init
```

Create Heroku application  

```
    $ heroku create [project name]
```

Push to Heroku  

```
    $ push heroku master
```

Set heroku shceduler  

```
    $ heroku addons:create scheduler:standard
    $ heroku addons:open scheduler:standard
```

Your browser will be opened, then you can set the time to tweet and enter command `python task.py`   

##License

    The MIT License (MIT)

    Copyright (c) 2015 Rompei

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

