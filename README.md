LetflySite
=========

Source code to letflysite.com
Due to no money, the site has been moved to [LETFLY'S LAB](http://blog.csdn.net/u012332571)


### Introduction

LetflySite is a personal website of personal interest and study practice. The website is developed using the django framework, which mainly includes blogs and pictures.

### Features

* Account: register, login, change password, reset the password by mail, register by email, etc.
* Blog: include tags, categories, rss feeds, searches, and more. To facilitate editing, but also embedded in the UEditor (baidu rich text editor).
* Image: currently only supports the most basic browsing.
* Interest: currently only supports the most basic browsing.
* Other: on with feedback, mail queue, picture processing, paging function and so on.

### Use a third party package

* Django-simple-captcha: a verification code module.
* Django Ueditor: baidu rich text editor. In order to meet the individual needs, the View has been recustomized.

### Currently imperfect function and known bugs

* Account: registration, password modification, password reset, etc. Not completed.
* Ueditor: upload images such as rewrite the view does not consider the path after the incoming.
* Mail: invitation email is not delivered.

### Copyright on LetflySite - UI

As a non-design born for me, making a decent UI is not easy for me, so I personally keep the copyright on the UI.Thanks!
