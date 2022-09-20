from .._schema import AnnotConfig
from ...activity import ActSet, ActClass

OPENPACK_OPERATIONS = ActSet((
    ActClass(100, "Picking", is_ignore=False),
    ActClass(200, "Relocate Item Label", is_ignore=False),
    ActClass(300, "Assemble Box", is_ignore=False),
    ActClass(400, "Insert Items", is_ignore=False),
    ActClass(500, "Close Box", is_ignore=False),
    ActClass(600, "Attach Box Label", is_ignore=False),
    ActClass(700, "Scan Label", is_ignore=False),
    ActClass(800, "Attach Shipping Label", is_ignore=False),
    ActClass(900, "Put on Back Table", is_ignore=False),
    ActClass(1000, "Fill out Order", is_ignore=False),
    ActClass(8100, "Null", is_ignore=True),
))

OPENPACK_OPERATIONS_ANNOTATION = AnnotConfig(
    name="openpack-operations",
    version="v3.2.2",
    classes=OPENPACK_OPERATIONS,
)


OPENPACK_ACTIONS = ActSet((
    ActClass(101, "Pick Up Sheet", is_ignore=False),
    ActClass(103, "Pick Up Item from Box", is_ignore=False),
    ActClass(104, "Pick Up Order Sheet & Walk to Rack - v2", is_ignore=False),
    ActClass(105, "Walk to Work Bench - v2", is_ignore=False),
    ActClass(106, "Pick Up Order Sheet & Walk to Rack with Prev Packed Box - v2", is_ignore=False),
    ActClass(107, "Pick Up Box Sheet", is_ignore=False),
    ActClass(108, "Walk to Work Bench", is_ignore=False),
    ActClass(201, "Remove Item Label", is_ignore=False),
    ActClass(202, "Attach to Order Sheet", is_ignore=False),
    ActClass(203, "Hold Pen", is_ignore=False),
    ActClass(204, "Write Check Mark", is_ignore=False),
    ActClass(205, "Put Item Small Bag", is_ignore=False),
    ActClass(206, "Relocate Item Label - v2", is_ignore=False),
    ActClass(207, "Write - v2", is_ignore=False),
    ActClass(301, "Pick Cardboard", is_ignore=False),
    ActClass(302, "Bend Flap", is_ignore=False),
    ActClass(303, "Attach Tape", is_ignore=False),
    ActClass(304, "Turn Over Box", is_ignore=False),
    ActClass(305, "Pick Up Assembled Box", is_ignore=False),
    ActClass(306, "Assemble Box - v2", is_ignore=False),
    ActClass(401, "Insert Item into Box", is_ignore=False),
    ActClass(402, "Air Cushion", is_ignore=False),
    ActClass(403, "Separate Air Cushion", is_ignore=False),
    ActClass(404, "Put Item Small Bag", is_ignore=False),
    ActClass(405, "Insert Items - v2", is_ignore=False),
    ActClass(501, "Bend Flap", is_ignore=False),
    ActClass(502, "Attach Tape", is_ignore=False),
    ActClass(503, "Close Box - v2", is_ignore=False),
    ActClass(601, "Attach Box Label", is_ignore=False),
    ActClass(602, "Attach Box Label - v2", is_ignore=False),
    ActClass(701, "Pick Up HT", is_ignore=False),
    ActClass(702, "Scan Order Sheet", is_ignore=False),
    ActClass(703, "Scan Box", is_ignore=False),
    ActClass(704, "Scan Item", is_ignore=False),
    ActClass(705, "Hold Scanner", is_ignore=False),
    ActClass(706, "Scan Order Sheet", is_ignore=False),
    ActClass(707, "Scan Printer", is_ignore=False),
    ActClass(708, "HT - v2", is_ignore=False),
    ActClass(709, "Printer - v2", is_ignore=False),
    ActClass(801, "Pick Up Shipping Label", is_ignore=False),
    ActClass(802, "Attach Shipping Label", is_ignore=False),
    ActClass(803, "Attach Shipping Label - v2", is_ignore=False),
    ActClass(901, "Pick Up Packed Box", is_ignore=False),
    ActClass(902, "Put Packed Box", is_ignore=False),
    ActClass(903, "Put on Back Table - v2", is_ignore=False),
    ActClass(1001, "Pick Up Pen", is_ignore=False),
    ActClass(1002, "Write Sign", is_ignore=False),
    ActClass(1003, "Push Order Sheet into Tray", is_ignore=False),
    ActClass(1004, "Fill out - v2", is_ignore=False),
    ActClass(1005, "Write - v2", is_ignore=False),
    ActClass(1006, "Insert - v2", is_ignore=False),
    ActClass(8101, "Others", is_ignore=True),
    ActClass(8102, "System Error", is_ignore=True),
    ActClass(8103, "Ignore", is_ignore=True),
    ActClass(8104, "Unknown", is_ignore=True),
    ActClass(8201, "System Error", is_ignore=True),
))

OPENPACK_ACTIONS_ANNOTATION = AnnotConfig(
    name="openpack-actions",
    version="v3.2.2",
    classes=OPENPACK_ACTIONS,
)


ACTIVITY_1S_ANNOTATION = AnnotConfig(
    name="activity-1s",
    version="",
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/annotation/activity-1s/",
        "fname": "${session}.csv",
    },
)
