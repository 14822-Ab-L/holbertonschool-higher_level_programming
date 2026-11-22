#!/usr/bin/python3
"""Generate personalised invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files for each attendee."""
    if not isinstance(template, str):
        print("Invalid template type")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Invalid attendees type")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + placeholder + "}", str(value)
            )

        filename = "output_{}.txt".format(index)

        with open(filename, "w") as file:
            file.write(invitation)
