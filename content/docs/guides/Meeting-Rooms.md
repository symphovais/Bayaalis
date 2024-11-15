---
title: "Meeting Rooms"
description: ""
date: 2024-11-15T13:57:06Z
draft: false
---

# **6 Meeting Rooms** 

In **Jabra+** for admins, **Meeting rooms** lets admin users digitally visualize, sort, and manage Jabra meeting room devices, effectively mapping physical meeting rooms used for online meetings and creating an organizational structure. 

## **Note** 

To migrate your meeting rooms from Jabra Xpress into **Jabra+** for admins, refer to the Migrating from Jabra Xpress topic. 

Meeting rooms address the challenges of remote identification, management, and troubleshooting of Jabra meeting room devices. An admin user (*Owner* or *Member with edit rights* for meeting rooms) can perform bulk management of settings and firmware, inspect real-time Jabra meeting room device status, reboot Jabra meeting room devices for troubleshooting, access activity logs for each meeting room, and other functionalities. 

Similar to personal devices, Jabra meeting room devices have a virtual inventory, called Room inventory. The **Meeting rooms** menu item is made up of the Room inventory, Room configurations, and Room clients. 

During provisioning, an admin user (or an AV installer) names the virtual room where the Jabra meeting room device is located, aiding identification in the **Room inventory** before moving it to a Location. The room name can also be renamed at any time. 

## **Tip** 

For P50 BYOD and P50 VBS, the room name is linked to the provisioned device name. For P50 RS, the meeting room computer name automatically appears as the room name in **Jabra+** for admins. It is recommended for the admin user to rename the meeting room computer to match the physical room name. 

After provisioning your Jabra meeting room devices and naming them, they appear in the **Room inventory** as an *unassigned room.* Admin users can then drag and drop these rooms into predetermined Locations, which serve as a grouping mechanism, similar to Device groups (for personal devices). This is designed to hierarchically group or organize Jabra meeting room devices based on real or made-up locations like, countries, cities, buildings, departments, rooms, or others. 

The following is an example of a tree structure within Locations. 

**Your Organization** (*root of tree structure*) o **United States** (*Parent*) 

	▪ 	**California** (*Child*) 

	• 	**Cupertino** **office** (*Child*) 

To keep Jabra meeting room devices updated with the latest firmware while minimizing disruptions for end users, admin users can modify scheduled device updates according to the organization’s working hours. For example, updates can be scheduled to take place at night. 

Clicking on a Jabra meeting room device in the **Room inventory** opens the **Room** page, displaying details such as *Room Type*, *Location*, *Software client*, and if applicable, *Room AV system*, *Video Service Provider*, and *Meeting room computer* or computing device information, among others. 

## **Note** 

The *Video Service Provider* pane is displayed only in Rooms with a Jabra PanaCast 50 Video Bar System (P50 VBS). Changing the video service provider between Microsoft® Teams Rooms and Zoom Rooms requires re-provisioning the affected P50 VBS. 

## **6.1 Room inventory for meeting room devices** 

The **Room inventory** is a repository or bucket for all Jabra meeting room devices added to a specific organization in the **Jabra+** for admins, similar to the Device inventory for personal devices. 

The Room inventory enables you to set up a structure to organize your meeting rooms and Jabra devices in your business organization, showing you a real-time overview of your meeting room devices. Be aware that you can only have one Room inventory per organization. All Jabra meeting room devices connected to the **Meeting room client** created from the same organization appear in the **Room inventory**. 

Through the **Room inventory**, you can also remove individual meeting room devices, or you can also delete the entire room, removing any Jabra meeting room device within it. 

### **Note** 

There are different procedures to remove Jabra meeting room devices from **Jabra+** for admins. See the Deleting a room or removing a meeting room device from a room topic for procedures. 

In a searchable and filterable list – the inventory outlines information such as *Room*, *Room Status*, *Location*, *Devices*, *Seat Count*, *Configuration*, and *Firmware* *Status*, all in real time. 

In the Room inventory, Jabra meeting room devices are first automatically sorted into **Rooms** (a primary grouping), and rooms can be further sorted into **Locations**, enabling you to create a secondary grouping for your rooms. For example, you can group rooms into different regions, countries, offices, and others, effectively building a hierarchical structure based on geography. 

When Jabra meeting room devices are added to the Room inventory – and to mass manage meeting room devices with a shared firmware policy and settings – a default **Standard Room** configuration is applied across the board to all Jabra meeting room devices in the **Room inventory**. 

See Standard Room configuration for further details. 

### **6.1.1 Assigning or moving a room into a location** 

