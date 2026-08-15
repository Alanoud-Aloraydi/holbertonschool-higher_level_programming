"""Generate personalized invitation files from a text template."""


def generate_invitations(template, attendees):
    """Create one invitation file for each attendee."""
    if not isinstance(template, str):
        print(
            "Invalid input type: template must be a string, "
            f"not {type(template).__name__}."
        )
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print(
            "Invalid input type: attendees must be a list of dictionaries."
        )
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = (
        "name",
        "event_title",
        "event_date",
        "event_location",
    )

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)
            replacement = "N/A" if value is None else str(value)
            invitation = invitation.replace(
                "{" + placeholder + "}", replacement
            )

        output_file = f"output_{index}.txt"

        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as error:
            print(f"Error writing {output_file}: {error}")
