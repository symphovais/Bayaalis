---
title: "Blast from the Past:  Embracing Interface Naming in C# Development"
description: ""
summary: ""
date: 2024-05-05T00:00:00Z
lastmod: 2024-05-05T00:00:00Z
draft: false
weight: 50
categories: []
tags: []
contributors: []
pinned: false
homepage: false
featuredImage: ""
seo:
  title: "" # custom title (optional)
  description: "" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  robots: "" # custom robot tags (optional)
---

Allow me to reintroduce a blog post from my archives, penned during my days as a software architect. Titled "My Name is Ovais and ICodeInCSharp, IDoPhotography, IWriteBlogs," this piece delves into the fascinating world of object-oriented programming, focusing on the art of naming model elements in C#. In this exploration, I share insights garnered from my experiences with dependency injection (IoC) and the profound impact it has had on my projects. The post highlights a pivotal moment during my foray into NServiceBus, where unconventional interface naming sparked a newfound curiosity. Without further ado, I present to you the original blog post, unaltered and as insightful as ever: I am a big fan of interfaces in a object oriented language like C#. I have been using dependency injection (IoC) in most of my previous projects and using DI your model contains many interfaces. I always try to spend some time in naming my model elements be it the name of interfaces, classes, methods or even the variables. When I look at code by other people one thing I usually notice is how they are naming their model elements. Some days back I was looking into NServiceBus the things I noticed while doing that other than shear brilliance was the way different interfaces were named. for example IHandleMessages or IContainSagaData. This was a bit different way of naming then what I usually use as normally I would use something like IMessageHandler. I thought this is an interesting way of naming something like a class is saving my Name is MessageHandler and I Handle Messages. Sounds more natural more understandable. I thought I should give this way of naming a try. In one of my projects, I tried to use similar naming. The first place I need to create Interfaces are the repositories. So I started with names like IStoreData (instead of IRepository sounds boring doesn’t it?), IStoreDataInSql and went on and making names like IStoreStatistics. Next place was the application controller where normally the interfaces for the services are named as IStatisticsService or IConfigurationService etc the names now became a bit different i.e. ILogStatistics, IManageSiteSurveryConfiguration, INotifyToExecuteAction INotifyWhenSiteSurveyConfigurationChanges. Thought it was fun way of naming interfaces in some cases it become as stagnant as the old approach like IProvideThis and IHandleThat but in some cases the names become very interesting like INotifyWhenSiteSurveyConfigurationChanges and INotifyToExecuteAction.
