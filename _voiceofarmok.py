# This file is a command-module for Dragonfly.
#

import time

try:
  import pkg_resources

  pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
  pass

from dragonfly import (
    Alternative,
    AppContext,
    CompoundRule,
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    Literal,
    MappingRule,
    Repetition,
    RuleRef,
    Sequence,
    Text,
  )

KEYSTROKE_DELAY = 0.1

df_context = AppContext(title="Dwarf Fortress")
disable_context = ~df_context

active_macro = None
macros = {}

main_menu_table = {
  # Spoken-form           command

  #### Main menu
  "announcements":          Key("a"),
  "view announcements":     Key("a"),
  "announce":               Key("a"),

  "build":                  Key("b"),

  "civilizations":          Key("c"),
  "view civilizations":     Key("c"),

  "designations":           Key("d"),
  "designate":              Key("d"),

  "unit list":              Key("u"),

  "military":               Key("u"),

  "points routes notes":    Text("N"),
  "points":                 Text("N"),
  "routes":                 Text("N"),
  "notes":                  Text("N"),

  "burrows":                Key("w"),
  "make burrows":           Key("w"),

  "stockpiles":             Key("p"),
  "stock":                  Key("p"),

  "set building tasks":     Key("q"),
  "building":               Key("q"),
  "query":                  Key("q"),

  "view rooms":             Text("R"),
  "rooms":                  Text("R"),

  "items":                  Key("t"),
  "view items in buildings":Key("t"),

  "view units":             Key("v"),

  "nobles":                 Key("n"),
  "parasites":              Key("n"),

  "status":                 Key("z"),

  "reports":                Key("r"),

  "orders":                 Key("o"),
  "set orders":             Key("o"),

  "jobs":                   Key("j"),
  "job list":               Key("j"),

  "squads":                 Key("s"),

  "hauling":                Key("h"),

  "zones":                  Key("i"),

  "hot keys":               Text("H"),

  "look":                   Key("k"),
  "examine":                Key("k"),

  "step [<n>]":             Key("dot:%(n)d"),

  "depot access":           Text("D"),

  "move menu":              Key("tab"),

  "help":                   Key("question"),

  # "movies":                 Key("semicolon"),

  "pause":                  Key("space"),
  "resume":                 Key("space"),
}

building_menu_table = {
  "armor stand":            Key("a"),

  "bed":                    Key("b"),

  "seat":                   Key("c"),
  "chair":                  Key("c"),

  "burial receptacle":      Key("n"),
  "coffin":                 Key("n"),

  "door":                   Key("d"),

  "floodgate":              Key("x"),

  "floor hatch":            Text("H"),

  "wall grate":             Text("W"),

  "floor grate":            Text("G"),

  "vertical bars":          Text("B"),

  "floor bars":             Key("a-b"),

  "cabinet":                Key("f"),

  "container":              Key("h"),
  "chest":                  Key("h"),

  "kennels":                Key("k"),

  "farm plot":              Key("p"),
  "farm":                   Key("p"),

  "weapon rack":            Key("r"),

  "statue":                 Key("s"),

  "slab":                   Key("a-s"),

  "table":                  Key("t"),

  "paved road":             Key("o"),

  "dirt road":              Text("O"),

  "bridge":                 Key("g"),

  "well":                   Key("l"),

  "siege engines":          Key("i"),

  "workshops":              Key("w"),

  "furnaces":               Key("e"),

  "glass window":           Key("y"),

  "gem window":             Key("Y"),

  "terrain":                Text("C"),
  "wall":                   Text("Cw"),
  "floor":                  Text("Cf"),
  "ramp":                   Text("Cr"),
  "up stair":               Text("Cu"),
  "down stair":             Text("Cd"),
  "stair":                  Text("Cx"),
  "fortification":          Text("CF"),
  "track":                  Text("CT"),
  "track":                  Text("CS"),

  "trade depot":            Text("D"),

  "traps":                  Key("T"),
  "stone fall trap":        Text("Ts"),
  "weapon trap":            Text("Tw"),
  "lever":                  Text("Tl"),
  "pressure plate":         Text("Tp"),
  "cage trap":              Text("Tc"),
  "upright spear":          Text("TS"),
  "upright spike":          Text("TS"),
  "spike trap":             Text("TS"),
  "spear trap":             Text("TS"),

  "machine components":     Text("M"),
  "mechanism":              Text("M"),
  "screw trap":             Key("s"),
  "water wheel":            Key("w"),
  "windmill":               Key("m"),
  "gear assembly":          Key("g"),
  "horizontal axle":        Key("h"),
  "vertical axle":          Key("v"),
  "rollers":                Key("r"),

  "support":                Key("S"),

  "animal trap":            Key("m"),

  "restraint":              Key("v"),

  "cage":                   Key("j"),

  "archery target":         Key("A"),

  "traction bench":         Key("R"),

  "nest box":               Key("N"),

  "hive":                   Key("a-h"),
}

