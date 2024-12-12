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

I am a big fan of interfaces in an object-oriented language like C#. I have been utilizing dependency injection (IoC) in most of my previous projects, which means my model often includes many interfaces. I always try to invest some time in naming my model elements, be it the names of interfaces, classes, methods, or even the variables.

When I review code written by others, one recurring observation is the naming conventions they choose for their model elements. Recently, while diving into **NServiceBus**, I noticed not just the sheer brilliance of its design but also the unique approach to interface naming. For example, names like `IHandleMessages` and `IContainSagaData` stood out to me. This approach differs from my usual convention, where I might name something `IMessageHandler`. 

The way **NServiceBus** names its interfaces resonates more naturally. It feels almost conversational when you think of a class as "My name is MessageHandler" instead of just labeling it as a handler. Intrigued by this naming style, I decided to give it a try in one of my projects.

Starting with repositories, I shifted to titles like `IStoreData` instead of the usual, somewhat bland `IRepository`. I also opted for `IStoreDataInSql` and even named one `IStoreStatistics`. Moving on to application controllers, where service interfaces are typically named `IStatisticsService` or `IConfigurationService`, I creatively rebranded them into `ILogStatistics`, `IManageSiteSurveyConfiguration`, and `INotifyToExecuteAction`. 

While some names reverted to the more traditional style—like `IProvideThis` and `IHandleThat`—others became quite engaging, such as `INotifyWhenSiteSurveyConfigurationChanges` and `INotifyToExecuteAction`. 

Overall, experimenting with naming conventions has been a worthwhile endeavor. It's not just about following established norms; it's about making the code more understandable and approachable. Embracing a little whimsy in naming can breathe new life into the way we think about code, ultimately enhancing collaboration among developers.