To perform this procedure, you must first have created one or more locations in your Room inventory. See the Moving rooms into locations and adding room details topic. 

### **6.1.2 Renaming a room** 

After provisioning a Jabra meeting room device, an admin user with the relevant permissions can choose to rename the room, when required. 

To rename a room: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room** **inventory**   
2. On the Room inventory list, click the relevant room name   
3. In the **Room** page, on the top right-hand side of the page, click the action menu (three-dot menu) and click **Edit room**   
4. Rename the room as desired and click **Save changes** to confirm 

### **6.1.3 Deleting a room or removing a meeting room device from a room** 

In **Jabra+** for admins, an *Owner* or *Member* *with edit rights* (for meeting rooms) can delete rooms from the **Room inventory** as well as remove a Jabra meeting room device from within a room. 

Be aware that when you remove a room from the Room inventory, you delete all Jabra meeting room devices within the room. 

Depending on the Jabra meeting room device – and to permanently delete the room – you must ensure that after removing a room or meeting room device from the Room inventory, that you also remove the software client from the meeting room computer it was installed on. 

Otherwise, when the meeting room computer is restarted, the Jabra meeting room device is automatically re-added to the Room inventory as an *unassigned room*. 

In the Room inventory, when you remove a single meeting room device from the room (i.e.: the structure created when the meeting room device was added to **Jabra+** for admins) the room itself remains empty within the Room inventory, ready to have a meeting room device provisioned to the inventory. 

#### **Note** 

An exception applies in the case of the Jabra PanaCast 50 BYOD, whereby if you delete the meeting room device from the **Room inventory**, you also delete the associated room. 

To remove a Jabra meeting room device from the Room inventory, you must first ensure the *Device status* appears as O*ffline* before removing it. 

To do this, ensure that you unplug the Jabra meeting room device from the power outlet and wait a few minutes for the *Device status* to appear as *Offline*. You can then perform the following procedure: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room** **inventory**   
2. On the Room inventory list, click the relevant room name   
3. On the **Room** page, click the action menu (three-dot menu) in the meeting room or personal device you want to remove and click **Remove device** 

   a. To remove the room entirely, including all the Jabra meeting room and personal devices within the room, on the top right-hand side of the page, click the action menu (three-dot menu) and click **Delete room**. 

| Important note  To permanently delete a room or Jabra meeting room device from a room, ensure that after you delete the meeting room device, you also delete the meeting room clients whenever possible.  Depending on the Jabra meeting room device, the client removal must be performed differently, and as follows:  Jabra PanaCast 50 BYOD: After the meeting room device has been deleted from a room, or a room has been deleted, the PanaCast 50 BYOD is removed. To re-add the meeting room device to Jabra+ for admins you must re-provision it.  Jabra PanaCast 50 RS: After the meeting room device has been deleted from a room or a room has been deleted, you must switch the PanaCast 50 RS OFF, and the USB cable must be unplugged. To re-add the meeting room device to Jabra+ for admins, you must reinstall the meeting room client.  Jabra PanaCast 50 VBS: After the meeting room device has been deleted from a room or a room has been deleted, the PanaCast 50 VBS is removed. To re-add the meeting room device to Jabra+ for admins you must factory reset it and then re-provision the meeting room device.  Failure to remove the clients can result in the Jabra meeting room device being detected by Jabra+ for admins again and reappearing in the Room inventory.  |
| :---- |

### **6.1.4 Room configurations** 

When you add a meeting room device to the **Room inventory**, **Jabra+** for admins automatically assigns a **Standard Room** **Configuration**. 

For room configurations (conceptual topic and procedures), see the Room configurations for meeting room devices topic. 

## **6.2 Activity logs – Device details and meeting room activity** 

Activity logs consist of device details and meeting room activities, allowing you to view information about Jabra meeting room devices and events in physical rooms. 

From the **Room Inventory**, clicking a room name shows a timeline of activities related to that room and its associated meeting room devices. The **Activity** tab on each device's **Room** page lists events such as reboots, status changes, firmware updates, and errors. 

Logs maintain a record of activities for the past 30 days, displayed in a searchable and filterable format, including **Events** in the room and their triggers (e.g., configuration changes or device additions/removals). 

The **Activity** tab also shows the exact time of events, and the serial number of the device involved. For example, if an admin user renames a room, this action is logged. 

Viewing additional **Details** and **Activity** aid troubleshooting by helping you identify the origin of issues, track actions, and resolve problems, such as rebooting the Jabra meeting room device. 

### **6.2.1 Viewing Jabra meeting room device details** 

