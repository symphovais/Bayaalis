---
title: "Introduction to Jabra+ and Jabra+ for admins"
description: ""
date: 2024-11-15T13:50:17Z
draft: false
---

# **1 Introduction to Jabra+ and Jabra+ for admins** 

**Jabra+** is a complete ecosystem of interconnected digital touchpoints, delivering on desired business requirements, and designed to streamline the remote management of Jabra devices.  

One of the main components of **Jabra+** is **Jabra+** for admins – a Software-as-a-Service (SaaS), multi-tenant, cloud-based service that centralizes the management of Jabra meeting room and personal devices within enterprise environments. With **Jabra+**, admin users can manage usage data, device data, APIs, security, and user interactions. 

Accessed through a web interface, **Jabra+** for admins contains features like usage tracking, advanced analytics, and real-time room availability, giving admin users a complete oversight of a fleet of Jabra meeting room and personal devices under their care around the world. 

Every user of **Jabra+** for admins is considered an admin user; however using role management they are divided into *Owners* and *Members*, who can mass manage, monitor, support, and integrate Jabra personal devices (including speakerphones) and meeting room devices remotely, including the creation of inventories of all the managed devices in the business organization.  

**Jabra+** for admins is accessible at the following URL: [https://cloud.jabra.com](https://cloud.jabra.com/) 

Other components of **Jabra+** are **Jabra+** for installers and the **Jabra+** desktop app. 

## **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

![][image1] 

To connect Jabra personal (audio) and meeting room devices to **Jabra+** for admins, the service uses locally installed client software. When the client software is installed on end-user computers, meeting room computers (or ThinkSmart™ Core), the software clients automatically detect new Jabra personal and meeting room devices connected to a computer and adds them to an organization’s virtual **Device inventory** or **Room inventory** for personal or meeting room devices respectively. 

The software clients also collect and send Jabra device data, usage metrics, and user data to **Jabra+** for admins. 

Through virtual inventories, admin users can get an overview of Jabra device models in circulation, enabling them to perform mass deployments, firmware updates, lock end-user settings or select a specific firmware to be used. 

![][image2] 

Using **Locations** or **Device groups**, admin users can group different Jabra meeting room or personal devices to sort the virtual inventories as well as create and apply custom or new configurations to specific Rooms or Device groups. 

Standardized configurations enable admin users to mass deploy and fine-tune settings for a variety of Jabra meeting room and personal devices, ensuring that all Jabra devices comply with corporate policies, and offering a centralized solution to access advanced data insights. 

## **1.1 How to use this guide** 

This guide is for an admin user who would like to configure and remotely manage one or more Jabra meeting room or personal devices in one or more organizations. 

* Chapters 1, 2, 3 enable an admin user with the *Owner* role to understand requirements, get started with **Jabra+** for admins as well as create an organization to lay the foundation for remote management of Jabra meeting room and personal device(s). 

* Chapter 4 contains walkthroughs that enable an admin user to quickly get started with managing Jabra meeting room and personal devices by provisioning and adding them to the relevant inventory in **Jabra+** for admins. 

* Chapters 5,6,7 and 8 provides further guidance, conceptual information, and procedures about each **Jabra+** for admins component (i.e., Software clients, Dashboard, Configurations etc.), helping admin users discover and understand the capabilities of **Jabra+** for admins. 

* Chapter 9 contains an Appendix & Troubleshooting section. **1.1.1 Limitations of this release** This release is limited as follows: 

* **Limited Personal devices management** o Personal device management is in *Beta* state for testing and compatible Jabra personal devices can be provisioned to **Jabra+** for admins at your own risk. o End-users cannot change settings through the **Jabra+** desktop app 

* **Limited Meeting room devices management** o The Jabra PanaCast 50 VBS (P50 VBS) meeting room device does not support the settings locking feature.  

* **Limited Jabra device support and connection options** o For personal devices, the following settings are unsupported in all Jabra device models and variants: 

  * Sound profile 

    * Sound Mode 

    * Spatial Sound o In **Jabra+** for admins, the following settings for P50 BYOD and P50 RS are not available: 

| Setting  |  | Description  |
| ----- | ----- | :---- |
| Audio notifications and feedback  | •  | Enable audio notifications and audio feedback from the Jabra meeting room device  |
| *Room safety capacity notifications (type, timing, and limit)*  | •  | Enable safety capacity notifications from the Jabra meeting room device  |
|  | •  | Select the type of notifications used  if the safety capacity limit is exceeded  |
|  | •  | Select when to notify meeting participants that the safety capacity limit has been exceeded  |
|  | •  | Select how many people are permitted to safely use the meeting room  |
| *Whiteboard view set up & sharing mode*  | •  | Set up a whiteboard view to be shared during a video conference  |
|  | •  | Select how the whiteboard view is shared during a video conference  |
| *Contrast enhancement*  | •  | Content Camera Contrast  Enhancement can be switched ON  |
|  |  | or OFF  |
| *Video transition style*   | •  | Select how the Jabra meeting room device camera transitions between different meeting participants  |
| *Preset 1 and 2 – Pan, Tilt, Zoom settings*  | •  | Edit the default *Pan*, *Tilt*, *Zoom* settings for the camera view. These settings are applied when Preset 1 or 2 is selected  |
| *Video flicker*  | •  | To prevent video flicker, select *Auto*  (50Hz/60Hz) for regions that support  PAL video format  |
| *Product information*    | •  | **Part number**: The stock keeping unit number of the Jabra meeting room device  |
|  | •  | **Bluetooth MAC address**: Device media access control address  |
|  | •  | **Certified for Microsoft Teams**: Shows whether or not the Jabra meeting room device is certified for Microsoft Teams  |
|  | •  | **Device registration**: Register your Jabra PanaCast 50 BYOD device to get security and firmware updates via email  |
| *People count*  | •  | The camera periodically counts the number of people in the meeting room  |
| *People count LED*  | •  | The camera LED blinks to indicate that the camera is counting people in the meeting room  |

* For all Jabra meeting room devices (i.e.: P50 BYOD, RS, VBS), **Whiteboard view** **setup** and **Intelligent Meeting Space** **setup** is not yet available in **Jabra+** for admins. 

  * Wi-Fi provisioning is not available on the Jabra P50 VBS meeting room device, and it must be performed using a cabled Ethernet connection.  

  * Automatic migration of room analytics data is not possible between Jabra Xpress and **Jabra+** for admins. An admin user (*Owner* or *Member with edit rights*) can export settings and room information from Jabra Xpress to **Jabra+** for admins. This must be done manually. See the Migration from Jabra Xpress to Jabra+ for admins section. 

  * **Jabra+** for admins does not currently support the **Room Insights** feature from 

  Jabra Xpress o **Jabra+** for admins´ user interface supports U.S. English only. 

## **1.2 Compatibility and migration guide** 

**Jabra+** for admins is compatible with an array of Jabra hardware such as meeting room devices, personal devices (including speakerphones). In certain cases, **Jabra+** for admins can be used alongside other device management systems. 

Be aware that using other Jabra software, such as Jabra Xpress or Jabra Direct, may inadvertently cause potential conflicts with Jabra hardware and **Jabra+** for admins. 

Regarding migration, it is possible to use other device management systems, however there are a few caveats. If you are migrating from Jabra Xpress, see the Migration from Jabra Xpress to Jabra+ for admins topic. 

### **1.2.1 Compatibility with other device management systems** 

The following table informs admin users of potential known issues and offers recommendations when more than one system is used at the same time with **Jabra+** for admins. 

**Device Management System matrix** 

| Device  Management System  | Potential issues  | Recommendation  |
| :---- | :---- | :---- |
| Jabra Xpress  | When using both systems at the same time, duplicate device management can cause a conflict.  | Not recommended. Avoid using **Jabra+** for admins and Jabra Xpress at the same time.  For more information, see the Migration from Jabra Xpress to Jabra+ for admins topic.  |
| Jabra Direct  | Using both systems simultaneously can cause device management  conflicts, except during initial setup for Jabra meeting room devices or when using older Jabra personal devices.    **Exception for Meeting room devices**  Setting up Whiteboard view and Intelligent Meeting Space in **Jabra+** for admins. For more information and procedures see the Jabra meeting room device [documentation](https://www.jabra.com/support) for guidance.    **Exception for Personal devices** Updating firmware of older Jabra personal devices using Jabra Direct or Jabra Xpress.  | Not recommended. Avoid using **Jabra+** for admins and Jabra Direct at the same time.    **For Meeting room devices**:  Ensure that after setting up  *Whiteboard view* and *Intelligent Meeting Space* in Jabra Direct, close, exit, or uninstall Jabra Direct and continue using **Jabra+** for admins only.    **For Personal devices**:  After updating, uninstall Jabra Direct and use the **Jabra+** desktop app. (See Supported Jabra devices chapter).  |
| Lenovo ThinkSmart™  Manager (basic \+ premium)  | When using both systems at the same time, duplicate device management can cause a conflict and settings can be overwritten.  | Not recommended. Avoid using  **Jabra+** for admins and Lenovo ThinkSmart™ Manager at the same time.  |
| Zoom Device  Management (Firmware management only)  | Managing device firmware on both device management systems is not recommended.      | Choose **Jabra+** for admins as the primary firmware management platform instead of Zoom Device Management.    If firmware must be managed  |

|  |  | using Zoom's Device  Management instead of Jabra+ for admins, ensure the firmware policy is disabled in Jabra+ for admins.  See the Firmware Policy chapter for the procedure.  |
| :---- | :---- | :---- |
| Microsoft Teams  Pro Manager  Portal  | Both device management systems can run at the same time.    No known conflicts exist.  | Ensure **Jabra+** for admins and  Microsoft Teams Pro Manager Portal are set up/configured to avoid conflicts.  |
| Windows Update (Firmware management only)  | Firmware management can be handled side by side only if one of the two firmware management systems is disabled. Either disable it in **Jabra+** for admins, or pause Windows Updates.    **Note**  If the organization has Jabra PanaCast 50 RS, VBS or BYOD meeting room devices, an *Owner* or *Member with edit rights* (for meeting rooms) must choose whether to firmware manage through Windows Update or through **Jabra+** for admins.  | To keep a fixed firmware version on Jabra PanaCast 50 RS, VBS or BYOD, then disable the **Always keep devices updated** toggle switch in **Jabra+** for admins and pause Windows Updates. To do this, see the Setting an existing firmware policy for specific Jabra device models procedure in the  Firmware Policy chapter.  |
| Crestron XiO Cloud  | When using both systems at the same time, duplicate device management can cause a conflict.  | Not recommended. Avoid using **Jabra+** for admins and XiO Cloud together.  |

### **1.2.2 Supported Jabra devices** 

#### **Note** 

**Jabra+** development is ongoing, and more Jabra personal and meeting room devices are continuously added as supported devices. Contact a Jabra representative to get the most updated list. 

## **Jabra personal devices** 

The following table shows the Jabra personal (audio) devices that are currently compatible with **Jabra+** for admins.   
![][image3]

## **Jabra meeting room devices** 

* Jabra PanaCast 50 Bring Your Own Device (BYOD)   
* Jabra PanaCast 50 Room System (RS) – with Lenovo® ThinkSmart™ Core and ThinkSmart™ Controller / Touch Controller (Computing device and display) 

* Jabra PanaCast 50 Video Bar System (VBS) All-in-one – with Jabra PanaCast Control (Touchscreen tablet)
