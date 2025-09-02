---
title: "A Few Thoughts on Building Software"
description: ""
summary: ""
date: 2025-09-01T00:00:00Z
lastmod: 2025-09-01T00:00:00Z
draft: false
weight: 50
categories: []
tags: []
contributors: []
pinned: false
homepage: false
featuredImage: "https://images.ctfassets.net/slui2y4fqnvv/34IlsD9jWGg6vRLno1BS6v/854c97bfb4cf6bfe7a3332b569b1e445/Gemini_Generated_Image_scv0scscv0scscv0.png"
seo:
  title: "" # custom title (optional)
  description: "" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  robots: "" # custom robot tags (optional)
---

After spending a good number of years in the tech industry, you start to see patterns. You see what works, what doesn't, and what just seems to get in the way. The other day, I sat down and jotted down some of the simple, guiding principles that I've found myself coming back to time and again.

None of this is revolutionary, and it’s certainly not a complete list of everything that matters. It’s just a handful of ideas that I’ve learned—often the hard way—help teams ship good work without getting tangled up in complexity. Maybe they'll be useful to you, too.

#### It's All About the Actual Product

This sounds obvious, but it's amazing how easily it gets forgotten.

* **Build for a specific product, not the shelf.** I’ve seen so much time spent on "groundwork" for frameworks that never get used. My rule of thumb now is that every piece of work should directly help a shippable product. If it doesn't, I get very suspicious. Refactoring is great, but it’s best done after you’ve actually delivered something.
* **Small wins are better than big promises.** It’s tempting to go after the huge, game-changing feature. But I've found that momentum and feedback are more valuable. Shipping small, useful bits of functionality keeps the team energized and allows you to learn from real users, which is always better than guessing.
* **When in doubt, pick the simpler path.** Overengineering is a trap. The simplest solution that gets the job done is almost always the right place to start. You can add complexity later if you really need it. I guess you could call it a personal Occam's Razor for coding.

#### How You Work Matters as Much as What You Work On

Having good habits around the process makes a huge difference.

* **Try things and be ready to be wrong.** The goal is to learn as fast as possible. That means building a quick version of an idea and getting it in front of people. If it works, great. If it doesn't, you found out quickly and cheaply. Speed of iteration beats polish in the early days.
* **Know how you'll measure success.** It’s a good idea to ask "how do we know if this is working?" before you build something. Having some simple metrics helps you make objective decisions about what to keep and what to retire. If something isn't making a difference, it's okay to let it go.
* **Demos should be about user value.** I’ve always found that the most effective sprint demos are the ones that only show things a customer would actually see or experience. It keeps everyone focused on the real goal: making things better for the end user.

#### A Few Notes on Engineering

Finally, here are a couple of technical principles I try to stick to.

* **Use the tools, but own the work.** GenAI tools are incredible for speeding things up. I think we should use them as much as possible. But at the end of the day, the developer shipping the code is accountable. You still have to understand and own every line.
* **If you can't test it, it's probably designed wrong.** This is a big one for me. If a piece of functionality is a nightmare to write an automated test for, it's usually a sign that the design is too complicated. Thinking about testability from the start leads to better, more reliable code.
* **Keep dependencies light.** Designing around clean interfaces and using sample data to get started can be a lifesaver. It lets people work without constantly being blocked by other teams or services. The fewer moving parts you're tied to, the faster you can go.

So, that's it. Just a few notes from my experience. I'm sure there are plenty of other things that matter, but these are the ones that were on my mind. Hope they're helpful.
