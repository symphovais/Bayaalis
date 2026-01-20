---
title: "Engineering TalkKeys: Porting to macOS with .NET 9 and Avalonia"
description: ""
summary: ""
date: 2026-01-19T00:00:00Z
lastmod: 2026-01-19T00:00:00Z
draft: false
weight: 50
categories: []
tags: []
contributors: []
pinned: false
homepage: false
featuredImage: "https://images.ctfassets.net/slui2y4fqnvv/6CQ3BlIqArUr9LWguHtjD2/f4de7d410741ebba2fa1d6c6bb376756/Gemini_Generated_Image_5hfuhp5hfuhp5hfu.png"
seo:
  title: "" # custom title (optional)
  description: "" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  robots: "" # custom robot tags (optional)
---

I recently reached a major milestone for TalkKeys: the official release of the macOS version.

Moving from a Windows-only WPF application to a cross-platform architecture required more than just a new UI. It required a complete decoupling of the system-level "muscles" from the application's "brain." Here is how I approached the architecture and why I’m currently maintaining two separate UI paths.

## The Strategy: "Dual-Track" Development

I made a strategic decision not to replace the Windows WPF version immediately. The WPF app is mature and currently holds a broader feature set. Instead of rushing a replacement, I am running a **Dual-Track** approach:

1. **TalkKeys.Avalonia:** Powers the new macOS version and serves as the future cross-platform foundation.
2. **HotkeyPaster (WPF):** Remains the primary Windows experience until the Avalonia version hits feature parity.

By sharing the **Core** and **ViewModel** projects across both, I can fix bugs and improve logic once, and have those improvements reflect on both platforms simultaneously.

---

## Technical Architecture

To make the app truly platform-agnostic, I relied heavily on interface-based abstraction within `TalkKeys.Core`. The UI never talks to the hardware; it only talks to interfaces.

### 1. Swapping System Services

Because macOS and Windows handle low-level input and audio differently, I implemented platform-specific libraries that are swapped at runtime via Dependency Injection:

| Service | Windows Implementation | macOS Implementation |
| --- | --- | --- |
| **Global Hotkeys** | H.Hooks | SharpHook |
| **Input Simulation** | H.InputSimulator | SharpHook |
| **Audio Capture** | NAudio | PortAudio |
| **Notifications** | Microsoft.Toolkit.Uwp | Native macOS (Foundation) |
| **Secure Storage** | Windows Credentials | macOS Keychain |

### 2. Deepgram Flux Integration

A major addition to this release is support for **Deepgram Flux**. By moving to a streaming-first approach, TalkKeys now achieves millisecond-latency transcription.

Using Flux’s features, I've implemented **hands-free completion**. The service detects the end of speech with high precision, allowing the app to automatically stop recording and simulate the text input (the "paste" action) without the user needing to trigger a second hotkey. This drastically reduces the friction of voice-to-text workflows.

---

## Implementation Details

In the Avalonia project, I use conditional MSBuild properties to ensure that macOS-specific dependencies like `PortAudioSharp2` are only included when building for that target.

```xml
<ItemGroup Condition="$([MSBuild]::IsOSPlatform('OSX'))">
    <ProjectReference Include="..\TalkKeys.Platform.macOS\TalkKeys.Platform.macOS.csproj" />
</ItemGroup>

```

At runtime, the `App.axaml.cs` handles the service registration:

```csharp
if (OperatingSystem.IsMacOS())
{
    services.AddSingleton<IAudioRecordingService, PortAudioRecordingService>();
    services.AddSingleton<IHotkeyService, SharpHookHotkeyService>();
    // ... other macOS services
}

```

## Moving Forward

The foundation is now in place. With .NET 9 and a decoupled architecture, I can iterate on the transcription engine and the UI independently. Once the Avalonia version achieves full parity with the WPF features, I will plan the retirement of the WPF-specific project to move to a single, unified codebase.

**Check out the project here:** [talkkeys.symphonytek.dk](https://talkkeys.symphonytek.dk/)