designation_table = {
  "mine":                   Key("d"),

  "channel":                Key("h"),

  "remove [up] ramp [up]":  Key("z"),
  "remove [up] stair [up]": Key("z"),

  "upward stairway":        Key("u"),
  "downward stairway":      Key("j"),
  "stairway":               Key("i"),

  "upward ramp":            Key("r"),
  "ramp up":                Key("r"),

  "chop [[down] trees]":    Key("t"),

  "gather [plants]":        Key("p"),

  "smooth [stone]":         Key("s"),

  "engrave [stone]":        Key("e"),

  "carve fortifications":   Key("a"),
  "carve fort":             Key("a"),
  "fortification":          Key("a"),
  "fortify":                Key("a"),

  "carve track":            Text("T"),
  "track":                  Text("T"),

  "toggle engravings":      Key("v"),

  "remove designation":     Key("x"),
  "remove construction":    Key("n"),

  "set [building] [item] properties":Key("b"),
  "properties":Key("b"),

  "[set] traffic [areas]":Key("o"),
}

building_item_properties_table = {
  "reclaim [items] [buildings]":Key("c"),

  "forbid [items] [buildings]":Key("f"),

  "melt [items]":           Key("m"),

  "unmelt [items]":         Text("M"),
  "remove melt":            Text("M"),

  "dump [items]":           Key("d"),

  "undump [items]":         Text("D"),
  "remove dump":            Text("D"),

  "hide [items] [buildings]":Key("h"),
  "unhide [items] [buildings]":Key("H"),
}

traffic_table = {
  "high traffic":           Key("h"),
  "normal traffic":         Key("n"),
  "low traffic":            Key("l"),
  "restricted traffic":     Key("r"),
}

stockpile_table = {
  "stock animal":           Key("a"),
  "stock furniture [storage]": Key("u"),
  "stock corpses":          Key("y"),
  "stock stone":            Key("s"),
  "stock gem":              Key("e"),
  "stock cloth":            Key("h"),
  "stock ammo":             Key("z"),
  "stock finished goods":   Key("g"),
  "stock weapons":          Key("p"),
  "stock food":             Key("f"),
  "stock refuse":           Key("r"),
  "stock wood":             Key("w"),
  "stock [bar] block":      Key("b"),
  "stock bar":              Key("b"),
  "stock leather":          Key("l"),
  "stock coins":            Key("n"),
  "stock armor":            Key("d"),
  "stock custom":           Key("c"),
  "custom stockpile":       Key("c"),
  "custom settings":        Key("t"),

  "enable":                 Key("e"),
  "disable":                Key("d"),
  "allow [all]":            Key("a"),
  "block [all]":            Key("b"),
  "permit":                 Key("p"),
  "forbid":                 Key("f"),
}