When a Jabra meeting room device is added to the Room inventory, you can see information such as *Room name* and *Status*, *Location*, *Devices*, *Seat Count*, *Configuration*, and *Firmware* *Status*. 

You can also find additional details of your Jabra meeting room device by drilling down into the **Device** page. 

On the **Room** page, the **Room Details** tab displays **Room Information**, **Room Configuration**, **Room AV system / Meeting room computer**, **Date and Time** for scheduled device updates, and more. 

The **Device Details** page shows you more granular information specific to the Jabra meeting room device, which includes *Installed Firmware* (version), *Firmware Policy*, when the device was *Last Seen as Connected* (online), and more. 

To view additional Room or Device details: 

1. On the left-hand navigation bar, click **Meeting rooms \> Room inventory**   
2. In the **Room inventory** page, in your **Locations** tree structure, click the name of your organization   
3. In the **Room inventory** list, click the relevant room name   
4. On the **Room** page, click the **Additional Details** tab to see more information about the   
   Room   
   o To see more information about the Jabra meeting room device in the Room, click the relevant pane in the **Room** page showing the Jabra meeting room device. 

### **6.2.2 Viewing room activity** 

In addition to Room Details and Device Details, the **Activity** tab is a source of information that helps you track events and their triggers in a Room. 

The **Activity** tab captures events that occurred in a Room, e.g.: *Firmware status*, *reboot*, *change of settings* of a meeting room device, and others. 

To view activity in a Room: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room inventory**   
2. In the **Room inventory** page, in your Locations tree structure, click the name of your organization   
3. In the **Room inventory** list, click the relevant room name   
4. In the **Room** page, find and click the **Activity** tab 

   The activity log in a Room (and the meeting room devices within) is now visible on a list that can be sorted by *Time*, *Trigger*, *Event*, and *User*. 

## **6.3 Locations** 

**Locations** are a secondary grouping, designed as a hierarchical tree structure that serves to sort and organize your organization´s virtual meeting rooms and meeting room devices. It is located within the **Room inventory** menu item. 

It is suggested that you use locations as a geographical representation of your organization. 

If you have created a location-based hierarchy, be aware that you can drill down several levels in the hierarchical structure. 

A location consists of a name and a placement in the hierarchy that you choose. The following example illustrates an organization with a simple hierarchical structure:   

* Your organization: **ABC Company** o Secondary grouping: (Location) **United States** 

* Tertiary grouping: (Location) **California** o Additional grouping: (Location) **Cupertino office rooms** 

However, your organization may be simpler and not need many locations. For example, it could instead be divided as follows:   

* Organization: **ABC Company** o Secondary grouping (Location): **Cupertino office rooms** 

In both examples, your Jabra meeting room device appears as a Room in the **Cupertino office rooms** location and all parent groupings, where **Cupertino office rooms** is grouped under. 

### **6.3.1 Adding, renaming, or deleting a location** 

An admin user can add, rename, or delete a location in the **Room inventory**. Similar to a parentchild hierarchy, when an admin user adds a location starting from the top of the tree structure they can create as many locations as the organization may need. 

Moreover, when you create more locations within the nested groups you can have up to six levels of hierarchy. You can also rename a location or delete a location. 

**Add a location**: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room inventory**   
2. On the left-hand side of the screen, on the locations tree structure, click the action menu (three-dot menu) and then click the **\+Add location** button   
3. In the **Add location** dialog box, in the *Location name* field, enter the name of the new location, and click **Create**   
   The new location appears beneath the location that you chose to group it under. 

**Rename a location**: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room inventory**   
2. On the left-hand side of the screen, on the locations tree structure, click the action menu (three-dot menu) of the relevant location you would like to rename, and then click   
   **Rename** 

3. In the **Rename location** dialog box, in the *Name* field, enter the new location name   
4. Click **Save** 

**Delete a location**: 

Be aware that when you delete a location you also delete all the *children* locations beneath, except in the case of a room with a Jabra PanaCast 50 RS. 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room inventory**   
2. On the left-hand side of the screen, on the locations tree structure, click the action menu (three-dot menu) of the relevant location you would like to delete, and then click **Delete**   
3. In the dialog box that appears, click **Delete** to confirm 

 	**Note** 

In the case of the P50 RS meeting room device, you must also delete the **Meeting room client** in the meeting room computer/computing device, otherwise, the meeting room device may get re-added to the Room inventory upon restarting. 

### **6.3.2 Moving rooms into locations and adding room details** 

After provisioning meeting room devices, an *unassigned room* is created in the locations tree structure, within the **Room inventory**. 

You can move the unassigned room into a predetermined location that you may have created in the tree structure. 

