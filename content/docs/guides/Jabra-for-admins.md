---
title: "Jabra+ for admins"
description: ""
date: 2024-11-15T13:56:10Z
draft: false
---

# **5 Jabra+ for admins** 

**Jabra+** for admins offers a web interface for managing Jabra personal and meeting room devices remotely. 

Admin users can track assets, usage, access analytics, and perform mass firmware updates. Organizations such as a business, corporation, or subsidiary – are grouped under unique names, and devices are automatically added to inventories upon software client deployment. 

Admin users can customize configurations for specific Jabra personal and meeting room device models and view key metrics on the **Dashboard**, including Jabra device counts and activity. You can access **Jabra+** for admins at: [https://cloud.jabra.com](https://cloud.jabra.com/) 

## **5.1 Dashboard** 

The Dashboard provides an overview of the key Jabra meeting room and personal device information, including the total number of managed Jabra meeting room and personal devices in a given organization, Jabra device activity, room status, firmware status, and other variables. Access the Dashboard from the main page after logging into **Jabra+** for admins or click the **Dashboard** menu in the left-hand navigation bar. 

The Dashboard also shows the percentage of the device limit used. All admin users see a notification when 90% of the limit is reached. Once the maximum number of Jabra devices is provisioned, the notification informs all admin users that no further provisioning is permitted. 

## **5.2 Organizations** 

An organization (such as a business or corporation) is a representation of your company/business in **Jabra+** and has a unique organization ID. When you log in to **Jabra+** for admins for the first time, you are prompted to create your organization, in which you take up the *Owner* role. 

Organizations serve as a primary grouping, purposefully letting you keep the Jabra device data separated between the different organizations. 

You can have more than one organization – for example, you may have a subsidiary or sister company. However, every domain is restricted to three organizations, where each organization has a default device limit that enables admin users to provision and manage up to 500 Jabra meeting room and or personal devices. 

### **Note** 

Usage or analytics data cannot be linked between organizations; each organization acts as a separate entity. 

The device limit can be increased to more than 500 Jabra meeting room and or personal devices. To do so, contact Jabra Support or your Jabra representative. 

When you are the *Owner* of more than one organization, the *Owner* can invite other admin users (*Owners* or *Member*s) to each organization, and determine their respective permissions i.e. *edit rights* or *read only* access for Meeting rooms or Personal devices. See the Roles and Permissions chapter. 

Moreover, if an admin user belongs to more than one organization, they can seamlessly switch between organizations when they make the relevant organization active. Consequently, the Device and Room inventories show Jabra personal and meeting room devices in the active organization, including any associated metadata. 

An *Owner* can only leave an organization if they first elevate another user to the *owner* role, at which point they can delete an organization altogether. 

If an organization has reached the device limit, and Jabra devices can no longer be provisioned to the organization, an admin user (*Owner* or *Member* with the relevant edit rights) can delete Jabra devices to free up a slot. For procedures, see Removing Jabra personal devices from the Device inventory and/or Deleting a room or removing a meeting room device from a room. 

### **5.2.1 Creating additional organizations** 

Every organization has their own Device and Room inventory, so all admin users in **Jabra+** for admins can create one or multiple organizations. 

To create an additional organization: 

1. On the bottom left-hand side of the navigation bar, click the name of the organization you currently belong to, and then click **Manage my** **organizations**   
2. On the top right-hand side of the page, click **Create organization**   
3. In the **Create organization** dialog box, in the *Name* field, enter a name for your organization. Ensure you provide a meaningful name as you may need to invite additional members or partners, and because you cannot rename an organization.   
4. In the **Create organization** dialog box, click **Continue** 

5. In the **Set up device metadata** dialog box, check the relevant device metadata checkboxes, and click **Continue.** For more information about device metadata, see the  Appendix & Troubleshooting section.   
6. In the **Organization created** dialog box, click **Next**   
7. In the **Welcome** dialog box, ensure you read the **Privacy Policy** and **License Agreement**, and then click **Get started** 

   You are now the *owner* of an additional organization. 

**5.2.1.1 Making an organization active when you have multiple organizations** 

To view or make changes to Jabra devices in different inventories, all admin users must first make the organization active by selecting it in the **Manage my organizations** menu item. 

To make an organization active: 

1. On the bottom left-hand side of the navigation bar, click the name of the organization you currently belong to, and then click **Manage my** **organizations**   
2. Within the **Organization** pane (the relevant organization's name), click the action menu (three-dot menu)   
3. From the drop-down menu, click **Select organization**. The organization you chose is now active.   

   When you make an organization active, you are taken to the **Dashboard** of the selected organization. 

### **5.2.2 Deleting an organization** 

When an *owner* deletes an organization, it permanently removes all Jabra device data in **Jabra+** for admins. All Jabra devices in the Device and Room inventory gradually stop sending device data. 

Moreover, the connection to **Jabra+** for admins that the relevant software client initially established is severed. 

However, the software client remains installed on end-user computers or meeting room computers/computing devices until it is uninstalled from the relevant devices on which it was installed. 

#### **Important note** 

Be aware that when an *owner* deletes an organization, Jabra personal and meeting room devices continue to operate, but the remote management of those devices in **Jabra+** for admins is terminated. 

The deletion process is not instantaneous and may take up to 24 hours to complete. All associated device data, usage data, and user data are then irrevocably deleted. 

When you have multiple organizations, and you would like to delete one, the admin user holding the *owner* role in the organization must first ensure they make an organization active and then perform the following procedure: 

1. On the bottom left-hand side of the navigation bar, click the name of the organization you currently belong to, and then click **Manage my** **organizations**   
2. Within the **Organization** pane of the organization you want to delete, click the action menu (three-dot menu) and click **Delete organization**   
3. In the **Revoke active PC Clients?** dialog box, confirm with **Yes, continue** 

4. In the **Delete organization?** dialog box, check the **I confirm to delete the organization** checkbox, and click **Yes, delete organization** 

If, instead, an admin user holding the *Owner* role is only part of one organization and deletes it, then the *Owner* is prompted to create a new organization. 

### **5.2.3 Leaving an organization as a member** 

An admin user holding the *Member* role can leave an organization on their own. Be aware that for an *Owner* to leave an organization, they must first elevate a user of **Jabra+** for admins holding the *Member* role to the *Owner* role. See the procedure, Leaving an organization as an owner. 

To leave an organization as a *Member*: 

1. The *Member* who wants to leave the organization must log in to **Jabra+** for admins using their credentials   
2. On the left-hand navigation bar, click the name of the organization you belong to, and then click **Manage my** **organizations**   
3. Within the **Organization** pane (of the organization you want to leave), click the action menu and click **Leave organization**   
4. In the **Leave organization** dialog box, click **Leave** to confirm   

   At this point, the *Owner* of the organization receives an email informing them that a *Member* has left the organization. 

### **5.2.4 Leaving an organization as an owner** 

An admin user holding the *Owner* role can leave an organization on their own, provided that the organization has more than one admin user with the *Owner* role. 

In this case, the *Owner* must first upgrade an admin user from *Member* to *Owner*. See the Changing roles, editing permissions, or removing a user as an owner procedure. 

After the *Owner* has elevated an admin user from *Member* to *Owner*, the *Owner* can leave an organization as follows: 

1. The *Owner* who wants to leave the organization must log in to **Jabra+** for admins using their credentials   
2. On the left-hand navigation bar, click the name of the organization you belong to, and then click **Admin users**   
3. In the **Admin users** page, on the list, find the row with your name and click the action menu (three-dot menu)    
4. Click **Leave organization**, and in the **Leave organization** dialog box, click **Leave** 

   At this point, the new *Owner* of the organization receives an email informing them that another *Owner* has left the organization. 

## **5.3 Roles and permissions** 

Admin users of **Jabra+** for admins are system / IT administrators for Jabra devices in their organization, and fall into the following two roles: 

* *Owner*: Elevated admin users who manage all Jabra devices and perform user management tasks, including inviting users, revoking invitations, changing roles, and deleting organizations. *Owners* can elevate *Members* to *Owner* status, manage their permissions, and choose to terminate or remove Member(s) access to their organization. 

* *Member*: Subordinate to *Owners*, *Members* can be classified as admin users with *edit* or *read only* *rights* for either Meeting rooms or Personal devices, or both: 

  * *Member with Edit Rights*: Can manage all Jabra meeting room and / or personal devices in the organization, depending on the permission given (Meeting rooms or Personal devices) 

  * *Member with Read-Only Rights*: Can only view Jabra meeting room and personal devices and associated data, with no user or Jabra device management capabilities. 

An admin user can hold both the *Owner* and *Member* roles simultaneously, provided the admin user belongs to more than one organization. Upon creating an organization, an *Owner* or *Member* becomes the owner of that organization.  

*Members* cannot perform user management tasks or change organization settings, such as disabling metadata collection. 

A *Member with edit rights* to either Meeting rooms or Personal devices has *read only* access to the other. A *Member with read only* rights for both Meeting rooms and Personal devices cannot perform any procedures in **Jabra+** for admins that affect Jabra devices or the organization. **5.3.1 Roles and permissions matrix** 

|   | Owner  | Member  (edit rights)  | Member  (read only)  |
| :---- | ----- | ----- | :---- |
| Create an organization  | Yes  | Yes  | Yes  |
| Delete an organization and change organization settings (Metadata collection)  | Yes  | No  | No  |
| Invite new admin users to the organization, change roles from *Owner* to *Member* (or vice versa), change permissions for *Members* *with edit rights* to *read only rights* (or vice versa), and remove *Owners* or  *Members* from the organization  | Yes  | No  | No  |
| Leave an organization  | No[^1]  | Yes  | Yes  |
| Access the **Meeting rooms** menu item to view Jabra meeting room devices in the Room inventory as well as associated data such as created Meeting room clients, created Room configurations, etc.  | Yes  | Yes  | Yes   |
| Name Meeting rooms, change Jabra meeting room device settings, download meeting room clients and/or create Room configurations  | Yes  | Yes2  | No  |
| Access the **Personal devices** menu item to view personal device details, Device inventory, Device groups, installed Desktop clients, number of Jabra devices provisioned, and Configurations menu items  | Yes  | Yes  | Yes  |
| Add Personal devices to the Device inventory, export the list of Jabra personal devices, create Device groups to sort Jabra personal devices, as well as create and assign Configurations  | Yes  | Yes3  | No  |
| Enable or disable firmware management and change Firmware policies for an organizations’ Jabra devices  | Yes  | Yes2, 3  | No  |
| Lock specific Jabra device settings and prevent endusers from changing them  | Yes  | Yes  | No  |
| Create and download software clients  | Yes  | Yes  | No  |
| Reboot Jabra meeting room devices  | Yes  | Yes  | No  |

2. Provided that the Member with edit rights has been given access to Meeting room management. See the Changing roles, editing permissions or removing a user as an owner for the procedure. 

3. Provided that the Member with edit rights has been given access to Personal device management. See the Changing roles, editing permissions or removing a user as an owner for details. 

### **5.3.2 Changing roles, editing permissions or removing a user as an owner** 

The *Owner* of an organization can perform user management tasks within their organization. For example, an *Owner* can change the role of a *Member*, effectively making the *Member* also an *Owner* of the organization. An *Owner* can also change their own role from *Owner* to *Member*, or downgrade other *Owner(s)* to *Member(s)*, provided that the organization has at least one *Owner*. 

Moreover, an *Owner* can edit the permissions of a *Member* to fine tune the access rights of the *Member* to either manage Jabra Meeting room devices, Personal devices or both. 

In addition, all admin users are notified via email of any role changes or changes in permission scope. An *Owner* can also remove or terminate access for a *Member* to their organization. 

Be aware that a *Member* cannot change its own role; however, it can leave an organization. 

To change roles, edit permissions: 

1. On the left-hand navigation bar, click the name of the organization you are currently the owner of, and then click **Admin users**   
2. In the **Admin users** page, on the list, find the user that you want to manage access rights for or to remove, click the action menu (three-dot menu) and click **Edit permissions**   
   1. To change the role of a *Member* to *Owner* or vice-versa, in the **Edit permissions** dialog box, in the **Role** pane, click the relevant radio button for **Member** or **Owner**, and then click **Save**   
   2. To edit the access rights or permissions for a *Member*, in the **Permissions** pane, click the relevant radio button **Edit** or **Read only** for Meeting rooms and or Personal devices, and click **Save** 

   Be aware that changes are applied instantly, and the user does not have to log out and log back in to **Jabra+** for admins. 

To remove a user: 

1. In the **Admin users** page, on the list, find the user that you want to terminate access for, and click the action menu (three-dot menu)   
2. Click **Remove user**, and in the **Remove user** dialog box, click **Remove** 

At this point, the *Member* that was removed by the *Owner*, can no longer access **Jabra+** for admins. If it is a *Member* terminating their own access, see the Leaving an organization as a member procedure. 

If the removed *Member* was also a member of other organizations, the removed member maintains their membership in the other organizations; however, the removed member can also be reinvited to the organization. 

## **5.4 Device inventory for personal devices** (*Beta*) 

The Device inventory is a repository for all Jabra personal devices (including speakerphones) added to a specific organization. It is automatically populated when the **Jabra+** desktop app is deployed and installed on your end-user’s computers and end user Jabra personal devices are paired (Bluetooth Jabra devices) or recognized by the app automatically (cabled or wired Jabra devices). 

### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

In a searchable and filterable list, the Device inventory outlines information such as *Device model*,   
*Connection status*, *Firmware status*, any *Device group(s)* it may belong to, and others. In the Device inventory, the collected metadata lets you search for keywords such as Computer Name or Windows Username. 

For more information about device metadata, see the Appendix & Troubleshooting section. 

In addition, admin users can further sort Jabra personal devices in the Device inventory into Device groups, enabling them to create a secondary grouping in the organization. For example, an admin user may want to group Jabra devices in the organization into different departments, such as Marketing, Human Resources, etc.   

Admin users may also want to classify Jabra personal devices in Device groups based on the location of the Jabra devices or another useful variable.   

When Jabra personal devices are added to the Device inventory, a default standard configuration is applied to all Jabra personal devices in the inventory. You can also manually remove one or multiple Jabra personal devices from the Device inventory. See Standard Configuration for further information. 

### **5.4.1 Adding Jabra personal devices to the Device inventory** *(Beta)* 

#### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Jabra personal devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

For the procedure, see the Generating, deploying, and installing the Jabra+ desktop app topic. 

### **5.4.2 Removing Jabra personal devices from the Device inventory** 

Admin users (*Owner* or *Member with edit rights*) can remove one or multiple Jabra devices from the Device inventory list. 

When you remove Jabra personal devices from the Device inventory, you also permanently remove the Jabra personal devices from Device groups. 

To remove a Jabra personal device from the Device inventory: 

1. On the left-hand navigation bar, click **Devices** **\>** **Device** **inventory**   
2. On the Device inventory list, check the checkbox next to the device you would like to remove   
3. In the bottom ribbon, click **Remove from inventory** and confirm 

   #### **Note** 

   Ensure that after the admin user removes Jabra personal devices from the Device inventory, they must also uninstall the **Jabra+** desktop app/**Desktop client** from the end-user computer it was installed on. 

   Otherwise, when the end-user reconnects their Jabra personal device to their computer, the Jabra personal device is automatically re-added to the Device inventory. 

### **5.4.3 Exporting the Device inventory list** 

To see a list of your Jabra personal devices on a comma-separated values list, you can export your Device inventory as a .csv file. The list contains details such as *Firmware status*, *Computer name*, *Firmware version*, *Electronic serial number*, and others. 

After exporting the .csv file you can import it into a spreadsheet or a storage database. You can also open it as a plain-text file. 

To export the list: 

• 	In the **Device inventory** page, in the top-right hand of the list, click the action menu and then click **Export to CSV**. The file is then downloaded to your default *Downloads* folder associated with your web browser. 

### **5.4.4 Viewing Jabra personal device details** 

When a Jabra personal device is added to the Device inventory, you can see information such as *Firmware status*, *Operating system*, *Computer name*, *Client version*, *Version Policy*, and others. To do this: 

• 	In the **Device inventory** page, click the device name on the list to see additional Jabra personal device details, such as Jabra Evolve2 65, Jabra Evolve2 75, etc. You can search for the specific Jabra personal device using filtering based on *Model*, *Device group*, *Firmware status,* or *Connection status*. **5.4.5 Sorting your personal devices into Device groups** See the Device groups topic. 

## **5.5 Device groups for Jabra personal devices** 

### **Important note** 

Personal device management in **Jabra+** for admins is currently in a *Beta* state for testing with a limited number of customers. Devices can still be provisioned to **Jabra+** for admins, however, Jabra cannot provide technical support through Jabra Support Services. 

To help admin users (*Owners* or *Members with edit rights*) manage and organize Jabra personal devices in the Device inventory, **Device groups** let the admin user sort the collection of Jabra personal devices into different containers or buckets. 

• 	Primary grouping: Organization (e.g., *ABC Company*)  o Secondary grouping: Device groups (e.g., *Marketing*, *Human Resources*) 

In this case, the admin user adds Jabra personal devices from the **Device inventory** into the individual Device groups that were created and named. 

Device groups are essential for creating configurations, enabling the deployment of specific settings to selected Jabra personal devices. For more information, see the Configurations chapter. 

### **5.5.1 Creating a Device group for personal devices** 

Creating a Device group can be helpful when you have a large number of Jabra personal devices in your Device inventory because it helps you create a container or bucket for them. 

You can also create a Device group to test a specific firmware version you would like to use with your Jabra devices. This feature can help you test and check of a setting before mass deployment. 

To create a Device group: 

1. On the left-hand navigation bar, click **Personal devices** **\>** **Device groups**   
2. In the **Device groups** page, click **Create device group** 

3. In the **Create device group** dialog box, in the *Name* field, enter a name for your Device group, for example, *Marketing department*. Optionally, in the *Description* field, enter a description of your Device group.   
4. Click **Create**   

   You are now taken to the **Device groups** page. 

### **5.5.2 Adding a personal Jabra device to a Device group** 

After creating and giving a name to a Device group, you can add Jabra personal devices from the Device inventory and sort them into Device groups. 

A Jabra personal device can only be affiliated with one Device group at a time. If the Jabra device is added to a different Device group, the new one replaces the previous affiliation. 

To add Jabra personal devices from the Device inventory to a Device group: 

1. On the left-hand navigation bar, click **Personal devices \> Device inventory**   
2. On the list, check the checkbox of the relevant Jabra device(s) to add   
3. In the bottom ribbon, click **Add devices to device group**   
4. In the **Add devices to device group** dialog box, select a Device group, and click **Add devices** 

   You have now added Jabra personal devices to a device group.