general_table = {
  "delve up [<n>]":         Key("langle/0.10:%(n)d"),
  "delve [down] [<n>]":     Key("rangle/0.10:%(n)d"),
  "surf [up] [<n>]":        Key("langle/0.10:%(n)d"),
  "surf down [<n>]":        Key("rangle/0.10:%(n)d"),
  "up [<n>] z level":       Key("langle/0.10:%(n)d"),
  "down [<n>] z level":     Key("rangle/0.10:%(n)d"),

  "up [<n>]":         Key("up:%(n)d"),
  "down [<n>]":       Key("down:%(n)d"),
  "left [<n>]":       Key("left:%(n)d"),
  "right [<n>]":      Key("right:%(n)d"),

  "gope [<n>]":       Key("s-up:%(n)d"),
  "drop [<n>]":       Key("s-down:%(n)d"),
  "lope [<n>]":       Key("s-left:%(n)d"),
  "yope [<n>]":       Key("s-right:%(n)d"),

  "next [<n>]":       Key("plus:%(n)d"),
  "prior [<n>]":      Key("minus:%(n)d"),
  "previous [<n>]":   Key("minus:%(n)d"),

  "wider [<n>]":      Key("k:%(n)d"),
  "taller [<n>]":     Key("u:%(n)d"),
  "narrower [<n>]":   Key("h:%(n)d"),
  "shorter [<n>]":    Key("m:%(n)d"),

  "ace [<n>]":        Key("space:%(n)d"),
  "spacebar [<n>]":   Key("space:%(n)d"),

  "act [<n>]":        Key("escape:%(n)d"),
  "cancel [<n>]":     Key("escape:%(n)d"),
  "escape [<n>]":     Key("escape:%(n)d"),
  "out [<n>]":        Key("escape:%(n)d"),

  "slap [<n>]":       Key("enter:%(n)d"),
  "enter [<n>]":      Key("enter:%(n)d"),
  "return [<n>]":     Key("enter:%(n)d"),
  "select [<n>]":     Key("enter:%(n)d"),
  "yes [<n>]":        Key("enter:%(n)d"),

  "tab [<n>]":        Key("tab:%(n)d"),

  "undesignate":      Text("dx"),
}

class CommandChainRule(MappingRule):
  exported = False

  extras = [
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]

  defaults = {"n": 1}

command_table = {}
command_table.update(main_menu_table)
command_table.update(building_menu_table)
command_table.update(general_table)
command_table.update(designation_table)
command_table.update(traffic_table)
command_table.update(building_item_properties_table)
command_table.update(stockpile_table)

mapping = dict((key, value) for (key, value) in command_table.iteritems())
single_action = RuleRef(rule=CommandChainRule(mapping=mapping, name="c"))

sequence = Repetition(single_action, min=1, max=16, name="sequence")

class RepeatRule(CompoundRule):
  spec = "[ <sequence> ] [repeat [that] <n> times]"

  defaults = {"n": 1}

  extras = [sequence, IntegerRef("n", 1, 100)]

  def _process_recognition(self, node, extras):
    if active_macro is not None:
      macros.setdefault(active_macro, [])

    sequence = extras.get("sequence", [])
    count = extras["n"]
    if active_macro is not None:
      macros[active_macro].append(([c for c in sequence], count))
    for i in xrange(count):
      time.sleep(KEYSTROKE_DELAY)
      for action in sequence:
        action.execute()

class MacroEnd(CompoundRule):
  spec = "end macro [<n>]"
  extras = [IntegerRef("n", 0, 100)] # n is ignored

  def _process_recognition(self, node, extras):
    global active_macro
    active_macro = None

class MacroPlay(CompoundRule):
  spec = "play macro <m> [<n> times]"
  extras = [
      IntegerRef("m", 0, 100),
      IntegerRef("n", 1, 100),
    ]
  defaults = {"n": 1}

  def _process_recognition(self, node, extras):
    for j in xrange(extras["n"]):
      for sequence, count in macros.get(extras["m"], []):
        for i in xrange(count):
          time.sleep(KEYSTROKE_DELAY)
          for action in sequence:
            action.execute()

class MacroBegin(CompoundRule):
  spec = "begin macro <n>"
  extras = [IntegerRef("n", 0, 100)]

  def _process_recognition(self, node, extras):
    global active_macro
    if active_macro is None:
      active_macro = extras["n"]
      macros[extras["n"]] = []

grammar = Grammar("voiceofarmok", context=df_context)
grammar.add_rule(RepeatRule())
grammar.add_rule(MacroBegin())
grammar.add_rule(MacroEnd())
grammar.add_rule(MacroPlay())

grammar.load()

def unload():
  global grammar
  if grammar:
    grammar.unload()
  grammar = None
