---
title: "Introduction to Jabra+ and the Jabra+ platform"
date: 2025-06-23T13:17:07.745Z
weight: 1
---

#### 1 Introduction to Jabra+ and the Jabra+ platform

Jabra+ is a cloud-based, comprehensive digital ecosystem designed for efficient remote management of Jabra devices, meeting business needs through interconnected digital touchpoints.

Jabra+ starting point is the platform -a multi-tenant Software-as-a-Service (SaaS) platform for IT administrators that centralizes management of Jabra meeting room devices, personal devices and speakerphones, offering features like usage tracking, advanced analytics, and real-time room availability, further providing a global oversight of meeting room device fleets and personal devices.

Every user of the platform is an admin user and is subdivided into owners and members, each with their own set of privileges enabling them to manage, monitor, and integrate devices remotely.

Using locations or device groups, you can group different Jabra meeting rooms or personal devices to sort the virtual inventories as well as create and apply custom or new configurations to specific rooms or device groups.

- - Access and Components Jabra+ : includes Jabra+ for installers and Jabra+ desktop (end-user app). Locally installed client software connects devices to the platform, automatically detecting and adding them to virtual inventories.
- - Device Management : Virtual inventories provide an overview of device models, enabling mass deployments, firmware updates, and settings management. You can group devices using locations or device groups to apply custom configurations. Standardized configurations ensure compliance with corporate policies and provide centralized access to advanced data insights.
- - Data Management : Software clients collect and send device data, usage metrics, and user data to the platform. Real-time data tracking is enabled by default; however, metadata collection can be disabled for privacy. You can also select specific metadata to send.

The platform can be accessed at https://cloud.jabra.com

#### 1.1 How to use this guide

This guide is for an admin user who would like to understand and use all the functionalities in the Jabra+ platform. It begins with a Quick Start Guide (QSG) to get you started with Jabra+ by creating an account, creating an organization, enabling single sign-on (SSO) and/or inviting additional admin users.

After you complete the procedures in the QSG, you must provision Jabra personal and/or meeting room devices into the platform by using the Device Provisioning and Onboarding Guide. Device provisioning can be performed by you, the admin user, or it can be delegated to an external party or Audio-Video installer (AV Installer).

After provisioning the Jabra devices, you can return to this guide to set up the Jabra+ platform, as well as find reference information and procedures on how to manage remotely one or more Jabra devices.

For further information, assistance, or feedback, contact Jabra support.

#### 1.1.1 Other documents

#### · Jabra+ Device Provisioning and Onboarding Guide

For details on how to provision Jabra personal and meeting room devices to the Jabra+ platform, download the Device Provisioning and Onboarding Guide.

#### · Jabra+ Security Framework Guide

For a complete overview of suggested security considerations, including technical information about data storage, architectural overview, and others, you can request the Security Framework Guide from a Jabra representative.

#### 1.1.2 Limitations

Jabra+ is currently limited as follows:

- - The platform user interface supports English-language only

#### · Limited personal devices management

- - End-users cannot adjust settings of their Jabra personal device through the Jabra+ desktop app
- - For personal devices, the following settings are unsupported in all Jabra device models and variants:
  - ▪ Sound profile
  - ▪ Sound Mode
  - ▪ Spatial Sound

#### · Limited meeting room devices management

- - The Jabra PanaCast 40/50 Video Bar System (VBS) All-in-one, and the Jabra PanaCast 40/50 Video Bar System (bar only) do not support the settings lock feature.
- - In the Jabra+ platform, the following settings for the Jabra PanaCast 50 -Bring Your Own Device (BYOD) and Jabra PanaCast 50 Room System (RS) are not available:

| Setting                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Audio notifications and feedback                              | • Enables audio notifications and audio feedback from the Jabra meeting room device                                                                                                                                                                                                                                                                                                      |
| Room safety capacity notifications (type, timing, and limit) | • Enables safety capacity notifications from the Jabra meeting room device  • Selects the type of notifications used if the safety capacity limit is exceeded  • Selects when to notify meeting participants that the safety capacity limit has been exceeded  • Selects how many people are permitted to safely use the meeting room                                                |
| Whiteboard view set up & sharing mode                         | • Sets up a whiteboard view to be shared during a video conference  • Selects how the whiteboard view is shared during a video conference                                                                                                                                                                                                                                                |
| Contrast enhancement                                          | • Content Camera Contrast Enhancement can be switched ON or OFF                                                                                                                                                                                                                                                                                                                        |
| Video transition style                                        | • Selects how the Jabra meeting room device camera transitions between different meeting participants                                                                                                                                                                                                                                                                                    |
| Preset 1 and 2 - Pan, Tilt, Zoom settings                     | • Edits the default Pan Tilt Zoom settings for the camera view. These settings are applied when Preset 1 or 2 are selected                                                                                                                                                                                                                                                     |
| Video flicker                                                 | • To prevent video flicker, select Auto (50Hz/60Hz) for regions that support the PAL video format                                                                                                                                                                                                                                                                                        |
| Product information                                           | • Part number : The stock keeping unit number of the Jabra meeting room device  • Bluetooth MAC address : Device media access control address  • Certified for Microsoft® Teams : Shows whether the Jabra meeting room device is certified for Microsoft® Teams  • Device registration : Registers your Jabra PanaCast 50 device to get security and firmware updates via email |

