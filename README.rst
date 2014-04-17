voice-of-armok
==============

Dragonfly commands and macros for playing Dwarf Fortress.

----

Alex Roper

alex@aroper.net

Status
======

Already quite useful. In active development as of April 2014.

Introduction
============

Dwarf Fortress is a really awesome game. Unfortunately, the interface is
extremely repetitive to use, particularly for tasks such as creating bedrooms,
pump stacks, and certain types of megaprojects. For extremely complicated
constructions, QuickFort works beautifully. For intermediate designations,
however, I find myself instead biting the bullet and spamming lots of keys.

Video games are supposed to be Fun.

Overall I appreciate DF's keyboard centric nature compared to the usual clickfest
nest of rat-addicted garbage that dominates video games, and here it is
particularly convenient as it makes it extremely amenable to voice scripting,
as the grammar closely resembles VIM's command mode (don't worry, I wasn't able
to type that with a straight face:-) ). Fortunately, I love VIM, not least
because it lets you specify *counts* and *lightweight macros*.

The purpose of this project is threefold:

* Provide a simple and intuitive (assuming you are somewhat familiar with DF's interface) control channel to complement the keyboard for tasks which are tedious on it, while staying out of the way when the keyboard makes sense.
* Provide a lightweight and powerful macro system, inspired by the lightweight macros in VIM.
* Allows the God of Blood to speak, and let their voice wield doom! Now cursing at your dwarves will actually do something (probably something Fun)!

The nice thing about voice is that while latency is high compared to keyboard,
information content is also high. For example, consider the phrase "select up 4
left 4 select left 2 down 4 repeat that 5 times" --  this simple expression
allows you to designate five 5x5 squares, separated by a single row.

I also find it convenient to not have to read through the menu to remember the
key for many of the more obscure commands that I tend to forget.

Some other examples of Fun commands you can use:

* "delve 99" -- move 99 Z levels down FAST
* "record macro 1" -- record all commands until you end recording
* "play macro 5 50 times" -- play macro 5 50 times
* "designate channel select up 15 select" -- channel 15 blocks up
* "build mechanism screw pump" -- select a screw pump

Installation
============

Unfortunately, installation is somewhat difficult. You will need to be on
Windows, and install a copy of Dragon NaturallySpeaking (you could try to use
just Windows Speech Recogniton and Dragonfly, but I have not tried this), as
well as Natlink and Dragonfly, two libraries that allow extension of Dragon
with custom grammars.

Setup instructions of this environment can be found various places on the web,
including https://github.com/calmofthestorm/aenea/blob/master/README.rst

Once you have Dragonfly and Natlink working, simply drop the module file into
your Natlink directory, and turn your microphone off then on.

Commands
========

I hate to be one of those people, but the best way to get a feel of the voice
commands you can use is to read the script. Nearly all commands will be
familiar and intuitive at first glance to a DF player; you really don't need
any programming knowledge to read it.

In particular, note that you can say up to 16 commands without pausing; you do
not need to pause and wait after each command. This is the main advantage of
Dragonfly over Dragon's built-in systems.

Most commands where it makes sense can take a number (up 5, delve 25, etc).

Additionally, after speaking a sequence of commands you may end the sequence
with "repeat that <n> times" to repeat the entire sequence N times (N may be
1-100).

Macros work as follows:

* You need to pause before and after the macro begin, end, and play commands.
* There are 101 macro slots, 0-100.
* Say "begin macro <m>" to record macro m, replacing any previous contents.
* Say "end macro" to stop recording a macro.
* Say "play macro <m>" To play macro n once.
* Say "play macro <m> <n> times" To play macro m n times. n may be 1-100.
* Currently, macros are not saved between reloads of the module (turning off the mic). The macro system in this module is intended to be a quick and lightweight way to accomplish tasks that are repetitive, and so I do not foresee this being a major issue. For more elaborate/persistent macros, look at Autohotkey or DF's own macro system (or see the page on the DF wiki for other options).

FAQ
===

Q: OH ARMOK'S SWEET ADAMANTINE BEARD WHY????

A: I've already written a number_ of grammars for Dragonfly, some quite complex (VIM), so it was a fairly quick process to crank out a grammar for DF. And I wanted to show Skyrim fans that they're not the only ones who can get mods for voice control!

Q: Are the commands at all dependent on context?

A: Not currently. If I had access to the context information it'd be trivial on the grammar side, but I don't know an easy way to extract state information out-of-process from DFHack. I see there's some RPC-based code in the repo, but it's years old and I can't find any documentation on it. If I could extract game state, this interface could get insanely smart, such as automagically using UMKH, up/down/left/right, +/- where appropriate. Not to mention specifying material verbally, etc.

Ideas
=====

No promises, but a few things I would like to implement in the future:

* Persist macros across module reloads.
* Hook into state via DFHack to allow awesome context dependence.
* Custom-named macros rather than just integers.

.. _number: https://github.com/calmofthestorm/aenea/tree/master/grammars_available

