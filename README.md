#Twitter bot maker

##Description
Twitter bot maker generate Twitter bot without coding. The bot tweets texts provided by you randomly.

##Usage

0. Access to [Twitter's developer page](https://apps.twitter.com) and get Twitter's `Consumer key` and `Consumer secret`.

1. Clone this repository to local


    $ git clone git@github.com:Rompei/botmaker.git

2. Prepare tweets text file like [this](https://github.com/Rompei/botmaker/test.txt)


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

3. Create a directory you want to generate the bot


    $ mkdir [directory-name]

4. Install [Tweepy](https://github.com/tweepy/tweepy) to use Twitter API.

If you use `pip` as package controll system, execute the command.


    $ pip install tweepy

5. Execute `python makebot.py [path-to-the-text-file-written-tweets] [path-to-the-directory(created at procedure 3)]`

6. Enter `Consumer key` and `Consumer secret`

7. Then give permit for this app.

8. Back to console and input validation code.

9. Files will be generated

That's it.

Then, you can upload generated files to your server and set a scheduler. Here is an example with Heroku.

1. Move to the directory named "bot" generated at procedure 5

2. Initialize Git repository


    $ git init

3. Create Heroku application


    $ heroku create [project name]

4. Push to Heroku


    $ push heroku master

5. Set heroku shceduler


    $ heroku addons:create scheduler:standard
    $ heroku addons:open scheduler:standard

6. Your browser will be opened, then you can set the time to tweet and enter command `python task.py`

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