Moreover, when you move a room into a location, an **Add details** dialog box appears, letting you add room information such as *Room name*, *Seat Count*, *Description*, and others. 

#### **Tip** 

The following procedure is also helpful when you have already provisioned several Jabra meeting room devices into **Jabra+** for admins as *unassigned rooms*, and you would like to bulk assign a configuration that you have previously created or change the room name. 

To do this: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room** **inventory**   
2. In the **Room inventory** page, and assuming that you have already created a locations structure, click **unassigned room**   
3. On the list of unassigned rooms, drag and drop the room into the desired location in the hierarchical structure   
4. In the **Add details** dialog box, if necessary, enter the relevant information in the provided fields, and then click **Save** 

## **6.4 Scheduled device updates** 

Jabra meeting room devices are an integral part of your organization´s Meeting rooms, and to keep meeting room devices updated with the latest features, they may require regularly scheduled downtime to implement firmware updates. 

As updates are made available by Jabra, a defined maintenance window for your Jabra meeting room devices lets you implement them without interrupting end-users. 

Scheduled device updates enable an admin user to choose a day of the week at a specific onehour time interval, whereby your Jabra meeting room devices are temporarily unavailable as their firmware is updated. With a weekly recurring schedule, changes made in **Room configurations** only take effect during the defined maintenance window. 

As a default schedule, all Jabra meeting room devices in your organization’s **Room inventory** perform available firmware updates between 00:00 and 01:00 (24-hour time format) Monday through Friday. 

**Note** 	 

Currently, for meeting room devices, firmware management is turned **OFF** by default. To 	 switch it **ON**, see the Enabling or disabling firmware management for Jabra meeting 	 room and personal devices topic.   

This default schedule cascades to all Locations and follows the local time zone of the Jabra meeting room device. You can use the default schedule or choose to define and set a custom weekly schedule for the entire organization. 

| Note  For Jabra meeting room devices to follow the schedule, they must have a time zone that was set during provisioning.  P50 BYOD or P50 VBS: If the time zone was incorrectly set or the meeting room device was moved to a location with a different time zone, you must re-provision the device(s)    P50 RS: To set the correct time zone an admin user must change the Windows® settings for the time zone on the meeting room computer/ThinkSmart™ Core, included in the P50 RS bundle  |
| :---- |

**Firmware updates** 

Firmware updates take place after following your organization's Firmware policy, which governs whether or not you can update the firmware of Jabra meeting room devices and keep them regularly updated to the latest firmware version. 

Unless you have a defined schedule for when updates can be installed, end-users may be interrupted during their online meetings. This is due to meeting room devices having to reboot to have the updates applied. 

Therefore, updating the firmware of meeting room devices only occurs during the time previously set in the maintenance schedule. 

If you experience any issues while updating your firmware, see the Appendix & Troubleshooting. 

### **6.4.1 Defining and setting a custom schedule for device updates** 

Defining and setting a custom schedule for device updates lets an admin user ensure that Jabra meeting room device downtime in your entire organization only occurs during non-office hours. 

This is based on the local time zone of where the device is physically located, therefore minimizing potential interruptions for end-users. 

#### **Note** 

Be aware that the custom schedule the admin user defined and set, overwrites the default schedule for all Jabra meeting room device updates in the organization. 

To do this: 

1. On the left-hand navigation bar, click **Meeting rooms** \> **Room inventory**   
2. On the left-hand Locations bar, at the top of the list, click the action menu (three-dot menu) next to the name of the organization   
3. Click **Scheduled device updates** 

4. In the **Scheduled device updates** dialog box, from the *Select time range* drop-down menu, choose a timeframe   
5. In the **Scheduled device updates** dialog box, in the **Repeats on** section, check or click to select at least one weekday, for example, **M** for Monday, **S** for Saturday, etc.   
   a. To uncheck, click on the first letter of the weekday, for example, **F** for Friday 

6. To save, confirm your organization’s weekly schedule for device updates, and click **Apply** **6.4.2 Viewing the schedule for meeting room device updates** 

All Jabra meeting room devices in your organization follow an automated schedule that recurs on a weekly basis, on specific days in a specific one-hour timeframe. In **Jabra+** for admins, you can view the schedule for updates that apply to your entire organization. 

To view the schedule for device updates in the room: 

1. On the left-hand navigation bar, click **Meeting rooms** **\>** **Room inventory**   
2. In the **Room inventory** page, to view the schedule for device updates, on the list of rooms, click the relevant room name   
3. On the **Room** page, on the **Details** tab, on the **Date and time** pane, you can see the **Scheduled Device Updates** timeframe
