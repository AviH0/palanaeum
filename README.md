# Huji CS Lab Support Interface (2019/20)

## Installation

Ensure sure your python version is at least **3.6** and the interpreter has the following packages installed:
**gspread, oauth2client**

```
pip install gspread oauth2client
```

Make sure you have the json file in your credentials directory (if you donwloaded the app from the github repository you will need to get it from somewehere else and place it in app/credentials/).

To run the program, simply run LabSupportClient.py

Note: It is now possible to update the installation using Update.py, however if your installed version is higher than 1.1.0, this will happen automatically whenever there is an update.
## Usage

The interface will show a color-coded list of the current students in the queue. Students that are still
waiting for their turn have no color. Students whose turn has arrived are yellow until their turn is over,
when they become green.

The interface will also show the current status - either waiting for a student to arrive or helping a student
(or nothing if there are not students requesting assistance), along with the student's name and the topic of his request.

The interface starts as waiting (if it doesn't, call the next student in the list using right-click).
When the student arrives, click 'Student has arrived'. When you are done with him, click 'Next student' to
call the next student on the list. Note: the interface will skip students in the list that are already yellow,
as it assumes they are being handled by another support person, but if there are more yellow colored students
than there are support people, call one of them using right-click.

If a student fails to show up when you are waiting for them, click 'No show' and that student will be moved to
the 'Missed' list, where they will be colored orange for half an hour and then cahnged to red.
If they show up while orange, use right-click to start helping them instead of the next students in line.

When you move to another student while in 'helping' status, the current student will be marked as finished.
If you move while in 'waiting' status the current student will be moved back to wait in line.

You can right-click on any name to:

- Call: Mark the student as yellow as his turn had arrived.
- Reset: Unmark the student so he is waiting in line.
- Start helping: Start helping the student.
- Remove: Remove the student from the list.

If something goes wrong, the best thing to do is to open the google sheet and sort it out manually.

## Github repository

All the code is available [here](https://github.com/AviH0/LabSupportInterface).

## Report a problem

If you encounter an issue, please report it [here](https://github.com/AviH0/LabSupportInterface/issues/new), and include a **detailed description of the issue and the steps to reproduce it**.

## Contribute

If you feel like making a contribution, please make a [pull request](https://github.com/AviH0/LabSupportInterface/compare) and decribe in detail the changes that you made.