- - For all Jabra meeting room devices, Whiteboard view setup is not yet available in the platform
- - The platform does not support the Room Insights feature from Jabra Xpress

| - - o Automatic migration of room analytics data is not possible between Jabra Xpress and Jabra+ . An admin user ( owner or member with edit rights ) can export settings and room information from Jabra Xpress to the Jabra+ platform, however this must be done manually.

#### 1.2 Compatibility and migration guide

The Jabra+ platform is compatible with an array of Jabra hardware such as meeting room devices, personal devices (including speakerphones). In certain cases, you can also use the platform alongside other device management systems.

Be aware that using other Jabra software, such as Jabra Xpress or Jabra Direct, together with Jabra+ may inadvertently cause potential conflicts with Jabra hardware.

If you are migrating from Jabra Xpress, see the Migration from Jabra Xpress to Jabra+ section.

#### 1.2.1 Compatibility with other device management systems

See the Device Management System matrix in the Appendix, informing you of potential known issues and offering recommendations when more than one device management system is used at the same time with Jabra+.

#### 1.3 Supported Jabra devices

The list of supported Jabra devices is constantly updated and can be found on the following link.

#### Important note

Certain older Jabra devices' firmware cannot be updated via Jabra+ . Instead, they must be updated using Jabra Direct or Jabra Xpress.

You can still use the older Jabra devices in Jabra+ and change settings, however, depending on the firmware version you are running, the list of settings that you can modify in Jabra+ can change.

To find out whether your device can be firmware updated or not, see the list of supported Jabra devices.

#### 1.4 Browser and security requirements to access Jabra+ platform

To log in to the platform, as a prerequisite, the computer must have the latest versions of the following browsers installed:

- - Google Chrome™
- - Microsoft® Edge

| - - ![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000009_a8f92aec2efd322e45f0afef961018989d1452a564a5967dd621511816fd5ae2.png) |

#### Security requirements -Whitelisted domains and subdomains

For the Jabra+ platform to work as intended, it is recommended that certain outbound TCP ports are open. The following domains, subdomains, and their outbound ports must be accessible.

#### Important note

In the case that your organization does not permit whitelisting domains with a wildcard (*) prefix, refer to the appendix for the specific subdomains.

#### Jabra+ core

| Domain (*= wildcard)                            | Outbound TCP port(s):   | Description                                                                                        |
|-------------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------|
| https://*.cloud.jabra.com/*                     | 443                     | Used to access the Jabra+ platform                                                                   |
| wss://*.cloud.jabra.com/*                       | 443                     | Used by SignalR WebSocket communication layer for responsive UI                                    |
| https://*.azure-devices.net/*                   | 443, 5671               | Used by Jabra devices, the IoT Hub service facilitates communication with Azure Cloud services     |
| https://global.azure-devices-provisioning.net/* | 443                     | Needed for device provisioning, regardless of device type (Headset, Android, or Linux)             |
| https://*.cookiebot.com/*                       | 443                     | Used for collecting consent. If no consent is given, no data is collected                        |

#### Jabra+ images

| Domain (*= wildcard)           | Outbound TCP port(s): | Description                                                           |
|--------------------------------|-------------------------|-----------------------------------------------------------------------|
| https://images.ctfassets.net/* | 443                     | Used by the Content Delivery Network (CDN) for Jabra device images     |

| - - ![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000010_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png) |

#### Jabra+ analytics related

The following domains and subdomains are used for data gathering at Jabra to improve Jabra + user experience, and general system monitoring.

Only anonymized Jabra+ usage details are collected, and it does not include personal information. For details, see the Metadata collection topic.

| Domain (*= wildcard)               | Outbound TCP port(s): | Description                                                      |
|------------------------------------|-------------------------|------------------------------------------------------------------|
| https://content.hotjar.io/*        | 443                     | Used for heatmaps, screen recordings, and feedback collection.   |
| https://*.hotjar.com/*             | 443                     | Used for heatmaps, screen recordings, and feedback collection.   |
| https://www.googletagmanager.com/* | 443                     | Used for in-app event statistics collection.                      |
| https://*.google-analytics.com/*   | 443                     | Used for in-app event statistics collection.                      |
| https://ssl.gstatic.com/*          | 443                     | Used for in-app event statistics collection.                      |
| https://www.google-analytics.com/* | 443                     | Used for in-app event statistics collection.                      |

#### Code signing

All Jabra+ software clients are digitally signed Microsoft Software Installer (*.msi) files, adhering to Microsoft's best practices for enhanced file security, authenticity and code integrity.

When launched, the Installer unpacks dependencies, including digitally signed Dynamic Link Libraries (*.dll files) and executable (*.exe) files.

When dependencies are unpacked, certain file extensions i.e.: *.json, *.version, *.xml, and *.config are not digitally signed, as they do not present a risk to overall security.