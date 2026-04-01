---
title: "Your Requirements Document Is Already Wrong"
description: ""
summary: ""
date: 2026-03-31T00:00:00Z
lastmod: 2026-03-31T00:00:00Z
draft: false
weight: 50
categories: []
tags: []
contributors: []
pinned: false
homepage: false
featuredImage: "https://images.ctfassets.net/slui2y4fqnvv/R9y2JOfaNViOfWb3smblU/f043bb6d9c313830b83f03be558fff15/ChatGPT_Image_Apr_1__2026__10_06_33_AM.png"
seo:
  title: "" # custom title (optional)
  description: "" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  robots: "" # custom robot tags (optional)
---

We were having an internal discussion about one of our systems when someone said, "the problem is we don't have requirements documented anywhere."

"What about the backlog? The epics, the features, the acceptance criteria?" I asked.

"Yes, but we don't have a *requirements document*. Something that tells us how the system actually works."

That single exchange has stayed with me. Not because the question was wrong, but because of the assumption behind it. That requirements need to live in a specific artifact, separate from the work, maintained alongside the code, to count as real.

I think that assumption is worth challenging.

## Let's go back to first principles

Think about everything we have done in software over the decades. The design patterns. The architectural principles. The endless debates about how to structure, organise, and express our systems. Gang of Four. Microservices. Dependency injection. Clean architecture. SOLID principles.

If you had to distil all of it, every pattern, every principle, every best practice, into a single sentence, what would it be?

I think it comes down to this: *do one thing, in one place, and do it really well.*

That's it. That's the philosophy underneath all of it. We don't want logic duplicated across ten services. We don't want business rules scattered across layers. We don't want the same concept expressed in two different places that can drift apart. Everything we build is, at its core, an attempt to find the right home for each piece of truth and then reference it everywhere else.

We apply this instinct ruthlessly when we write code.

And then we open a Word document and forget everything we know.

## Requirements have a lifecycle

So let's talk about requirements. What are they, really?

They are an input. A statement of work. Before you build something, you need to capture the intent: what needs to be done, why it matters, and how you'll know it's done. That's a legitimate and necessary artifact. It has a job to do.

And in modern software development, that job is already being done in your backlog. Your epics describe the problem space. Your features break it into deliverable chunks. Your acceptance criteria defines exactly what done looks like. That *is* your requirements document. It just doesn't have that label on it.

But here is the important part, and this is what I think most teams miss.

Requirements have a lifecycle. They don't live forever. They serve their purpose at the start, guiding what needs to be built. But the moment a feature is closed, the code is written, the tests are passing, the acceptance criteria has been met, something shifts. The backlog item doesn't disappear, but its role changes. It becomes a reference. A record of the original intent. The source of truth has moved somewhere else.

The question is: where did it go?

## Where did the truth go?

It went into the code.

More specifically, it went into the tests.

Think about what a test actually is. It's not just a quality check. It's a precise, executable expression of intent. It says: *given this input, this is what the system must do.* It captures the acceptance criteria not as a description written by a human, but as a verification run by a machine. It can't be vague. It can't be open to interpretation. And critically, it can't lie. If the code drifts from the original intent, the test breaks. Immediately. Loudly. Traceably.

Now think about what sits underneath all of this: your version control history. Every feature connected to a commit. Every change recorded with who made it, when, and why. A complete, unbroken timeline of how the system evolved from day one. Not a snapshot. Not a summary. The full picture.

No requirements document has ever come close to that level of fidelity. You would have to work incredibly hard, and continuously, to manually maintain something that git gives you automatically, as a byproduct of simply doing the work.

This is the source of truth. It was always going to end up here.

## But what about compliance?

That said, does this mean we never need system behaviour expressed in a document at all?

It's a fair question. Compliance is probably the first use case that comes to mind. In regulated industries like medical devices, hardware, and safety-critical systems, external auditors need to see that your system does what you specified. They need a traceable history of every change. They need documentation they can review, sign off on, and file.

But let's look at what compliance actually demands: your system does what it says it does, you can prove it, and you have a full record of everything that has changed since the beginning.

Isn't that exactly what good engineering already gives you? Features connected to commits. Tests that verify acceptance criteria. A git history going back to day one, showing every decision, every change, every evolution of the system. That's not just as good as a compliance document. It's more accurate, more complete, and always current.

## So why did we create requirements documents in the first place?

Because non-technical stakeholders couldn't read code. So we built a translation layer. We wrote prose, called it documentation, maintained it manually, watched it drift, and then created more of it.

It was always a workaround. We just didn't have anything better.

That is what has changed.

AI can now read your code, your tests, your commit history and explain it to anyone, in whatever form they need, at whatever level of detail makes sense for their context. A product manager asking how a feature behaves. A compliance auditor needing a traceability report. An executive wanting a plain language summary of what shipped last quarter. The same source of truth, interpreted in real time, for any audience.

The translation problem is solved. The workaround is no longer necessary. And for compliance specifically, you don't need to maintain a separate document for auditors. You need good engineering practices and an agent that can generate whatever report they need, on demand, from the only source of truth that was ever really accurate.

## But what about architecture docs?

Another fair question. And here there is a distinction worth making.

There is a difference between documentation that *describes* what already exists and documentation that *prescribes* what to do next. The first kind is where rot sets in. Someone reads the code, writes down what they think it does, and from that moment the clock is ticking. The second kind guides rather than mirrors. Architecture guidelines, engineering conventions, patterns and principles that shape how new code gets written. These are forward-looking. They have a job to do that the code itself cannot do, and they are worth maintaining.

Most requirements documents, if you look at them closely, fall into the first category. They're someone's interpretation of what the system does, expressed in prose. That's precisely where the drift begins.

How we create and interact with even these forward-looking documents is itself starting to change, but that's a conversation for another day.

## The tools are here. The excuse is gone.

The source of truth in software has always been the code. We knew this. We just kept building workarounds because we didn't have the tools to make it legible to everyone who needed to understand it. Requirements documents, system descriptions, behaviour specifications: they were our best attempt at bridging that gap.

But here is the thing about workarounds. When the underlying problem is solved, they don't become best practices. They become unnecessary overhead.

What's left is simply good engineering, the kind we always knew mattered. Meaningful commits. Excellent test coverage. Every feature connected to a statement of work. A codebase that expresses intent clearly enough that any question about what the system does can be answered directly from it.

We didn't need AI to tell us that was the right way to work. We always knew. We just finally have the tools to make it enough.
